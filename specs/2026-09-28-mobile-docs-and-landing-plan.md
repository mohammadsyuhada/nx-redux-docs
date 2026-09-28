# Mobile Docs and Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the site into Handheld and Mobile sections with a header platform toggle, add the first mobile pages, and put a two-device landing page in front.

**Architecture:** One MkDocs Material build. The current pages move under `docs/handheld/`, and `mkdocs-redirects` covers every old URL. New pages go in `docs/mobile/`, and text shared by both sections lives as `pymdownx.snippets` fragments in `docs/_shared/`. A build hook writes `platform-pages.json`, which a small header script uses to swap `handheld/` ↔ `mobile/`. The landing page is a Material template override (`overrides/home.html`) with inline-SVG device frames.

**Tech Stack:** MkDocs 1.6.1, mkdocs-material 9.7.7, pymdown-extensions 10.21.3, mkdocs-redirects (new), plain JS (no build step), Python 3.9 check script, `node:test` (Node 22) for the toggle logic.

**Spec:** `specs/2026-09-28-mobile-docs-and-landing-design.md`

## Global Constraints

- Work in the worktree `/Users/mohammadsyuhada/Work/Personal/nx-redux-docs-mobile`, on branch `feat/mobile-docs-landing`. Never commit to `main`.
- The worktree has no venv. Use `V=/Users/mohammadsyuhada/Work/Personal/nx-redux-docs/.venv/bin` and call `$V/mkdocs` / `$V/python` / `$V/pip`.
- Build with `$V/mkdocs build --strict`. It must print no `WARNING`. The existing `INFO` about `#supported-cores` in `apps/artwork-manager.md` is known and out of scope.
- Commit messages: one line, `type(scope): summary`, no trailers, no Co-Authored-By.
- Colours come only from Material's CSS variables (`--md-default-bg-color`, `--md-default-fg-color*`, `--md-accent-fg-color`, `--md-primary-fg-color`, `--md-primary-bg-color`), so light and dark mode both work.
- No external scripts or fonts beyond what Material already loads.
- Devices: TrimUI **Brick Pro** (1024×768 panel, the same as the Brick, so the existing screenshots are valid) and Samsung **Galaxy Z Fold 8, folded, cover screen**.
- Mobile is unreleased. The landing page shows a **Coming soon** badge, and `/mobile/` pages are still built and linked.
- Shared fragments in `docs/_shared/` must contain **no relative links**. They are inlined into pages at different depths, so a relative link would break in one of them.

### Deviations from the spec (decided while planning)

- `_shared/` has two fragments, `map-txt.md` and `collections.md`. `saves.md` and `folder-layout.md` are dropped: saves behave differently on each platform, and the handheld folder table has many handheld-only rows, so neither has text both sides can use as-is.
- Handheld landing screenshots reuse `docs/assets/screenshots/`, since they are already Brick Pro-resolution captures. Only `docs/assets/landing/mobile/` is new.
- The toggle does not use `localStorage`. The URL already says which platform you're on, and the toggle is hidden everywhere else, so a stored value would never be read.
- The folded phone is drawn **in portrait**. Folded, it's held upright, and its width matches the Brick Pro's. If the captures come back landscape, only the SVG `viewBox` and screen rect in Task 4 change.

## Review Focus

1. **An old bookmark with an anchor** (`/guide/main-menu/#collections`) must land on the same section of the new page. Pinned by the `location.hash` check in Task 1.
2. **Images inside moved pages** must still load. Strict mode doesn't check `<img src>` or `![]()` targets reliably, so they're pinned by the image-resolution check in Task 1.
3. **Toggling from a page that exists on only one side, at any depth** (`handheld/settings/led-control/`) must reach the other side's overview, not a 404. Pinned by the node tests in Task 3.
4. **If `platform-pages.json` fails to load** (offline, `file://`), the toggle must still work and go to the other overview. Pinned by the fallback-`href` check in Task 3.
5. **The landing page on a 375 px phone** must have no horizontal scroll. Pinned by the browser check in Task 4. The slideshow must stop under reduced motion, pinned by a markup check in Task 4.

---

## File Structure

```
mkdocs.yml                         nav tabs, plugins (search, redirects), hooks, custom_dir, snippets, exclude_docs
requirements.txt                   + mkdocs-redirects
tools/check_site.py                post-build assertions (grows each task)
tools/platform-switch.test.cjs     node tests for the toggle's pure logic
hooks/platform_pages.py            writes site/platform-pages.json
overrides/main.html                exposes base/page URL to JS
overrides/home.html                landing page
docs/index.md                      landing stub (template: home.html)
docs/handheld/...                  all current pages, moved
docs/mobile/{index,getting-started,library,controls,emulators}.md
docs/_shared/{map-txt,collections}.md
docs/javascripts/platform-switch.js
docs/stylesheets/extra.css         + toggle styles
docs/stylesheets/home.css          landing styles
docs/assets/landing/mobile/placeholder.svg
```

---

### Task 1: Move handheld pages under `handheld/` with redirects and tabs

**Files:**
- Create: `tools/check_site.py`, `tools/migrate_handheld.py` (one-off, deleted before commit)
- Move: `docs/{index.md,getting-started.md,desktop.md,netplay.md,guide/,apps/,emulators/,settings/}` → `docs/handheld/`
- Create: `docs/index.md` (temporary stub, replaced in Task 4)
- Modify: `mkdocs.yml`, `requirements.txt`, every `.md` whose relative links cross the moved boundary (the script handles these)

**Interfaces:**
- Produces: `tools/check_site.py`, which has a `CHECKS` list of zero-arg functions calling `check(cond, msg)`. Later tasks add functions to `CHECKS`. Run it as `$V/python tools/check_site.py` after a build. It exits 1 and lists failures if any check fails.
- Produces: the URL layout `handheld/<old path>/`.

- [ ] **Step 1: Write the failing check script**

`tools/check_site.py`:

