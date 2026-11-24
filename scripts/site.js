'use strict';

// This is a standalone project-showcase interaction, NOT the Figma game code.
// Mission notes are educational summaries from Team Orbit Smiths' pitch script.
const missions = {
  apollo: {
    world: 'MOON · APOLLO PROGRAM',
    title: 'Apollo Lunar Rover',
    description: 'The Lunar Roving Vehicle let Apollo astronauts investigate terrain beyond their landing site, supporting a much wider scientific exploration of the Moon.',
    fact: 'Exploring farther from the landing site',
    source: 'https://www.nasa.gov/mission/apollo-17/',
    planet: 'moon'
  },
  sojourner: {
    world: 'MARS · MARS PATHFINDER',
    title: 'Sojourner',
    description: 'Sojourner became the first robotic rover to operate on Mars, demonstrating that a small mobile explorer could examine rocks and soil on another planet.',
    fact: 'The first rover to operate on Mars',
    source: 'https://science.nasa.gov/mission/mars-pathfinder/',
    planet: 'mars'
  },
  opportunity: {
    world: 'MARS · EXPLORATION ROVER',
    title: 'Opportunity',
    description: 'Designed to last about 90 Martian days, Opportunity explored for nearly fifteen years and uncovered important evidence that liquid water had once existed on Mars.',
    fact: 'Nearly 15 years of exploration',
    source: 'https://science.nasa.gov/mission/mer-opportunity/',
    planet: 'mars'
  }
};

const missionButtons = document.querySelectorAll('[data-mission]');
const missionWorld = document.querySelector('#mission-world');
const missionTitle = document.querySelector('#mission-title');
const missionDescription = document.querySelector('#mission-description');
const missionFact = document.querySelector('#mission-fact');
const missionSource = document.querySelector('#mission-source');
const planetArt = document.querySelector('#planet-art');

missionButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const mission = missions[button.dataset.mission];
    if (!mission) return;
    missionButtons.forEach((choice) => {
      const selected = choice === button;
      choice.classList.toggle('active', selected);
      choice.setAttribute('aria-pressed', String(selected));
    });
    missionWorld.textContent = mission.world;
    missionTitle.textContent = mission.title;
    missionDescription.textContent = mission.description;
    missionFact.textContent = mission.fact;
    missionSource.href = mission.source;
    planetArt.className = `planet-art ${mission.planet}`;
  });
});

const quizButtons = document.querySelectorAll('[data-answer]');
const quizResult = document.querySelector('#quiz-result');
quizButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const correct = button.dataset.answer === 'correct';
    quizButtons.forEach((choice) => {
      choice.classList.remove('correct', 'incorrect');
      choice.setAttribute('aria-pressed', String(choice === button));
    });
    button.classList.add(correct ? 'correct' : 'incorrect');
    quizResult.textContent = correct
      ? 'Correct! Opportunity outlasted its planned 90-Martian-day mission by many years.'
      : 'Not quite. Try again: Opportunity explored Mars for nearly 15 years.';
  });
});
