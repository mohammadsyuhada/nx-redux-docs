# Mobile Docs Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the Mobile docs up to date with the app as of 2026-10-04, with
real Galaxy Z Fold captures, and refresh the Fold slideshow in the landing
hero.

**Architecture:**
- Captures come first, from a single agent driving one device over adb. The
  raw PNGs are processed by one crop script into WebP.
- Then four writing tasks each own a disjoint set of pages.
- A final task wires the nav and runs the checks.

**Tech Stack:** MkDocs + Material (`.venv/bin/mkdocs`), adb, Python 3 with
Pillow, the `nx-mobile` Compose sources for labels.

**Spec:** `specs/2026-10-04-mobile-docs-refresh-design.md`. Read it before any
task; it holds the page list, crop rules and shot list this plan executes.

## Global Constraints

- **Repos:**
  - Docs: `/Users/mohammadsyuhada/Work/Personal/nx-redux-docs`, branch `mobile-docs-refresh`.
  - App (read-only): `/Users/mohammadsyuhada/Work/Personal/nx-mobile`.
- **Commits:** none. The user commits personally. Leave all changes uncommitted.
- **Device:** Galaxy Z Fold `R5GL66XJS2F`, folded, cover screen 1248×1972,
  status bar inset 110 px (`InsetsSource type=statusBars frame=[0,0][1248,110]`).
  Every adb command passes `-s R5GL66XJS2F`. Never touch any other device.
- **App:** package `com.nxredux.mobile`, a debuggable build (`run-as` works).
  Settings are stored in `shared_prefs/nx-mobile.xml`.
- **Scratchpad:** `S=/private/tmp/claude-501/-Users-mohammadsyuhada-Work-Personal-nx-mobile/5939e4ed-0f61-41c9-8089-0e42b9223144/scratchpad`.
  Raw captures go to `$S/raw/`, the manifest to `$S/captures.md`.
- **Image output:**
  - Docs images: `docs/assets/screenshots/mobile/<id>.webp`, portrait scaled to
    624 px wide, landscape and unfolded at the same scale (×0.5), WebP quality 85.
  - Landing images: `docs/assets/landing/mobile/<name>.webp`, full uncropped
    cover screen at 624×986.
- **Release framing:** one "Coming soon" admonition on `mobile/getting-started.md`
  only. No other page says "not released", "coming soon" or "planned".
- **Name:** the product is "NX Redux Mobile" in the docs. The app's own title is
  "NX Redux".
- **Labels:** copy UI labels exactly as the Compose code has them. Most live
  under `nx-mobile/shared/src/commonMain/kotlin/com/nxredux/mobile/`:
  - `ui/AppState.kt`, `ui/ContextMenus.kt`, `ui/MenuTabs.kt`, `ui/Tools.kt`
  - `ui/ArtworkModel.kt`, `ui/ArtworkScreens.kt`, `ui/GameTime*.kt`, `ui/EmulatorSettings*.kt`
  - `ui/nx/InGameMenuModel.kt`, `ui/nx/HomeScreen.kt`, `ui/nx/HomeLayout.kt`
  - `options/FrontendOptions.kt`, `options/PadOptions.kt`, `options/NdsOptions.kt`
  - `settings/Accent.kt`, `settings/MenuStyles.kt`

  Where the device disagrees with the code, the device wins; the capture
  manifest records those cases.
- **Style:** match `docs/handheld/guide/main-menu.md` and
  `docs/handheld/guide/layouts.md`:
  - short sentences, second person
  - buttons as `A`, `B`, `MENU` in backticks
  - menu paths as **Tools → Settings → Library**
  - tables for settings rows
- **Privacy:** RetroAchievements and ScreenScraper usernames and any API key are
  blurred before a capture is saved.

## Review Focus

1. **Stale claims surviving in a page nobody rewrote:**
   - the "does not download art"
   - "Dreamcast is not included"
   - Genesis `GPGX`
   - "Console Settings | Nintendo DS only"
   - `Aspect - LCD Grid.png` as the Overlay default
   - "Game art style"
   - "not released"

   These must not appear outside the one banner. Task 8 greps for them.
2. **Wrong crop on in-game shots.** A portrait in-game shot that still shows a
   slice of the pad, or that cuts into the game picture. Task 1's crop script
   asserts on the bounds, and Task 3 eyeballs every in-game crop.
