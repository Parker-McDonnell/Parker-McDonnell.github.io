"""Make the site's assets/sea/sea.css and sea.js from the concept (concepts/ma-slideshow/index.html), adapted from one
file with #pages to a Jekyll site: settings, placements and a paper's citations come from the page (Jekyll data), each
part runs only on the pages that have it, links are real pages, and Arrange is offered only when asked for (?arrange)."""
import re
import sys
from pathlib import Path

concept, out = Path(sys.argv[1]), Path(sys.argv[2])
html = concept.read_text(encoding="utf-8")
css = html[html.index("<style>\n") + len("<style>\n"):html.index("</style>")]
js = html[html.index("<script>\n") + len("<script>\n"):html.rindex("</script>")]

def sub(text, a, b, count=1):
    assert text.count(a) == count, (text.count(a), a[:90])
    return text.replace(a, b)

css = sub(css, "/* Concept A, \"Catalogue\": a quiet catalogue.", "/* Parker McDonnell's site: the sea design, carried from concepts/ma-slideshow into al-folio. A quiet catalogue.")
css = "/* Made from concepts/ma-slideshow/index.html; change the concept and remake this, or edit here once the concept is retired. */\n" + css

# settings: from _data/theme.yml, which the layout writes into the page, instead of fetching theme.yml
js = sub(js, """// Settings: theme.yml is read once the page has loaded and handed to every part of the page that uses it.""",
         """// Settings: _data/theme.yml, written into the page by the layout, is applied once the page has loaded and handed to
// every part of the page that uses it.""")
js = sub(js, """  addEventListener('load', async () => {
    try {
      const text = await (await fetch('theme.yml', { cache: 'no-store' })).text();
      s.set(jsyaml.load(text));
    } catch (e) { console.warn('theme.yml not read; using the built-in look', e); }
  });""", """  addEventListener('load', () => { if (window.SITE_THEME) s.set(window.SITE_THEME); });""")

# placements: from _data/placements.yml, written into the page
js = sub(js, "Placements come from placements.yml beside this page, then from the\n// Artifact's own store (where Arrange saves when the page is an Artifact) or this browser (when it is not).",
         "Placements come from _data/placements.yml (written into the page),\n// then from this browser, where Arrange saves; Arrange is offered when the address ends in ?arrange.")
js = sub(js, """  fetch('placements.yml').then(r => r.ok ? r.text() : '').then(t => { if (t && window.jsyaml) { merge(jsyaml.load(t)); resettle(); } }).catch(() => {});""",
         """  merge(window.SITE_PLACEMENTS || {});
  const asked = new URLSearchParams(location.search).has('arrange');""")
js = sub(js, """      try { merge(JSON.parse(localStorage.getItem('placements') || '{}')); } catch {}""",
         """      if (asked) try { merge(JSON.parse(localStorage.getItem('placements') || '{}')); } catch {}""")
js = sub(js, """      resettle();
      offerArrange();
    }""", """      resettle();
      if (asked) offerArrange();
    }""")
js = sub(js, "const text = '# Where the sea creatures sit, placed by hand with Arrange.",
         "const text = '# Where the sea creatures sit, placed by hand with Arrange: save as _data/placements.yml.")
# js-yaml is not loaded on the site; the placements download writes YAML by way of JSON (YAML reads JSON)
js = sub(js, "jsyaml.dump(placements)", "JSON.stringify(placements, null, 1)")

# QR codes: the site's address at the foot, this page's own address on a work's page
js = sub(js, """  const NAME = { home: 'this site', paper: 'this paper', talk: 'this talk', tool: 'this tool' };
  site.use(cfg => {
    const base = (cfg.qr?.site_url || location.href).split('#')[0];""", """  site.use(cfg => {
    const base = cfg.qr?.site_url || location.origin + '/';""")
js = sub(js, """      const page = fig.dataset.qr, url = page === 'home' ? base : `${base}#${page}`;""",
         """      const page = fig.dataset.qr, url = page === 'home' ? base : location.href.split(/[?#]/)[0];""")
js = sub(js, "`<figcaption>Scan to open ${NAME[page]} on your phone</figcaption>`",
         "`<figcaption>Scan to open ${page === 'home' ? 'this site' : fig.dataset.name || 'this page'} on your phone</figcaption>`")

# pages: each is its own page now; only the #works link is still a place on the home page
start = js.index("// Pages: show the one named in the address")
end = js.index("// Slideshow: touch swiping")
js = js[:start] + """// Pages: each work and the about page are pages of their own; a link to #works scrolls to the timeline.
if (location.hash === '#works') addEventListener('load', () => document.getElementById('works')?.scrollIntoView());

""" + js[end:]

# each part runs only where its piece of page is
js = sub(js, """  const show = document.querySelector('.show'), box = document.getElementById('frames');
""", """  const show = document.querySelector('.show'), box = document.getElementById('frames');
  if (!box) return;
""")
start = js.index("  const refs = [\n")
end = js.index("  const examples = [")
js = js[:start] + "  // [doi, year, title, authors, journal], from the work's `cites:` front matter\n  const refs = window.PAGE_CITES || [];\n" + js[end:]
js = sub(js, "  const map = document.getElementById('cmap'), svg = map.querySelector('.cmap-lines'), node = map.querySelector('.cmap-node');",
         "  const map = document.getElementById('cmap');\n  if (!map) return;\n  const svg = map.querySelector('.cmap-lines'), node = map.querySelector('.cmap-node');")
js = sub(js, "// Citation map: the paper's reference list as deposited with Crossref (fetched 25 October 2026), newest first,\n// each joined to the paper by a curve. The real site would fetch these, and the works that cite it, when it is built.",
         "// Citation map: the paper's reference list as deposited with Crossref (its `cites:` front matter), newest first,\n// each joined to the paper by a curve. Works that cite it are still to come (from Crossref or OpenAlex at build time).")
js = sub(js, "  const feed = document.getElementById('feed'), items = [...feed.children];",
         "  const feed = document.getElementById('feed');\n  if (!feed) return;\n  const items = [...feed.children];")
js = sub(js, "  const play = document.getElementById('play');\n", "  const play = document.getElementById('play');\n  if (!play) return;\n")

out.mkdir(parents=True, exist_ok=True)
(out / "sea.css").write_text(css, encoding="utf-8", newline="\n")
(out / "sea.js").write_text("// Made from concepts/ma-slideshow/index.html; change the concept and remake this, or edit here once the concept is retired.\n" + js,
                            encoding="utf-8", newline="\n")
print("ok", len(css.splitlines()), len(js.splitlines()))
