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

- **Concept A, slideshow version.** It's a single readable column. At the top is a swipeable slideshow of featured work, which snaps into place, advances every 6 seconds and pauses while touched. Below that is a timeline (one row each for papers, talks, tools and methods, marks placed by date and linked both ways to the list), then the "Selected work" list.
- **Template:** al-folio was recommended, but Parker hasn't said yes to it explicitly.
- **Paper details from Crossref:** "Plenty of fish in the sea, but only one multimodal feather star robot". Parker McDonnell and Nicole W. Xu. *Science Advances* 12(41), eaem0495, 9 October 2026. doi `10.1126/sciadv.aem0495`.

## Built and checked (`ma-slideshow/index.html`)

The latest commit adds talk, tool and about pages, a richer paper page (video-loop slot, related work, "In the media"), a vertical name in the margin on wide screens, and a footer switcher for Vermilion, Indigo and Moss accents. One file holds all five pages, and `#home`, `#paper`, `#talk`, `#tool` or `#about` picks which one shows.

**Page switching works** (checked 2026-10-25 over a local HTTP server at 375 px and 1280 px wide): from the menu, the list, the timeline dots, the slideshow, typed and reloaded addresses, and the back button. The earlier failure was the preview opening the file from disk. Pages are marked with `data-page`, not an `id`, so the browser doesn't jump partway down the page as it would to a fragment; keep it that way. To test locally, serve the folder (`python -m http.server`) rather than opening the file.

## Still waiting on Parker

1. Final yes on al-folio as the template. The other options were plain HTML or Quarto.
2. **The paper's figure licence.** Science Advances publishes some articles as CC BY and some as CC BY-NC, and Crossref listed none for this one. Check the article page before putting up any figure.
3. Real content: summary, key findings, talk details, bio, portrait, email, ORCID, Scholar link, CV, and his list of works. Everything apart from the paper's details is placeholder.
4. ~~Whether to keep the vertical name in the margin.~~ Removed 2026-10-25: the vertical timeline now uses that margin.

## The theme file (`concepts/ma-slideshow/theme.yml`)

Fonts, the colour palette, column width, slideshow speed, the timeline's style and the citation demo are all set in `theme.yml`. The page reads it on load and falls back to the built-in Journal Light look if it can't (for example when opened from disk). It's YAML because al-folio is Jekyll: the same file can move to `_data/theme.yml` on the real site and be read at build time.

- **Palettes:** Journal Light (the default, matching the comps slides) and Journal Crimson are copied from `PhD-Comps-Exam/Code/themes/palettes/*.json`, each with its dark version. If those change, copy them again. "Warm paper" is the concept's first look, kept for comparison.
- **Playground:** footer buttons try palettes, timeline marks, dates and the demo for that visit only. Nothing is remembered, so the file stays the one place the look is decided. Set `playground: false` for the real site.
- **Citation demo:** `citation_map.demo: true` fills "cited by" with three made-up papers marked "Example". Turn it off once real citations exist.
- **Timeline marks:** `dot`, `number` (counted from the oldest work, like a reference list, so new works don't renumber old ones) or `icon` (paper, talk, tool, method), with or without dates. The same mark appears in the list entry.

## Added 2026-10-25 (Parker's ideas)

- **Vertical timeline.** "Selected work" is now a list of entries with thumbnails. While it is on screen, a timeline runs down the side: in the left margin on wide screens (years, a dot per work, the current entry's name), and as a thin rail in the right gutter on phones. It marks the entry being read as you scroll, and a click on a dot or anywhere on the rail scrolls to the nearest entry. It replaces the horizontal timeline.
- **Citation map** on the paper page: what the paper cites on the left, the paper in the middle, what cites it on the right (stacked on phones). It holds the 9 references Crossref had on 25 October 2026, and nothing cites the paper yet. On the real site, the build should fetch both sides (Crossref references, OpenAlex or OpenCitations for "cited by") and link works that are Parker's own to their pages. A site-wide map joining all his papers is a possible later step.

## Next steps

1. ~~Fix and verify the page switching~~ Done 2026-10-25; the Artifact is linked in the table above.
2. Keep refining the concept with Parker ("jam" on it); there's no rush to go live.
3. Once Parker approves, build the real site on al-folio in this style on `redesign`. One file per work should feed the slideshow, the timeline and the list. Add schema.org metadata and links to Scholar and ORCID.
4. Only with Parker's OK: merge to `main` to go live.
