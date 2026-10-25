# Hand-off: personal site redesign

## Goal

Replace Parker's 2024 Jekyll "freelancer" site with a calm, gallery-like portfolio served by GitHub Pages at `parker-mcdonnell.github.io`. It should have its own page for each paper, talk, and tool or method. The first paper to feature is his Science Advances paper.

Parker asked for "simple and sleek", like a "high class art gallery", using a known template. Keep the minimal look (lots of empty space, restrained type, one accent colour, large images, quiet motion), but **no Japanese characters, symbols or words**. Parker felt they edge toward cultural appropriation, so they were removed on 2026-10-24.

## Rules

- **Never push to `main`.** That publishes the live site, and Parker must approve it first. All work goes on `redesign`.
- The old site is saved on the `old-jekyll-site` branch, which is pushed.
- Don't use any journal figure until its licence is checked (see below).
- Keywords Parker uses: (discuss) means talk only, (write up) means draft without committing, (go) means commit and push. With no keyword, go ahead as usual.

## What's here (`concepts/`)

| Folder | Concept | Template it maps to | Artifact (on Parker's first account) |
|---|---|---|---|
| `ma-slideshow/` | **A, slideshow version (chosen)** | al-folio (Jekyll, MIT) | https://claude.ai/artifact/PJHdr9E6CvwNrVoKcZF7Yw (current, published 2026-10-25). The older https://claude.ai/artifact/PRwmShLz2V284Kcv4Vx2di is out of date: it still shows the Japanese numerals |
| `ma/` | A, grid version | al-folio | https://claude.ai/artifact/H4SUKqzrhAq9f8De9g8zHt. **Out of date:** it still shows the Japanese numerals and the old "Ma" name |
| `gallery/` | B, dark gallery | HTML5 UP (CC BY 3.0, credit required) | https://claude.ai/artifact/1WUCMSHQCEicC1af8ujYVV |
| `scroll/` | C, margin-notes layout | Quarto | https://claude.ai/artifact/E17noUvrL5YJcRbhvM5dkK |

`concepts/README.md` compares the templates, their licences and the trade-offs. The Artifacts belong to the first account. A session on another account should publish fresh Artifacts from the files rather than update these ones.

## Decided

- **Concept A, slideshow version.** It's a single readable column. At the top is a swipeable slideshow of featured work, which snaps into place, advances every 6 seconds and pauses while touched. Below that is "Selected work", which is itself a timeline centred down the page (see the theme file section).
- **Colours:** Journal Light, matching Parker's comps slides (Journal Crimson is the alternative).
- **Parker's reactions so far (2026-10-25):** loved the timeline with icons and dates, and the faded curves to every work ("super cool", "very snazzy"). He found the side timeline disconnected from the page, and thought the centre or branch versions might be better. The ocean must stay "a slight flourish, not overbearing or distracting". He wants the page's own pieces to be part of the sea (a crab on a card, plants growing from works, bubbles passing in front).
- **Template:** al-folio was recommended, but Parker hasn't said yes to it explicitly.
- **Paper details from Crossref:** "Plenty of fish in the sea, but only one multimodal feather star robot". Parker McDonnell and Nicole W. Xu. *Science Advances* 12(41), eaem0495, 9 October 2026. doi `10.1126/sciadv.aem0495`.

## Built and checked (`ma-slideshow/index.html`)

One file holds all five pages (home, paper, talk, tool, about), and `#home`, `#paper`, `#talk`, `#tool` or `#about` picks which one shows. The paper page has a video-loop slot, related work, a citation map and "In the media". The look comes from `theme.yml`, and footer buttons try its options. To publish the Artifact, send `theme.yml` along as a `text/plain` file (the Artifact host doesn't serve `.yml`).

**Page switching works** (checked 2026-10-25 over a local HTTP server at 375 px and 1280 px wide): from the menu, the list, the timeline dots, the slideshow, typed and reloaded addresses, and the back button. The earlier failure was the preview opening the file from disk. Pages are marked with `data-page`, not an `id`, so the browser doesn't jump partway down the page as it would to a fragment; keep it that way. To test locally, serve the folder (`python -m http.server`) rather than opening the file.

## Still waiting on Parker

1. Final yes on al-folio as the template. The other options were plain HTML or Quarto.
2. **The paper's figure licence.** Science Advances publishes some articles as CC BY and some as CC BY-NC, and Crossref listed none for this one. Check the article page before putting up any figure.
3. Real content: summary, key findings, talk details, bio, portrait, email, ORCID, Scholar link, CV, and his list of works. Everything apart from the paper's details is placeholder.
4. ~~Whether to keep the vertical name in the margin.~~ Removed 2026-10-25: the vertical timeline now uses that margin.

## The theme file (`concepts/ma-slideshow/theme.yml`)

Fonts, the colour palette, column width, slideshow speed, the timeline's style and the citation demo are all set in `theme.yml`. The page reads it on load and falls back to the built-in Journal Light look if it can't (for example when opened from disk). It's YAML because al-folio is Jekyll: the same file can move to `_data/theme.yml` on the real site and be read at build time.

- **Palettes:** Journal Light (the default, matching the comps slides) and Journal Crimson are copied from `PhD-Comps-Exam/Code/themes/palettes/*.json`, each with its dark version. If those change, copy them again. "Warm paper" is the concept's first look, kept for comparison.
- **Playground:** footer buttons try palettes, the ocean, accent bars, the spine, card marks and the citation demo for that visit only. Nothing is remembered, so the file stays the one place the look is decided. Set `playground: false` for the real site.
- **Citation demo:** `citation_map.demo: true` fills "cited by" with three made-up papers marked "Example". Turn it off once real citations exist.
- **Accent bars:** `accent_bars.header` (none, thin, thick, or band across the full window) and `accent_bars.sections` (none, short dash, or full line above each section heading). Parker asked for a splash of colour to break up the sections.
- **Timeline (decided 2026-10-25: the centred timeline only, with every work shown):** the work list is the timeline. A spine runs down the middle, works alternate sides, and each sits at its date on a fixed scale (`timeline.space_per_year`), so gaps in time show as gaps on the page. Cards are pushed down only to clear the one above, and a faded accent curve joins each to its exact date, the work being read in full colour. Works on one date stack their nodes. The spine is a kelp stalk (`timeline.spine: kelp`, Parker's idea) that sways, has leaves between works and rises from a holdfast, or a straight line. Each card carries an icon for its kind (`timeline.marks: icon`; `number` counts from the oldest work like a reference list; `dot` shows none). On phones the spine runs down the left and the scale stretches to fit the cards. Three of the works (a dataset, SignalShepherd 2.0, a poster) are made-up placeholders.
- **Tried and dropped (2026-10-25):** a list with a separate timeline at its side (left or right, with labels and curves), and two git-graph versions: branches per project that fold to their headline, and a lane per kind of work. Parker chose the centred one. They're in the git history (`be0b89b`, `1428e57`) if they're wanted again.
- **Ocean** (`ocean.enabled`, `ocean.motion`; Parker's idea, "a slight flourish, not distracting"): scrolling down sinks through the water. The page shades a little toward the accent at the bottom. One thin sine line drifts at the top (Parker's choice, after trying three), and light shafts fall from a sun up to the right, fading out over the first screen and a bit of scrolling (`ocean.light_shafts`). Fish, a school, moon jellyfish, bubbles and the feather star robot swim **inside the reading column**, not the margins (Parker, 2026-10-25: "part of the center of the website"), a few of them just under the surface by his name. Each has a place written in the `SEA` list, and the page moves it to the nearest open water clear of every word, picture and control; one with no room near its place is not shown (so phones show fewer). Drawings vary in size and fade with distance (the last number in each entry, 0 far to 1 near), so the water has depth. Every page ends on a sea floor with a crab, a sea urchin, rocks, kelp and grass, with smaller, fainter ones further back. Parker's rules for the drawings: only fish and jellyfish (moon jellyfish) float in open water, never plants, and nothing grows on the selected-work cards (removed at his request). Bubbles and the robot stay because he asked for them. Some drawings sit on the page itself: a crab on the footer line, and bubbles rising past the slideshow. All motion is very slow and stops for viewers who ask for less motion. The drawings and their places are the `ART`, `SEA`, `FLOOR` and `PERCH` lists in the page script. Parker wants outline drawings of the lab's robots added over time. Keep the waves plain swells, never a Japanese wave pattern.

## Added 2026-10-25 (Parker's ideas)

- **Citation map** on the paper page: what the paper cites on the left, the paper in the middle, what cites it on the right (stacked on phones). It holds the 9 references Crossref had on 25 October 2026, and nothing cites the paper yet. On the real site, the build should fetch both sides (Crossref references, OpenAlex or OpenCitations for "cited by") and link works that are Parker's own to their pages. A site-wide map joining all his papers is a possible later step.

- **QR codes** (Parker, 2026-10-25): the footer has one for the site, and the paper, talk and tool pages each have one for that page, so a visitor at a poster or talk can open it on a phone. They're drawn in the page (qrcode-generator 1.4.4 from cdnjs) as dark squares on a light tile in both themes. They point at `qr.site_url` in `theme.yml`, or at the page's own address while that is empty; set it to `https://parker-mcdonnell.github.io/` for the real site. In the Artifact the codes point at the Artifact's inner frame, which won't open on a phone, so judge them there by look only.

## Next steps

1. ~~Fix and verify the page switching~~ Done 2026-10-25; the Artifact is linked in the table above.
2. Keep refining the concept with Parker ("jam" on it); there's no rush to go live. Open choices: which header bar is the default (thin now, or full width), and the robot outlines to add to the ocean.
3. Once Parker approves, build the real site on al-folio in this style on `redesign`. One file per work should feed the slideshow, the timeline and the list. Add schema.org metadata and links to Scholar and ORCID.
4. Only with Parker's OK: merge to `main` to go live.
