# CrisisMapper — UNDP RAPIDA Community Reporting Tool

**Live Demo:** https://[your-username].github.io/crisis-mapper/

A community-facing damage reporting MVP built for the UNDP/Innocentive  
"Build the Future of Crisis Mapping" challenge (June 2026).  
Powered by **DBbun LLC** — Executable Publication Layer.

---

## What It Does

CrisisMapper enables communities to capture and submit infrastructure damage  
reports in real-time following sudden-onset crises (earthquakes, floods,  
hurricanes, wildfires, conflicts).

### Features

| Feature | Status |
|---|---|
| 📷 Photo capture (camera + upload) | ✅ |
| ⚠️ Damage classification (Minimal / Partial / Complete) | ✅ |
| 🏗️ Infrastructure type + crisis type selection | ✅ |
| 📍 GPS geolocation + map-pick fallback | ✅ |
| 🗺️ Live map with colored pins (Leaflet + OpenStreetMap) | ✅ |
| 📴 Offline-first (localStorage queue, syncs on reconnect) | ✅ |
| 🌐 6 UN languages (EN, FR, ES, AR, ZH, RU) | ✅ |
| 📊 Dashboard with stats + report table | ✅ |
| ⬇️ CSV export | ✅ |
| 🌐 GeoJSON export (RAPIDA-compatible) | ✅ |
| 🔢 Report versioning (same-location updates) | ✅ |
| 🤖 DBbun AI analysis backend (Claude Sonnet) | ✅ demo |

---

## RAPIDA Export Schema

GeoJSON output includes mandatory UNDP fields:

```json
{
  "type": "Feature",
  "geometry": { "type": "Point", "coordinates": [lng, lat] },
  "properties": {
    "id": "RPT-1234567890",
    "timestamp": "2026-06-02T14:32:00.000Z",
    "damage_classification": "partial",
    "infrastructure_type": "residential",
    "crisis_type": "earthquake",
    "debris": "yes",
    "description": "...",
    "landmark": "...",
    "version": 1,
    "sync_status": "synced"
  }
}
```

---

## DBbun Backend Pipeline

Submitted reports feed into the **DBbun INGEST/DIGEST/SUGGEST** pipeline:

```
Community Reports (GeoJSON/CSV)
        ↓ INGEST
DBbun document-to-simulator engine
        ↓ DIGEST
Claude Sonnet AI analysis
        ↓ SIMULATE
Synthetic damage datasets + scenario bundles
        ↓ EXPORT
RAPIDA-compatible outputs for UNDP analysts
```

---

## Deployment

### GitHub Pages (recommended)

```bash
git clone https://github.com/[your-username]/crisis-mapper
cd crisis-mapper
# Enable GitHub Pages in repo Settings → Pages → Deploy from main branch
```

No build step. No dependencies. Single HTML file.

### Local

```bash
# Just open index.html in any browser
open index.html
```

---

## Technology

- **Frontend:** Vanilla HTML/CSS/JS — no framework, no build step
- **Map:** Leaflet.js + OpenStreetMap
- **Storage:** Browser localStorage (offline-first)
- **AI:** Claude Sonnet (claude-sonnet-4-6) via DBbun proxy
- **Export:** CSV + GeoJSON (RAPIDA schema)
- **Languages:** i18n via built-in translation strings

---

## License

Open source — MIT License.  
Built by **DBbun LLC** (Cambridge, MA) for UNDP crisis response.  
Contact: dbbun.com

---

## Challenge

UNDP / Innocentive — Build the Future of Crisis Mapping  
Prize: $50,000 USD | Deadline: June 23, 2026  
Submission by: Uri Kartoun, PhD — DBbun LLC
