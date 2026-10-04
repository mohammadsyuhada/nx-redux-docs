# Mobile docs refresh — design

Date: 2026-10-04
Branch: `mobile-docs-refresh`
App state documented: `nx-mobile` `main` at `8acbcfb0` (2026-10-04).

## Goal

Bring the Mobile section up to date with the app as it is on 2026-10-04, add
pages for the features that have none, and replace every screenshot
placeholder with a real capture from the Galaxy Z Fold. Refresh the Fold
slideshow in the landing page hero so it matches the Brick Pro one.

The pages were written on 2026-09-28. Since then the app has gained the tabbed
main menu with Home, four layouts, accents, launcher mode and Android games,
the artwork scraper, Game Tracker, Emulator Settings and Game Settings,
Dreamcast, Controller Layout and Controller Type, Flex mode and two-pane
screens. Several pages now say wrong things (no artwork download, no
Dreamcast, Genesis on `GPGX`, Console Settings DS-only, the old Overlay
default, "colors and UI scale are not in the app yet").

## Later changes (2026-10-05)

- At the user's request, Netplay, Device Sync, local multiplayer (2 to 4
  players on their own controllers), more systems (Nintendo 3DS, home
  computers) and iOS are described as coming in a later release. Only
  RetroAchievements hardcore mode is stated as not available, the same as
  on the handheld. This replaces the "only shipped behaviour, not promised"
  rule for these items.
- Getting Started shows the Home screenshot inside the Z Fold 8 frame.
- Portrait menu shots stop above the on-screen pad too (raw y 110–995), not
  only in-game shots. Only the pad shots and the framed Home shot keep the pad.

## Decisions

- Refresh existing pages in place; add new pages named after their handheld
  counterparts. No full rewrite: Cheats, RetroAchievements, Game Switcher,
  Library and most of Emulators are still largely accurate.
- **Release framing:** the app is not released. One "Coming soon" banner on
  Getting Started only. Every other page describes features as they are,
  with no per-page "not released / planned" notes. The landing page's
  "Coming soon" badge stays. Release notes keep their one "not released yet"
  line.
- **Name:** the docs keep "NX Redux Mobile" as the product name, so it is
  clear next to the handheld. Getting Started says the app's icon and title
  read "NX Redux".
- **Only shipped behaviour is documented.** Things that are still missing
  are named once in "What's different" or the FAQ, not promised: RA
  hardcore, Netplay, Device Sync, button remapping, two-player, home
  computer cores, 3DS, iOS.
- Exact UI labels come from the app's Compose code. Where the code and the
  device disagree, the device wins.
- Section names follow the handheld docs. Tone and structure follow
  `handheld/guide/main-menu.md` and `handheld/guide/layouts.md`.

## Docs structure

`✚` new page, `✎` rewrite, `·` refresh.

```
mobile/
  getting-started.md      ✎  intro, full portrait Home shot, Coming soon banner,
                             install (placeholder until release), home folder,
                             ROMs folder, Android games question, What's different
  main-menu.md            ✚  tabs, Home (Continue, pinned tools, pinned games,
                             stats strip, Pick a game), Consoles / Collections /
                             Tools, game lists, context menus, hint bar
  layouts.md              ✚  List / Grid / Carousel / Backdrop, Horizontal vs
                             Vertical, Vertical alignment, Controller art, Reset
  library.md              ·  ROM folders page, Default emulators moved,
                             Genesis = MD only, Unassigned games row, GDI rule
  controls.md             ✎  portrait band, landscape overlay pad (system row
                             at the top, cutout), per-console drawings, button
                             position detection, Controller Layout / Type,
                             menu confirm/back rules
  in-game-menu.md         ·  Console Settings for all consoles, Overlay default
                             None, accent colours, notification position
  game-switcher.md        ·  Remove prompt, art fallback, SELECT "Recent"
  foldables.md            ✚  Flex mode, wide and large Home faces and shelves,
                             two-pane Settings / RA / in-game menu
  launcher.md             ✚  Use as home screen, Android apps, Android games
  artwork.md              ✎  Tools → Artwork scraper, sources and order,
                             Account keys and quotas, Replace / Reset, background
                             job, Fetch art, typed .media folders, where each
                             image shows, abstract art, source credits
  game-tracker.md         ✚  totals, Sessions, Merge / Unmerge / Delete
  emulator-settings.md    ✚  Emulator Settings, Game Settings, Default emulators
  cheats.md               ·  naming only
  retroachievements.md    ·  Home strip count and Sign in
  emulators.md            ·  core table + flycast and Android, Genesis MD only,
                             Controller Type, N64 mapping
  dreamcast.md            ✚  Dreamcast / NAOMI / Atomiswave: BIOS, GDI folders,
                             VMU and saves, state size, missing-BIOS message
  settings.md             ✚  Settings overview: Library / Emulators /
                             Appearance / Launcher / About
  appearance.md           ✎  Pad theme, UI Scale, Accent, Secondary accent,
                             Layouts link, Reset to defaults
  about.md                ✚  About rows, Copy device info
reference/faq/mobile.md   ·  fix stale answers, add home screen, foldables,
                             artwork keys, why Android games have no play time
```

