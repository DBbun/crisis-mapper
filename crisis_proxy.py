"""
crisis_proxy.py — DBbun Crisis Mapper AI Analysis Proxy
Add this as a new route in your existing Render Flask app,
or deploy as a standalone service.

Route: POST /analyze-damage
Receives: { image_b64, infrastructure_type, crisis_type }
Returns:  { damage_classification, description, confidence }
"""

import os, base64, json
from flask import request, jsonify
import anthropic

# Add this route to your existing Flask app
# from crisis_proxy import analyze_damage_route
# app.add_url_rule('/analyze-damage', 'analyze_damage', analyze_damage_route, methods=['POST'])

def analyze_damage_route():
    """Claude Sonnet damage classification from photo."""
    try:
        data = request.get_json()
        image_b64 = data.get('image_b64', '')
        infra_type = data.get('infrastructure_type', 'unknown')
        crisis_type = data.get('crisis_type', 'unknown')

        # Strip data URL prefix if present
        if ',' in image_b64:
            image_b64 = image_b64.split(',', 1)[1]

        # Detect media type
        media_type = 'image/jpeg'
        raw = base64.b64decode(image_b64[:16])
        if raw[:4] == b'\x89PNG':
            media_type = 'image/png'
        elif raw[:4] == b'RIFF':
            media_type = 'image/webp'

        client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

        prompt = f"""You are a UNDP RAPIDA crisis assessment AI analyzing field photos of infrastructure damage.

Infrastructure type: {infra_type}
Crisis type: {crisis_type}

Analyze this photo and respond with ONLY valid JSON in this exact format:
{{
  "damage_classification": "minimal" | "partial" | "complete",
  "description": "2-3 sentence technical assessment of visible damage",
  "confidence": "high" | "medium" | "low",
  "debris_present": true | false,
  "immediate_risk": true | false
}}

Damage definitions:
- minimal: Structurally sound, cosmetic damage only, safe to use
- partial: Repairable damage, usable with caution, structural integrity partially compromised
- complete: Structurally unsafe or destroyed, do not enter

Respond only with the JSON object, no preamble."""

        response = client.messages.create(
            model='claude-sonnet-4-6',
            max_tokens=512,
            messages=[{
                'role': 'user',
                'content': [
                    {
                        'type': 'image',
                        'source': {
                            'type': 'base64',
                            'media_type': media_type,
                            'data': image_b64
                        }
                    },
                    {'type': 'text', 'text': prompt}
                ]
            }]
        )

        text = response.content[0].text.strip()
        # Clean JSON fences if present
        if text.startswith('```'):
            text = text.split('\n', 1)[1].rsplit('```', 1)[0].strip()

        result = json.loads(text)
        return jsonify(result), 200

    except json.JSONDecodeError:
        # Fallback if JSON parse fails
        return jsonify({
            'damage_classification': 'partial',
            'description': 'AI analysis returned unstructured result. Please classify manually.',
            'confidence': 'low',
            'debris_present': False,
            'immediate_risk': False
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ── CORS headers (add to your Flask app) ──────────────────────────────────────
# from flask_cors import CORS
# CORS(app, resources={r"/analyze-damage": {"origins": "https://[your-username].github.io"}})
#
# Or manually:
# @app.after_request
# def add_cors(response):
#     response.headers['Access-Control-Allow-Origin'] = 'https://[your-username].github.io'
#     response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
#     return response


# ── STANDALONE DEPLOYMENT (if not adding to existing app) ────────────────────
if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    @app.route('/analyze-damage', methods=['POST', 'OPTIONS'])
    def analyze_damage():
        if request.method == 'OPTIONS':
            response = jsonify({})
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            return response, 200
        resp = analyze_damage_route()
        if isinstance(resp, tuple):
            response, code = resp
        else:
            response, code = resp, 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response, code

    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
