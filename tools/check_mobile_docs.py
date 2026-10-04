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
    r"not released", r"[Cc]oming soon", r"(?m)^(?!.*legacy).*\bGPGX\b",  # GPGX only on a line that says legacy
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
