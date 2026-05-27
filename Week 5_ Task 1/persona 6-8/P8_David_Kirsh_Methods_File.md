# Task 1 Methods File — P8 · Prof. David Kirsh · Principal Investigator / Site Owner
## Track 4, Task 1 · COGS 160 Spring 2026
## Date: 2026-05-07

---

## 1. Overview

| Source | Questions in Corpus | % |
|--------|--------------------|----|
| Source 1 — LLM Panel | 43 | 86.0% |
| Source 2 — Literature Mining | 5 | 10.0% |
| Source 3 — Cross-Product Synthesis | 2 | 4.0% |
| **Total** | **50** | **100%** |

All 50 questions passed the canonical-value validator (no non-canonical axis tags). The corpus is within the 40–60 target range. No winnowing was required; the 50 raw questions satisfied all minimum sub-flavour requirements without reduction.

**Methodological note on source distribution.** The P8 corpus is panel-dominant (86.0%) by structural necessity, not by methodological failure. Prof. Kirsh's questions are not about environmental psychology findings — they are about the Atlas as an epistemic instrument and operational system. The PNU template library and the IV × DV cross-product matrix are primary sources for content questions (what does the science say about nature views?), not for system-state questions (has the warrant for the nature-view claim drifted in the past 24 hours?). Literature mining and cross-product synthesis were applied where applicable — to questions about template backing-study coverage and IV × DV matrix completeness — but their natural scope for this persona is narrow.

---

## 2. Source 1 — LLM Panel

### 2.1 Panel Configuration

| Panellist | Sub-Flavour | Orientation | Time Budget | Device |
|-----------|-------------|-------------|-------------|--------|
| Kirsh-TriageOperator | P8-triage-operator | Morning-arrival scan — needs to know whether anything is broken, blocked, or drifting before reading any email | 3 min | `ka_pi_dashboard.html` (to be designed), desktop |
| Kirsh-EpistemicGraphReader | P8-epistemic-graph-reader | Evidence-graph inspector — queries the state of the Atlas's epistemic graph for underdetermination accumulation, warrant drift, and thin template chains | 15 min | Desktop, full-screen graph view |
| Kirsh-StudentPipelineMonitor | P8-student-pipeline-monitor | Instructor / supervisor — checks student progress across all four tracks for milestone lag, review bottlenecks, and duplication of effort | 8 min | Desktop, student dashboard view |
| Kirsh-QualityController | P8-quality-controller | System reliability analyst — monitors extractor IRR, tagging drift, overconfidence, and quality-gate bypass | 12 min | Desktop, reliability metrics panel |
| Kirsh-SiteArchitect | P8-site-architect | Dashboard designer — asks what the `ka_pi_dashboard.html` page should contain, how it should be sorted, and how it should signal different error types | 20 min | Desktop, wireframing notes alongside |

Three panels were run with the above five panellists. Panel-A was scoped to operational triage and quality-control scenarios — the questions Kirsh asks when something may be wrong. Panel-B was scoped to student-pipeline and pedagogical scenarios — the questions he asks as an instructor. Panel-C was scoped to epistemic-graph reading and site-architecture scenarios — the questions he asks as the laboratory director designing and reading his own instrument panel.

### 2.2 Scenario Card Scaffold (Q1–Q4)

Each panellist received four scenario card questions derived from their sub-flavour context:

- **Q1** — What would the panellist look at first on `ka_pi_dashboard.html`? (or, since this page does not yet exist: what would he open first in the current system to answer this question?)
- **Q2** — What information would satisfy him? (adequacy threshold — what the dashboard must show for him to trust the reading and act)
- **Q3** — What would make the information feel insufficient or dishonest? (failure mode — what triggers the "instrument panel is lying to me" response)
- **Q4** — What further question would he ask after receiving an initial answer? (follow-on that reveals the underlying laboratory-director concern)

### 2.3 Panel Run Record

| Field | Panel-A | Panel-B | Panel-C |
|-------|---------|---------|---------|
| Run ID | Kirsh-Panel-01 | Kirsh-Panel-02 | Kirsh-Panel-03 |
| Operational scope | System health, extractor reliability, quality gate | Student pipeline, milestone tracking, pedagogical compliance | Epistemic graph, dashboard design, site architecture |
| Target page | `ka_pi_dashboard.html` (not yet built) | `ka_pi_dashboard.html` student view | `ka_home_theory.html` + planned dashboard |
| Panellists active | TriageOperator, QualityController | StudentPipelineMonitor, TriageOperator | EpistemicGraphReader, SiteArchitect |
| Questions generated | 18 | 10 | 15 |
| Falsifier Hypothesis 1 | **Falsified** — no `ka_pi_dashboard.html` exists; triage information is not aggregated anywhere in the current system | **Falsified** — no student-activity summary exists; pipeline stage per student is not visible in any single view | **Partially falsified** — epistemic graph is present but underdetermination density and warrant drift are not surfaced as navigable indicators |
| Falsifier Hypothesis 2 | `page_serves_persona: no` — dashboard page does not exist; the persona's primary need is unmet at the system level | `page_serves_persona: no` — student pipeline visibility requires manual cross-tab inspection across four track pages | `page_serves_persona: partially` — graph exists; triage-readable summary does not |

