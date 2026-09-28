# Mobile docs and landing page — design

Date: 2026-09-28
Branch: `feat/mobile-docs-landing`

## Goal

Add documentation for NX Redux Mobile (`../nx-mobile`) to this site next to the
existing handheld docs, and put a showcase landing page in front of both.

Readers mostly use one platform, so each platform gets its own docs section,
and a header toggle switches between them. Shared conventions are written once.

## Decisions

- One MkDocs Material site, one build, one repo. The domain stays nxredux.com.
- Two parallel sections, `handheld/` and `mobile/`, each with its own sidebar.
- A platform toggle in the header switches between the two sections.
- Mobile starts small and grows as its features ship.
- The landing page uses drawn device frames with real screenshots inside,
  not photos.
- The devices shown are the **TrimUI Brick Pro** and the **Samsung Galaxy
  Z Fold 8, folded, on its cover screen**.
- Mobile is unreleased, so the landing page shows a "Coming soon" badge for
  it. Its docs are still reachable.
- The "Why NX Redux?" blurb moves from the home page to the Handheld overview.

## Part 1 — Docs structure

```
docs/
  index.md              landing page (custom template, no sidebar, no TOC)
  handheld/             all current pages, moved unchanged
    index.md            current home content + "Why NX Redux?" blurb
    getting-started.md, desktop.md, netplay.md
    guide/, apps/, emulators/, settings/
  mobile/
    index.md            overview, "coming soon" note
    getting-started.md  install, choosing the home folder
    library.md          home folder, extra folders, Unassigned, Rescan library
    controls.md         touch pad, controllers, game-list context menu
    emulators.md        cores per system (melonDS DS, mupen64plus-next,
                        PPSSPP, pcsx_rearmed …; no Dreamcast yet)
  _shared/              snippet fragments only, never pages
    folder-layout.md, map-txt.md, collections.md, saves.md
  reference/            shared by both platforms
    release-notes.md    split under "Handheld" / "Mobile" headings
    faq.md, credits.md, disclaimer.md
```

### Navigation

- Top tabs: **Handheld | Mobile | Reference** (`navigation.tabs`). Each tab's
  sidebar lists only its own pages.
- The landing page (`index.md`) is outside the tabs and has no sidebar.

### Platform toggle

- `overrides/main.html` extends the Material base and adds a two-state
  Handheld / Mobile control to the header.
- `docs/javascripts/platform-switch.js`:
  - Switching swaps the `handheld/` ↔ `mobile/` path prefix. If that page
    does not exist, it goes to the other section's `index`.
  - Existence check: a MkDocs hook (`hooks/platform_pages.py`, registered
    under `hooks:`) writes `platform-pages.json`, a list of every page URL,
    at build time. The script fetches it once and caches it for the session.
  - The last platform is saved in `localStorage` (every access wrapped in
    try/catch) and only sets the toggle's state. The landing page cards
    always link to their own platform explicitly.
  - On `reference/` pages and the landing page, the toggle is hidden.
- Works with Material's `navigation.instant` if that is turned on later.

### Shared content

- `pymdownx.snippets` with `base_path: docs/_shared`. Pages include
  fragments with `--8<-- "folder-layout.md"`.
- `_shared/` is excluded from the build output and search through
  `exclude_docs`.
- A page that is mostly shared but differs a little stays as two pages. Each
  includes the shared fragment and adds its own paragraph. There are no
  per-platform content tabs.

### Redirects

- Add `mkdocs-redirects` to `requirements.txt`.
- Map every moved page, e.g. `guide/context-menu.md` →
  `handheld/guide/context-menu.md`, `getting-started.md` →
  `handheld/getting-started.md`. The full map is generated from the current
  nav, so no page is missed.
- Internal links inside moved pages are relative. They keep working because
  the whole tree moves together. Links from `reference/` into handheld
  pages get updated.

## Part 2 — Landing page

Built as `overrides/home.html` (a template for `index.md` only) plus
`docs/stylesheets/home.css`.

1. **Hero**
   - The NX Redux logo, plus a one-line tagline covering both platforms.
   - Brick Pro and folded Z Fold 8 side by side. Each is an inline SVG device
     frame with a screenshot slot.
   - Each slot fades through 3–4 screenshots. Start with main menu, game
     list, in-game and context menu, refined later. The fade is paused under
     `prefers-reduced-motion`.
2. **Platform cards**
   - Handheld: "Custom firmware for TrimUI handhelds" ·
     [Read the docs] → `handheld/` · [Download] → GitHub releases.
   - Mobile: "Android companion" · **Coming soon** badge ·
     [Preview the docs] → `mobile/`.
3. **"One library, two devices" strip**: a short explanation that the
   `Roms/`, `Saves/`, `Collections/` layout works on both, linking to the
   shared folder-layout content.
4. **Footer**: GitHub, YouTube demo, and the existing Material footer.

### Visual

- The existing palette: black primary, deep-orange accent, light and dark
  schemes through Material's own colour variables.
- Phone width: the devices stack vertically, and the cards become one column.

### Screenshots and frames

- Frame proportions come from real captures: Brick Pro at its native
  resolution, and the Z Fold 8 cover screen in landscape through
  `adb exec-out screencap -p`. Existing 1024×768 captures are from the
  Brick and are a placeholder until Brick Pro captures exist.
- Landing images live in `docs/assets/landing/{handheld,mobile}/`.
- Until phone captures exist, the mobile frame shows a placeholder image.

## Out of scope

- Mobile pages beyond the five listed.
- iOS documentation.
- Versioned docs.
- Moving to a different static site generator.

## Verification

- `mkdocs build --strict` passes (no broken links, no missing nav entries).
- Every old URL redirects to its new page. Checked by a script over the old
  nav list against `site/`.
- The toggle swaps between matching pages, and falls back to the index when
  the other side has no match.
- The landing page is checked in a browser in light and dark mode, and at
  desktop and phone widths.