3. **A capture leaks a username or key** (RA settings, the Artwork Account page,
   About → Device). Task 3 lists the blurred ids in the manifest. Task 8 reviews
   those images.
4. **The user's app settings are left changed** after the captures (a layout,
   accent, pin or home-screen choice). The backup and restore in Tasks 2 and 3
   is followed by a diff of `nx-mobile.xml`.
5. **Image and link drift between tasks.** A page references a capture id that
   was dropped or renamed, or a capture is never used. Task 8's check script
   fails on both.

---

## File map

| File | Task | Change |
| --- | --- | --- |
| `$S/tools/crop.py`, `$S/tools/cap.sh` | 1 | create (scratch, not in repo) |
| `docs/assets/landing/mobile/{home,consoles-list,consoles-carousel,game-list-carousel,game-list-backdrop-v,game-list-grid}.webp` | 2 | create |
| `docs/assets/landing/mobile/{main-menu,game-list}.webp` | 2 | delete |
| `overrides/home.html` (lines 52–57, the Fold slide list) | 2 | modify |
| `docs/assets/screenshots/mobile/*.webp` | 3 | create |
| `$S/captures.md` | 3 | create (manifest + device findings) |
| `docs/mobile/{getting-started,main-menu,layouts,settings,appearance,about}.md` | 4 | rewrite / create |
| `docs/mobile/{library,controls,in-game-menu,game-switcher,foldables,launcher}.md` | 5 | refresh / create |
| `docs/mobile/{artwork,cheats,emulator-settings,game-tracker,retroachievements}.md` | 6 | rewrite / create |
| `docs/mobile/{emulators,dreamcast}.md`, `docs/reference/faq/mobile.md` | 7 | refresh / create |
| `mkdocs.yml` (Mobile nav), `tools/check_mobile_docs.py` | 8 | modify / create |

Tasks 1 → 2 → 3 run in order on the device. Tasks 4–7 run in parallel after
Task 3, each touching only its own files. Task 8 runs last.

---

### Task 1: Capture and crop tooling

**Files:**
- Create: `$S/tools/cap.sh`, `$S/tools/crop.py`

**Interfaces:**
- Produces:
  - `cap.sh <id>`: writes `$S/raw/<id>.png`, a raw screencap.
  - `crop.py <mode> <id> <out> [--rect x0,y0,x1,y1] [--blur x0,y0,x1,y1 ...]` with these modes:
    - `full` resizes to 624 wide.
    - `menu` cuts the top 110 px, then resizes.
    - `game` crops `--rect`.
    - `land` keeps the full landscape frame and scales by 0.5.
    - `unfolded` behaves like `land`.

    It writes WebP q85.

- [ ] **Step 1: Write `cap.sh`**

```bash
#!/bin/bash
# Raw screencap of the Fold into $S/raw/<id>.png
set -euo pipefail
S=/private/tmp/claude-501/-Users-mohammadsyuhada-Work-Personal-nx-mobile/5939e4ed-0f61-41c9-8089-0e42b9223144/scratchpad
mkdir -p "$S/raw"
adb -s R5GL66XJS2F exec-out screencap -p > "$S/raw/$1.png"
python3 -c "from PIL import Image; im=Image.open('$S/raw/$1.png'); print('$1', im.size)"
```

- [ ] **Step 2: Write `crop.py`**