### 2.4 Panel Questions Retained After Winnowing

All 43 panel questions were retained. Rationale: all five sub-flavours are represented with exactly 10 questions each; no semantic duplicates were identified across panels; and all cognitive_purpose values present in the corpus are accounted for across the panel-sourced questions. The two closest potential duplicates — D-Q-002 (HITL items over 48 hours, triage) and D-Q-022 (student contributions not reviewed in 48 hours, pipeline-monitor) — involve the same time threshold applied to structurally different review queues (HITL queue vs. TA review queue); both retained.

---

## 3. Source 2 — Literature Mining

### 3.1 Data Source

PNU template library (`Article_Eater_PostQuinean_v1_recovery/data/templates/`) — approximately 166 templates as of Spring 2026. For P8, the mining prompt was adapted: instead of asking "what follow-up questions would a person who received this template's answer ask?", it asked "what questions does a PI responsible for this template's epistemic integrity ask about the template's backing, scope, and reliability?" This re-framing is appropriate because Kirsh's relationship to templates is supervisory (is it honest?) rather than content-seeking (what does it say?).

### 3.2 Templates Sampled

| Template ID | Mining angle | Question type produced |
|-------------|--------------|------------------------|
| template-single-study-warrant-dependency | How many downstream claims depend on this single template's anchor study — and what is the retraction risk? | Epistemic-graph-reader: warrant-chain fragility |
| template-backing-study-coverage | What percentage of templates have ≥2 independent backing studies, and how has that changed this term? | Quality-controller: coverage metric trending |
| template-tag-misapplication-audit | Which tags are being applied to articles that do not match their definition, according to HITL review? | Quality-controller: Tagging_Contractor reliability |
| template-evidential-demand-tagging-audit | Are claims tagged causal-with-mechanism backed only by correlational studies — an inflation error? | Epistemic-graph-reader: tag-to-study mismatch |
| template-answer-shape-consistency-audit | Are Task 2 question-to-shape fittings internally consistent per the schema-fitting decision tree? | Student-pipeline-monitor: Track 2 compliance check |

### 3.3 Mining Procedure

For each template, the following steps were applied:

1. Read the template's core claim structure to identify what a PI responsible for its integrity would need to verify.
2. Phrase the question in Kirsh's laboratory-director voice — framed as a quality-check or epistemic-audit question, not a content question.
3. Generate one to two follow-up questions he would ask after receiving the audit result.
4. Tag each question on all five axes using only canonical values.
5. Set `source: mining` and `provenance: [template-id]`.
6. Apply the persona-fit gate: questions were reviewed to ensure they are unaskable by any student, practitioner, or theory explorer — they require PI-level visibility into the full pipeline.

---

## 4. Source 3 — Cross-Product Synthesis

### 4.1 Data Source

For P8, the IV × DV cross-product was applied not to environmental psychology variables but to system-level variables: IV = system inputs (warrant state changes, extractor outputs, student contribution events) and DV = system health outcomes (triage accuracy, epistemic reliability, dashboard readability). This is a deliberate re-interpretation of the cross-product method for a persona whose domain is the Atlas system, not its content.

### 4.2 Four Corners Selected

| Corner | IV (System domain) | DV (System outcome) | Rationale |
|--------|--------------------|---------------------|-----------|
| Low / Low | `system[warrant-state-change]` (single discrete event) | `system[triage-accuracy]` (direct dashboard reading) | Warrant drift indicator design — what should the simplest warrant-change signal look like on the dashboard? |
| High / High | `IV:* × DV:*` (full cross-product matrix) | `system[mining-coverage]` (coverage completeness) | Which cells of the IV × DV matrix are unpopulated — evidence gap vs. mining gap diagnosis |

Only two cross-product questions were generated because the system-variable re-interpretation of the cross-product is structurally thinner than the content-variable application: the Atlas system has fewer meaningful IV × DV pairs than the environmental psychology literature. Additional cross-product generation would have produced artificial questions with no grounding in the actual system architecture.

### 4.3 Questions per Corner

One question per corner × two applicable corners = 2 cross-product questions (D-Q-046 and D-Q-019). These are the only questions in the corpus that treat system-level variables through the cross-product frame; all other system-design questions were generated through panel runs with site-architect and epistemic-graph-reader scenario cards.

---

## 5. Known LLM-Panel Limitations

**The page does not exist.** The most fundamental limitation: `ka_pi_dashboard.html` does not exist. Every question in the P8-site-architect sub-flavour and many in the P8-triage-operator sub-flavour are questions about a system that has not yet been built. Panel runs simulated Kirsh's behaviour at a hypothetical dashboard, not at an actual one. Questions about what alert thresholds should be (D-Q-043), how queue depth should be displayed (D-Q-042), and what the above-fold zone should contain (D-Q-041) are design requirements, not user observations.