```python
"""Post-build checks for the built site.

Run after `mkdocs build --strict` from the repo root: python tools/check_site.py
"""
import re
import subprocess
import sys
from pathlib import Path

SITE = Path("site")
BASE_COMMIT = "c384838"  # main before the handheld/mobile split
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


def url_dir(md):
    """guide/osd.md -> guide/osd/, emulators/index.md -> emulators/."""
    stem = md[:-3]
    if stem == "index":
        return ""
    if stem.endswith("/index"):
        return stem[: -len("index")]
    return stem + "/"


def old_handheld_pages():
    nav = subprocess.run(
        ["git", "show", f"{BASE_COMMIT}:mkdocs.yml"],
        capture_output=True, text=True, check=True,
    ).stdout
    pages = re.findall(r"([a-z0-9/-]+\.md)", nav)
    return [p for p in pages if p != "index.md" and not p.startswith("reference/")]


def check_redirects():
    for md in old_handheld_pages():
        old = SITE / url_dir(md) / "index.html"
        new = "handheld/" + url_dir(md)
        check((SITE / new / "index.html").exists(), f"moved page missing: {new}")
        check(old.exists(), f"no redirect page for old URL {url_dir(md)}")
        if old.exists():
            html = old.read_text()
            check(new in html, f"redirect {url_dir(md)} does not point at {new}")
            check("location.hash" in html, f"redirect {url_dir(md)} drops the #anchor")


def check_images():
    for html_file in (SITE / "handheld").rglob("index.html"):
        html = html_file.read_text()
        for src in re.findall(r'<img[^>]+src="([^"]+)"', html):
            if re.match(r"^[a-z]+:|^/", src):
                continue
            target = (html_file.parent / src.split("#")[0]).resolve()
            check(target.exists(), f"{html_file.relative_to(SITE)}: broken image {src}")


def check_handheld_overview():
    html = (SITE / "handheld" / "index.html").read_text()
    check('id="why-nx-redux"' in html, "handheld overview lacks the Why NX Redux section")


CHECKS = [check_redirects, check_images, check_handheld_overview]


def main():
    for fn in CHECKS:
        try:
            fn()
        except Exception as exc:  # a missing file is a failure, not a crash
            failures.append(f"{fn.__name__}: {exc!r}")
    for f in failures:
        print("FAIL", f)
    print(f"{len(failures)} failure(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and confirm it fails**

```bash
cd /Users/mohammadsyuhada/Work/Personal/nx-redux-docs-mobile
V=/Users/mohammadsyuhada/Work/Personal/nx-redux-docs/.venv/bin
$V/mkdocs build --strict && $V/python tools/check_site.py
```
Expected: many `FAIL moved page missing: handheld/...` lines and a non-zero exit.

- [ ] **Step 3: Confirm the link shapes the script must handle**

Run: `grep -rnE '^\[[^]]*\]: ' docs; grep -rn 'src="' docs | grep -v '^docs/.*:.*```'`
Expected: no reference-style link definitions. Any `src="..."` hits are HTML images inside `md_in_html` blocks, which the script handles. If reference-style definitions do show up, add a third regex `^(\[[^\]]+\]:\s*)(\S+)` to the script before continuing.

- [ ] **Step 4: Write the one-off migration script**

`tools/migrate_handheld.py`:

```python
"""One-off: move handheld pages under docs/handheld/ and fix relative links."""
import os
import posixpath
import re
import subprocess

DOCS = "docs"
MOVED = ["index.md", "getting-started.md", "desktop.md", "netplay.md",
         "guide", "apps", "emulators", "settings"]
MD_LINK = re.compile(r"(\]\()([^)\s]+)")
HTML_ATTR = re.compile(r'((?:src|href)=")([^"]+)"')


def new_path(old):
    return "handheld/" + old if old.split("/")[0] in MOVED else old


def fix(target, old_file):
    if re.match(r"^[a-z]+:|^/|^#", target):
        return target
    path, sep, frag = target.partition("#")
    old_target = posixpath.normpath(posixpath.join(posixpath.dirname(old_file), path))
    if old_target.startswith(".."):
        return target
    new_file = new_path(old_file)
    rel = posixpath.relpath(new_path(old_target), posixpath.dirname(new_file) or ".")
    return rel + sep + frag


def main():
    files = []
    for root, _, names in os.walk(DOCS):
        for n in names:
            if n.endswith(".md"):
                files.append(posixpath.relpath(posixpath.join(root, n), DOCS))
    rewritten = {}
    for f in files:
        with open(posixpath.join(DOCS, f)) as fh:
            text = fh.read()
        text = MD_LINK.sub(lambda m: m.group(1) + fix(m.group(2), f), text)
        text = HTML_ATTR.sub(lambda m: m.group(1) + fix(m.group(2), f) + '"', text)
        rewritten[new_path(f)] = text
    os.makedirs(f"{DOCS}/handheld", exist_ok=True)
    for item in MOVED:
        subprocess.run(["git", "mv", f"{DOCS}/{item}", f"{DOCS}/handheld/{item}"], check=True)
    for f, text in rewritten.items():
        with open(posixpath.join(DOCS, f), "w") as fh:
            fh.write(text)


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run it, check the diff and delete it**

```bash
$V/python tools/migrate_handheld.py && rm tools/migrate_handheld.py
git diff --stat -M | tail -3
git diff -M docs/reference/faq.md | head -20
git diff -M docs/handheld/guide/main-menu.md | grep '^[-+]' | head -10
```
Expected: `faq.md` links now read `../handheld/...`. In `main-menu.md`, only links that point outside the moved tree change (image paths `../assets/...` → `../../assets/...`, and anything into `reference/`). Links between moved pages are unchanged.

- [ ] **Step 6: Make the handheld overview a section page**

In `docs/handheld/index.md`:
- Delete the front matter block (`---` / `hide:` / `  - navigation` / `---`) so the sidebar shows.
- Change the H1 `# NX Redux` to `# NX Redux for TrimUI handhelds`.

The "Why NX Redux?" section is already on this page, since the old home moved here. Leave it where it is.

- [ ] **Step 7: Add the temporary landing stub**

`docs/index.md`:

```markdown
---
hide:
  - navigation
  - toc
---

# NX Redux

- [Handheld documentation](handheld/index.md)
```

- [ ] **Step 8: Install and pin `mkdocs-redirects`**

```bash
$V/pip install mkdocs-redirects && $V/pip show mkdocs-redirects | grep Version
```
Append `mkdocs-redirects==<that version>` to `requirements.txt`.

- [ ] **Step 9: Update `mkdocs.yml`**

1. Generate the redirect map:
   ```bash
   git show c384838:mkdocs.yml | grep -oE '[a-z0-9/-]+\.md' | grep -vE '^(index\.md|reference/)' \
     | awk '{print "        "$1": handheld/"$1}'
   ```
2. Add this after `extra_css:`, pasting the generated lines under `redirect_maps:`:
   ```yaml
   plugins:
     - search
     - redirects:
         redirect_maps:
           getting-started.md: handheld/getting-started.md
           # … rest of the generated lines …
   ```
