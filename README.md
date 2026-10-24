# Scouting Out Scouts

Scouting America opportunities (NYLT, ILST/ILSC, NAYLE, Wood Badge, BALOO/IOLS, merit badge events, Order of the Arrow, camps) and scholarships from councils within about two hours of Laurel, MD.

- `index.html` (Opportunities), `calendars.html` (Calendars), `help.html` (Help paying), `save.html` (Save on Scouting), `guides.html` (Guides), `about.html` (About) and `print.html` (printable sheet and flyer) are the pages.
- `data.json` holds every opportunity, council and scholarship. Edit this file to add or change listings; no page needs editing for that.
- `assets/` holds the shared styles, shared code (including the approved-link list) and the QR code.
- `MAINTAINING.md` is the hand-off guide for volunteers.

## Editing data.json by hand
Each opportunity looks like this:

```json
{ "id": "bac-nylt-281", "council": "bac", "type": "NYLT", "audience": "Youth", "status": "open",
  "title": "NYLT 2028-1 (Spring)", "start": "2028-04-21", "end": "2028-05-21",
  "location": "Camp Oest, Broad Creek", "cost": "$275", "url": "https://scoutingevent.com/220-...", "note": "" }
```

- `type`: NYLT, ILST / ILSC, NAYLE, Wood Badge, BALOO / IOLS, Adult Training (shown as "Other adult courses"), Merit Badge, Order of the Arrow, Camp, Activity (shown as "Events & activities")
- `audience`: Youth, Adult or Both
- `status`: open, soon (dates set, registration not open), tentative (save the date), tba (dates not posted)
- `start` / `end`: YYYY-MM-DD, or null when not posted. Past events hide themselves automatically.

Always confirm dates on the council's own page before registering.

## Automatic updates and safety
A scheduled Claude task checks the councils every Monday morning, updates `data.json`, runs `tools/check_data.py`, and commits only if the check passes. See [CONTENT-STANDARDS.md](CONTENT-STANDARDS.md) for the rules every listing must follow.
