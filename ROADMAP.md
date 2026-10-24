# Roadmap

Plans for Scouting Out Scouts, a Wood Badge ticket project to make Scouting easier to find, join and afford. The name comes from Ian's (Eagle Scout) fundraising book.

## The Scouting spirit behind this site
Everything we add should be something we'd be proud to share at a roundtable or a campfire.

- **A Scout is Trustworthy.** Every fact comes from an official source and every link is checked weekly. When we're not sure, we say so or leave it out.
- **A Scout is Helpful.** Write for the family who has never heard the word "den" and the volunteer with ten minutes to spare. Plain words, no jargon without an explanation.
- **A Scout is Friendly and Courteous.** Welcoming to every family, whatever their background, budget or experience. Never make anyone feel behind.
- **A Scout is Kind.** Skits, songs and humor build people up. No put-downs, no embarrassing anyone.
- **A Scout is Thrifty.** Help families save, swap and earn their own way, and point them to the help that exists so cost is never the reason a youth misses out.
- **A Scout is Clean and Reverent.** Nothing on the site that we wouldn't show a Cub Scout and their grandparents.
- **Official sources first.** Link to Scouting America's own published material rather than rewriting it, so the official version stays the source of truth.
- **Spread the load.** Every adult takes on a part of Scouting, so no one burns out and every family has a stake in the program.

## Ticket map: five goals, five lasting systems
The Wood Badge ticket's vision: every Scout can take part, whatever their family's finances, background or ability to pay. Each goal becomes a system that keeps running after the ticket is signed off. Every system has the same four parts:

1. **A home on the site** that anyone can find.
2. **A how-to** written so any adult can run it without help.
3. **A refresh rhythm**, automatic where possible and on a calendar where not.
4. **A hand-off**: who owns it next, written into MAINTAINING.md.

| Goal | The system | Home on the site | Refresh | Status |
|---|---|---|---|---|
| 1. Scoutbook advancement mentoring packet and toolkit | Scoutbook toolkit: a step-by-step guide plus a short recorded walkthrough, why up-to-date records matter, and a checklist for new advancement helpers | Guides → Keeping advancement up to date (links to official Scoutbook help) | Review each August before the program year | Toolkit page live; recorded walkthrough and training session to come |
| 2. Uniform and gear resource and referral system | Gear and uniform help: resource guide, the Scout It Out swap group (the virtual exchange), and a how-to for a portable unit uniform bin brought to meetings and bridging ceremonies | Save on Scouting | Swap group runs continuously; resource links checked every Monday | Live |
| 3. Scholarship and financial-aid navigation | Financial-aid navigator: every council, district and national camp and trip aid option with a yearly deadline calendar, plus a private way for families to ask for help (a form that goes only to unit leadership, never public) | Help paying (live) → expand with deadline calendar and private request link | Links checked every Monday; deadline calendar reviewed each fall before camp registration | Live; each unit sets up its own private form |
| 4. Opportunity-awareness system for parents | Opportunity finder: the site itself, updated automatically every week (more often than the quarterly sheet the goal calls for), plus a printable one-page sheet and a QR-code flyer for drop-off tables so parents reach it directly | Opportunities (live) → add printable sheet and QR flyer | Automatic every Monday | Live |
| 5. Recruit and mentor a merit badge counselor | Counselor pipeline: why counselors matter, how to apply, required training, and a short prep-conversation guide a mentor can use with any new recruit | Guides → Becoming a merit badge counselor | Reviewed yearly; links checked every Monday | Guide live; recruiting and mentoring are in-person steps |

### Suggested build order (by ticket deadline)
1. Goal 4 finishing touches: printable sheet and QR flyer (closest to done, and the first sheet is due within about two months).
2. Goal 1: Scoutbook toolkit (January 2027 deadline).
3. Goal 2: Save on Scouting page and uniform bin how-to (3 to 5 months).
4. Goal 3: deadline calendar and private request process (4 to 8 months).
5. Goal 5: counselor guide (4 to 6 months).
6. Then the rest of the roadmap: New to Scouting, Scouting is for everyone, Spanish, Fun Stuff.

### Notes for the ticket
- Goal 1's "Timely" box is still blank in the draft. A date such as "toolkit drafted by December 2026, training delivered by January 2027" would complete it.
- Privacy: personal contact details from the ticket worksheet stay off this public site.