### Nav

```yaml
- Mobile:
    - Getting Started: mobile/getting-started.md
    - User Guide:
        - Main Menu & Home: mobile/main-menu.md
        - Menu Layouts: mobile/layouts.md
        - Library & ROM folders: mobile/library.md
        - Controls: mobile/controls.md
        - In-game Menu: mobile/in-game-menu.md
        - Game Switcher: mobile/game-switcher.md
        - Foldables & Large Screens: mobile/foldables.md
        - Launcher Mode & Android Games: mobile/launcher.md
    - Apps & Features:
        - Artwork: mobile/artwork.md
        - Cheats: mobile/cheats.md
        - Emulator Settings: mobile/emulator-settings.md
        - Game Tracker: mobile/game-tracker.md
        - RetroAchievements: mobile/retroachievements.md
    - Emulators:
        - Bundled Emulators: mobile/emulators.md
        - Sega Dreamcast: mobile/dreamcast.md
    - Settings:
        - Overview: mobile/settings.md
        - Appearance: mobile/appearance.md
        - About: mobile/about.md
```

No page moves, so no new redirects.

## Screenshots

### Device and capture

- Galaxy Z Fold `R5GL66XJS2F`, **folded, cover screen** (1248×1972, 104 px
  camera cutout at the top), captured with `adb exec-out screencap -p`.
- One capture agent drives the device. Captures run before any writing, and
  never in parallel (one device).
- Before capturing, the agent records the current app settings it will
  change (layouts, orientations, alignment, accent, secondary accent, UI
  Scale, pad theme, pins, Use as home screen) and restores them afterwards.
- Games used are ones already on the Fold that have art. The landing shots
  use Sega Genesis and Streets of Rage 2 (see below).
- RetroAchievements and ScreenScraper usernames, and API keys, are blurred.
- The agent stops and asks when it needs a hand: a game state it can't
  reach, a missing game, or a screen it can't open.

### Crop rules (docs pages)

| Kind | Crop |
| --- | --- |
| Menu screens, portrait | Below the status bar and camera cutout, so only the app shows |
| In-game, portrait | The game viewport only: the pad band below it is cut. Bounds come from the game surface's rect in `dumpsys SurfaceFlinger`, not from eyeballing |
| Getting Started intro | One full, uncropped portrait shot of Home |
| Landscape | Only where orientation is the point: Horizontal vs Vertical layouts, portrait band vs landscape overlay pad, DS landscape layouts |
| Controls page pad shots | Keep the pad, since the pad is the subject |
| Unfolded main screen | Only on Foldables & Large Screens (shelves, two-pane), which the cover screen can't show |

Flex mode is described in words. A screencap can't show the hinge.

### Format

- Docs pages: `docs/assets/screenshots/mobile/<id>.webp`, scaled to 624 px
  wide for portrait (half the cover screen), quality 85. Landscape and
  unfolded shots are scaled to the same pixel density.
- Images are placed with plain Markdown, `![alt](../assets/screenshots/mobile/<id>.webp)`,
  matching the handheld pages. Side-by-side comparisons use the same
  `md_in_html` pattern the handheld layouts page uses.
- Every `<!-- SCREENSHOT: ... -->` placeholder in `docs/mobile/` is replaced
  or removed.

### Shot list

Portrait cover screen, cropped, unless marked: **F** full uncropped,
**L** landscape, **U** unfolded main screen, **P** in-game with the pad kept.

