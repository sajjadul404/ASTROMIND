# Prototype & user experience

## What is the primary prototype?

The primary prototype is a **Figma interactive design**, not an app executable hosted on GitHub.

**Open:** [ASTROMIND Figma prototype](https://www.figma.com/proto/OkwNxRuUFlf88F82MKg0HP/Nasa-space-app-challenge-2026?node-id=48-3&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=3%3A6)

The above link was preserved from the earlier ASTROMIND project materials. It should be opened and checked for public access before final submission.

## Proposed learner journey

1. **Enter ASTROMIND.** The start-screen screenshot introduces a cinematic rocket/astronaut aesthetic with a large START call to action.
2. **Choose an astronaut.** The learner identifies with an explorer character.
3. **Choose a destination.** Moon or Mars provides geographic and mission context.
4. **Meet a machine.** Apollo Lunar Rover, Sojourner, or Opportunity anchors a mission story.
5. **Discover the evidence.** Show source-attributed NASA mission photos and concise technical explanations.
6. **Answer a quiz.** Reinforce a mission fact and explain both the right answer and the significance.
7. **Continue exploring.** Introduce the next mission and its legacy.

These steps follow the team's script and design goals. Do not claim that each step is implemented or connected in the Figma file until someone has walked through the current version of the prototype.

## Visual assets currently included

- `../assets/images/astromind-start-screen.png` — supplied opening screen screenshot.
- `../assets/images/orbit-smiths-team.png` — supplied team poster.

We have **not** fabricated additional gameplay screenshots. Export new ones from Figma if you want a richer visual walkthrough: astronaut selection, destination map, machine exploration, fact card, quiz interaction and completion screen. Store them under `assets/images/screens/` and add source captions.

## Figma vs GitHub companion website

| | Figma prototype | GitHub Pages companion |
|---|---|---|
| Main purpose | Show the intended game interaction and visual language | Explain the project clearly to judges and collaborators |
| Contains | Figma screens and connections | Landing page, mission summaries, small showcase quiz, team poster |
| Deliverable | Figma URL | Static HTML/CSS/JS in this repo |
| Live NASA data | Not demonstrated by repository | Not integrated |

## Interaction and accessibility priorities

- Use a visible focus state and sufficiently large tap targets.
- Add optional captions/alt text for source imagery.
- Keep educational text brief and age-appropriate.
- Show answer explanations, not only a correct/incorrect label.
- Support reduced-motion users when building a game runtime.
- Confirm that the landscape opening screen still works on common device aspect ratios.

The companion website includes semantic controls, keyboard focus indicators and a reduced-motion CSS preference. Its quiz is **not** evidence that the Figma prototype contains an equivalent working quiz.