```python
#!/usr/bin/env python3
"""Crop a raw Fold capture into a docs WebP. See the spec's crop rules."""
import argparse
from PIL import Image, ImageFilter

S = "/private/tmp/claude-501/-Users-mohammadsyuhada-Work-Personal-nx-mobile/5939e4ed-0f61-41c9-8089-0e42b9223144/scratchpad"
STATUS_BAR = 110

def box(s):
    v = [int(n) for n in s.split(",")]
    assert len(v) == 4 and v[0] < v[2] and v[1] < v[3], s
    return tuple(v)

p = argparse.ArgumentParser()
p.add_argument("mode", choices=["full", "menu", "game", "land", "unfolded"])
p.add_argument("id")
p.add_argument("out")
p.add_argument("--rect", type=box)
p.add_argument("--blur", type=box, action="append", default=[])
a = p.parse_args()

im = Image.open(f"{S}/raw/{a.id}.png").convert("RGB")
for b in a.blur:  # blur in raw coordinates, before any crop
    im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(14)), b[:2])

w, h = im.size
if a.mode == "full":
    assert h > w, "full is portrait only"
elif a.mode == "menu":
    assert h > w, "menu is portrait only"
    im = im.crop((0, STATUS_BAR, w, h))
elif a.mode == "game":
    assert a.rect, "game needs --rect from the game surface bounds"
    x0, y0, x1, y1 = a.rect
    assert x1 <= w and y1 <= h, f"rect {a.rect} outside {w}x{h}"
    im = im.crop(a.rect)
elif a.mode in ("land", "unfolded"):
    pass

scale = 0.5 if a.mode in ("land", "unfolded", "game") else 624 / im.size[0]
im = im.resize((round(im.size[0] * scale), round(im.size[1] * scale)), Image.LANCZOS)
im.save(a.out, "WEBP", quality=85, method=6)
print(a.out, im.size)
```

- [ ] **Step 3: Check the tooling on a live menu capture**

With the app open on any menu screen:
```bash
bash $S/tools/cap.sh _probe && python3 $S/tools/crop.py menu _probe $S/_probe.webp && python3 $S/tools/crop.py full _probe $S/_probe_full.webp
```
Expected:
- `_probe (1248, 1972)`
- a menu WebP of `(624, 931)`
- a full WebP of `(624, 986)`

Open `$S/_probe.webp` with Read and confirm there's no status bar or cutout at the top.

- [ ] **Step 4: Find the in-game crop rect**

Start any portrait game (a Sega Genesis game), then run:
```bash
adb -s R5GL66XJS2F shell dumpsys SurfaceFlinger | grep -B2 -A12 -i 'SurfaceView' | grep -iE 'name=|bounds|crop|frame|destinationFrame'
```
- Take the game surface's on-screen rect.
- If the surface fills more than the picture (letterboxing inside a GL view), use the libretro viewport: the region inside the surface whose rows are not uniformly black.
- Record the rect per system in `$S/captures.md`, since aspect ratios differ.

Expected: `crop.py game _probe_game ... --rect <rect>` produces an image with no pad band at the bottom and no black bars cutting the picture. Check it with Read.

---

### Task 2: Settings backup and the landing hero

**Files:**
- Create: `docs/assets/landing/mobile/{home,consoles-list,consoles-carousel,game-list-carousel,game-list-backdrop-v,game-list-grid}.webp`
- Delete: `docs/assets/landing/mobile/main-menu.webp`, `docs/assets/landing/mobile/game-list.webp`
- Modify: `overrides/home.html:52-57`

**Interfaces:**
- Consumes: `cap.sh`, `crop.py full` from Task 1.
- Produces: `$S/nx-mobile.xml.bak`, which Task 3 restores.

- [ ] **Step 1: Back up the app settings**

```bash
adb -s R5GL66XJS2F shell run-as com.nxredux.mobile cat shared_prefs/nx-mobile.xml > $S/nx-mobile.xml.bak
wc -c $S/nx-mobile.xml.bak
```
- Expected: a non-empty XML.
- Also run `adb -s R5GL66XJS2F shell run-as com.nxredux.mobile ls -R files databases 2>/dev/null` and note in the manifest where pins live, if they're not in the prefs. If pins are in a database, copy that file to `$S/` too.

- [ ] **Step 2: Check the content exists**

- Open Consoles and find **Sega Genesis**, then **Streets of Rage 2** with art.
- If it's missing, or has no art, **stop and report back** to the orchestrator with what is there. Don't substitute another game.
- Home must show a Continue card. If it doesn't, play any game with art for a few seconds and quit.

- [ ] **Step 3: Capture the six slides, full uncropped**

For each slide, set the layout in **Tools → Settings → Appearance → Layouts**, navigate to the screen, then capture:

| id | Screen | Layout setting |
| --- | --- | --- |
| `hero-home` | Home tab | — |
| `hero-consoles-list` | Consoles, Sega Genesis focused | Consoles = List |
| `hero-consoles-carousel` | Consoles, Sega Genesis | Consoles = Carousel, Horizontal |
| `hero-game-list-carousel` | Sega Genesis, Streets of Rage 2 focused | Game lists = Carousel, Horizontal |
| `hero-game-list-backdrop-v` | same | Game lists = Backdrop, Vertical |
| `hero-game-list-grid` | same | Game lists = Grid |