## Done
- Opportunities list from 10 councils within about two hours of Laurel, MD (NYLT, ILST/ILSC, NAYLE, Wood Badge, BALOO/IOLS, merit badges, OA, camps), with Councils and Training path tabs.
- Site menu on every page and a shared look (`assets/`).
- Goal 1: Scoutbook Plus toolkit on Guides (recorded walkthrough still to come).
- Goal 2: Save on Scouting page with the Scout It Out swap group, NCAC's gear program and the uniform bin how-to.
- Goal 3: Help paying page with private-request steps for families and leaders, aid by council, national help and the yearly calendar.
- Goal 4: Printable one-page sheet and QR flyer (`print.html`).
- Goal 5: Becoming a merit badge counselor guide with a mentor's prep conversation, plus the 2026 Eagle-required list.
- About page mapping every goal to the Scout Oath and Law and the Wood Badge themes.
- Hand-off guide (`MAINTAINING.md`).
- Calendars page linking every council's official calendar.
- "Your ZIP code" distances, closest-first sort and distance filter, computed privately in the browser.
- Safe Scouting page: training, barriers to abuse, tenting rules, health forms, reporting and the Scouts First Helpline, all linked to official documents.
- "Official sources come first" disclaimer on every page.
- Weekly automatic update with a safety check, content standards and a link check of every page.

## Site layout when built
A small menu across the top of every page:

| Page | For |
|---|---|
| Opportunities (current home page) | Training, merit badge events, OA, camps, scholarships |
| New to Scouting | Parents and families just starting out |
| Save on Scouting | Families looking to cut costs |
| Guides | Merit badges, counselors, fundraising, adult roles |
| Fun Stuff | Recipes, skits, songs |
| Resources | Links to materials the team creates |

## Planned: New to Scouting (parent guide)
A friendly, non-intimidating first stop for families. Short sections, plain words, a glossary, and links to the official pages.

- **What Scouting is** and the programs by age:
  - Cub Scouts (packs and dens), by grade: Lion (K), Tiger (1st), Wolf (2nd), Bear (3rd), Webelos (4th), Arrow of Light (5th). Family involvement is part of the program. Girls have been welcome since 2017; family dens (co-ed) are allowed for Lion through Webelos since 2023.
  - Scouts BSA (troops and patrols). Earning Arrow of Light lets a youth join a troop at 10 instead of 11. Confirm current age rules on scouting.org when building.
  - Venturing, Sea Scouts and Exploring for older youth.
- **How Scouting is organized:** national Scouting America → council (ours is Baltimore Area Council) → district (ours is National Pike, Howard and SW Baltimore Counties) → your pack, troop, crew or ship, sponsored by a chartered organization.
- **Order of the Arrow:** Scouting's national honor society. Each council has one lodge (Baltimore's is Nentico Lodge) and each lodge has chapters that usually match districts (ours is the National Pike Chapter). Scouts are elected by their own troop. To be on the ballot: First Class rank, 15 nights of camping in the past two years including one long-term camp of at least five nights, and unit leader approval. Official site: oa-scouting.org. A 2020 chapter letter lists NationalPike@Nentico.org as the chapter contact; confirm before publishing.
- **Finding a pack or troop:** BeAScout (beascout.org, which goes to beascout.scouting.org), searchable by ZIP code. Also link each council's own "find a unit" page.
- **Keeping kids safe:** Youth Protection, two-deep leadership, the Guide to Safe Scouting, and how parents can take Youth Protection training too. Link only official scouting.org pages.
- **What it costs, honestly:** national fee (one council page lists $85 for youth in Cub Scouts, Scouts BSA, Venturing and Sea Scouts, $50 for Exploring, $65 for adults; confirm on scouting.org before publishing) plus a council fee that varies by council, plus unit dues, uniform and camp. Link straight to Save on Scouting.
- **Your first meeting:** what to expect, what to bring, questions to ask the unit leader.
- **Every adult has a role:** a gentle invitation to help, linking to the Guides page.
- **Glossary:** den, pack, patrol, troop, crew, ship, Akela, Cubmaster, Scoutmaster, SPL, blue card, Scoutmaster conference, board of review, Eagle, OA.

## Planned: Save on Scouting
Practical ways to lower the cost, local and national.

- **Gear and uniform swaps:**
  - **Scout It Out - Gear & Uniform Swap**: the team's private Facebook group for families around Laurel, MD (20708) to swap uniforms, Scouting gear and camping equipment. Open to families from any Scouting-type organization. Private to protect members; admins approve each request to join after three membership questions. Link: https://www.facebook.com/share/g/1Qb6uhd7Yv/ (approve this exact link only, not all of Facebook). On the site, explain that it's private, how to request to join, and summarize the group rules.
  - Group rules (written October 2026): 1 Be kind, courteous and friendly. 2 Keep our youth safe (adults only, no youth names or faces, adults arrange every swap). 3 Free first, fair always (no reselling or businesses). 4 Be trustworthy (honest descriptions). 5 Meet safely (public places, addresses by private message only). 6 Follow through. 7 Scouting items only (no swapping earned awards; knives, axes and fuel adult to adult; no firearms or ammunition). 8 Pay it forward. 9 Admins keep it safe (report harm to law enforcement or child protective services first; Scouting America concerns also to the Scouts First Helpline, 844-726-8871).
  - NCAC's H.O.S.T.I.N.G. committee (Helping Other Scout Troops Incorporate Needed Gear): uniforms and camping gear, pickup in Silver Spring, MD. See ncacscouting.org/resources/for-scouts/uniforms-and-gear-for-scouts/
  - Ask each council about a uniform closet or exchange; ask your unit about used-uniform bins and loaner gear.
