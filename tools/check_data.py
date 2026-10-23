#!/usr/bin/env python3
"""Safety check for data.json. Every automatic update must pass this before it is published.

Usage: python3 tools/check_data.py data.json [previous_data.json]
Exits non-zero with a list of problems if anything fails.
"""
import json
import re
import sys
from datetime import date
from urllib.parse import urlparse

# Same list the page enforces. Links anywhere else are rejected.
APPROVED = [
    "scouting.org", "scoutingevent.com", "247scouting.com", "summitbsa.org", "nesa.org",
    "baltimorescouting.org", "broadcreekscouting.org", "ncacscouting.org", "gotosnyder.org",
    "delmarvacouncil.org", "sacscouting.org", "newbirthoffreedom.org", "padutchbsa.org", "cccbsa.org",
    "hovc.org", "scoutingphilly.org", "virginiaheadwaters.org",
]
TYPES = {"NYLT", "ILST / ILSC", "NAYLE", "Wood Badge", "BALOO / IOLS", "Adult Training",
         "Merit Badge", "Order of the Arrow", "Camp"}
AUDIENCES = {"Youth", "Adult", "Both"}
STATUSES = {"open", "soon", "tentative", "tba"}
# Words that never belong on a Scouting youth site. A hit blocks publishing for human review.
BLOCKED_WORDS = [
    "porn", "xxx", "nude", "naked", "sex", "escort", "onlyfans", "casino", "gambling", "bet ",
    "beer", "wine", "liquor", "alcohol", "cannabis", "marijuana", "vape", "dating", "hookup",
    "crypto", "bitcoin", "viagra", "nsfw",
]
MAX_LEN = 400
MAX_REMOVALS = 15


def host_ok(url):
    try:
        u = urlparse(url)
    except Exception:
        return False
    if u.scheme not in ("http", "https") or not u.hostname:
        return False
    h = u.hostname.lower()
    return any(h == d or h.endswith("." + d) for d in APPROVED)


def walk_strings(obj, path=""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f"{path}[{i}]")


def is_date(s):
    try:
        date.fromisoformat(s)
        return True
    except Exception:
        return False


def main():
    problems = []
    data = json.load(open(sys.argv[1]))
    for key in ("lastChecked", "councils", "opportunities", "aid"):
        if key not in data:
            problems.append(f"missing top-level key: {key}")
    councils = {c.get("id") for c in data.get("councils", [])}

    for path, s in walk_strings(data):
        low = s.lower()
        if len(s) > MAX_LEN:
            problems.append(f"{path}: text longer than {MAX_LEN} characters")
        if re.search(r"<[a-z!/]", low) or "javascript:" in low or "data:" in low:
            problems.append(f"{path}: contains markup or a script/data link")
        for w in BLOCKED_WORDS:
            if re.search(r"\b" + re.escape(w.strip()) + r"\b", low):
                problems.append(f"{path}: contains blocked word '{w.strip()}'")

    for c in data.get("councils", []):
        for l in c.get("links", []):
            if not host_ok(l.get("url", "")):
                problems.append(f"council {c.get('id')}: link not on approved list: {l.get('url')}")

    ids = set()
    for o in data.get("opportunities", []):
        oid = o.get("id", "?")
        if oid in ids:
            problems.append(f"duplicate id: {oid}")
        ids.add(oid)
        if o.get("council") not in councils:
            problems.append(f"{oid}: unknown council {o.get('council')}")
        if o.get("type") not in TYPES:
            problems.append(f"{oid}: bad type {o.get('type')}")
        if o.get("audience") not in AUDIENCES:
            problems.append(f"{oid}: bad audience {o.get('audience')}")
        if o.get("status") not in STATUSES:
            problems.append(f"{oid}: bad status {o.get('status')}")
        if not o.get("title"):
            problems.append(f"{oid}: missing title")
        for f in ("start", "end"):
            v = o.get(f)
            if v is not None and not is_date(v):
                problems.append(f"{oid}: {f} is not YYYY-MM-DD: {v}")
        if o.get("start") and o.get("end") and o["end"] < o["start"]:
            problems.append(f"{oid}: end before start")
        if not host_ok(o.get("url", "")):
            problems.append(f"{oid}: link not on approved list: {o.get('url')}")

    for a in data.get("aid", []):
        if a.get("council") not in councils:
            problems.append(f"aid '{a.get('title')}': unknown council")
        if not host_ok(a.get("url", "")):
            problems.append(f"aid '{a.get('title')}': link not on approved list: {a.get('url')}")

    if len(sys.argv) > 2:
        prev = json.load(open(sys.argv[2]))
        prev_ids = {o["id"] for o in prev.get("opportunities", [])}
        removed = prev_ids - ids
        if len(removed) > MAX_REMOVALS:
            problems.append(f"{len(removed)} opportunities removed at once (limit {MAX_REMOVALS}); needs a human look")
        if {c["id"] for c in prev.get("councils", [])} - councils:
            problems.append("a council was removed; needs a human look")

    if problems:
        print("CHECK FAILED:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print(f"CHECK PASSED: {len(ids)} opportunities, {len(councils)} councils, {len(data.get('aid', []))} aid entries")


if __name__ == "__main__":
    main()