3. Replace the whole `nav:` block with the version below. Its page order is the current one, with the `Home` entry gone and `Netplay` inside Handheld:
   ```yaml
   not_in_nav: |
     /index.md

   nav:
     - Handheld:
         - Overview: handheld/index.md
         - Getting Started: handheld/getting-started.md
         - Desktop App: handheld/desktop.md
         - User Guide:
             - Main Menu & Game Lists: handheld/guide/main-menu.md
             - Game Switcher: handheld/guide/game-switcher.md
             - Game Context Menu: handheld/guide/context-menu.md
             - Five-Game Menu: handheld/guide/five-game-menu.md
             - Playing Games: handheld/guide/playing-games.md
             - In-game Options: handheld/guide/in-game-options.md
             - Buttons & Shortcuts: handheld/guide/shortcuts.md
             - Button Layout: handheld/guide/button-layout.md
             - Emulator Options: handheld/guide/emulator-options.md
             - On-Screen Display: handheld/guide/osd.md
             - Simple Mode: handheld/guide/simple-mode.md
             - Accessing Your Files: handheld/guide/file-access.md
         - Apps & Tools:
             - Tools Overview: handheld/apps/tools.md
             - Artwork Manager: handheld/apps/artwork-manager.md
             - Cheats: handheld/apps/cheats.md
             - Device Sync: handheld/apps/device-sync.md
             - Emulator Settings: handheld/apps/emulator-settings.md
             - Files: handheld/apps/files.md
             - Game Tracker: handheld/apps/game-tracker.md
             - Image Viewer: handheld/apps/image-viewer.md
             - Media Player: handheld/apps/media-player.md
             - Music Player: handheld/apps/music-player.md
             - PortMaster: handheld/apps/portmaster.md
             - RetroAchievements: handheld/apps/retroachievements.md
             - Xtras Store: handheld/apps/xtras.md
         - Emulators:
             - Bundled Emulators: handheld/emulators/index.md
             - Cores & BIOS Files: handheld/emulators/cores.md
             - ROM File Formats: handheld/emulators/rom-formats.md
             - Arcade (FBNeo): handheld/emulators/arcade.md
             - Nintendo 64: handheld/emulators/nintendo-64.md
             - Sega Dreamcast: handheld/emulators/dreamcast.md
             - Nintendo DS: handheld/emulators/nintendo-ds.md
             - Additional Emulators: handheld/emulators/additional.md
         - Netplay: handheld/netplay.md
         - Settings:
             - Overview: handheld/settings/index.md
             - Display: handheld/settings/display.md
             - Appearance: handheld/settings/appearance.md
             - In-game Notifications: handheld/settings/notifications.md
             - LED Control: handheld/settings/led-control.md
             - Network: handheld/settings/network.md
             - Bluetooth: handheld/settings/bluetooth.md
             - Audio: handheld/settings/audio.md
             - FN Switch: handheld/settings/fn-switch.md
             - F1 / F2 Keys: handheld/settings/fn-keys.md
             - Simple Mode: handheld/settings/simple-mode.md
             - System: handheld/settings/system.md
             - Developer: handheld/settings/developer.md
             - Input Tester: handheld/settings/input-tester.md
             - About: handheld/settings/about.md
     - Reference:
         - Release Notes: reference/release-notes.md
         - FAQ: reference/faq.md
         - Credits: reference/credits.md
         - Disclaimer: reference/disclaimer.md
   ```

- [ ] **Step 10: Build and run the checks**

```bash
$V/mkdocs build --strict 2>&1 | grep -E "WARNING|ERROR" ; $V/python tools/check_site.py
```
Expected: no WARNING or ERROR lines, and `0 failure(s)`.

- [ ] **Step 11: Commit**

```bash
git add -A docs mkdocs.yml requirements.txt tools/check_site.py
git commit -m "refactor(docs): move handheld pages under handheld/ with redirects and platform tabs"
```

---

### Task 2: Shared fragments, mobile section, release-notes split

**Files:**
- Create: `docs/_shared/map-txt.md`, `docs/_shared/collections.md`
- Create: `docs/mobile/{index,getting-started,library,controls,emulators}.md`
- Modify: `docs/handheld/guide/main-menu.md` (the "Custom display names" and "Collections" sections), `docs/reference/release-notes.md`, `mkdocs.yml`, `tools/check_site.py`

**Interfaces:**
- Consumes: `check`/`CHECKS` from Task 1.
- Produces: URLs `mobile/`, `mobile/getting-started/`, `mobile/library/`, `mobile/controls/`, `mobile/emulators/`, used by Tasks 3 and 4.

- [ ] **Step 1: Add the failing checks**

Add to `tools/check_site.py` above `CHECKS`, then add both names to `CHECKS`:

```python
MOBILE_PAGES = ["", "getting-started/", "library/", "controls/", "emulators/"]


def check_mobile_section():
    for p in MOBILE_PAGES:
        check((SITE / "mobile" / p / "index.html").exists(), f"mobile page missing: mobile/{p}")
    check(not (SITE / "_shared").exists(), "_shared fragments were published as pages")


def check_snippets_inlined():
    marker = "Collections/RPG Nights.txt"
    for page in ["handheld/guide/main-menu", "mobile/library"]:
        html = (SITE / page / "index.html").read_text()
        check(marker in html, f"{page}: collections fragment not inlined")
        check("--8&lt;--" not in html and "--8<--" not in html, f"{page}: raw snippet marker left")
```

Run: `$V/mkdocs build --strict; $V/python tools/check_site.py`
Expected: FAIL for the missing mobile pages and the missing fragment in `mobile/library`.

- [ ] **Step 2: Configure snippets and exclusion in `mkdocs.yml`**

Under `markdown_extensions:`, add:
```yaml
  - pymdownx.snippets:
      base_path: [docs/_shared]
      check_paths: true
```
At the top level, add:
```yaml
exclude_docs: |
  _shared/
```

- [ ] **Step 3: Create the fragments**

`docs/_shared/map-txt.md`. Copy the two example lines inside the code block **from `docs/handheld/guide/main-menu.md` lines 148–149**, so the literal TAB between file name and alias is kept:

````markdown
To rename games without touching the files, drop a `map.txt` inside the
system folder. Each line maps a **filename** to a display name, separated
by a single **tab**:

```
Roms/Game Boy Advance (GBA)/map.txt:

Advance Wars 2 - Black Hole Rising (USA).gba	Advance Wars 2
Legend of Zelda, The - The Minish Cap (USA).gba	Zelda: Minish Cap
```

The list re-sorts by the new display names. Since the files themselves are
untouched, save files, states and box art all stay matched. An alias starting
with a dot (e.g. `Track01.bin	.hidden`) **hides** the entry from the list
entirely.

A `map.txt` at the top level (`Roms/map.txt`) does the same for the
**system folders** — an alternative to renaming the folders themselves.
````

`docs/_shared/collections.md`:

````markdown
Under the hood each collection is a plain text file at
`Collections/<Name>.txt`, with one path per line, relative to the top of your
library (the SD card on a handheld). You can also build them on a computer:

