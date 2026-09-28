"""Post-build checks for the built site.

Run after `mkdocs build --strict` from the repo root: python tools/check_site.py
"""
import os
import re
import subprocess
import sys
from pathlib import Path

SITE = Path(os.environ.get("SITE_DIR", "site"))
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
    moved_elsewhere = {"index.md", "desktop.md"}  # landing page; Desktop has its own section
    return [p for p in pages if p not in moved_elsewhere and not p.startswith("reference/")]


def check_desktop_section():
    html = (SITE / "desktop" / "index.html").read_text()
    check('id="desktop-app"' in html, "desktop/ is not the Desktop App page")
    check(not (SITE / "handheld" / "desktop").exists(), "Desktop App still published under handheld/")


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


def check_about():
    html = (SITE / "about" / "index.html").read_text()
    check('id="why-nx-redux"' in html, "About page lacks the Why NX Redux section")
    for href in ["../handheld/getting-started/", "../mobile/getting-started/", "../desktop/"]:
        check(f'href="{href}"' in html, f"About page lacks a link to {href}")
    for old, new in [("handheld", "handheld/getting-started/"), ("mobile", "mobile/getting-started/")]:
        page = (SITE / old / "index.html").read_text()
        check(new.split("/", 1)[1] in page and "location" in page, f"/{old}/ does not redirect to {new}")


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


def check_no_platform_toggle():
    check(not (SITE / "platform-pages.json").exists(), "platform-pages.json is still published")
    html = (SITE / "handheld" / "index.html").read_text()
    check("nx-platform" not in html and "platform-switch.js" not in html, "header platform toggle is still wired")


def check_landing():
    html = (SITE / "index.html").read_text()
    for needle in ['class="nx-menu"', 'nx-device--handheld', 'nx-device--mobile', 'Coming soon',
                   'href="handheld/getting-started/"', 'href="mobile/getting-started/"', 'class="nx-hints"',
                   'prefers-reduced-motion', 'home.css']:
        check(needle in html, f"landing lacks {needle!r}")
    check("nx-card" not in html, "landing still has the old platform cards")
    check('id="why-nx-redux"' not in html,
          "Why NX Redux blurb should live on the handheld overview, not the landing page")
    check(html.count('class="nx-slide') == 4, "each device should cycle the same 2 screens (4 slides)")
    for asset in ["handheld/brick-pro.webp", "handheld/main-menu.webp", "handheld/game-list.webp", "mobile/zfold8.webp", "mobile/main-menu.webp", "mobile/game-list.webp"]:
        check((SITE / "assets" / "landing" / asset).exists(), f"landing image not published: {asset}")
    css = (SITE / "stylesheets" / "home.css").read_text()
    check("misans-semibold.woff2" in css, "landing does not load the NX Redux UI font")
    check((SITE / "assets" / "fonts" / "misans-semibold.woff2").exists(), "MiSans font file not published")


HIGHLIGHT_LINKS = ["handheld/netplay/", "handheld/emulators/", "handheld/guide/game-switcher/",
                   "handheld/apps/retroachievements/", "handheld/apps/device-sync/",
                   "handheld/apps/music-player/", "handheld/guide/osd/", "handheld/apps/artwork-manager/",
                   "handheld/apps/game-tracker/", "handheld/apps/portmaster/", "handheld/apps/cheats/"]


def check_highlights():
    html = (SITE / "index.html").read_text()
    check(html.count('class="nx-feature"') == len(HIGHLIGHT_LINKS), "every feature needs a row")
    check(html.count('class="nx-features__pane') == len(HIGHLIGHT_LINKS), "each feature needs a preview pane")
    for href in HIGHLIGHT_LINKS:
        check(f'href="{href}"' in html, f"features lack a link to {href}")
        check((SITE / href / "index.html").exists(), f"feature target missing: {href}")
    for src in re.findall(r'class="nx-features__shot"[^>]*src="([^"]+)"', html):
        check((SITE / src).exists(), f"feature screenshot missing: {src}")
    for name in ["home", "games", "game", "detail"]:
        check(f"assets/landing/features/ra-{name}.webp" in html, f"achievements slideshow lacks the {name} screen")
    for name in ["join", "connection", "select-host", "connected", "playing"]:
        check(f"assets/landing/features/netplay-{name}.webp" in html, f"netplay slideshow lacks the {name} screen")
    check(html.count('role="tab" id="nx-tab-') == len(HIGHLIGHT_LINKS), "feature rows should be tabs that select, not links")
    check(html.count('class="nx-features__link"') == len(HIGHLIGHT_LINKS), "each feature description needs its docs link")


def check_not_found():
    html = (SITE / "404.html").read_text()
    check('class="nx-screen nx-error"' in html, "404 page is not the NX Redux error screen")
    check("No cartridge detected." in html, "404 page lacks its message")
    check('id="nx-error-home"' in html and 'id="nx-error-back"' in html, "404 page lacks Home and Back")
    check('for="__search"' in html, "404 page lacks the search hint")


def check_sidebars():
    # Pages inside a multi-page section keep the sidebar; only the landing,
    # About and Desktop (one page in their tab) hide it.
    allowed = {"index.md", "about.md", "desktop/index.md"}
    for md in Path("docs").rglob("*.md"):
        rel = md.relative_to("docs").as_posix()
        if rel.startswith("_shared/") or rel in allowed:
            continue
        head = md.read_text().split("\n---", 1)[0] if md.read_text().startswith("---") else ""
        check("navigation" not in head, f"{rel} hides the sidebar")


CHECKS = [check_redirects, check_desktop_section, check_images, check_about, check_mobile_section, check_snippets_inlined,
          check_no_platform_toggle, check_landing, check_highlights, check_not_found, check_sidebars]


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