**Single-user persona with no variation.** Unlike the researcher persona (five sub-flavours with genuine variation in career stage and disciplinary home), P8 is a single user — David Kirsh — with no meaningful analogues. All five panellists are therefore variants of the same person in different operational modes, not genuinely different individuals. The inter-panellist variation that makes panel generation useful is replaced by intra-session mode variation (triage mode vs. graph-reading mode vs. design mode).

**System knowledge assumed.** Panel agents were configured with knowledge of the Atlas's pipeline architecture (extractor → HITL → Tagging_Contractor → PNU template → warrant state). This knowledge was stipulated in the scenario cards rather than derived from observation of the actual system. Questions that reference specific system components (Article_Eater, Tagging_Contractor registry, Outcome_Contractor ontology) encode assumed system architecture that should be verified against the actual codebase before the corpus is used in journey design.

**Measurement-grade dominance is structurally correct but unusual.** 72.0% of questions carry `measurement-grade` evidential demand. This is not a tagging error — it reflects the fact that Kirsh's questions about his own instrument panel require precise, actionable answers (a specific IRR value, a specific count of overdue items, a specific latency relative to baseline). A dashboard that answers his questions with "probably" or "seems like" is not a trustworthy instrument. However, this distribution is so extreme that the Codebook Custodian should verify it does not reflect a miscalibrated understanding of the evidential-demand axis.

**Mining and cross-product are methodologically thin.** The honest limitation of this corpus is that two of the three required sources (mining and cross-product) are poorly matched to a persona whose questions are about system health rather than evidence content. The 14.0% non-panel sourcing is the lowest of the three corpora and reflects a genuine methodological constraint rather than a generation failure. The team's Mining Lead and Cross-Product Lead should note this when assessing corpus balance.

---

## 6. Winnowing Record

No winnowing was required. All 50 questions satisfied the rubric minimums:

- All five sub-flavours have ≥5 questions: P8-triage-operator (10), P8-epistemic-graph-reader (10), P8-student-pipeline-monitor (10), P8-quality-controller (10), P8-site-architect (10). All pass the ≥5 gate.
- Cognitive_purpose values: information-seeking (21), deliberation (14), inquiry (14), discovery (1). Persuasion is absent — a PI managing his own laboratory does not load positions into debates; he makes adjudication decisions. Discovery is nearly absent (1 question: D-Q-019, on unpopulated IV × DV cells) because the PI's goal is triage, not exploration.
- Cross-product corners are populated (two corners, per the system-variable re-interpretation).
- Total of 50 is within the 40–60 range.

The closest potential duplicate triplet — D-Q-001 (highest-priority action in 30 minutes), D-Q-009 (single action to prevent worst downstream consequence in 20 minutes), and D-Q-050 (five data points before clicking through) — probe structurally different questions: D-Q-001 asks what the current priority is; D-Q-009 asks what the single action is; D-Q-050 asks how the dashboard should be designed to answer D-Q-001 reliably. All three retained.

---

## 7. Final Coverage Summary

| Axis | Value | Count | % |
|------|-------|-------|---|
| **cognitive_purpose** | information-seeking | 21 | 42.0% |
| | deliberation | 14 | 28.0% |
| | inquiry | 14 | 28.0% |
| | discovery | 1 | 2.0% |
| | persuasion | 0 | 0.0% |
| **answer_shape** | ranked-brief | 32 | 64.0% |
| | contrast-pair | 7 | 14.0% |
| | field-map | 5 | 10.0% |
| | Toulmin | 4 | 8.0% |
| | procedure | 2 | 4.0% |
| **evidential_demand** | measurement-grade | 36 | 72.0% |
| | suggestive | 10 | 20.0% |
| | converging | 3 | 6.0% |
| | mechanistic | 1 | 2.0% |
| | causal-with-mechanism | 0 | 0.0% |
| **persona_fit** | P8-triage-operator | 10 | 20.0% |
| | P8-epistemic-graph-reader | 10 | 20.0% |
| | P8-student-pipeline-monitor | 10 | 20.0% |
| | P8-quality-controller | 10 | 20.0% |
| | P8-site-architect | 10 | 20.0% |
| **source** | panel | 43 | 86.0% |
| | mining | 5 | 10.0% |
| | cross-product | 2 | 4.0% |

The corpus is information-seeking-dominant (42.0%) and measurement-grade-dominant (72.0%), jointly reflecting the PI's triage imperative: fast, precise, actionable. The ranked-brief answer shape (64.0%) is the highest concentration of any single shape across all three corpora and reflects the dashboard's natural output format — sorted lists of items requiring attention, not argument structures or procedure guides. The complete absence of `causal-with-mechanism` evidential demand is the most defining structural feature of this corpus: Kirsh is not asking what mechanism links ceiling height to abstract thinking; he is asking whether the warrant for that claim has changed state in the past 24 hours. His questions presuppose the content layer of the Atlas and operate entirely at the epistemic-integrity and operational layer above it.