```
Collections/RPG Nights.txt:

/Roms/Game Boy Advance (GBA)/Golden Sun.gba
/Roms/Sony PlayStation (PS)/Final Fantasy VII/Final Fantasy VII.m3u
```

Entries whose file is missing are silently skipped, and a
`Collections/map.txt` can alias the displayed names, in the same format as a
system folder's `map.txt`.
````

- [ ] **Step 4: Use the fragments in the handheld page**

In `docs/handheld/guide/main-menu.md`, replace the body of `## Custom display names (map.txt)` from "To rename games…" through "…renaming the folders themselves." with:

```markdown
--8<-- "map-txt.md"

The number-prefix trick above works inside aliases too. The context menu's
[**Rename Rom**](context-menu.md) writes these aliases for you — renaming
on the device edits the `map.txt` rather than the file.
```

Keep the "Arcade folders don't need a `map.txt`…" paragraph after it, unchanged. In `## Collections`, keep the first paragraph ("Build your own game collections…"), and replace everything from "Under the hood…" to the end of the section with `--8<-- "collections.md"`.

- [ ] **Step 5: Write the mobile pages**

Every fact below comes from `../nx-mobile/README.md` (Goals, Bundled cores, Non-goals). Don't add claims that aren't there.

`docs/mobile/index.md`:

```markdown
# NX Redux Mobile

!!! info "Coming soon"
    NX Redux Mobile is not released yet. These pages grow as its features
    ship.

NX Redux Mobile brings the NX Redux look, folder layout and in-game features
to Android phones, tablets and Android handhelds. It runs retro systems
through bundled libretro cores, with no downloads needed. An iOS version is
planned after Android.

It uses the same `Roms/<Name (TAG)>/`, `Bios/<TAG>/`, `Saves/<TAG>/`,
`Collections/` and `map.txt` layout as NX Redux on TrimUI handhelds, so one
library can serve both.

## What's different from the handheld

- **Emulators:** Nintendo DS runs melonDS DS (DraStic is not available), and
  Sega Dreamcast is not included in the first release. See
  [Emulators](emulators.md).
- **Library:** besides the home folder, the app can scan extra folders in
  place. See [Library & ROM folders](library.md).
- **Controls:** an on-screen pad, or any Android controller. See
  [Controls](controls.md).
- **Left to Android:** Wi-Fi and Bluetooth management, the on-screen display,
  the music player, PortMaster, Device Sync, firmware updates and netplay are
  not part of the app.

Ready? Start with [Getting Started](getting-started.md).
```

`docs/mobile/getting-started.md`:

```markdown
# Getting Started

## Install

NX Redux Mobile is not released yet. This section will list where to get it
once it is out.

## Choose a home folder

On first start the app asks for a **home folder** through Android's folder
picker. It creates the NX Redux layout inside it:

| Folder | What goes there |
| --- | --- |
| `Roms/<Display Name (TAG)>/` | Games, one folder per system |
| `Bios/<TAG>/` | BIOS files for systems that need them |
| `Saves/<TAG>/` | Battery saves, mirrored from the app |
| `Collections/` | Your game collections |

The folders are visible to file managers, so you can copy games in from a
computer. The home folder can sit on an SD card.

If your games already follow the NX Redux layout from a handheld, the same
folder names and `Bios/<TAG>/` files work unchanged.

## Add more folders

Games elsewhere on the phone can stay where they are: add their folders as
**extra folders** in **Tools → Settings → Library**. See
[Library & ROM folders](library.md).
```

`docs/mobile/library.md`:

````markdown
# Library & ROM folders

## Home folder and extra folders

The library comes from two kinds of folder:

- **The home folder**, laid out as `Roms/<Name (TAG)>/`. The app created it
  and writes only inside it.
- **Extra folders**, any number of them, scanned in place and never written
  to.

Files in an extra folder are matched to a console:

1. by a `(TAG)` or an alias in the folder name (a short alias such as `GBA`
   may be followed only by roms, games or isos, singular or plural),
2. then by an extension only one console uses (a zip by its first entry, a 7z
   only by its folder).

Anything left over lands in **Unassigned** until you pick its console. The
choice is saved in a `systems.txt` (`<file><TAB><TAG>`). For extra folders
this file lives in the home folder under `Roms/.sources/`, so the extra folder
itself is never changed.

## Rescanning

The scanned library is kept in an index, so the app starts without walking
your folders. After adding or removing games outside the app, use
**Rescan library** in **Tools → Settings → Library**.

A folder on an SD card that is taken out keeps its place: its games are left
out until the card is back, and **Settings → Library** marks it
**Not available**. A folder that was deleted, or whose access was revoked, is
removed with a notice.

## Game names

Bracketed region and version text is dropped from names, as on the handheld:
"Tetris (World) (Rev 1)" shows as "Tetris". If two games would end up with the
same name, both show their file names.

## Custom display names (map.txt)

--8<-- "map-txt.md"

**Rename Rom** in the game-list context menu writes these aliases for you. For
games in an extra folder the alias goes into a `map.txt` under
`Roms/.sources/` in the home folder, and it overrides the extra folder's own
`map.txt`.

## Collections

Use **Add to Collection** in the game-list context menu.

--8<-- "collections.md"

## Saves

Cores play from a private working copy of each battery save, mirrored to
`Saves/<TAG>/` in the home folder. The mirror is updated after each save
write and when you quit. Replace files in `Saves/<TAG>/` only while that game
is not running, because the working copy wins on the next write.

BIOS files are read from `Bios/<TAG>/` before each launch.

Pinned and hidden games are stored inside the app. Hidden games can be shown
again from **Tools → Settings → Library**. Nothing in the app deletes a ROM.
````

`docs/mobile/controls.md`:

```markdown
# Controls

## On-screen pad and controllers

Without a controller the app shows an on-screen pad. Connect any Android
controller to play with real buttons instead. In landscape the pad sits over
the game, and **Pad Opacity (landscape)** in the in-game options sets how
opaque it is: 100, 60, 40 or 25 % (40 % by default), saved per game or
console.

Menus show key hints you can tap when a controller or the on-screen pad is
present, and real buttons in landscape without one.

## Game-list context menu

Press `MENU`, or long-press a game, for the same context menu as on the
handheld:

- **Pin Item / Unpin**
- **Hide Game**
- **Rename Rom** (writes a `map.txt` alias; the file is never renamed)
- **Add to / Remove from Collection**
- **Remove from Recently Played**
- **Emulator / Console** to switch which system a game runs as

## In-game menu

The in-game menu has saves, save states, per-core options, cheats,
RetroAchievements and game time. `X` shows an option's full description when
it is cut off, and `UP` / `DOWN` scroll a long one.
```

`docs/mobile/emulators.md`. The table rows come from the README's "Bundled cores" table, in the same order, with licences dropped:

```markdown
# Emulators

Every core is bundled in the app. Folder and tag names match NX Redux on the
handheld.

| System | Tag(s) | Core |
| --- | --- | --- |
| Nintendo DS | `NDS` | melonDS DS |
| Nintendo 64 | `N64` | mupen64plus-next |
| PlayStation Portable | `PSP` | PPSSPP |
| Game Boy / Game Boy Color | `GB`, `GBC` | Gambatte |
| Game Boy Advance | `GBA` | gpSP |
| Game Boy Advance, Super Game Boy | `MGBA`, `SGB` | mGBA |
| NES / Famicom Disk System | `FC`, `FDS` | FCEUmm |
| Super Nintendo | `SFC` | Snes9x |
| Super Nintendo | `SUPA` | Mednafen Supafaust |
| Genesis / Mega Drive, Master System, Game Gear, SG-1000, Sega CD | `GPGX`, `MD`, `SMS`, `GG`, `SG1000`, `SEGACD` | Genesis Plus GX |
| PlayStation | `PS` | PCSX ReARMed |
| Neo Geo Pocket / Color | `NGP`, `NGPC` | RACE |
| PC Engine | `PCE` | Mednafen PCE Fast |
| Virtual Boy | `VB` | Mednafen VB |
| Atari Lynx | `LYNX` | Handy |
| Atari 2600 | `A2600` | Stella 2014 |
| Atari 5200 | `A5200` | a5200 |
| Atari 7800 | `A7800` | ProSystem |
| Pokémon Mini | `PKM` | PokeMini |
| WonderSwan Color | `WSC` | Mednafen WonderSwan |
| PICO-8 | `P8` | fake-08 |
| Doom | `PRBOOM` | PrBoom |
| Sega 32X | `32X` | PicoDrive |
| ColecoVision | `COLECO` | Gearcoleco |
| Arcade | `FBN` | FinalBurn Neo |

Sega Genesis uses `GPGX` by default, like the handheld, with `MD` as a second
tag on the same core.

## BIOS files

Put BIOS files in `Bios/<TAG>/`. A launch also reads the folders of tags that
share its core, so a handheld's layout (`Bios/FC/disksys.rom`,
`Bios/MD/bios_CD_*.bin`, `Bios/PS/psxonpsp660.bin`) works unchanged.
Famicom Disk System, Sega CD, PC Engine CD and ColecoVision
(`Bios/COLECO/colecovision.rom`) need their BIOS, which is checked before
launch. PlayStation has a BIOS built in and uses a real one when present.

## Zip and 7z files

An archive holding one game plays on every core. The app unpacks it on first
launch, and saves use the archive's name, as on the handheld. Archives with
several games or a password are refused with a message. Arcade (`FBN`) zips
are the game itself and are never unpacked; parent and BIOS sets such as
`neogeo.zip` are found in the same folder or in `Bios/FBN/`.

## Nintendo DS

The two screens can be stacked, side by side, picture in picture or single
screen, set separately for portrait and landscape in
**Options → Console Settings**. With a controller, `R2` swaps the big screen,
`SELECT` + `LEFT` / `RIGHT` cycles the layout, and `L2` toggles stylus mode.
3D runs on the GPU at 2× internal resolution by default (1×–8× in
**Core Options → Video**).

## Not available yet

- **Sega Dreamcast** is not in the first release.
- **PlayStation `.exe` homebrew** does not load yet.
- **PICO-8** save states and auto-resume do not work yet.
```

- [ ] **Step 6: Split the release notes**

```bash
$V/python - <<'EOF'
import re
p = "docs/reference/release-notes.md"
lines = open(p).read().split("\n")
out, inserted = [], False
for line in lines:
    if line.startswith("## ") and not inserted:
        out += ["## Mobile", "", "NX Redux Mobile has not been released yet.", "", "## Handheld", ""]
        inserted = True
    if re.match(r"^#{2,5} ", line):
        line = "#" + line
    out.append(line)
open(p, "w").write("\n".join(out))
EOF
grep -n '^#' docs/reference/release-notes.md | head -6
```
Expected: `# Release Notes`, `## Mobile`, `## Handheld`, `### v1.13.0`, `#### New features`, …

- [ ] **Step 7: Add the Mobile tab to `nav`**

Between the `Handheld:` and `Reference:` entries, add:
```yaml
  - Mobile:
      - Overview: mobile/index.md
      - Getting Started: mobile/getting-started.md
      - Library & ROM folders: mobile/library.md
      - Controls: mobile/controls.md
      - Emulators: mobile/emulators.md
```

- [ ] **Step 8: Build and run the checks**

```bash
$V/mkdocs build --strict 2>&1 | grep -E "WARNING|ERROR" ; $V/python tools/check_site.py
```
Expected: no WARNING or ERROR, and `0 failure(s)`.

- [ ] **Step 9: Commit**

```bash
git add -A docs mkdocs.yml tools/check_site.py
git commit -m "docs(mobile): add mobile section, shared map.txt/collections fragments, split release notes"
```

---

### Task 3: Handheld / Mobile header toggle

**Files:**
- Create: `hooks/platform_pages.py`, `overrides/main.html`, `docs/javascripts/platform-switch.js`, `tools/platform-switch.test.cjs`
- Modify: `mkdocs.yml`, `docs/stylesheets/extra.css`, `tools/check_site.py`

**Interfaces:**
- Consumes: the `handheld/` and `mobile/` URL prefixes from Tasks 1–2.
- Produces: `site/platform-pages.json`, a sorted JSON array of page URLs such as `"handheld/guide/osd/"` and `"mobile/"`. Also the globals `window.NX_BASE_URL` and `window.NX_PAGE_URL` from `overrides/main.html`, which Task 4's `home.html` extends.
- Produces: `counterpart(pageUrl: string, pages: string[]) -> string | null` and `platformOf(pageUrl: string) -> "handheld" | "mobile" | null`, exported for tests.

- [ ] **Step 1: Write the failing node tests**

`tools/platform-switch.test.cjs`:

