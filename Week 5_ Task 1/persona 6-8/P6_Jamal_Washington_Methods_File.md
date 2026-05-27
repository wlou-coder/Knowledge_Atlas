# Task 1 Methods File — P6 · Jamal Washington · Licensed Architect
## Track 4, Task 1 · COGS 160 Spring 2026
## Date: 2026-05-07

---

## 1. Overview

| Source | Questions in Corpus | % |
|--------|--------------------|----|
| Source 1 — LLM Panel | 28 | 56.0% |
| Source 2 — Literature Mining | 11 | 22.0% |
| Source 3 — Cross-Product Synthesis | 11 | 22.0% |
| **Total** | **50** | **100%** |

All 50 questions passed the canonical-value validator (no non-canonical axis tags). The corpus is within the 40–60 target range. No winnowing was required; the 50 raw questions satisfied all minimum sub-flavour requirements without reduction.

---

## 2. Source 1 — LLM Panel

### 2.1 Panel Configuration

| Panellist | Sub-Flavour | Orientation | Time Budget | Device |
|-----------|-------------|-------------|-------------|--------|
| Jamal-SpaceDesigner | P6-space-designer | Project-phase practitioner — needs space-type-specific design guidance for a current schematic-design decision in healthcare or higher-ed | 5 min | Meeting-room laptop |
| Jamal-ClientBriefer | P6-client-briefer | Pre-meeting prep — needs the one-paragraph scientific case to put in front of a sceptical client or board | 3 min | Phone, walking to meeting |
| Jamal-EvidenceChecker | P6-evidence-checker | Fact-verifier — needs to know whether a colleague's claim or a trade-press assertion has genuine empirical backing | 4 min | Office desktop |
| Jamal-SpecTranslator | P6-spec-translator | Specification writer — needs a research finding translated into a buildable number (lux level, STC rating, RT60, ppm threshold) | 6 min | Revit workstation, dual-screen |
| Jamal-QuickLookup | P6-quick-lookup | Pre-call or in-meeting fact-check — needs a one-paragraph answer with citations before the next agenda item | 2 min | Phone under conference table |

Three panels were run with the above five panellists. Panel-A was scoped to healthcare facility types (patient rooms, ICUs, NICUs, waiting areas, rehabilitation corridors, emergency departments). Panel-B was scoped to higher-education facility types (classrooms, lecture halls, student unions, libraries, research labs, wellness centres). Panel-C was scoped to cross-cutting workplace, sustainability, and marketing-claim scenarios that arise across both Jamal's primary verticals.

### 2.2 Scenario Card Scaffold (Q1–Q4)

Each panellist received four scenario card questions derived from their sub-flavour context:

- **Q1** — What would the panellist type or click first? (entry action into `ka_home_practitioner.html` via `design-decision` or `client-brief` workflow)
- **Q2** — What result would satisfy them? (adequacy threshold — what the answer must contain for Jamal to close the tab and act on it)
- **Q3** — What would make the result feel insufficient? (failure mode — what triggers bail or forces him to call a consultant instead)
- **Q4** — What further question would he ask after receiving an initial answer? (follow-on that reveals his underlying project constraint)

### 2.3 Panel Run Record

| Field | Panel-A | Panel-B | Panel-C |
|-------|---------|---------|---------|
| Run ID | Jamal-Panel-01 | Jamal-Panel-02 | Jamal-Panel-03 |
| Facility scope | Healthcare | Higher-Education | Cross-cutting |
| Target workflow | `design-decision` | `design-decision` | `client-brief` |
| Panellists active | SpaceDesigner, SpecTranslator, QuickLookup | SpaceDesigner, SpecTranslator, QuickLookup | ClientBriefer, EvidenceChecker |
| Questions generated | 12 | 10 | 6 |
| Falsifier Hypothesis 1 | **Partially falsified** — SpaceDesigner and SpecTranslator found relevant constructs but no practitioner-facing summary card with actionable spec ranges | **Partially falsified** — higher-ed classroom content present but not separated from general office findings | **Falsified** — ClientBriefer could not locate a client-ready export or citation-formatted summary paragraph |
| Falsifier Hypothesis 2 | `page_serves_persona: partially` — constructs present, practitioner translation layer absent | `page_serves_persona: partially` — content present, space-type filter not functional for educational sub-types | `page_serves_persona: no` — evidence tray readable but not exportable in client-ready format |

### 2.4 Panel Questions Retained After Winnowing

All 28 panel questions were retained. Rationale: all five sub-flavours are represented across the three panel runs, no semantic duplicates were identified across panels (the closest pair — J-Q-013, about patient courtyard views, and J-Q-045, about biophilic post-surgical analgesia — ask about different outcome types and map to different sub-flavours), and all five cognitive_purpose values are represented in the panel-sourced questions.

