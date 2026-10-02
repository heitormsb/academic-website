#!/usr/bin/env python3
"""Render the PDF CV from _data/cv.yml with RenderCV.

_data/cv.yml also feeds the web CV (/cv/), which reads a few keys that RenderCV's
schema rejects (`label`, `summary`, `address`). Publication URLs are also dropped:
they make the title clickable on the web but print as long, unbreakable lines in
the PDF. This script writes the filtered data to a temporary copy next to cv.yml (the paths in assets/rendercv/settings.yaml are
relative to it), renders, and cleans up.

Usage: python3 bin/render_cv.py   (requires `pip install -r requirements.txt`)
"""

import pathlib
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_data" / "cv.yml"
TEMP = ROOT / "_data" / "cv.rendercv.yml"
RENDERCV_DIR = ROOT / "assets" / "rendercv"
WEB_ONLY_KEYS = ("label", "summary", "address")


def main() -> int:
    data = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    for key in WEB_ONLY_KEYS:
        data["cv"].pop(key, None)
    for entry in data["cv"].get("sections", {}).get("Publications", []):
        entry.pop("url", None)
    TEMP.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    try:
        return subprocess.call(
            [
                "rendercv",
                "render",
                str(TEMP),
                "--design",
                str(RENDERCV_DIR / "design.yaml"),
                "--locale-catalog",
                str(RENDERCV_DIR / "locale.yaml"),
                "--settings",
                str(RENDERCV_DIR / "settings.yaml"),
            ]
        )
    finally:
        TEMP.unlink(missing_ok=True)
        for typ in (RENDERCV_DIR / "rendercv_output").glob("*.typ"):
            typ.unlink()


if __name__ == "__main__":
    sys.exit(main())
