# Working notes for this repo

Jekyll site (academicpages fork) published to jingwei-zuo.com via GitHub Pages
from `master`. Several designs, one set of facts.

The art-directed front pages are numbered editions. Each is a single
self-contained page (`layout: null`, its own CSS/JS inline) and each keeps its
old path as a `redirect_from`, so nothing that was ever linked goes dead:

| path | file | what it is |
| --- | --- | --- |
| `/` | `index.md` | nothing but `redirect_to: /v3/` — the root always points at the current edition |
| `/v1/` | `atelier.html` | first edition, the atelier (was `/atelier/`) |
| `/v2/` | `lab.html` | second, the overprint (was `/lab/`) |
| `/v3/` | `lab2.html` | **current front page** — WebGL attention field, three acts (was `/lab2/`) |

Alongside them:

- `/classic/` — `_pages/about.md`, the conventional academicpages design
  (was `/`, `/about/`, `/about.html`).
- `/blogs/` — the writing, in the current edition's language (see below).
- `/projects/` — hobby projects, academicpages design.
- `/90s.html` — a plain-HTML edition.

**Promoting a new edition** means two edits: point `index.md`'s `redirect_to`
at it, and give the outgoing edition a `/vN/` permalink with its old path in
`redirect_from`. Then re-point the cross-links: the `.doors` row and the
`#hero .top` link on each edition, and the header of `_layouts/blog-base.html`.

## Facts live in `_data/`, never in a template

`profile.yml` (name, English name, pronunciation, location + globe lat/lon,
discipline, intro), `publications.yml`, `experiences.yml`, `education.yml`,
`opensource.yml`, `services.yml`, `research.yml`, `news.yml`, `projects.yml`.

Every design reads the same file. If a fact has to be updated in two places,
that is a bug — move it into `_data/` and have both templates read it.

## Writing lives in `_blogs/`

Drop a Markdown file into `_blogs/`; nothing else needs editing. No date in the
filename — the slug *is* the filename, so `_blogs/my-post.md` serves at
`/blogs/my-post/`.

```markdown
---
title: "My post title"
date: 2026-09-28
excerpt: "One or two sentences; used on the cards and as the page's <lede>."
tags: [Agents, Research]     # optional
og_image: /images/blogs/x.png # optional, defaults to the profile photo
---
```

Every surface reads `site.blogs` and sorts newest-first, so one file appears in
four places at once: the index at `/blogs/`, the *Things I wrote* section on
`/v3/`, the Blogs section on `/classic/`, and the neighbour links at the foot of
each post. Post images go in `images/blogs/` and are referenced absolutely, in a
`<figure class="blog-figure">`.

- `_layouts/blog-base.html` — the shell: night at the edges, paper where the
  reading happens. It **restates** `/v3/`'s tokens and type rather than sharing
  them (a `layout: null` page loads no theme CSS). If a colour or face changes in
  `lab2.html`, change it here too.
- `_layouts/blog-post.html` — one post, inside that shell.
- `_pages/blogs.html` — the index, inside that shell.
- `_includes/blog-list.html` + the "Blog cards" block in `assets/css/main.scss`
  — the `/classic/` rendering only.

Being `layout: null`, these pages hit the trap below: they include
`analytics.html` explicitly **and** carry their own `.visitor-widget` hiding
rule.

## Build and preview

No Ruby locally; build in Docker and serve the **built** output — never judge a
change by reading the source.

```sh
docker build -t drleft-jekyll .                      # once
docker run --rm -v "$PWD":/usr/src/app -w /usr/src/app \
  drleft-jekyll bundle exec jekyll build             # writes _site/ (owned by root)
cd _site && python3 -m http.server 8123 --bind 127.0.0.1
```

Screenshots via Playwright (`pip install playwright && playwright install chromium`,
launch with `--enable-unsafe-swiftshader` for WebGL). Disable smooth scrolling
before measuring: `document.documentElement.style.scrollBehavior = 'auto'`.

## Double-check support on every platform before shipping

Anything visual ships only after it has been *seen* in each of these. This list
exists because each line is a bug that actually reached the live site.

- **Device pixel ratio 1 _and_ 2.** A whole build was verified at DPR 1 only,
  which hid that `<canvas>` is a *replaced* element: with `width:auto`, an
  absolutely positioned one takes its intrinsic (drawing-buffer) size and
  `right` is ignored, so `inset:0` never stretched it and the canvas laid out at
  twice the viewport on every HiDPI screen. Related: `gl_PointSize` is in
  framebuffer pixels, so point sizes must scale with the pixel ratio.
- **Viewport shapes**, not just widths: wide-and-short (1566×780) alongside
  1512×950, 1920×1080, 2560×1440 and 412×900. Short viewports overflow the hero;
  wide ones expose rail/content collisions.
- **No horizontal overflow.** `html`/`body` use `overflow-x: clip`, so overflow
  is *invisible* — there is no scrollbar to notice. Assert
  `document.documentElement.scrollWidth === clientWidth`, and check that every
  section shares one left and right edge (an `#id { padding: … }` shorthand beats
  `.wrap`'s side padding and silently removes a section's gutters).
- **Gutter assertion.** Walk every `.wrap` and compare content-box insets:
  they must all share one left and one right value at each width. An
  `#id { padding: … }` shorthand silently zeroes the side gutters (it has bitten
  three sections of the front page and then the figure on /lab/), and overflow
  tests do not catch it because nothing overflows.
- **`prefers-reduced-motion: reduce`** — curtain, reveals and all motion off, no
  console errors.
- **No WebGL / CDN blocked** (route `**/three*.js` to abort): the page must set
  `body.nofield`, hide the held stage and the copy that refers to the field, and
  stay readable.
- **Keyboard focus** visible on every link, and no console/`pageerror` output on
  any of the above.

## Other things that have bitten

- **This file must stay in `_config.yml`'s `exclude:`.** It is not site
  content, and while a local `jekyll build` copies it harmlessly, the GitHub
  Pages build failed silently for ten minutes with it present (it contains
  literal Liquid delimiters in the note below). Nothing deployed until it was
  excluded. The same goes for any new repo-level `.md`.
- When a push does not appear live, check whether a page added two commits ago
  is serving before assuming slowness: a canary file proves whether the build
  ran at all. Pages gives no error at the URL, only an email to the owner.
- `jekyll-redirect-from` must stay in **both** `plugins:` and `whitelist:` in
  `_config.yml`; the gem being installed is not enough, and without it every
  `redirect_from` in the repo is silently dead.
- `overflow-x: hidden` on `body` breaks `position: sticky`; use `clip`.
- The `mapmyvisitors` counter rides `_includes/analytics.html`, which the theme
  layouts include. A `layout: null` page must include it explicitly (and hide
  `.visitor-widget` itself, since the theme CSS that hides it is not loaded).
- `atelier.html` is Liquid-rendered: never write a literal `{{` or `{%` inside
  its CSS or JS.
- Emoji and CJK need a declared webfont (`Noto Serif SC`, subset with `&text=`)
  or they render as tofu; prefer drawn SVG marks over emoji.

## Deploying

Commit and push to `master`; GitHub Pages rebuilds in ~60–90s. Then verify the
live URL, not just the local build.
