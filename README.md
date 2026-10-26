# parker-mcdonnell.github.io

Parker McDonnell's site: soft robots that swim the way sea animals do. Built on [al-folio](https://github.com/alshedivat/al-folio) (MIT, v1.2) with its own look: the sea design from `concepts/ma-slideshow/`.

## Where things are

| To change | Edit |
|---|---|
| A work (paper, talk, tool, dataset...) | its file in `_projects/`, one per work: settings at the top, the page's text below in Markdown. It feeds the home page's slideshow (`featured: true`), the timeline and the work's own page. To add one, copy `_projects/_template.md` |
| The introduction on the home page | `_pages/home.md` |
| About, contact, links, education | `_pages/about.md`, in Markdown: the bio first, then a `##` heading for each part |
| Colours, fonts, the ocean, the timeline's motion | `_data/theme.yml` |
| A journal's accent colour on its papers' pages | `_data/venues.yml` (a work names it with `venue_key:`) |
| Where the sea creatures sit | open any page with `?arrange` at the end of its address, arrange, download, save as `_data/placements.yml` |
| Site name, address, description | `_config.yml` |

The page shell and layouts are in `_layouts/` (they override al-folio's own); the styles and behaviour are in `assets/sea/`.

## Building and publishing

- **`redesign`** is the working branch. Every push is built by `.github/workflows/build-check.yml`, which publishes nothing and keeps the built site as a download for 14 days.
- **`main`** is the live site. `.github/workflows/deploy.yml` builds it and publishes it to the `gh-pages` branch; GitHub Pages must serve from `gh-pages`. Nothing goes to `main` without Parker's OK.
- The 2024 site is kept on the `old-jekyll-site` branch.

**To preview** without installing anything: `python bin/preview.py` downloads the site GitHub last built from `redesign` and serves it at http://127.0.0.1:8000 (needs the GitHub CLI, signed in). To build on your own computer instead you need Ruby 3.3 and Bundler: `bundle install`, then `bundle exec jekyll serve`, which also rebuilds as you edit.

`HANDOFF.md` has the design decisions and what's still to do.