```bash
bash $S/tools/cap.sh hero-home
python3 $S/tools/crop.py full hero-home docs/assets/landing/mobile/home.webp
```
Repeat for each, with the out name being the id without `hero-`. Each output must print `(624, 986)`.

- [ ] **Step 4: Update the slide list in `overrides/home.html`**

Replace lines 53–54:
```html
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/main-menu.webp' | url }}" alt="" loading="lazy">
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/game-list.webp' | url }}" alt="" loading="lazy">
```
with:
```html
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/home.webp' | url }}" alt="" loading="lazy">
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/consoles-list.webp' | url }}" alt="" loading="lazy">
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/consoles-carousel.webp' | url }}" alt="" loading="lazy">
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/game-list-carousel.webp' | url }}" alt="" loading="lazy">
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/game-list-backdrop-v.webp' | url }}" alt="" loading="lazy">
                    <img class="nx-slide" src="{{ 'assets/landing/mobile/game-list-grid.webp' | url }}" alt="" loading="lazy">
```
Keep the existing indentation of the surrounding lines. Leave the three `controls/pad-*.webp` lines after them as they are. Then delete the two old files:
```bash
rm docs/assets/landing/mobile/main-menu.webp docs/assets/landing/mobile/game-list.webp
grep -rn 'landing/mobile/\(main-menu\|game-list\)\.webp' overrides docs || echo "no stale refs"
```
Expected: `no stale refs`.

- [ ] **Step 5: Build and look**

```bash
.venv/bin/mkdocs build --strict 2>&1 | tail -3
```
- Expected: no warnings or errors.
- Then open all six images with Read and confirm each matches its Brick counterpart (same console, same focused game).

---

### Task 3: Docs captures, device checks and settings restore

**Files:**
- Create: `docs/assets/screenshots/mobile/<id>.webp`, one per shot in the spec's shot list
- Create: `$S/captures.md`

**Interfaces:**
- Consumes: Tasks 1 and 2.
- Produces: `$S/captures.md`, which Tasks 4–8 read. Its format:

```markdown
## Shots
| id | status | mode | game / screen | notes |
| home | ok | menu | Home tab | |
| unassigned | dropped | — | — | no unassigned games on device |
## Game rects
| system | rect |
## Device findings
- Unassigned on main menu: yes|no — <where it is>
- Recently Played reachable: yes|no — <how>
- .media/bg.png replaces console background: yes|no
- Label differences vs code: <label in code> → <label on device>
## Blurred
- ra-settings: username (x0,y0,x1,y1)
```

- [ ] **Step 1: Portrait menu shots**

For every shot in the spec's shot list without a marker, navigate there and run `cap.sh <id>`, then `crop.py menu <id> docs/assets/screenshots/mobile/<id>.webp`.
- Reach screens through the UI with `adb shell input tap/keyevent`. `adb shell uiautomator dump` can help find tap targets.
- Use the app's default layout (Carousel) for `game-list`, `context-menu` and similar shots, unless the shot names a layout.
- For `accent-home`, set Accent to a non-White preset, capture, and set it back.
- For `ra-settings`, `artwork-account` and `settings-about`, add `--blur` boxes over the usernames, keys and device serials. List them under **Blurred**.
- For `home-full`, use `crop.py full`.

- [ ] **Step 2: In-game and pad shots**

- **In-game portrait shots** (in-game menu, cheats, achievements, `dc-game`, the DS portrait layouts): use `crop.py game --rect <rect>`, with the rect for that system from Task 1 Step 4. Record it under **Game rects**.
- **`P` shots** (`pad-charcoal`, `pad-retro`, `pad-ps`): use `crop.py menu`, which keeps the pad and cuts the status bar. If the game hides the status bar, use `full`.
- **`pad-retro`:** set Pad theme to Retro, capture, and set it back.

- [ ] **Step 3: Landscape shots (`L`)**

- Rotate with the phone's auto-rotate, or by tapping the app's own rotation if it has one. Don't change the system rotation setting unless the user agrees.
- If rotation needs the user, add it to a **Needs user** list and continue with other shots.
- Run `crop.py land` for each.