```js
const test = require("node:test");
const assert = require("node:assert");
const { counterpart, platformOf } = require("../docs/javascripts/platform-switch.js");

const pages = ["", "handheld/", "handheld/guide/context-menu/", "handheld/settings/led-control/",
  "mobile/", "mobile/library/", "reference/faq/"];

test("platformOf reads the first path segment", () => {
  assert.strictEqual(platformOf("handheld/guide/osd/"), "handheld");
  assert.strictEqual(platformOf("mobile/"), "mobile");
  assert.strictEqual(platformOf("reference/faq/"), null);
  assert.strictEqual(platformOf(""), null);
});

test("section overviews map to each other", () => {
  assert.strictEqual(counterpart("handheld/", pages), "mobile/");
  assert.strictEqual(counterpart("mobile/", pages), "handheld/");
});

test("a page with no match falls back to the other overview", () => {
  assert.strictEqual(counterpart("handheld/settings/led-control/", pages), "mobile/");
  assert.strictEqual(counterpart("mobile/library/", pages), "handheld/");
});

test("a matching page on the other side is used", () => {
  const withMatch = pages.concat(["mobile/guide/context-menu/"]);
  assert.strictEqual(counterpart("handheld/guide/context-menu/", withMatch), "mobile/guide/context-menu/");
});

test("an empty page list still returns the other overview", () => {
  assert.strictEqual(counterpart("handheld/guide/osd/", []), "mobile/");
});

test("pages outside a platform have no counterpart", () => {
  assert.strictEqual(counterpart("reference/faq/", pages), null);
});
```

Run: `node --test tools/`
Expected: FAIL with `Cannot find module '../docs/javascripts/platform-switch.js'`.

- [ ] **Step 2: Write the toggle script**

`docs/javascripts/platform-switch.js`:

```js
// Handheld / Mobile header toggle. Switching keeps the page's path under the
// other platform when that page exists, else goes to its overview.
(function () {
  var PLATFORMS = ["handheld", "mobile"];
  var LABELS = { handheld: "Handheld", mobile: "Mobile" };

  function platformOf(pageUrl) {
    var first = pageUrl.split("/")[0];
    return PLATFORMS.indexOf(first) >= 0 ? first : null;
  }

  function counterpart(pageUrl, pages) {
    var from = platformOf(pageUrl);
    if (!from) return null;
    var to = from === "handheld" ? "mobile" : "handheld";
    var candidate = to + pageUrl.slice(from.length);
    return pages.indexOf(candidate) >= 0 ? candidate : to + "/";
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { counterpart: counterpart, platformOf: platformOf };
    return;
  }

  function mount() {
    var page = window.NX_PAGE_URL || "";
    var base = window.NX_BASE_URL || ".";
    var current = platformOf(page);
    var header = document.querySelector(".md-header__inner");
    if (!current || !header) return;

    var group = document.createElement("nav");
    group.className = "nx-platform";
    group.setAttribute("aria-label", "Platform");

    PLATFORMS.forEach(function (p) {
      var link = document.createElement("a");
      link.className = "nx-platform__option";
      link.textContent = LABELS[p];
      if (p === current) {
        link.href = base + "/" + page;
        link.setAttribute("aria-current", "page");
      } else {
        // Overview first, so the link works even if the page list never loads.
        link.href = base + "/" + p + "/";
        fetch(base + "/platform-pages.json")
          .then(function (r) { return r.json(); })
          .then(function (pages) { link.href = base + "/" + counterpart(page, pages); })
          .catch(function () {});
      }
      group.appendChild(link);
    });

    header.insertBefore(group, header.querySelector(".md-search"));
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
```

- [ ] **Step 3: Run the node tests**

Run: `node --test tools/`
Expected: `# pass 6`, `# fail 0`.

- [ ] **Step 4: Add the failing site checks**

Add `import json` to the imports at the top of `tools/check_site.py`, then add these functions above `CHECKS` and both names to `CHECKS`:

```python
def check_platform_pages():
    pages = json.loads((SITE / "platform-pages.json").read_text())
    for url in ["handheld/", "handheld/guide/osd/", "mobile/", "mobile/library/"]:
        check(url in pages, f"platform-pages.json lacks {url}")
    check(not any(u.startswith("_shared") for u in pages), "platform-pages.json lists _shared")


def check_toggle_wired():
    for page in ["handheld/guide/osd", "mobile/library", "reference/faq"]:
        html = (SITE / page / "index.html").read_text()
        check("platform-switch.js" in html, f"{page}: toggle script not loaded")
        check("NX_PAGE_URL" in html, f"{page}: page URL not exposed")
```

Run: `$V/mkdocs build --strict; $V/python tools/check_site.py`
Expected: FAIL (`platform-pages.json` missing, script not loaded).

- [ ] **Step 5: Write the hook**

`hooks/platform_pages.py`:

```python
"""Writes platform-pages.json: every page URL, for the Handheld / Mobile toggle."""
import json
from pathlib import Path

_urls = []


def on_files(files, config):
    _urls[:] = sorted(f.url for f in files.documentation_pages())
    return files


def on_post_build(config):
    Path(config["site_dir"], "platform-pages.json").write_text(json.dumps(_urls))
```

- [ ] **Step 6: Write the template override**

`overrides/main.html`:

```html
{% extends "base.html" %}

{% block scripts %}
  <script>
    window.NX_BASE_URL = "{{ base_url }}";
    window.NX_PAGE_URL = "{{ page.url if page else '' }}";
  </script>
  {{ super() }}
{% endblock %}
```

- [ ] **Step 7: Wire it into `mkdocs.yml`**

- Under `theme:`, add `custom_dir: overrides`.
- At the top level, add:
  ```yaml
  hooks:
    - hooks/platform_pages.py

  extra_javascript:
    - javascripts/platform-switch.js
  ```

- [ ] **Step 8: Style the toggle**

Append to `docs/stylesheets/extra.css`:

```css
/* Handheld / Mobile platform toggle in the header */
.nx-platform {
  display: flex;
  flex-shrink: 0;
  gap: 0.1rem;
  margin: 0 0.4rem;
  padding: 0.1rem;
  border-radius: 1rem;
  background: rgba(255, 255, 255, 0.1);
}

.nx-platform__option {
  padding: 0.2rem 0.6rem;
  border-radius: 1rem;
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--md-primary-bg-color);
  opacity: 0.7;
}

.nx-platform__option:hover,
.nx-platform__option[aria-current] {
  opacity: 1;
}

.nx-platform__option[aria-current] {
  background: var(--md-accent-fg-color);
}
```

- [ ] **Step 9: Build, check and test**

```bash
$V/mkdocs build --strict 2>&1 | grep -E "WARNING|ERROR" ; $V/python tools/check_site.py && node --test tools/
```
Expected: no WARNING or ERROR, `0 failure(s)`, `# fail 0`.

- [ ] **Step 10: Check in a browser**

Run `$V/mkdocs serve -a 127.0.0.1:8123` in the background. Using the Playwright tools:
1. Open `/handheld/guide/context-menu/`. The toggle shows with **Handheld** highlighted. Click **Mobile**: you land on `/mobile/`, since there's no matching mobile page.
2. Open `/mobile/library/`. Click **Handheld**: you land on `/handheld/`.
3. Open `/reference/faq/`: no toggle is shown.
4. Resize to 375×800 on `/handheld/`: the toggle fits in the header, and `document.documentElement.scrollWidth <= innerWidth`.
5. **Review Focus 4:** on `/handheld/`, block `**/platform-pages.json` (via `browser_run_code_unsafe` with `page.route(..., r => r.abort())`), reload, and confirm the Mobile link's `href` ends with `mobile/`.

