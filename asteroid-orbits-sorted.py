import requests
import re
from datetime import datetime

BASE = "https://jsonmock.hackerrank.com/api/asteroids/search"

def _fetch_all(param="asteroid"):
    page = 1
    results = []
    while True:
        r = requests.get(BASE, params={"parameter": param, "page": page}, timeout=10)
        r.raise_for_status()
        data = r.json()
        results.extend(data.get("data", []))
        if page >= data.get("total_pages", 0):
            break
        page += 1
    return results

def _extract_year(date_str):
    if not date_str:
        return None
    for fmt in ("%Y-%m-%d", "%Y %b %d", "%d %b %Y", "%b %d, %Y", "%Y"):
        try:
            return datetime.strptime(date_str, fmt).year
        except Exception:
            pass
    m = re.search(r"(\d{4})", date_str)
    return int(m.group(1)) if m else None

def asteroidOrbits(year, orbitclass):
    orbitclass = orbitclass.lower().strip()
    asteroids = _fetch_all("asteroid")
    filtered = []
    for a in asteroids:
        disc_year = _extract_year(a.get("discovery_date"))
        if disc_year != year:
            continue
        oc = (a.get("orbit_class") or "").lower()
        if orbitclass not in oc:
            continue
        try:
            p = float(a.get("period_yr", 1) or 1)
        except Exception:
            p = 1
        filtered.append((p, a.get("designation", "")))
    # Sort by period then designation
    filtered.sort(key=lambda t: (t[0], t[1]))
    return [d for _, d in filtered]