| Page | Shots |
| --- | --- |
| getting-started | `home-full` F, `first-run-home-folder`, `first-run-add-roms`, `first-run-android-games` |
| main-menu | `home`, `home-pins`, `tab-consoles`, `tab-collections`, `tab-tools`, `game-list`, `context-menu`, `tool-menu` |
| layouts | `settings-layouts`, `consoles-list`, `consoles-grid`, `consoles-carousel`, `consoles-carousel-vertical`, `game-list-list`, `game-list-grid`, `game-list-carousel`, `game-list-backdrop`, `game-list-backdrop-vertical-left`, `game-list-backdrop-vertical-right`, `game-list-carousel-landscape` L, `game-list-backdrop-landscape` L |
| library | `settings-library`, `rom-folders`, `unassigned` (if any exist) |
| controls | `pad-charcoal` P, `pad-retro` P, `pad-landscape` L, `pad-ps` P; reuse `landing/controls/pad-{n64,dc,md6}.webp` |
| in-game-menu | `in-game-menu-root`, `in-game-options`, `in-game-frontend`, `in-game-console-settings`, `in-game-save-changes`, `in-game-menu-adjust` |
| game-switcher | `game-switcher` |
| foldables | `home-large` U, `settings-two-pane` U, `in-game-menu-two-pane` U, `ra-game-two-pane` U |
| launcher | `settings-launcher`, `android-apps-picker`, `android-console` |
| artwork | `artwork`, `artwork-account` (blurred), `artwork-settings`, `artwork-fetch-by-console`, `artwork-progress` |
| game-tracker | `game-tracker`, `game-tracker-sessions` |
| emulator-settings | `emulator-settings`, `emulator-settings-core`, `game-settings`, `default-emulators` |
| cheats | `cheat-database`, `in-game-cheats`, `in-game-cheats-merged` |
| retroachievements | `ra-home`, `ra-settings` (blurred), `ra-games`, `ra-game` |
| emulators | `ds-portrait-stacked`, `ds-portrait-pip`, `ds-portrait-single`, `ds-landscape-side-by-side` L, `ds-landscape-single` L, `ds-landscape-pip` L, `ds-landscape-pad-opacity` L P, `ds-touch-mode` L |
| dreamcast | `dc-game` |
| settings | `settings` |
| appearance | `settings-appearance`, `accent-home` (Home in a non-default accent) |
| about | `settings-about` |

A shot that can't be reached (no game for it, no unassigned games) is
dropped and the text is left without an image. It is not faked.

### Things to check on the device while capturing

- Whether Unassigned still shows on the main menu, or only under Settings →
  Library → Unassigned games.
- Whether a Recently Played list can be opened from the main menu.
- Whether `.media/bg.png` still replaces a console's background.

The pages document what the device shows.

## Landing page hero

The Fold slideshow mirrors the Brick Pro one, minus the Brick's last three
(game list List, Collections Grid, Tools Grid). The Fold keeps its three
controller shots in their place.

| # | File (`docs/assets/landing/mobile/`) | Shows |
| --- | --- | --- |
| 1 | `logo.webp` | unchanged |
| 2 | `home.webp` | Home with a Continue card |
| 3 | `consoles-list.webp` | Consoles, List, Sega Genesis focused |
| 4 | `consoles-carousel.webp` | Consoles, Carousel (Horizontal), Sega Genesis |
| 5 | `game-list-carousel.webp` | Sega Genesis, Carousel, Streets of Rage 2 focused |
| 6 | `game-list-backdrop-v.webp` | Sega Genesis, Backdrop Vertical, Streets of Rage 2 |
| 7 | `game-list-grid.webp` | Sega Genesis, Grid, Streets of Rage 2 |
| 8–10 | `../controls/pad-{n64,dc,md6}.webp` | unchanged |

- Full, uncropped cover-screen portraits at 624×986, the same as the
  existing Fold slides.
- If Streets of Rage 2 is not on the Fold with art, the agent asks before
  using anything else.
- `main-menu.webp` and `game-list.webp` are deleted. `overrides/home.html`
  lists the new files in this order. The handheld slides and the feature
  cards are untouched.

## Execution

1. **Capture** (one Opus agent, device): landing hero, then the docs shot
   list, then the device checks. It saves raw captures in the scratchpad and
   writes the processed ones in place.
2. **Write** (about four Opus agents in parallel, grouped by nav section).
   Each gets the gap analysis, the label sources in `nx-mobile`, its page
   list and its captures. Each touches only its own pages.
3. **Integrate:** `mkdocs.yml` nav, the landing `home.html` list, and the
   FAQ.
4. **Verify**, then hand over. No commits until asked.

## Out of scope

- Handheld pages, the landing feature cards and the menu demo.
- A release notes entry (there is no release yet).
- iOS.
- Changes to the app.

## Verification

- `mkdocs build --strict` passes.
- `tools/check_site.py` passes. Its existing PortMaster failure, which
  predates this work, is reported, not hidden.
- No `<!-- SCREENSHOT` placeholder is left under `docs/mobile/`.
- Every image referenced exists, and every new image is referenced.
- A spot check of labels against the Compose sources for each new page.
- The landing hero and three mobile pages are checked in a browser, light
  and dark, at desktop and phone widths.