Stop the server afterwards.

- [ ] **Step 11: Commit**

```bash
git add hooks overrides docs/javascripts docs/stylesheets/extra.css mkdocs.yml tools
git commit -m "feat(site): add Handheld / Mobile header toggle"
```

---

### Task 4: Landing page with Brick Pro and Z Fold 8 frames

**Files:**
- Create: `overrides/home.html`, `docs/stylesheets/home.css`, `docs/assets/landing/mobile/placeholder.svg`
- Modify: `docs/index.md` (replace the Task 1 stub), `tools/check_site.py`

**Interfaces:**
- Consumes: `overrides/main.html` (Task 3), `docs/assets/screenshots/{main-menu,game-list,in-game,context-menu}.png`, and the URLs `handheld/`, `mobile/`, `handheld/guide/file-access/`, `mobile/library/`.
- Produces: device markup `.nx-device--handheld` / `.nx-device--mobile`, each holding `image.nx-slide` elements. To add phone screenshots later, add one `<image class="nx-slide">` per capture in the mobile SVG.

- [ ] **Step 1: Add the failing check**

Add to `tools/check_site.py`, and add it to `CHECKS`:

```python
def check_landing():
    html = (SITE / "index.html").read_text()
    for needle in ['nx-device--handheld', 'nx-device--mobile', 'Coming soon',
                   'href="handheld/"', 'href="mobile/"', 'prefers-reduced-motion',
                   'home.css']:
        check(needle in html, f"landing lacks {needle!r}")
    check("Why &quot;NX Redux&quot;" not in html and 'id="why-nx-redux"' not in html,
          "Why NX Redux blurb should live on the handheld overview, not the landing page")
    check(html.count('class="nx-slide') >= 5, "landing should have 4 handheld slides + 1 mobile slide")
```

Run: `$V/mkdocs build --strict; $V/python tools/check_site.py`
Expected: FAIL for each missing needle.

- [ ] **Step 2: Replace `docs/index.md`**

```markdown
---
template: home.html
title: NX Redux
hide:
  - navigation
  - toc
---
```

- [ ] **Step 3: Create the mobile placeholder image**

`docs/assets/landing/mobile/placeholder.svg` (portrait, the same ratio as the phone screen rect in Step 4):

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 1530">
  <rect width="680" height="1530" fill="#111"/>
  <text x="340" y="740" fill="#ff6e40" font-family="sans-serif" font-size="64" font-weight="700" text-anchor="middle">NX Redux</text>
  <text x="340" y="820" fill="#aaa" font-family="sans-serif" font-size="40" text-anchor="middle">Screenshots coming soon</text>
