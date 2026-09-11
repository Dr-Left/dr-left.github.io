# Working notes for this repo

Jekyll site (academicpages fork) published to jingwei-zuo.com via GitHub Pages
from `master`. Two designs, one set of facts:

- `/` — `atelier.html`, a single self-contained art-directed page (`layout: null`,
  WebGL field, its own CSS/JS inline).
- `/classic/` — `_pages/about.md`, the conventional academicpages design.
- `/90s.html` — a plain-HTML edition.

## Facts live in `_data/`, never in a template

`profile.yml` (name, English name, pronunciation, location + globe lat/lon,
discipline, intro), `publications.yml`, `experiences.yml`, `education.yml`,
`opensource.yml`, `services.yml`, `research.yml`, `news.yml`, `projects.yml`.

Every design reads the same file. If a fact has to be updated in two places,
that is a bug — move it into `_data/` and have both templates read it.

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
