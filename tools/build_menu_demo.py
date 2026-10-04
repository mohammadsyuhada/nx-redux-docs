"""Build the landing page's mobile main menu demo from the nx-mobile mockup.

The mockup (nx-mobile/.local/main-menu-mockup/nx-showcase.html) is a working
design file: a heading, the option rows, the phone screen, the pad, then design
notes. The demo keeps the options, the screen and the pad, drops the heading
and the notes, and sits on the landing page's black so it reads as part of it.

Run from the repo root: python tools/build_menu_demo.py [path/to/nx-showcase.html]
"""
import re
import sys
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else
           "../nx-mobile/.local/main-menu-mockup/nx-showcase.html")
OUT = Path("docs/assets/landing/mobile/menu-demo.html")


def cut(html, pattern, what):
    html, n = re.subn(pattern, "", html, count=1, flags=re.S)
    if n != 1:
        sys.exit(f"build_menu_demo: could not find {what} in {SRC}")
    return html


html = SRC.read_text(encoding="utf-8")
html = cut(html, r'\n  <header class="top">.*?</header>\n', "the heading")
html = cut(html, r'\n  <div class="notes">.*?\n  </div>\n(?=</div>)', "the notes")
html = html.replace("<title>NX Showcase Menu</title>", "<title>NX Redux main menu</title>", 1)
# a first visit opens game lists on Backdrop, Vertical, so their Orientation and Vertical alignment
# options show (they only appear under Carousel / Backdrop, alignment only when Vertical)
for old, new in (('games: "grid" };', 'games: "bd" };'),
                 ('tools: "h", games: "h" };', 'tools: "h", games: "v" };')):
    if html.count(old) != 1:
        sys.exit(f"build_menu_demo: could not find the default {old!r} in {SRC}")
    html = html.replace(old, new)
if not html.lstrip().lower().startswith("<!doctype"):
    html = '<!doctype html>\n<meta name="viewport" content="width=device-width, initial-scale=1">\n' + html
# the landing page's black, no page padding: the iframe sits inside the page's own column
html = html.replace("</style>", """
/* landing page demo (tools/build_menu_demo.py) */
:root { --page: #000; }
body { margin: 0; padding: 0 0 4px; }
.wrap { max-width: none; }
</style>""", 1)
OUT.write_text(html, encoding="utf-8")
print(f"{OUT}: {len(html) / 1e6:.2f} MB")
