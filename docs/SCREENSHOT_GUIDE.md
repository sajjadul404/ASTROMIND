# ASTROMIND Screenshot Replacement Guide

This repository includes **seven temporary labeled PNG placeholders** so it renders without broken images before the team adds actual Figma screenshots. These are **not representations of actual game screens**.

## Export setup

- Orientation: **horizontal / landscape**, preferably **16:9**.
- Suggested resolution: **1600 × 900 px** or **1920 × 1080 px**.
- Format: **PNG**, RGB, ideally under 1–2 MB each for GitHub readability.
- Crop to the actual design frame; keep important UI away from the edges.
- Export from the actual Figma prototype. Avoid staged or invented screens.
- Preserve accurate attribution for external NASA imagery and fonts.

## Exact filenames

All screenshot files go inside **`assets/screenshots/`**. Overwrite the matching placeholder without changing the filename:

| Order | Filename | What to export |
|:--:|:--|:--|
| 01 | `01-character-selection.png` | A wide screenshot showing the start of the student journey and astronaut options. |
| 02 | `02-mission-selection.png` | A wide screenshot with the Moon / Mars mission map and mission choices. |
| 03 | `03-apollo-lunar-rover.png` | A wide screenshot introducing the Apollo lunar rover and its contribution. |
| 04 | `04-sojourner-on-mars.png` | A wide screenshot of the Sojourner mission story and learning content. |
| 05 | `05-opportunity-on-mars.png` | A wide screenshot highlighting Opportunity and the evidence for ancient water. |
| 06 | `06-knowledge-quiz.png` | A wide screenshot showing a real educational quiz question. |
| 07 | `07-quiz-feedback.png` | A wide screenshot showing the quiz response or learning summary. |

## How to replace an image

1. Export your horizontal screenshot from Figma.
2. Rename it to the exact filename above.
3. Replace the current file in `assets/screenshots/`.
4. Preview the `README.md` directly in VS Code or on GitHub.
5. If no matching screen exists in the prototype, **remove that image section** from `README.md` and the corresponding gallery card from `index.html`. Never leave a placeholder that could be mistaken for implemented gameplay.
6. Edit the screenshot caption if your screen displays a different feature.

The start screen and team poster are **already genuine team-provided images** in `assets/images/` and do not need replacing.

## Why horizontal images?

A 16:9 landscape frame remains readable across desktop GitHub README rendering and corresponds to the team's shared landscape mobile-game design. For long screens, use multiple captures rather than shrinking UI text into an unreadable composite.

## Note about NASA content and external images

When the Figma screen includes NASA photos, cite a specific official source and keep source/copyright notes in `docs/ASSET_CREDITS.md`. A NASA link alone does not prove an API integration.
