# Content standards

Scouting Out Scouts is for Scouts, families and volunteers. Everything on it must be accurate and appropriate for a Scouting America youth audience. These rules apply to people and to the automatic weekly update alike.

## What belongs
- Scouting America programs, plus guidance for families and volunteers on joining, saving money, paying for Scouting, advancement and becoming a counselor.
- Listings are Scouting America programs only: NYLT, ILST/ILSC, NAYLE, Wood Badge, BALOO, IOLS and other leader training, merit badge events, Order of the Arrow, council camps, Scout-facing council and district events and activities (camporees, STEM days, range days, service projects, Life to Eagle seminars), and scholarships or financial aid for these.
- Councils within about two hours of Laurel, MD, plus national courses open to everyone.

## Accuracy
- Link to Scouting America's own published material instead of rewriting it, so the official version stays the source of truth.
- Every date, fee and link must come from an official council page, scoutingevent.com, scouting.org or summitbsa.org. Never guess. If a detail isn't posted, leave it blank or mark the course "dates not posted".
- Past events are removed after they end.

## What never goes on the site
- Links to anything other than the approved official Scouting sites (the list is in `assets/site.js` and `tools/check_data.py`). The written pages may also link to a short list of reviewed exceptions: the Scout It Out swap group on Facebook and this project's own GitHub repository. Each new exception is reviewed by a person and added here first.
- Images, video, HTML or code inside `data.json`.
- Photos of people, unless everyone pictured has agreed (and a parent or guardian has agreed for anyone under 18). Photos never carry names, and their hidden location data is removed before upload. Photos appear only on the written pages, never in `data.json`.
- Anything sexual, violent, hateful, or about alcohol, drugs, gambling or dating.
- Listings for fundraisers, social events for adults, committee meetings and roundtables. (Guidance on approved ways to earn money, on the Save on Scouting page, is fine.)
- Personal phone numbers or emails, except a course contact the council itself published for that course.

## Safeguards
1. Pages only show text from `data.json`, never markup, and only link to approved sites. The written pages (`help.html`, `save.html`, `guides.html`, `about.html`) are written and reviewed by people, and the automatic update never edits them.
2. Every automatic update runs `python3 tools/check_data.py data.json <previous copy>`. If the check fails, the update is not published and the owner is emailed the reasons.
3. An update that would remove more than 15 listings or any council stops for a human look.
4. Each weekly run emails the owner a summary of what changed, so a person reviews every change.
5. Every Monday, every link on the site is checked. Links that are broken, moved or retired are reported to the owner for a decision, not silently removed.
6. Only the `scoutinginclusive` account and collaborators it adds can change the repository.
7. Visitor privacy: the ZIP-code distance feature runs entirely in the visitor's browser using the published `assets/zips.json` table. No ZIP code or other visitor information is ever sent anywhere or collected.

## Reporting a problem
If anything on the site looks wrong or inappropriate, edit `data.json` to remove it (or revert the latest commit on GitHub), then tell the owner.
