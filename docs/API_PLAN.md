# NASA data integration plan

> **Implementation status: NOT CONNECTED.** The ASTROMIND Figma prototype is a visual/interactive design; this GitHub Pages companion website does not call external NASA APIs. The team's 240-second script still contains a placeholder requesting the exact source/API used, so do not advertise a completed integration without evidence.

## Recommended services

### 1) NASA Image and Video Library API — first integration priority

**Why:** The most direct way to show authentic mission history is to surface NASA media and captions for Apollo, Mars Pathfinder / Sojourner, and Opportunity.

- Documentation: [NASA Image and Video Library API](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)
- Example search endpoint: `https://images-api.nasa.gov/search?q=Sojourner&media_type=image`
- Example users see: an image, NASA-provided caption, date, NASA ID, attribution, a link to the original media record.
- Integration work: fetch search results, sanitize/curate results, show loading and errors, cache approved media, and track credit lines.

**Privacy & reliability:** No API key is required for basic image searches, but rate limits and media-credit requirements still matter. Avoid automatically treating every search result as a verified illustration of a particular fact.

### 2) Moon Trek and Mars Trek — surface exploration maps

**Why:** Students could navigate real surface maps around significant mission locations rather than a generic illustration.

- Documentation: [NASA Trek Tile Services](https://trek.nasa.gov/tiles/apidoc/)
- Data type: map image tile layers via WMTS, with map projection and layer-specific constraints.
- Example users see: a labeled lunar/Martian basemap with mission positions and a small NASA source panel.
- Integration work: select WMTS layers and compatible projection, implement a tile client, align site coordinates, check attribution.

**Caution:** A Figma mockup is not evidence that geospatial layers or accurate coordinates are already built.

### 3) Planetary Data System Search API — research enrichment

**Why:** PDS archives can provide machine-readable metadata that supports accurate explanations of science and investigations.

- Documentation: [PDS Search API](https://nasa-pds.github.io/pds-api/)
- Example users see: a short science finding, a source reference, the mission/instrument and a plain-language explanation.
- Integration work: understand relevant product collections, map archive metadata to educational content, verify interpretations with NASA publications.

**Caution:** PDS metadata is often technical. It needs human curation before becoming student-facing language or quiz content.

## Suggested implementation stages

| Stage | Deliverable | Verification |
|---|---|---|
| 0 — Current | Mission summaries + NASA reference links | Links visible in repository and website |
| 1 — Media | NASA Image API results displayed with credit fields | Save example NASA IDs and dated screenshots of real responses |
| 2 — Geography | Moon/Mars real surface basemap | Document tile source, layer, projection and mission coordinates |
| 3 — Science | PDS-backed science facts and source IDs | Independent review of factual accuracy |
| 4 — Learning | Quiz and progress linked to evidence | Test with student participants and record findings |

## Data model suggestion

Existing `data/mission-highlights.json` separates authored educational text from source references. For a future integration, extend each mission with fields such as:

```json
{
  "nasaMediaId": null,
  "mediaCredit": null,
  "mediaSourceUrl": null,
  "apiFetchVerifiedAt": null,
  "mapLayerId": null,
  "pdsProductId": null
}
```

Do not fill these with guesses.

## Safe 30-second script wording

Until one of the services is integrated and shown on screen:

> "Grounded in NASA's public mission resources, students explore real discoveries and test their knowledge through quizzes."

After integration, you can name **only** the actually implemented service and describe what data the user sees. The PDF's `[NAME THE EXACT NASA SOURCE OR API IMPLEMENTED]` remains an explicit TODO until that evidence exists.
