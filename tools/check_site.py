"""Post-build checks for the built site.

Run after `mkdocs build --strict` from the repo root: python tools/check_site.py
"""
import json
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


CHECKS = [check_redirects, check_images, check_handheld_overview, check_mobile_section, check_snippets_inlined,
          check_platform_pages, check_toggle_wired]


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
