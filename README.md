# CrisisMapper — UNDP RAPIDA Community Reporting Tool

**Live Demo:** https://dbbun.github.io/crisis-mapper/

A community-facing damage reporting MVP enabling real-time crisis assessment.  
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
| 🤖 AI-assisted damage classification via DBbun backend | ✅ |

---

## RAPIDA Export Schema

GeoJSON output includes mandatory fields:

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
AI-assisted damage analysis
        ↓ SIMULATE
Synthetic damage datasets + scenario bundles
        ↓ EXPORT
RAPIDA-compatible outputs for analysts
```

---

## Deployment

### GitHub Pages

No build step. No dependencies. Single HTML file.

```bash
git clone https://github.com/DBbun/crisis-mapper
cd crisis-mapper
# Enable GitHub Pages in repo Settings → Pages → Deploy from main branch
```

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
- **AI:** AI-assisted damage classification via DBbun analysis backend
- **Export:** CSV + GeoJSON (RAPIDA schema)
- **Languages:** Built-in i18n (EN, FR, ES, AR, ZH, RU)

---

## License

© 2026 DBbun LLC. All rights reserved.

This prototype is submitted to the UNDP/Innocentive Crisis Mapping Challenge.
Source code is made available for evaluation purposes only.
Any commercial use, redistribution, or deployment requires written consent from DBbun LLC.
Contact: dbbun.com