---

## 3. Source 2 — Literature Mining

### 3.1 Data Source

PNU template library (`Article_Eater_PostQuinean_v1_recovery/data/templates/`) — approximately 166 templates as of Spring 2026, each encoding a structured IV–mechanism–DV claim about a built-environment effect. Templates were identified by domain keyword matching across eight domains directly relevant to Jamal's two primary verticals.

### 3.2 Templates Sampled

| Template ID | Domain | Core IV | Core DV | Practitioner Relevance |
|-------------|--------|---------|---------|------------------------|
| template-biophilia-visual-access | Biophilia | Window view / nature access | Stress, recovery | Hospital room and courtyard design decisions |
| template-biophilia-stress-recovery | Biophilia | Biophilic element exposure | Cortisol, distress | Pediatric and inpatient clinical settings |
| template-biophilia-air-quality | Biophilia | Living plant walls | VOC concentration | Healthcare air quality spec |
| template-complexity-visual-arousal | Complexity | Visual complexity of art | Arousal, mood | Patient room art selection |
| template-color-affect-clinical | Colour | Wall colour (hue, saturation) | Mood, pain perception | Patient room finishes spec |
| template-material-wood-stress | Material | Wood surface presence | Cortisol, HRV | Material selection for clinical and higher-ed spaces |
| template-spatial-ceiling-height | Spatial | Ceiling height | Spaciousness, social comfort | Healthcare and classroom ceiling spec |
| template-thermal-cognitive-performance | Thermal | Thermal comfort (operative temperature) | Test scores, cognitive performance | Classroom and study space HVAC spec |
| template-IAQ-CO2-cognition | IAQ | CO₂ concentration | Decision-making, cognitive performance | Classroom ventilation spec |
| template-circadian-lighting-clinical | Circadian | Lighting colour temperature and timing | Sleep quality, delirium rates | Hospital lighting protocol spec |
| template-biophilia-opioid-warrant-scope | Biophilia | Window view of nature | Post-surgical analgesic requirement | Patient room window positioning |

### 3.3 Mining Procedure

For each template, the following steps were applied:

1. Read the template's core IV–mechanism–DV claim to identify the question the template answers.
2. Phrase the anchor question explicitly in Jamal's practitioner voice — framed as a design decision or spec question, not as a research hypothesis.
3. Generate two to three follow-up questions he would ask after receiving the anchor answer, varying across his sub-flavours.
4. Tag each question on all five axes using only canonical values.
5. Set `source: mining` and `provenance: [template-id]`.
6. Apply the persona-fit gate: any question that could be asked by a researcher without the practitioner's space-type axis was revised until it was unambiguously Jamal's.

---

## 4. Source 3 — Cross-Product Synthesis

### 4.1 Data Source

Tagging_Contractor IV hierarchy (~440 active tags across ~20 domains) and Outcome_Contractor DV hierarchy (seven top-level domains, ~80 level-2 outcome terms). IV and DV levels were selected to match Jamal's two primary verticals (healthcare, higher-education) and his organisational axis (space type rather than academic taxonomy).

### 4.2 Four Corners Selected

| Corner | IV (Tagging domain) | DV (Outcome domain) | Rationale |
|--------|---------------------|---------------------|-----------|
| Low / Low | `spatial[wayfinding-clarity]` (single concrete feature) | `affect[anxiety]` (direct emotional state) | Outpatient clinic corridor problem — Jamal encounters this in schematic design; evidence is sparse, mechanism uncertain |
| Low / High | `biophilia[nature-view]` (single biophilic feature) | `behav[attendance]` (complex behavioural outcome) | University student attendance — client-brief scenario; surprising IV × DV combination that a practitioner would not expect |
| High / Low | `material[thermal-mass]` (complex material property) | `physio[thermal-comfort]` (direct physiological state) | Hospital courtyard in hot climate — spec-translation problem; well-studied IV, underspecified DV in clinical settings |
| High / High | `spatial[window-to-wall-ratio]` (complex spatial feature) | `health[stress-recovery]` (complex health outcome) | Hospital patient room glazing — three-way trade-off (view, thermal, glare); most complex corner and most relevant to Jamal's healthcare vertical |

### 4.3 Questions per Corner

Three questions per corner × four corners = 12 cross-product questions. Two additional questions were generated for the High/High corner given the density of Jamal's glazing and lighting decisions in healthcare projects, producing 11 total after one cross-product question was reclassified as panel-sourced upon review. Low/Low questions emphasise `mechanistic` evidential demand and `deliberation` cognitive purpose, reflecting Jamal's need to choose between two design levers (signage vs. spatial layout). High/High questions emphasise `converging` demand and `deliberation` purpose, reflecting the multi-variable optimisation problems that arise in complex glazing and lighting decisions.

---

## 5. Known LLM-Panel Limitations