- [ ] **Step 4: Unfolded shots (`U`)**

These need the phone unfolded: `home-large`, `settings-two-pane`, `in-game-menu-two-pane`, `ra-game-two-pane`. Batch them at the end. Return to the orchestrator with "unfold the Fold" in **Needs user**; the orchestrator relays it, and the user replies with one word when it's done. Then capture them with `crop.py unfolded`.

- [ ] **Step 5: Device checks**

Answer the three questions in **Device findings** by looking on the device.
- Note any label that differs from the code labels in the Global Constraints.

- [ ] **Step 6: Restore settings and verify**

```bash
adb -s R5GL66XJS2F shell am force-stop com.nxredux.mobile
adb -s R5GL66XJS2F shell run-as com.nxredux.mobile sh -c 'cat > shared_prefs/nx-mobile.xml' < $S/nx-mobile.xml.bak
adb -s R5GL66XJS2F shell run-as com.nxredux.mobile cat shared_prefs/nx-mobile.xml | diff - $S/nx-mobile.xml.bak && echo restored
```
Expected: `restored`. If pins were in a database (Task 2 Step 1), restore that file the same way. Relaunch the app and confirm that Home and the Layouts page look as they did before.

- [ ] **Step 7: Check the set**

```bash
ls docs/assets/screenshots/mobile | wc -l
python3 - <<'E'
from PIL import Image; import glob
for f in sorted(glob.glob('docs/assets/screenshots/mobile/*.webp')):
    w,h = Image.open(f).size
    assert w <= 1300, (f, w)
print("ok")
E
```
- Expected: `ok`, and the count equals the `ok` rows in the manifest.
- Open every in-game crop with Read to confirm there's no pad slice and no cut-off picture.

---

### Task 4: Pages A: Getting Started, Main Menu & Home, Layouts, Settings, Appearance, About

**Files:**
- Rewrite: `docs/mobile/getting-started.md`, `docs/mobile/appearance.md`
- Create: `docs/mobile/main-menu.md`, `docs/mobile/layouts.md`, `docs/mobile/settings.md`, `docs/mobile/about.md`

**Interfaces:**
- Consumes:
  - `$S/captures.md` (only use `ok` ids)
  - the label sources
  - the spec's Docs structure entries for these pages
- Produces: the page paths above. Other tasks link to them by these exact names.

- [ ] **Step 1: Read the references**
  - the spec
  - `$S/captures.md`
  - the handheld pages `guide/main-menu.md`, `guide/layouts.md`, `settings/appearance.md`, `settings/about.md`
  - the existing `mobile/getting-started.md` and `mobile/appearance.md`
  - for Home and tabs: `ui/MenuTabs.kt`, `ui/nx/HomeScreen.kt`, `ui/nx/HomeLayout.kt`
  - for Settings: `ui/AppState.kt` (`settingsRows`, `SettingsSection`)
  - `settings/Accent.kt`, `settings/MenuStyles.kt`
- [ ] **Step 2: Write `getting-started.md`**
  - The single `!!! info "Coming soon"` banner.
  - The `home-full` image near the top.
  - Install: one line saying the APK will be on the GitHub releases page at release.
  - Home folder and Add a ROMs folder, kept and corrected. Add the folder later through **Tools → Settings → Library → ROM folders → Add ROM folder**.
  - The Android games question.
  - "What's different": Dreamcast is included, the app downloads art, launcher mode and Flex mode exist. Still missing: RA hardcore, Netplay, Device Sync, remapping, home computer cores.
- [ ] **Step 3: Write `main-menu.md`**
  - Tabs: Home, Consoles, Collections, Tools.
  - Home: Continue, Pick a game, pinned tools and "+N", pinned games, the stats strip.
  - Shelves get one line linking to `foldables.md`.
  - Game lists and their hints.
  - Context menus: console list, collection, Unassigned, Android.
  - Collections: Rename and Delete.
  - Tools: Pin and Unpin.
  - Images: `home`, `home-pins`, `tab-*`, `game-list`, `context-menu`, `tool-menu`.
