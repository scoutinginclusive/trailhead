# Keeping Scouting Out Scouts going

A hand-off guide for any volunteer. No coding needed for the everyday jobs.

## How the site works
- **Pages:** `index.html` (Opportunities), `help.html` (Help paying), `save.html` (Save on Scouting), `guides.html` (Guides), `about.html` (About) and `print.html` (printable sheet and flyer).
- **The list:** every course, event, council and aid link shown on Opportunities, Help paying and the printable sheet comes from `data.json`.
- **Shared look:** `assets/site.css` (styles), `assets/site.js` (shared code and the approved-link list), `assets/qr-site.svg` (QR code to the site).
- **Hosting:** GitHub Pages, free, with HTTPS. Any change committed to the `main` branch is live within a couple of minutes.

## What happens automatically every Monday morning
1. A scheduled Claude task checks each council's event listings and course pages.
2. It adds new courses, updates dates and registration status, and removes events that have ended.
3. It checks every link on the site and reports any that are broken, moved or retired.
4. It runs the safety check (`tools/check_data.py`). Only if the check passes is the update published.
5. The owner gets an email and phone notification summarizing what changed, the link health, and anything that needs a person to decide.

## Weekly job: read the Monday email (5 minutes)
- **Changes:** skim for anything that looks wrong.
- **Link health:** for each flagged link, open it yourself. If it's really gone, remove or replace it (see below). "Could not check" often just means a site blocked the automatic check, or that it's the private Facebook group.
- **Needs a human:** make the call, or ask the council.

## Fixing or removing a listing
1. Sign in to GitHub as the site account and open `data.json`.
2. Click the pencil icon to edit.
3. Find the listing (use Ctrl+F or Cmd+F for its title) and change or delete it. Each listing sits between `{ }`; if you delete one, also delete the comma that separated it from the next.
4. Click **Commit changes**. The site updates in a couple of minutes.
5. If something breaks, open the file's **History**, pick the last good version, and restore it.

Every field is explained in `README.md`. Every listing must follow `CONTENT-STANDARDS.md`.

## Yearly job: refresh the Help paying calendar (each fall, about 30 minutes)
1. Open each council's campership or financial-aid page (linked on Help paying).
2. Note this year's opening dates and deadlines.
3. Edit the "Through the year" table in `help.html` and replace last season's dates.
4. Commit.

## Yearly job: review the guides (each August)
- Check the Scoutbook steps in `guides.html` against Scoutbook Plus's own help pages, since screens change.
- Check the Eagle-required list against scouting.org.
- Train any new advancement helpers using the EDGE steps on the Guides page.

## Each quarter: print and share
Open the **printable sheet** (`print.html`), print it, and leave copies at drop-off and pick-up tables, in newsletters and at parent meetings. It always shows the next three months, so there's nothing to edit.

## Adding a new outside website
The site only links to approved Scouting websites. To add a new one:
1. Make sure it's an official council or Scouting America site, or a family-friendly resource that a person has reviewed.
2. Add its domain to the list in **both** `assets/site.js` and `tools/check_data.py`.
3. Note the addition in `CONTENT-STANDARDS.md`.

## Handing over to the next volunteer
- Give them access to the GitHub account (or add them as a collaborator under Settings → Collaborators).
- The Monday scheduled task belongs to the Claude account that created it. A new owner can recreate it from their own Claude account by asking Claude to set up the weekly update described in this file.
- Walk them through this guide using EDGE: explain it, show them one Monday email, let them handle the next one with you nearby, then let them run it.