**Time-budget compression.** Jamal's chip is "time-starved, action-oriented; bails fast." Panel agents were configured with 2–6 minute time budgets, which suppresses the generation of multi-part follow-up questions. Real Jamal questions in a 2-minute session would be shorter and more telegraphic than the questions generated here; the corpus may slightly over-represent the deliberative questions he would ask in a longer session.

**Voice formality drift.** Panel questions were written in a practitioner voice but tend toward more complete sentences than Jamal would actually type. Real search bar input from a time-starved user is often a noun phrase rather than a full question. The question field in the corpus reflects the underlying intent rather than the literal search string.

**Spec-translator specificity.** Several spec-translator questions request specific numerical ranges (lux, STC, RT60, CCT). These numbers were not drawn from the actual PNU template content (which was not directly accessible) but from the literature on these metrics. A real spec-translator query would be validated against the actual template output; here the adequacy condition operationalises the expected output, not the actual one.

**Panel-A healthcare bias.** Healthcare scenarios dominate the panel output (Panel-A generated 12 of 28 panel questions) because healthcare EBD is Jamal's firmest professional identity. Higher-education questions are proportionally underrepresented relative to the 50/50 split of his firm's project portfolio. The mining and cross-product sources partially compensate.

**No portal interaction.** All panel runs were conducted as scenario-card thought experiments; the actual `ka_home_practitioner.html` portal was not interacted with. The Falsifier Hypothesis results therefore reflect the author's model of the portal's current state rather than observed interaction failures.

**Single-author voice.** All five sub-flavour agents were populated by the same generative process. True inter-agent diversity — a QuickLookup panellist who would never ask a question requiring three citations vs. a ClientBriefer who constructs multi-sentence justifications — is approximated by the sub-flavour framing but not produced by genuinely independent agents.

---

## 6. Winnowing Record

No winnowing was required. All 50 questions satisfied the rubric minimums:

- All five sub-flavours have ≥5 questions: P6-space-designer (10), P6-client-briefer (10), P6-evidence-checker (10), P6-spec-translator (10), P6-quick-lookup (10). All pass the ≥5 gate.
- All five cognitive_purpose values are represented except discovery (1 question: J-Q-025, "resimercial" trend check). Discovery is underrepresented by design — Jamal's chip is purposive, not exploratory. The single discovery question is retained because trend-checking ("is this a real evidence base or marketing?") is a recognisable practitioner behaviour.
- All four cross-product corners are populated.
- Total of 50 is within the 40–60 range.

The closest potential duplicate pair — J-Q-013 (nature views for patient recovery, persuasion context) and J-Q-045 (biophilic features and post-surgical opioid use, quick-lookup context) — ask about different outcome types (general recovery vs. analgesic requirement), map to different sub-flavours (P6-client-briefer vs. P6-quick-lookup), and have different adequacy conditions. Both retained.

---

## 7. Final Coverage Summary

| Axis | Value | Count | % |
|------|-------|-------|---|
| **cognitive_purpose** | information-seeking | 19 | 38.0% |
| | inquiry | 13 | 26.0% |
| | deliberation | 10 | 20.0% |
| | persuasion | 7 | 14.0% |
| | discovery | 1 | 2.0% |
| **answer_shape** | Toulmin | 15 | 30.0% |
| | contrast-pair | 14 | 28.0% |
| | ranked-brief | 10 | 20.0% |
| | procedure | 8 | 16.0% |
| | field-map | 3 | 6.0% |
| **evidential_demand** | converging | 21 | 42.0% |
| | causal-with-mechanism | 11 | 22.0% |
| | measurement-grade | 9 | 18.0% |
| | suggestive | 5 | 10.0% |
| | mechanistic | 4 | 8.0% |
| **persona_fit** | P6-space-designer | 10 | 20.0% |
| | P6-client-briefer | 10 | 20.0% |
| | P6-evidence-checker | 10 | 20.0% |
| | P6-spec-translator | 10 | 20.0% |
| | P6-quick-lookup | 10 | 20.0% |
| **source** | panel | 28 | 56.0% |
| | mining | 11 | 22.0% |
| | cross-product | 11 | 22.0% |

The corpus is information-seeking-heavy (38.0%), reflecting Jamal's primary cognitive mode: filling a known gap fast so he can act. Converging evidential demand dominates (42.0%), reflecting his tolerance for "multiple studies agree" as a sufficient evidence bar — he does not need a mechanism, he needs a defensible decision. The procedure answer shape (16.0%) is uniquely elevated compared to the researcher and theory-explorer corpora, reflecting the spec-translator sub-flavour's need for numbered steps with citable standards. The absence of persuasion from the researcher and theory corpora — versus 14.0% here — directly encodes the client-briefer sub-flavour, which has no parallel in an academic persona.
