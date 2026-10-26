"""_data/placements.yml from the placements Parker arranged in the concept Artifact (its store, read 2026-10-25)."""
import json
import sys
from pathlib import Path

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
# the store holds only the page~screen layouts arranged in that Artifact, so each replaces its own in the file and
# the rest of the file is kept (the file is JSON under a comment header)
out = {}
if dst.exists():
    text = dst.read_text(encoding="utf-8")
    out = json.loads(text[text.index("{"):])
for f in sorted(src.glob("*.json")):
    doc = json.loads(f.read_text(encoding="utf-8"))
    key = f.stem.replace("@", "~")
    items = doc.get("items", doc.get("data", {}).get("items"))
    assert isinstance(items, dict), (f, list(doc)[:5])
    out[key] = items
head = ("# Where the sea creatures sit, placed by hand. Parker arranged these in the concept (2026-10-25, again 2026-10-26); they were copied\n"
        "# from its store. To change them: open any page with ?arrange at the end of its address, arrange the drawings, then\n"
        "# \"Download placements.yml\" and save it over this file. Keyed by page~screen (wide or narrow), then drawing.\n"
        "# Written as JSON, which YAML reads as it is.\n")
dst.write_text(head + json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
print("from the store:", sorted(f.stem.replace("@", "~") for f in src.glob("*.json")), {k: len(v) for k, v in out.items()})
