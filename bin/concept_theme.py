"""_data/theme.yml for the site, from the concept's theme.yml: no playground buttons, no made-up citations, QR codes to
the real address."""
import sys
from pathlib import Path

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
lines = src.read_text(encoding="utf-8").split("\n")
out = []
for l in lines:
    if l.startswith("  site_url: \"\""):
        l = '  site_url: "https://parker-mcdonnell.github.io/"   # the address the QR codes at the foot of each page point to'
    elif l.startswith("  demo: true"):
        l = "  demo: false                         # true shows made-up citing papers, marked \"Example\" (for the concept only)"
    elif l.startswith("playground: true"):
        l = "playground: false                     # the concept's footer buttons for trying options; off on the site"
    out.append(l)
text = "\n".join(out)
assert 'site_url: "https://parker' in text and "demo: false" in text and "playground: false" in text
head = ("# The site's look and behaviour, read by every page (the layout writes it into the page for assets/sea/sea.js).\n"
        "# Started from concepts/ma-slideshow/theme.yml on 2026-10-25; this file now decides the site, the concept's only the concept.\n")
dst.write_text(head + text, encoding="utf-8", newline="\n")
print("ok")
