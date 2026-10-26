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

## Parker's notes of 2026-10-25, all done the same day

Parker: "the site is looking awesome". Then:

1. **Moon jellyfish:** wavy tentacles, the four stomachs in a ring at the top of the bell, each turned 35 degrees so it swims diagonally (its bob runs along its own axis).
2. **Light shafts:** toned down, and gone a little under a screen down.
3. **Bubbles:** the ones by the name rise through the swell and vanish at it (motion `surface`).
4. **Sailboats:** two (one near, one far and faint) cross the swell left to right now and then, rocking. The water line was lowered so they fit, and the headline brought up.
5. **QR codes:** sunk into the page with an inner shadow, the code kept clear of it.
6. **Arrange mode (placing by hand):** "Arrange the sea" in the footer, shown only to editors of the Artifact (and always when served locally). Motion stops; drag a drawing to move it, its corner to size it, the knob above it to turn it (Shift snaps to 15 degrees), the cross to hide it on this page, the plus to copy it (a copy is named after its original, as `sea-6+k3x`, exists only on the page and screen where it was made, and its cross removes it). The page leaves room below itself for the arrange bar, so the sea floor can be scrolled up above it. Each placement is kept per page and per screen size (wide or narrow), pinned to the heading, work or other piece of the page above it, so it survives text changes; the sea floor is one placement for every page. **Where it's saved:** in the Artifact, its own store (collection `placements`, one document per `page~screen`, `{items: {...}}`; only editors can write). Served locally, this browser, with a "Download placements.yml" button. **To bring Parker's placements into the repository:** read the store (`ArtifactData list placements`) and write it into `concepts/ma-slideshow/placements.yml` (the format is described at its top), which the page reads first. Not tested by hand inside the Artifact yet; tested locally (move, size, turn, hide, saving, reloading).

