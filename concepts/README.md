# Site redesign: three concepts

Each folder holds one static mock-up: a home page, then a sample paper page further down the same file (the "Paper" link jumps to it). All content is placeholder. No journal figures are used yet: the Science Advances article's licence (CC BY or CC BY-NC; it varies by article) still needs checking on the article page before any figure goes up.

All three share one approach: lots of empty space, two typefaces, one accent colour, large image areas, and very little motion (a slow hover, nothing else). All three work in light and dark mode.

| | A · Catalogue (`ma/`) | B · Gallery (`gallery/`) | C · Scroll (`scroll/`) |
|---|---|---|---|
| Feel | A quiet catalogue on pale paper, works listed like a museum's object index | A dark exhibition room: big tiles, each with a small wall label | An asymmetric reading page like a hanging scroll, with margin notes |
| Accent | Vermilion | Muted gold | Indigo |
| Base template | [al-folio](https://github.com/alshedivat/al-folio), a Jekyll theme for academics | [HTML5 UP Multiverse or Lens](https://html5up.net), plain HTML/CSS/JS | A [Quarto](https://quarto.org) website |
| Licence | MIT | CC BY 3.0: a visible "Design by HTML5 UP" credit must stay (or buy a Pixelarity licence) | Open-source tool; the site you make with it is yours |
| GitHub Pages | Builds with a GitHub Actions workflow (comes with the theme) | Served as-is, no build at all | Rendered locally with `quarto publish gh-pages`, or by an Actions workflow |
| Adding a paper | Add a BibTeX entry to `_bibliography/papers.bib` and a short Markdown page. The publications list and cite box come from the BibTeX | Copy a paper page's HTML file, edit the text, add a tile to the home grid by hand | Add a `.qmd` (Markdown) file to `papers/`. The listing page picks it up by itself |
| Adding a talk or tool | A Markdown file in `_projects/` with a category | Copy a page and add a tile | A `.qmd` file in `talks/` or `tools/` |
| Good at | Academic plumbing out of the box: BibTeX publications, CV, Scholar and ORCID links, schema markup. Large user base | Images first; looks most like an art gallery. Nothing to install, nothing to break | Writing-heavy pages, margin notes, figures and code rendered from Python notebooks |
| Weak at | Heavy theme: a lot to strip back to get this calm look, and updates from upstream can conflict | Every page is hand-edited HTML, so lists get out of step as the site grows. Attribution credit is required | Needs Quarto installed; the default look must be restyled to get here |

## Recommendation

**A (al-folio)** if the main job is a page per paper with a cite box, and you want BibTeX to drive it, since findability (Scholar, ORCID, schema.org) comes nearly for free later.
**B** if the gallery feeling matters most and the site will stay small.
**C** if you expect to write longer explainers with figures generated from your own code.

The look and the template can be mixed: any of the three looks can be put on any of the three templates. The table is about the plumbing.