- [ ] **Step 4: Write `layouts.md`**
  - The Layouts table: rows, values and defaults.
  - One section per style.
  - Orientation and Vertical alignment, with side-by-side image pairs using the same `md_in_html` pattern as `handheld/guide/layouts.md`.
  - The landscape pair shows orientation.
  - Controller art, and Reset to defaults.
- [ ] **Step 5: Write `settings.md`, `appearance.md` and `about.md`**
  - `settings.md`: the five sections, each linking to its page (Library → `library.md`, Emulators → `emulator-settings.md`, Launcher → `launcher.md`).
  - `appearance.md`: Pad theme, UI Scale, Accent (list the nine presets), Secondary accent, Layouts link, Reset to defaults. Images: `settings-appearance`, `accent-home`.
  - `about.md`: the rows and Copy device info.
- [ ] **Step 6: Check the pages**

```bash
.venv/bin/mkdocs build -d $S/site-task4 2>&1 | grep -E 'WARNING|ERROR' | grep -E 'mobile/(getting-started|main-menu|layouts|settings|appearance|about)' || echo clean
```
- Expected: `clean`. Links to pages from other tasks may warn until those exist; ignore only warnings that name `foldables.md`, `launcher.md` or `emulator-settings.md`.
- Spot-check five labels per page against the code.

---

### Task 5: Pages B: Library, Controls, In-game Menu, Game Switcher, Foldables, Launcher

**Files:**
- Modify: `docs/mobile/library.md`, `docs/mobile/controls.md`, `docs/mobile/in-game-menu.md`, `docs/mobile/game-switcher.md`
- Create: `docs/mobile/foldables.md`, `docs/mobile/launcher.md`

**Interfaces:**
- Consumes:
  - `$S/captures.md`, especially **Device findings**
  - the label sources
  - the spec
- Produces: the page paths above.

- [ ] **Step 1: Read the references**
  - the spec and the manifest
  - these existing pages
  - `ui/AppState.kt` (Library and Launcher rows), `ui/ContextMenus.kt`
  - `options/PadOptions.kt`, `options/FrontendOptions.kt`, `ui/nx/InGameMenuModel.kt`
  - `git -C ../nx-mobile log --oneline -150` for Flex mode and two-pane commits, and the code they touch
- [ ] **Step 2: Refresh `library.md`**
  - The Library details and rows table.
  - The ROM folders page: Home folder, the folder states, Add ROM folder, the Remove dialog.
  - Default emulators moved: link to `emulator-settings.md`.
  - Genesis is `MD` only, and only GBA and SFC/SUPA cycle.
  - Unassigned placement per **Device findings**.
  - The GDI folder rule.
  - Android as a console.
  - Images: `settings-library`, `rom-folders`, `unassigned` if ok.
- [ ] **Step 3: Rewrite the stale parts of `controls.md`**
  - Face buttons by position: Nintendo vs Xbox detection, the Controller Layout override.
  - N64 by name.
  - Controller Type for Sega.
  - Menu confirm and back, including PS/PSP × and ○.
  - The landscape pad layout: system row at the top, avoiding the cutout.
  - Per-console drawings, using `pad-ps` plus the reused `../assets/landing/controls/pad-{n64,dc,md6}.webp`.
  - The pad themes pair.
  - Context menu items: add Game Settings and Fetch art; remove Sega Genesis from the Emulator list.
  - The Recently Played line per **Device findings**.
- [ ] **Step 4: Refresh `in-game-menu.md`**
  - Console Settings is for every console except N64: Controller Layout, Controller Type.
  - The DS rows stay.
  - Overlay default is None.
  - Accent colours on the root, notifications top-centre.
  - Two-pane: one line linking to `foldables.md`.
  - Emulator Settings: one line linking to `emulator-settings.md`.
  - Replace the placeholders with `in-game-*` images.
- [ ] **Step 5: Refresh `game-switcher.md`**
  - The exact Remove prompt.
  - The art fallback order.
  - SELECT "Recent" from the main menu.
  - The `game-switcher` image.
- [ ] **Step 6: Write `foldables.md` and `launcher.md`**
  - `foldables.md`:
    - Flex mode, described in words: horizontal hinge, what goes below it in portrait, landscape and with a controller, DS excluded, the main menu too.
    - The wide and large Home faces, and the shelves rules (New 30 days, Not started, Pick up again after 14 days).
    - Two-pane at 600 dp: Settings, RA, in-game menu.
    - The `U` images.
  - `launcher.md`:
    - Use as home screen (what Back and Home do).
    - The Android apps and Android games pickers.
    - Android games' art and their missing play time.
    - The app icon brings a running game back.
    - Images.
