# Deployment Instructions — CrisisMapper

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `crisis-mapper`
3. Set to **Public**
4. Click "Create repository"

## Step 2: Push Files

```bash
cd crisis-mapper/
git init
git add .
git commit -m "Initial CrisisMapper MVP — UNDP crisis reporting tool"
git branch -M main
git remote add origin https://github.com/DBbun/crisis-mapper.git
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repo → Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: `main` / `/ (root)`
4. Click Save
5. Wait 2-3 minutes
6. Your URL: `https://DBbun.github.io/crisis-mapper/`

## Step 4: Add Render Proxy (for AI feature in demo)

1. Add `crisis_proxy.py` to your existing Render app
2. Set environment variable: `ANTHROPIC_API_KEY=sk-ant-...`
3. Add the route to your Flask app
4. Update `DBBUN_PROXY` in `index.html`:
   ```javascript
   var DBBUN_PROXY = 'https://your-app.onrender.com/analyze-damage';
   ```
5. Push updated index.html to GitHub

## Step 5: Test

- Open `https://DBbun.github.io/crisis-mapper/` on mobile
- Take a photo, select damage level, pick location
- Submit → check Dashboard tab
- Export CSV and GeoJSON
- Test language toggle
- Test offline: turn off WiFi, submit report, turn on WiFi, verify sync toast

## Step 6: Record Demo Video (2 minutes)

Script:
1. (0:00) Open app on mobile, show language toggle → switch to French
2. (0:15) Tap Report tab → take/upload a damage photo
3. (0:30) Tap "Analyze with DBbun AI" → show AI classification result
4. (0:45) Apply suggestion, fill infrastructure/crisis type, set GPS location
5. (1:00) Submit → show success toast
6. (1:10) Switch to Map tab → show colored pin on map, tap popup
7. (1:30) Switch to Dashboard → show stats, table, export CSV
8. (1:45) Show GeoJSON file opened in text editor
9. (1:55) Show offline badge by disabling WiFi, submit another report
10. (2:00) End

## Submission Checklist

- [ ] Live URL working on mobile
- [ ] 2-minute demo video recorded
- [ ] Written proposal drafted
- [ ] GeoJSON export sample attached
- [ ] CSV export sample attached
- [ ] Submitted on Innocentive by June 23, 2026 11:59 PM ET
