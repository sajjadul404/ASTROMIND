#!/usr/bin/env python3
"""Offline, dependency-free checks for the ASTROMIND presentation repository."""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        errors.append(message)


expected = [
    "README.md", "index.html", "styles/site.css", "scripts/site.js", "docs/SCREENSHOT_GUIDE.md",
    "assets/images/astromind-start-screen.png", "assets/images/orbit-smiths-team.png",
    "assets/icons/orbit-mark.svg", "data/mission-highlights.json",
    "docs/PROJECT_OVERVIEW.md", "docs/PROTOTYPE_AND_UX.md", "docs/SOURCES.md",
    "docs/API_PLAN.md", "docs/PRESENTATION.md", "docs/TEAM.md",
    "docs/ROADMAP.md", "docs/ASSET_CREDITS.md", "docs/DEPLOYMENT.md",
    "docs/presentation/ASTROMIND-240-Second-Script.pdf",
    ".github/workflows/validate.yml", ".nojekyll", "PUSH_NEW_REPOSITORY.ps1",
]
for relative_path in expected:
    check((ROOT / relative_path).is_file(), f"Missing file: {relative_path}")

class ResourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.resources: list[str] = []
        self.ids: set[str] = set()
        self.scripts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        props = dict(attrs)
        if props.get("id"):
            self.ids.add(props["id"])
        for attr in ("href", "src"):
            value = props.get(attr)
            if value:
                self.resources.append(value)
        if tag == "script" and props.get("src"):
            self.scripts.append(props["src"])

html = (ROOT / "index.html").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
parser = ResourceParser()
parser.feed(html)

for url in parser.resources:
    if url.startswith(("https://", "http://", "mailto:", "data:", "#")):
        if url.startswith("#"):
            check(url[1:] in parser.ids, f"Missing HTML fragment anchor: {url}")
        continue
    relative = url.split("?", 1)[0].split("#", 1)[0]
    check((ROOT / relative).exists(), f"Local HTML resource not found: {url}")

for filename in ("astromind-start-screen.png", "orbit-smiths-team.png"):
    image = ROOT / "assets/images" / filename
    if image.exists():
        check(image.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n", f"Not a valid PNG signature: {filename}")

pdf = ROOT / "docs/presentation/ASTROMIND-240-Second-Script.pdf"
if pdf.exists():
    check(pdf.read_bytes()[:5] == b"%PDF-", "The provided pitch file is not a PDF")

missions_path = ROOT / "data/mission-highlights.json"
if missions_path.exists():
    data = json.loads(missions_path.read_text(encoding="utf-8"))
    check(data.get("apiConnected") is False, "API implementation status should remain false until verified")
    missions = data.get("missions", [])
    check(len(missions) == 3, "Expected three featured mission records")
    ids: list[str] = []
    for mission in missions:
        ids.append(mission.get("id", ""))
        choices = mission.get("quizOptions", [])
        answer = mission.get("correctOptionIndex")
        check(len(choices) >= 2, f"Not enough choices for {mission.get('name')}")
        check(isinstance(answer, int) and 0 <= answer < len(choices), f"Invalid quiz answer: {mission.get('name')}")
        check(mission.get("nasaReference", "").startswith("https://"), f"Missing NASA source: {mission.get('name')}")
    check(len(set(ids)) == len(ids), "Mission IDs should be unique")

# Screenshot slots must be real PNG files with landscape dimensions.
import struct
screenshot_names = [
    "01-character-selection.png", "02-mission-selection.png", "03-apollo-lunar-rover.png",
    "04-sojourner-on-mars.png", "05-opportunity-on-mars.png", "06-knowledge-quiz.png",
    "07-quiz-feedback.png",
]
for filename in screenshot_names:
    item = ROOT / "assets/screenshots" / filename
    check(item.is_file(), f"Missing screenshot slot: {filename}")
    if item.is_file():
        check(item.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n", f"Invalid screenshot PNG: {filename}")
        raw = item.read_bytes()
        if len(raw) >= 24 and raw[:8] == b"\x89PNG\r\n\x1a\n":
            width, height = struct.unpack(">II", raw[16:24])
            check(width > height, f"Screenshot is not horizontal: {filename}")
    check(filename in readme, f"Screenshot not used in README: {filename}")
check("figma.com/proto/" in readme, "Figma prototype URL missing from README")
check("astromind-start-screen.png" in readme, "Opening screenshot missing from README")
check("orbit-smiths-team.png" in readme, "Team poster missing from README")
check("not" in readme.lower() and "api" in readme.lower(), "README should describe API status")
check("mission-feature" in parser.ids and "quiz-result" in parser.ids, "Missing interactive showcase containers")

if errors:
    print(f"FAILED: {len(errors)} of {checks} checks did not pass")
    for problem in errors:
        print(f" - {problem}")
    raise SystemExit(1)
print(f"PASS: {checks} offline checks (files, images, PDF, page assets, missions, source references, status)")