- [ ] **Step 7: Check the pages**

The same build grep as Task 4 Step 6, with its own `-d $S/site-taskN` (N = this task), for these six pages. Spot-check labels.

---

### Task 6: Pages C: Artwork, Cheats, Emulator Settings, Game Tracker, RetroAchievements

**Files:**
- Rewrite: `docs/mobile/artwork.md`
- Modify: `docs/mobile/cheats.md`, `docs/mobile/retroachievements.md`
- Create: `docs/mobile/emulator-settings.md`, `docs/mobile/game-tracker.md`

**Interfaces:**
- Consumes: the manifest, the label sources, the spec, and the handheld `apps/artwork-manager.md`, `apps/game-tracker.md` and `apps/emulator-settings.md` for structure.
- Produces: the page paths above.

- [ ] **Step 1: Read the references**
  - `ui/ArtworkModel.kt`, `ui/ArtworkScreens.kt`, the artwork source code in `nx-mobile` (grep `libretro-thumbnails`, `SteamGridDB`)
  - `ui/GameTime*.kt`, `ui/EmulatorSettings*.kt`
  - the RA settings code
- [ ] **Step 2: Rewrite `artwork.md`**
  - The Tools → Artwork rows.
  - Sources in order for box and screenshot art, and the hero/grid fallback.
  - Account: the ScreenScraper sign-in, the SteamGridDB and TheGamesDB keys, the quota lines.
  - Art settings: Replace existing art, Reset artwork (the confirm text).
  - The background job: notification, Pause/Cancel, Resume.
  - Per-game Fetch art.
  - Typed `.media/{boxart,box2d,screenshot,grid,hero}/`, and that the old Mix is ignored.
  - Where fetched art goes for extra folders.
  - Where each image shows.
  - Abstract art.
  - Android game art.
  - Credits for each source.
  - `.media/bg.png` per **Device findings**.
- [ ] **Step 3: Write `emulator-settings.md`**
  - The path, the core list, Console settings vs Core settings, applying at once (including start-only options).
  - The no-option-table message.
  - Game Settings and "Use emulator settings".
  - Default emulators: the caption and which consoles cycle.
- [ ] **Step 4: Write `game-tracker.md`**
  - The title and total, the empty state, Sessions.
  - Merge into, Unmerge, Delete, with their prompts.
  - Which sessions are dropped.
  - That Android games are not tracked.
- [ ] **Step 5: Light refresh of `cheats.md` and `retroachievements.md`**
  - Naming.
  - The RA Home strip count and Sign in.
  - Replace placeholders with the `cheat-database`, `in-game-cheats*` and `ra-*` images.
  - `ra-game` keeps its portrait capture. The wide variant lives in `foldables.md`.
- [ ] **Step 6: Check the pages**

The same build grep as Task 4 Step 6, with its own `-d $S/site-taskN` (N = this task), for these five pages. Spot-check labels.

---

### Task 7: Pages D: Emulators, Dreamcast, FAQ

**Files:**
- Modify: `docs/mobile/emulators.md`, `docs/reference/faq/mobile.md`
- Create: `docs/mobile/dreamcast.md`

**Interfaces:**
- Consumes: the manifest, the spec, `nx-mobile` core and system tables (grep `flycast`, `GPGX`, `dc_boot.bin`), and the handheld `emulators/dreamcast.md` for structure.
- Produces: the page paths above.

- [ ] **Step 1: Refresh `emulators.md`**
  - Genesis is `MD` only; `GPGX` is a legacy folder.
  - Add Dreamcast, NAOMI and Atomiswave on flycast, linking to `dreamcast.md`.
  - Add Android as a console, linking to `launcher.md`.
  - Remove "not in the first release".
  - Controller Type for Sega.
  - N64 button mapping.
  - Emulator Settings: a link.
  - Replace the eight DS placeholders with the `ds-*` images. The landscape ones stay landscape; that is their point.