</svg>
```

- [ ] **Step 4: Write the template**

`overrides/home.html`. Device geometry is in SVG units at about 1 unit = 1 mm. Both bodies are 73 wide, so they appear the same size:

```html
{% extends "main.html" %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="{{ 'stylesheets/home.css' | url }}">
{% endblock %}

{% block tabs %}
  {{ super() }}
  <div class="nx-home">
    <section class="nx-hero">
      <img class="nx-hero__logo" src="{{ 'assets/logo.svg' | url }}" alt="">
      <h1 class="nx-hero__title">NX Redux</h1>
      <p class="nx-hero__tagline">Pick up, pick a game, play — on TrimUI handhelds and on your phone.</p>

      <div class="nx-devices">
        <figure class="nx-device nx-device--handheld">
          <svg viewBox="0 0 73 113" role="img" aria-label="NX Redux running on a TrimUI Brick Pro">
            <defs><clipPath id="nx-brick-screen"><rect x="7" y="7" width="59" height="44.25" rx="1"/></clipPath></defs>
            <rect class="nx-device__body" x="0.5" y="0.5" width="72" height="112" rx="6"/>
            <rect class="nx-device__bezel" x="4.5" y="4.5" width="64" height="49.25" rx="2.5"/>
            <g clip-path="url(#nx-brick-screen)">
              <image class="nx-slide is-active" href="{{ 'assets/screenshots/main-menu.png' | url }}" x="7" y="7" width="59" height="44.25" preserveAspectRatio="xMidYMid slice"/>
              <image class="nx-slide" href="{{ 'assets/screenshots/game-list.png' | url }}" x="7" y="7" width="59" height="44.25" preserveAspectRatio="xMidYMid slice"/>
              <image class="nx-slide" href="{{ 'assets/screenshots/in-game.png' | url }}" x="7" y="7" width="59" height="44.25" preserveAspectRatio="xMidYMid slice"/>
              <image class="nx-slide" href="{{ 'assets/screenshots/context-menu.png' | url }}" x="7" y="7" width="59" height="44.25" preserveAspectRatio="xMidYMid slice"/>
            </g>
            <g class="nx-device__controls">
              <rect x="14" y="68" width="8" height="22" rx="1.5"/>
              <rect x="7" y="75" width="22" height="8" rx="1.5"/>
              <circle cx="56" cy="71" r="3.4"/>
              <circle cx="63" cy="79" r="3.4"/>
              <circle cx="56" cy="87" r="3.4"/>
              <circle cx="49" cy="79" r="3.4"/>
              <rect x="25" y="101" width="9" height="3" rx="1.5"/>
              <rect x="39" y="101" width="9" height="3" rx="1.5"/>
            </g>
          </svg>
          <figcaption>TrimUI Brick Pro</figcaption>
        </figure>

        <figure class="nx-device nx-device--mobile">
          <svg viewBox="0 0 73 158" role="img" aria-label="NX Redux Mobile on a folded Galaxy Z Fold 8 cover screen">
            <defs><clipPath id="nx-phone-screen"><rect x="2.5" y="2.5" width="68" height="153" rx="7"/></clipPath></defs>
            <rect class="nx-device__body" x="0.5" y="0.5" width="72" height="157" rx="9"/>
            <g clip-path="url(#nx-phone-screen)">
              <image class="nx-slide is-active" href="{{ 'assets/landing/mobile/placeholder.svg' | url }}" x="2.5" y="2.5" width="68" height="153" preserveAspectRatio="xMidYMid slice"/>
            </g>
            <circle class="nx-device__camera" cx="36.5" cy="7" r="1.6"/>
          </svg>
          <figcaption>Galaxy Z Fold 8 · cover screen</figcaption>
        </figure>
      </div>
    </section>

    <section class="nx-cards">
      <article class="nx-card">
        <h2>Handheld</h2>
        <p>Custom firmware for TrimUI handhelds.</p>
        <div class="nx-card__actions">
          <a class="md-button md-button--primary" href="{{ 'handheld/' | url }}">Read the docs</a>
          <a class="md-button" href="https://github.com/mohammadsyuhada/nx-redux/releases">Download</a>
        </div>
      </article>
      <article class="nx-card">
        <h2>Mobile <span class="nx-badge">Coming soon</span></h2>
        <p>The Android app for phones, tablets and Android handhelds.</p>
        <div class="nx-card__actions">
          <a class="md-button" href="{{ 'mobile/' | url }}">Preview the docs</a>
        </div>
      </article>
    </section>

    <section class="nx-strip">
      <h2>One library, two devices</h2>
      <p>Both use the same <code>Roms/</code>, <code>Bios/</code>, <code>Saves/</code> and
        <code>Collections/</code> layout, so your games are organised the same way on either.</p>
      <p>
        <a href="{{ 'handheld/guide/file-access/' | url }}">Handheld folders</a> ·
        <a href="{{ 'mobile/library/' | url }}">Mobile library</a> ·
        <a href="https://www.youtube.com/watch?v=l4iJBRgUe4U">Watch the demo</a>
      </p>
    </section>
  </div>
{% endblock %}

{% block content %}{% endblock %}

{% block scripts %}
  {{ super() }}
  <script>
    (function () {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
      document.querySelectorAll(".nx-device").forEach(function (device) {
        var slides = device.querySelectorAll(".nx-slide");
        if (slides.length < 2) return;
        var i = 0;
        setInterval(function () {
          slides[i].classList.remove("is-active");
          i = (i + 1) % slides.length;
          slides[i].classList.add("is-active");
        }, 3500);
      });
    })();
  </script>
{% endblock %}
```

Note: `{{ 'handheld/' | url }}` renders as `handheld/` on the root page, which is what `check_landing` looks for.

- [ ] **Step 5: Write the landing styles**

`docs/stylesheets/home.css`. It's only loaded by `home.html`:

```css
/* Landing page. Loaded only by overrides/home.html. */
.md-main { display: none; }

.nx-home {
  max-width: 61rem;
  margin: 0 auto;
  padding: 0 1rem 3rem;
  color: var(--md-default-fg-color);
}

.nx-hero { text-align: center; padding-top: 2.5rem; }
.nx-hero__logo { width: 3.5rem; height: 3.5rem; }
.nx-hero__title { margin: 0.4rem 0 0; font-size: 2.2rem; font-weight: 800; }
.nx-hero__tagline { margin: 0.4rem auto 0; max-width: 32rem; font-size: 1rem; color: var(--md-default-fg-color--light); }

.nx-devices {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: 3rem;
  margin-top: 2.5rem;
}

.nx-device { margin: 0; }
.nx-device svg { display: block; height: auto; }
.nx-device--handheld svg { width: 13rem; }
.nx-device--mobile svg { width: 13rem; }
.nx-device figcaption { margin-top: 0.6rem; font-size: 0.7rem; color: var(--md-default-fg-color--light); }

.nx-device__body { fill: #2a2a2e; stroke: var(--md-default-fg-color--lightest); stroke-width: 0.6; }
.nx-device__bezel { fill: #0c0c0c; }
.nx-device__controls { fill: #45454b; }
.nx-device__camera { fill: #050505; }

.nx-slide { opacity: 0; transition: opacity 0.8s ease; }
.nx-slide.is-active { opacity: 1; }

.nx-cards {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 3rem;
}

.nx-card {
  padding: 1.2rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.6rem;
  background: var(--md-default-bg-color);
}

.nx-card h2 { margin: 0; font-size: 1.1rem; font-weight: 700; }
.nx-card p { margin: 0.4rem 0 1rem; color: var(--md-default-fg-color--light); }
.nx-card__actions { display: flex; flex-wrap: wrap; gap: 0.5rem; }

.nx-badge {
  display: inline-block;
  margin-left: 0.4rem;
  padding: 0.1rem 0.5rem;
  border-radius: 1rem;
  font-size: 0.6rem;
  font-weight: 700;
  vertical-align: middle;
  color: var(--md-accent-fg-color);
  border: 1px solid var(--md-accent-fg-color);
}

.nx-strip { margin-top: 3rem; text-align: center; }
.nx-strip h2 { font-size: 1.1rem; font-weight: 700; }
.nx-strip p { max-width: 36rem; margin: 0.4rem auto; color: var(--md-default-fg-color--light); }
.nx-strip a { color: var(--md-accent-fg-color); }

@media (prefers-reduced-motion: reduce) {
  .nx-slide { transition: none; }
}

@media screen and (max-width: 44.9375em) {
  .nx-devices { flex-direction: column; align-items: center; gap: 2rem; }
  .nx-cards { grid-template-columns: 1fr; }
  .nx-hero__title { font-size: 1.8rem; }
}
```

- [ ] **Step 6: Build and run all checks**

```bash
$V/mkdocs build --strict 2>&1 | grep -E "WARNING|ERROR" ; $V/python tools/check_site.py && node --test tools/
```
Expected: no WARNING or ERROR, `0 failure(s)`, `# fail 0`.

- [ ] **Step 7: Check in a browser**

Run `$V/mkdocs serve -a 127.0.0.1:8123` in the background. Using the Playwright tools, take a screenshot of `/` for each of:
1. 1280×900, light mode (`browser_emulate_media` colorScheme `light`)
2. 1280×900, dark mode
3. 375×800, dark mode

Confirm:
- Both devices are visible and the Brick Pro's screen shows a screenshot.
- The cards and the strip are readable in both modes.
- At 375 px the devices stack and `document.documentElement.scrollWidth <= innerWidth`.
- After 4 s the Brick's active slide has changed (`document.querySelector('.nx-device--handheld .is-active').getAttribute('href')` differs).
- With `browser_emulate_media` reducedMotion `reduce` and a reload, it has not changed after 4 s.
- The Material palette toggle still works on the landing page.
- **Read the docs** goes to `/handheld/`.

Stop the server and show the user the screenshots.

- [ ] **Step 8: Commit**

```bash
git add overrides/home.html docs/index.md docs/stylesheets/home.css docs/assets/landing tools/check_site.py
git commit -m "feat(site): add landing page with Brick Pro and Z Fold 8 frames"
```

---

## After the plan

- Phone screenshots: capture from the Fold 8 cover screen with
  `adb exec-out screencap -p > docs/assets/landing/mobile/<name>.png`. Add one
  `<image class="nx-slide">` each in the mobile SVG, remove the placeholder,
  and adjust the screen rect to the capture's real ratio.
- Refine the slideshow picks and the device outlines against the real
  hardware.
