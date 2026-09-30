#!/usr/bin/env python3
"""Render the link-preview card for a blog post.

    python3 _tools/og_card.py move-slowly-in-the-agentic-era

reads _blogs/<slug>.md (title, title_em, date) and writes
images/blogs/<slug>-og.png at 1200x630, in the site's own fonts and colours.
Point the post's `og_image` at that path. With no slug it writes the generic
card, images/blogs/og-default.png, used when a post names none.

Needs Playwright with Chromium (see CLAUDE.md) and network access for the
Google Fonts the site itself uses.
"""
import asyncio, datetime, html, os, re, sys, tempfile, shutil
from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def front_matter(slug):
    src = open(os.path.join(ROOT, "_blogs", slug + ".md"), encoding="utf-8").read()
    fm = re.match(r"---\n(.*?)\n---", src, re.S).group(1)
    def get(k):
        m = re.search(r"^%s:\s*(.+)$" % k, fm, re.M)
        return m.group(1).strip().strip('"\'') if m else ""
    return get("title"), get("title_em"), get("date")

def page(title, em, kicker):
    t = html.escape(title)
    if em:
        t = t.replace(html.escape(em), "<em>%s</em>" % html.escape(em), 1)
    return """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400&display=block" rel="stylesheet">
<style>
html,body{margin:0;width:1200px;height:630px;overflow:hidden}
body{background:#07080c;color:#f4f1ea;position:relative;font-family:"Instrument Serif",Georgia,serif}
body::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(70% 90% at 12% 110%,rgba(226,73,42,.22),transparent 60%),
             radial-gradient(50% 60% at 95% -10%,rgba(217,164,65,.10),transparent 60%)}
.k{position:absolute;left:88px;top:78px;right:88px;display:flex;align-items:center;gap:18px;
  font:400 17px/1 "JetBrains Mono",monospace;letter-spacing:.26em;text-transform:uppercase;color:#d9a441}
.k::after{content:"";flex:1;height:1px;background:currentColor;opacity:.32}
h1{position:absolute;left:84px;right:88px;top:138px;margin:0;font-weight:400;
  font-size:@SIZE@px;line-height:.98;letter-spacing:-.02em;text-wrap:balance}
h1 em{font-style:italic;color:#e2492a;text-shadow:0 0 60px rgba(226,73,42,.35)}
.sig{position:absolute;left:88px;bottom:70px;display:flex;align-items:center;gap:26px}
.seal{width:104px;height:104px;background:#e4e9ed;padding:6px;box-sizing:border-box;transform:rotate(-3.5deg);
  box-shadow:0 14px 40px -16px rgba(226,73,42,.8)}
.seal img{width:100%;height:100%;display:block}
.who{font-size:36px;line-height:1.05}
.who small{display:block;margin-top:10px;font:400 15px/1 "JetBrains Mono",monospace;letter-spacing:.24em;
  text-transform:uppercase;color:rgba(244,241,234,.45)}
</style></head><body>
<div class="k">@KICKER@</div>
<h1>@TITLE@</h1>
<div class="sig"><div class="seal"><img src="seal.jpg"></div>
<div class="who">Jingwei (Chris) Zuo<small>jingwei-zuo.com</small></div></div>
</body></html>""".replace("@TITLE@", t).replace("@KICKER@", html.escape(kicker)) \
                   .replace("@SIZE@", "112" if len(title) <= 34 else "92")

async def render(markup, out):
    d = tempfile.mkdtemp()
    try:
        shutil.copy(os.path.join(ROOT, "images", "seal.jpg"), d)
        open(os.path.join(d, "card.html"), "w", encoding="utf-8").write(markup)
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": 1200, "height": 630})
            await pg.goto("file://" + os.path.join(d, "card.html"), wait_until="networkidle")
            await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=out)
            await b.close()
    finally:
        shutil.rmtree(d)

def main():
    os.makedirs(os.path.join(ROOT, "images", "blogs"), exist_ok=True)
    if len(sys.argv) > 1:
        slug = sys.argv[1]
        title, em, date = front_matter(slug)
        when = datetime.date.fromisoformat(date[:10]).strftime("%B %Y") if date else ""
        kicker = "Blogpost" + (" \u00b7 " + when if when else "")
        out = os.path.join(ROOT, "images", "blogs", slug + "-og.png")
    else:
        title, em, kicker = "Writing", "", "Blog"
        out = os.path.join(ROOT, "images", "blogs", "og-default.png")
    asyncio.run(render(page(title, em, kicker), out))
    print(os.path.relpath(out, ROOT))

if __name__ == "__main__":
    main()
