# Content standards

Scouting Out Scouts is for Scouts, families and volunteers. Everything on it must be accurate and appropriate for a Scouting America youth audience. These rules apply to people and to the automatic weekly update alike.

## What belongs
- Scouting America programs only: NYLT, ILST/ILSC, NAYLE, Wood Badge, BALOO, IOLS and other leader training, merit badge events, Order of the Arrow, council camps, and scholarships or financial aid for these.
- Councils within about two hours of Laurel, MD, plus national courses open to everyone.

## Accuracy
- Link to Scouting America's own published material instead of rewriting it, so the official version stays the source of truth.
- Every date, fee and link must come from an official council page, scoutingevent.com, scouting.org or summitbsa.org. Never guess. If a detail isn't posted, leave it blank or mark the course "dates not posted".
- Past events are removed after they end.

## What never goes on the site
- Links to anything other than the approved official Scouting sites (the list is in `index.html` and `tools/check_data.py`).
- Images, video, HTML or code inside `data.json`.
- Anything sexual, violent, hateful, or about alcohol, drugs, gambling or dating.
- Fundraisers, social events for adults, committee meetings and roundtables.
- Personal phone numbers or emails, except a course contact the council itself published for that course.

## Safeguards
1. The page only shows text from `data.json`, never markup, and only links to approved sites.
2. Every automatic update runs `python3 tools/check_data.py data.json <previous copy>`. If the check fails, the update is not published and the owner is emailed the reasons.
3. An update that would remove more than 15 listings or any council stops for a human look.
4. Each weekly run emails the owner a summary of what changed, so a person reviews every change.
5. Every Monday, every link on the site is checked. Links that are broken, moved or retired are reported to the owner for a decision, not silently removed.
6. Only the `scoutinginclusive` account and collaborators it adds can change the repository.

## Reporting a problem
If anything on the site looks wrong or inappropriate, edit `data.json` to remove it (or revert the latest commit on GitHub), then tell the owner.