- **Blocks over the sea** (Parker, 2026-10-25): the creatures sit behind the page, and each block of words (timeline cards, headings, paragraphs, links, QR) stands on a ground that hides what swims behind it. `ocean.blocks` in `theme.yml`, also a footer button: `soft` (frosted, fading edge; the default) or `none`. Sunken text blocks were tried and dropped: Parker wants only the pictures sunken.
- **Pictures sunk into the page** (Parker, 2026-10-25): every picture (slides, timeline thumbnails, related work) has a hairline border, a fine light edge just inside and a soft inner shadow, drawn over the picture so real photos and video sit in it the same way.
- **The timeline unfolds as you scroll** (Parker's ideas, 2026-10-25; `timeline.unfold`, footer button "Unfold"). Four ways to compare, all scroll-linked (scrolling back reverses them), all simply open for viewers who ask for less motion or with the sea still:
  - `fold` (the default; Parker: "your method is super cool"): each card folds down open from its top edge, an origami crease across its middle flattening as it opens; curves and nodes fade in; the kelp stalk grows down ahead of the reader. Swinging sideways from the spine was tried first; Parker wanted it vertical.
  - `scroll`: the timeline unrolls like a paper scroll above a paper roll that travels down ahead of the reader.
  - `light` (Parker: "I love the submarine"): a line-drawn submarine goes to the work being read and lights it with a warm lamp; the other works wait dim. It rides the kelp line at the clear spot nearest its work's node (clear of every node and year label, below if that's as near as above), and turns so its nose and lamp point straight at the middle of the work (Parker: on the line, never over a dot, the light in line with the way it faces). The beam is sized to the card so the light pools on it, and the lit work casts soft shadows away from the lamp (text and picture; Parker's idea). Tried and dropped on the way: on the spine over the node, across the spine from the work, in the gap above the curve, and below the card on a fixed 45 degree line.
  - `fade`: works fade in slowly, rising a little, and the kelp leaves fade in with them.
  - `grow` (Parker's idea): each work grows like a leaf: its node appears, then its line draws out, then the card grows outward from the spine and fades in.
  - `focus` (Parker's idea): a vignette. The work in the middle of the screen is sharp and solid; works further up or down fade and blur, their nodes and lines with them.
  Parker's verdict so far: Fold's 3D look and Scroll are out; Grow good but zoomed too much (now only 6%); Submarine loved. Fold is still the default until he picks. The kelp leaves were made bigger (and a little further apart) the same day, and Selected work has no soft grounds (Parker: no shading there).
- **Undo asks first, and Bring back** (Parker lost his placements to one stray click, 2026-10-25): "Undo this page" needs a second click within 4 seconds; what it removes is kept (the store's `placements-undone` collection, or this browser), and "Bring back" restores the last undo of that page and screen size, even after a reload.
- **The sub hides behind the slideshow** (Parker, 2026-10-25): from beside the headline it sinks down the right side behind the slideshow (`.show` has z-index 1, above the timeline), comes out below it and waits in the gap above "Selected work", then glides to the kelp line as the first work reaches the reading line. Parker's alternatives, not built: narrow the slideshow a little so the sub fits beside it, or turn the sub so only its beam shows past the slideshow.
- **Sub beside the kelp; see-through slideshow** (Parker, 2026-10-25, "let's see what it looks like"): along the timeline the sub swims 92px off the stalk on the side opposite the work it lights, level with that work's node, and shines across the stalk at it (on a phone it still rides the line). While diving, its lamp reaches all the way to the left edge of the page. In Submarine mode the slideshow's picture area is 70% opaque, so the sub shows faintly as it passes behind (real pictures and video will be opaque, so it will show only around them).
- **Focus is the default** (Parker, 2026-10-25: "focus is the default and then submarine is an option"); its blur at the screen edges is now 1.6px. In Submarine mode the sub starts in the open water just right of the headline, level with its middle and facing it, far enough back (22% of the screen past the end of the text) that its lamp's cone has opened over the ends of both lines; the beam starts from a point at the lamp; flooding both lines and narrowing to a short glow as it sinks; the sub is drawn bigger (scale 1.15, .8 on a phone) (Parker, 2026-10-25), and sinks straight down the right side as the reader scrolls, easing after the scroll rather than moving with it 1:1 (which juddered), level (Parker: a tilted dive looked weird), passing over the slideshow with its lamp dimmed, and in the last stretch glides across to its spot on the kelp line by the first work as that work reaches 45% down the screen. The floor explorer travels by a composited `translate` in container units (`cqw`) rather than animating `left`, which snapped to whole pixels and juddered at its slow pace.
- **Evenly spaced timeline** (Parker, 2026-10-25: "the order and year matter, not realistic timing"): works sit in order, newest first, an even step apart on alternating sides; a year label sits where each year begins (halfway between the last work of the year before and the first of its own); `space_per_year` is gone. The kelp stalk is drawn in the text colour (white on dark) and no longer faded, so it's easy to follow. Focus mode is sharp across the middle 40% of the screen and blurs only lightly toward the edges (Parker: too blurry, focus sooner).
- **Timeline lines join the pictures** (Parker, 2026-10-25: "like it is part of it"): each curve runs from its node into the spine-side edge of the work's picture frame, level with its middle, with no end dot, and arches up on its way like a leaf's stalk even when node and frame are level (Parker: curved, organic, never straight). Measured from the layout, not the screen, so cards caught mid-animation no longer throw the lines off (that was why they missed).
- **More life** (Parker, 2026-10-25): fish tails flick now and then, as if turning in and out of the page (`.tail`); crab claws wave wide and slow (`.claw`); glints twinkle in the sun rays, and each ray shimmers at its own pace. The introduction has no soft ground, so the rays fall across it.
- **Explorer submarine on the sea floor** (Parker, 2026-10-25): on every page a submarine patrols just above the sand, slowly (150 s for a round trip), stopping at each end to look around, its lamp sweeping down over the creatures (`.explorer`).
- **Each creature keeps its own time** (Parker, 2026-10-25): a pace between 0.75 and 1.35 fixed by its name (`--pace`) slows or quickens its pulse and tail flicks; the fish in a school flick out of step; an Arrange copy gets its own pace and start, never its original's.
- **Jellyfish tentacles vary** (Parker: "too uniform"): uneven spacing, length, curl and drift, from fixed pseudo-random numbers so they look the same on every visit.
- **Jellyfish pulse** (Parker, 2026-10-25): the bell squeezes in fast and the jellyfish lurches forward along its slant, then relaxes slowly, each on its own rhythm (`.beat`).
- **Perched drawings can be arranged too:** the crab on the footer line and the bubbles by the slideshow (placements under `perch~wide` / `perch~narrow`, across and down from the piece they sit on).

## Next steps

1. ~~Fix and verify the page switching~~ Done 2026-10-25; the Artifact is linked in the table above.
2. Keep refining the concept with Parker ("jam" on it); there's no rush to go live. Open choices: which header bar is the default (thin now, or full width), and the robot outlines to add to the ocean.
3. Once Parker approves, build the real site on al-folio in this style on `redesign`. One file per work should feed the slideshow, the timeline and the list. Add schema.org metadata and links to Scholar and ORCID.
4. Only with Parker's OK: merge to `main` to go live.