- [ ] **Step 2: Write `dreamcast.md`**
  - BIOS in `Bios/DC/` (`dc_boot.bin`, `naomi.zip`, `awbios.zip`).
  - GDI games in their own folder.
  - VMU and save names.
  - State size of about 36 MB.
  - NAOMI and Atomiswave sets, and the missing-BIOS message (exact text from the code).
  - RA hashing for discs.
  - The `dc-game` image.
- [ ] **Step 3: Fix `faq/mobile.md`**
  - Remove "not released yet" (the banner lives on Getting Started).
  - Fix the DraStic/Dreamcast question: DraStic is still absent, Dreamcast is now included.
  - Fix remapping: Controller Layout exists, free remapping doesn't.
  - Rewrite the artwork answer around the scraper.
  - Reword the Genesis states note.
  - Add questions:
    - use as home screen
    - foldables
    - why ScreenScraper or API keys are needed
    - why Android games have no play time
- [ ] **Step 4: Check the pages**

The same build grep as Task 4 Step 6, with its own `-d $S/site-taskN` (N = this task), for these three pages.

---

### Task 8: Nav, checks and handover

**Files:**
- Modify: `mkdocs.yml` (the `- Mobile:` block)
- Create: `tools/check_mobile_docs.py`

**Interfaces:**
- Consumes: all pages and images from Tasks 2–7.

- [ ] **Step 1: Write the check script and run it before the nav change**

```python
"""Checks for the mobile docs: placeholders, stale claims, image references.

Run from the repo root: python tools/check_mobile_docs.py
"""
import re
import sys
from pathlib import Path

DOCS = Path("docs")
pages = sorted((DOCS / "mobile").glob("*.md")) + [DOCS / "reference/faq/mobile.md"]
shots = DOCS / "assets/screenshots/mobile"
failures = []

STALE = [
    r"does not download", r"doesn't download", r"not included in the first release",
    r"Nintendo DS only", r"Aspect - LCD Grid", r"Game art style", r"Game art width",
    r"not released", r"[Cc]oming soon", r"\bGPGX\b(?!.*legacy)",
]

referenced = set()
for page in pages:
    text = page.read_text()
    if "<!-- SCREENSHOT" in text:
        failures.append(f"{page}: placeholder left")
    for pat in STALE:
        for m in re.finditer(pat, text):
            line = text.count("\n", 0, m.start()) + 1
            allowed = page.name == "getting-started.md" and pat in (r"[Cc]oming soon", r"not released")
            if not allowed:
                failures.append(f"{page}:{line}: stale claim /{pat}/")
    for ref in re.findall(r"\]\(([^)\s]+\.(?:webp|png))", text):
        target = (page.parent / ref).resolve()
        if not target.exists():
            failures.append(f"{page}: missing image {ref}")
        referenced.add(target)

for img in shots.glob("*.webp"):
    if img.resolve() not in referenced:
        failures.append(f"unused image {img}")

print("\n".join(failures) or "mobile docs ok")
sys.exit(1 if failures else 0)
```

Run `python3 tools/check_mobile_docs.py`.
- Expected: `mobile docs ok`.
- Fix any finding in the page that owns it. A `GPGX` hit that's genuinely about the legacy folder should say "legacy" on the same line.

- [ ] **Step 2: Replace the Mobile nav in `mkdocs.yml`**

Replace the `- Mobile:` block with the nav from the spec's **Nav** section, verbatim.

- [ ] **Step 3: Strict build and site check**

```bash
.venv/bin/mkdocs build --strict 2>&1 | tail -5
python3 tools/check_site.py
```
- Expected: the build has no warnings.
- `check_site.py` passes, except for the PortMaster failure that predates this work. Quote that failure's output as-is in the handover, and treat any other failure as a bug to fix.

- [ ] **Step 4: Review blurred images and the browser check**

- Open every image listed under **Blurred** in the manifest with Read, and confirm nothing is readable.
- Run `.venv/bin/mkdocs serve` in the background and open these in a browser:
  - the landing page (watch the Fold slideshow cycle)
  - `mobile/getting-started/`, `mobile/layouts/`, `mobile/controls/`

  Check each in light and dark, at desktop width and at 390 px.
- Stop the server afterwards.

- [ ] **Step 5: Hand over**

Report:
- files changed (`git status -s`)
- the device findings
- dropped shots
- anything that needed the user
- the PortMaster note

Don't commit.