- **Buying used or low-cost gear:** vetted outside sources for used camping gear and free community swaps. Each must be reviewed and added to the approved-link list one by one.
- **What you don't need to buy right away:** a starter list versus a "later" list, so new families don't overspend in the first month. Base it on official uniform and gear guidance.
- **Earning your own way:** popcorn and camp card sales, and the unit money-earning approval process for other fundraisers.
- **Financial help:** link to the Help paying tab (camperships, council fee assistance, Wood Badge and NYLT scholarships) plus national help such as the Military Family Fee Waiver (announced June 8, 2026; waives national registration fees for youth whose parent or guardian serves on active duty, in the Reserves or in the National Guard; families apply through their council).

## Planned: Guides
Step-by-step guides built from official Scouting America material, each linking to the source documents.

1. **Merit badges, focused on Eagle-required badges:** how the process works, the current Eagle-required list (checked against the official list when built, since it changes), and where to earn them locally.
2. **Becoming a merit badge counselor:** why counselors matter, the application, required training including Youth Protection, council approval, and who to contact in each council.
3. **Approved fundraising:** what Scouting America and the councils endorse, and the unit money-earning approval process, so units stay within the rules.
4. **Every adult has a role:** why it matters, the kinds of roles available (unit, district, council, counselor, trainer), and how to start.

## Planned: Fun Stuff
Just for fun, always in the Scouting spirit.

- **Camp recipes:** original, easy recipes for patrol and family camping (foil packets, Dutch oven cobbler, walking tacos, campfire banana boats, pancakes). Each with serving size, gear needed, and allergy and food-safety notes.
- **Skits:** short, original write-ups of classic campfire skit ideas. Every skit must pass the Scout-appropriate test: no put-downs, no bathroom or underwear humor, no making fun of anyone's background, nothing that embarrasses a participant. Scouting magazine has published guidance on this; read it and link it when building.
- **Songs:** full lyrics only for traditional songs old enough to be in the public domain (published before 1929, such as rounds like "Row, Row, Row Your Boat"). Popular modern campfire songs get a link to an official source instead of lyrics, so we respect copyright.

## Planned: Scouting is for everyone
A section that makes inclusion visible, linking to official resources: Scouts with disabilities and special needs (Baltimore has a Special Needs Committee), religious emblems for all faiths, girls and family dens, families new to the country, and making cost a non-issue.

## Planned: Languages
- A visible language switch at the top of every page: **English | Español** to start, more languages later if the community asks.
- Translate the parts new families rely on first: the menu, buttons and filters, New to Scouting, Save on Scouting, Help paying and Scouting is for everyone. Event titles from councils stay in their original English, with Spanish labels around them.
- Translations are prepared carefully, then reviewed by a fluent Spanish-speaking volunteer before they go live, so Scouting terms come out right.
- Point Spanish-speaking families to Scouting America's own Spanish-language materials, researched and verified when building.
- One switch changes the whole site, not one page at a time. The choice follows the visitor from page to page and is remembered on their next visit.
- If a visitor's phone or computer is set to Spanish, the site opens in Spanish automatically; the switch stays visible to change it.
- Every page keeps the same address in both languages.
- Where an official Spanish version of a linked page exists, Spanish readers get that link instead.

## Planned: Ticket summary and hand-off
- A one-page summary for the ticket counselor that follows the ticket map above, with evidence for each goal: what was built, where it lives, and how it keeps running.
- A hand-off guide (MAINTAINING.md) so other volunteers can keep the site going: how the Monday update and link check work, how to read the weekly email, how to fix or remove a listing on GitHub, how to add a resource, and who to contact. This is what makes the project self-sustaining after the ticket is complete.

## Planned: Resources section
- Permanent links to resources the team creates, kept separate from dated listings so the weekly update never removes them.
- Each new hosting location (Google Drive, a Google Site, the Facebook swap group) gets added to the approved-link list in `index.html` and `tools/check_data.py`, as an exact link where possible.

## Before building any of this
- Update CONTENT-STANDARDS.md: the approved-link list grows to include a few vetted, family-friendly outside resources, each reviewed by a person first.
- Extend the Monday link check to every page, not just data.json.
- Confirm every fact marked "confirm" above against the official page.
