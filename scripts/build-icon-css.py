"""Regenerate the pixelarticons mask rules in custom.css.

Mintlify renders a page or card icon given as a path ("/icons/bell.svg") as an
<img>, which can't take a text color. Each rule below turns that <img> into a
mask over `currentColor`, so icons follow the theme (dim, hover, amber active).

The selectors match the path anywhere in the URL, not only at the end: in
production, card icons are served from mintcdn.com with a query string
(".../icons/zap.svg?fit=max&..."), while sidebar icons are not.

Run after adding an SVG to /icons:  python3 scripts/build-icon-css.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = "/* @icons:start */", "/* @icons:end */"

names = sorted(f[:-4] for f in os.listdir(os.path.join(ROOT, "icons")) if f.endswith(".svg"))
rules = "\n".join(
    f'img[src*="/icons/{n}.svg"] {{ -webkit-mask-image: url(/icons/{n}.svg); mask-image: url(/icons/{n}.svg); }}'
    for n in names
)
block = f"{START}\n{rules}\n{END}"

path = os.path.join(ROOT, "custom.css")
css = open(path, encoding="utf-8").read()
css = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, css, flags=re.S) if START in css else css + "\n" + block + "\n"
open(path, "w", encoding="utf-8").write(css)
print(f"{len(names)} icon rules written")
