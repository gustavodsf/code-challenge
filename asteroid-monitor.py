import requests
from datetime import datetime

BASE = "https://jsonmock.hackerrank.com/api/asteroids/search"

def _get_all_pages(param="asteroid"):
    page = 1
    results = []
    while True:
        resp = requests.get(BASE, params={"parameter": param, "page": page}, timeout=10)
        resp.raise_for_status()
        js = resp.json()
        data = js.get("data", [])
        results.extend(data)
        if page >= js.get("total_pages", 0):
            break
        page += 1
    return results

def _year_from_date(s):
    # discovery_date examples vary; be robust
    # Try parse with datetime, else fallback to last 4-digit year found
    if not s:
        return None
    # common formats: "2011-01-12", "2011 Jan 12", etc.
    for fmt in ("%Y-%m-%d", "%Y %b %d", "%d %b %Y", "%b %d, %Y", "%Y"):
        try:
            return datetime.strptime(s, fmt).year
        except Exception:
            pass
    # fallback: extract 4 consecutive digits
    import re
    m = re.search(r"(\d{4})", s)
    return int(m.group(1)) if m else None

def asteroidMonitor(year, pha):
    # Fetch all asteroids; the problem description suggests using keyword search,
    # but examples use the default parameter. We’ll pull all pages for generality.
    asteroids = _get_all_pages(param="asteroid")

    filtered = []
    for a in asteroids:
        disc_year = _year_from_date(a.get("discovery_date"))
        if disc_year != year:
            continue
        pha_val = a.get("pha")
        if pha_val != pha:
            continue
        # period_yr can be missing or non-numeric; treat missing as 0
        p = a.get("period_yr")
        try:
            period = float(p) if p is not None and p != "" else 0.0
        except Exception:
            period = 0.0
        filtered.append((period, a.get("designation", "")))

    # Sort: period_yr asc, then designation asc
    filtered.sort(key=lambda x: (x[0], x[1]))

    # Return only designations
    return [d for _, d in filtered]