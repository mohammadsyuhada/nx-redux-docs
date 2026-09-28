"""Writes platform-pages.json: every page URL, for the Handheld / Mobile toggle."""
import json
from pathlib import Path

_urls = []


def on_files(files, config):
    _urls[:] = sorted(f.url for f in files.documentation_pages())
    return files


def on_post_build(config):
    Path(config["site_dir"], "platform-pages.json").write_text(json.dumps(_urls))
