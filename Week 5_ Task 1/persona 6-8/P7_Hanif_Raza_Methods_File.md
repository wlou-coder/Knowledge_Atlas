# Task 1 Methods File — P7 · Dr. Hanif Raza · Philosopher of Cognitive Science
## Track 4, Task 1 · COGS 160 Spring 2026
## Date: 2026-05-07

---

## 1. Overview

| Source | Questions in Corpus | % |
|--------|--------------------|----|
| Source 1 — LLM Panel | 27 | 54.0% |
| Source 2 — Literature Mining | 15 | 30.0% |
| Source 3 — Cross-Product Synthesis | 8 | 16.0% |
| **Total** | **50** | **100%** |

All 50 questions passed the canonical-value validator (no non-canonical axis tags). The corpus is within the 40–60 target range. No winnowing was required; the 50 raw questions satisfied all minimum sub-flavour requirements without reduction.

---

## 2. Source 1 — LLM Panel

### 2.1 Panel Configuration

| Panellist | Sub-Flavour | Orientation | Time Budget | Device |
|-----------|-------------|-------------|-------------|--------|
| Hanif-MechanismTracer | P7-mechanism-tracer | Causal-chain analyst — enters via `mechanism-trace` workflow; wants the full MDC-style decomposition of a claimed effect | 25 min | Desktop, Zotero open in adjacent window |
| Hanif-RivalTheorist | P7-rival-theorist | Theory comparativist — seeks a side-by-side matrix of competing accounts and their discriminating predictions | 30 min | Desktop, argument-mapping software open |
| Hanif-UnderdeterminationProber | P7-underdetermination-prober | Coherentist epistemologist — probes whether the Atlas's evidence base can actually adjudicate between rivals or merely converges within a paradigm | 20 min | Desktop, paper notes |
| Hanif-WarrantAuditor | P7-warrant-auditor | Logical analyst — treats each Atlas claim as a Toulmin argument structure to be decomposed and evaluated | 20 min | Desktop, annotating a printed page |
| Hanif-CriticalTestSeeker | P7-critical-test-seeker | Experimental designer — asks what study would falsify one account but not its rival; often ends a long structural session | 15 min | Desktop, after extended mechanism-trace session |

Three panels were run with the above five panellists. Panel-A was scoped to restoration and stress-recovery theories (ART, SRT, predictive processing). Panel-B was scoped to spatial and perceptual theories (construal level, embodied cognition, wayfinding, fractal complexity). Panel-C was scoped to meta-epistemic questions about the Atlas's own argumentation layer (warrant structure, convergence, the WELL standard's Duhem-Quine vulnerability).

### 2.2 Scenario Card Scaffold (Q1–Q4)

Each panellist received four scenario card questions derived from their sub-flavour context:

- **Q1** — What would the panellist type or navigate to first? (entry action into `ka_home_theory.html` via `mechanism-trace` workflow)
- **Q2** — What result would satisfy them? (adequacy threshold — what the Atlas must show for Hanif to regard it as epistemically honest)
- **Q3** — What would make the result feel insufficient? (failure mode — what triggers loss of confidence in the Atlas as a philosophical testbed)
- **Q4** — What further question would he ask after receiving an initial answer? (follow-on that reveals the deeper theoretical commitment driving the session)

### 2.3 Panel Run Record

| Field | Panel-A | Panel-B | Panel-C |
|-------|---------|---------|---------|
| Run ID | Hanif-Panel-01 | Hanif-Panel-02 | Hanif-Panel-03 |
| Theoretical scope | ART / SRT / predictive processing | Construal level / embodied cognition / fractal complexity | Meta-epistemic (warrant structure, convergence, WELL standard) |
| Target workflow | `mechanism-trace` | `mechanism-trace` | `mechanism-trace` (theory-comparison branch) |
| Panellists active | MechanismTracer, RivalTheorist, UnderdeterminationProber | MechanismTracer, RivalTheorist, CriticalTestSeeker | WarrantAuditor, UnderdeterminationProber, CriticalTestSeeker |
| Questions generated | 11 | 9 | 7 |
| Falsifier Hypothesis 1 | **Falsified** — mechanism chain for ART present at summary level but not decomposed to intermediate steps; no underdetermination alert visible | **Partially falsified** — construal-level account present; embodied-cognition rival absent; no comparison matrix | **Falsified** — warrant structure not exposed as decomposable Toulmin diagram; backing type not distinguished from warrant |
| Falsifier Hypothesis 2 | `page_serves_persona: partially` — restoration literature present but theory-comparison view unavailable | `page_serves_persona: partially` — spatial content present, rival-theory comparison absent | `page_serves_persona: no` — argumentation layer not exposed as a navigable element |

### 2.4 Panel Questions Retained After Winnowing

All 27 panel questions were retained. Rationale: all five sub-flavours are represented across the three panels; no semantic duplicates were identified (the closest pair — H-Q-021, on ART/SRT adjudication, and H-Q-025, on whether convergence within a paradigm constitutes genuine confirmation — probe different epistemic concepts despite both addressing the ART/SRT literature); and all cognitive_purpose values represented in the panel-sourced subset are consistent with Hanif's chip (no persuasion questions appear, as expected for a Theory Explorer in long structural sessions).

---

## 3. Source 2 — Literature Mining

### 3.1 Data Source

PNU template library (`Article_Eater_PostQuinean_v1_recovery/data/templates/`) — approximately 166 templates as of Spring 2026. Templates were identified by theoretical-framework keyword matching across seven theory families directly relevant to Hanif's mechanism-trace and rival-theory sub-flavours.

### 3.2 Templates Sampled

| Template ID | Domain | Core theoretical claim | Hanif's entry angle |
|-------------|--------|------------------------|---------------------|
| template-spatial-ceiling-height-mechanism | Spatial | Ceiling height → construal-level → abstract thinking | Mechanism decomposition: cognitive vs. embodied pathway |
| template-sound-reading-comprehension | Sound | Acoustic distraction → phonological interference → reading impairment | Rival-mechanism: phonological vs. arousal account |
| template-color-affect-mechanism | Colour | Colour exposure → psychophysiological response → mood change | Rival mechanism: direct vs. learned-association vs. priming |
| template-biophilia-evolutionary-vs-cultural | Biophilia | Nature preference → evolutionary vs. cultural account | Rival-theory: evolutionary vs. cultural-learning |
| template-biophilia-valence-vs-nature-specificity | Biophilia | Window view → recovery; affective valence as rival IV | Rival-IV: nature specificity vs. affective valence |
| template-complexity-fractal-underdetermination | Complexity | Fractal D ~1.3–1.5 preference; evolutionary and fluency accounts co-extensive | Underdetermination: two accounts predict same range |
| template-material-wood-stress | Material | Wood surfaces → cortisol reduction | Mechanism audit: aesthetics vs. direct psychophysiology |
| template-material-wood-warrant-scope | Material | Wood stress claim; population qualifier (Japanese samples, lab settings) | Warrant audit: scope conditions and generalisability |
| template-biophilia-opioid-warrant-scope | Biophilia | Nature view → reduced analgesic requirement; Ulrich 1984 anchor | Warrant audit: has the qualifier been empirically widened? |
| template-thermal-underdetermination | Thermal | Thermal comfort → productivity; direct physiology vs. arousal accounts | Underdetermination: dissociation design needed |
| template-circadian-measurement-warrant | Circadian | Circadian lighting → patient outcomes; measurement-grade warrant criteria | Warrant audit: what metrological standard is applied? |
| template-sound-classroom-warrant-scope | Sound | Acoustic distraction → reading; ecological validity of lab qualifier | Warrant audit: does qualifier cover real classrooms? |
| template-color-attention-rival-theories | Colour | Hue → attention; valence-activation vs. ecological-valence rival accounts | Rival-theory: discriminating predictions by task type |
| template-color-evolutionary-vs-cultural-test | Colour | Colour-affect; evolutionary valence vs. cultural conditioning | Critical test: cross-cultural population design |
| template-thermal-cognitive-mechanism | Thermal | Heat → cognitive impairment; peripheral vs. central mechanism ordering | Mechanism trace: bottom-up vs. top-down impairment |

### 3.3 Mining Procedure

For each template, the following steps were applied:

1. Read the template's core theoretical claim to identify the question the template answers and the rival account it implicitly suppresses.
2. Phrase the anchor question in Hanif's philosophical voice — framed as a mechanism-decomposition or theory-comparison question, not a practitioner or empirical-summary question.
3. Generate two to three follow-up questions he would ask after receiving the anchor answer, varying across his five sub-flavours.
4. Tag each question on all five axes using only canonical values.
5. Set `source: mining` and `provenance: [template-id]`.
6. Apply the persona-fit gate: any question phraseable by a researcher without Hanif's philosophical frame (underdetermination, Toulmin structure, Duhem-Quine) was revised until it was unambiguously the Theory Explorer's.

---

## 4. Source 3 — Cross-Product Synthesis

### 4.1 Data Source

Tagging_Contractor IV hierarchy (~440 active tags across ~20 domains) and Outcome_Contractor DV hierarchy (seven top-level domains, ~80 level-2 outcome terms). For Hanif, IV × DV pairs were selected not for practitioner relevance but for theoretical richness — cells where two competing theoretical accounts make overlapping or conflicting predictions are more interesting to him than well-populated consensus cells.

### 4.2 Four Corners Selected

| Corner | IV (Tagging domain) | DV (Outcome domain) | Theoretical richness rationale |
|--------|---------------------|---------------------|-------------------------------|
| Low / Low | `spatial[wayfinding-clarity]` | `affect[anxiety]` | Causal arrow is contested: does disorientation produce anxiety or does anxiety impair wayfinding? Mechanism-trace entry |
| Low / High | `biophilia[nature-view]` | `behav[attendance]` + `cog[fatigue]` | Two DV outcomes may share a common cause (ART fatigue-recovery pathway) or be sequentially mediated — underdetermination probing |
| High / Low | `color[wall-lightness]` | `cog[visual-acuity]` + `affect[calm]` | Dual DV cell: optimising for one may conflict with the other; rival-account entry for ICU lighting |
| High / High | `complexity[fractal-dimension]` | `affect[perceived-restorativeness]` | Most theoretically live corner: evolutionary, fluency, and restorative-engagement accounts all predict the same D-range, producing genuine underdetermination |

### 4.3 Questions per Corner

Two questions per corner × four corners = 8 cross-product questions. The low count relative to the other corpora reflects Hanif's preference for deep mechanism-trace sessions over broad IV × DV scanning. Cross-product questions in this corpus are not discovery questions (as they would be for a student) but underdetermination-probing and critical-test questions — the IV × DV frame is a tool for surfacing theoretical conflicts, not for mapping the evidence landscape.

---

## 5. Known LLM-Panel Limitations

**Philosophical vocabulary bias.** Panel agents configured with Hanif's theoretical commitments (Quinean coherentism, Duhem-Quine, Machamer-Darden-Craver mechanism, Toulmin argument structure) generate questions that deploy these frameworks fluently. However, a real philosopher of cognitive science might also ask simpler, more direct questions that do not foreground their theoretical vocabulary — the corpus likely over-represents the sophisticated framing and under-represents the exploratory browsing that precedes it.

**Absent adversarial agent.** No panel agent was configured as a Hanif-sceptic (a reviewer who doubts the Atlas's epistemic claims). The underdetermination-prober sub-flavour approximates this role, but a genuinely adversarial agent would generate harder questions — including questions about whether the Atlas's own claim structure is coherent. H-Q-029 (on paradigm-level theoretical assumptions in convergence) is the closest approximation; a real adversarial run would produce more questions of this type.

**Panel-C meta-epistemic scope.** Panel-C questions (warrant structure, WELL standard, Duhem-Quine) are the most distinctive for Hanif and the hardest to generate without genuine philosophical expertise. These seven questions required the most revision to avoid collapsing into generic methodology questions that any researcher could ask. The Codebook Custodian should apply extra scrutiny to this sub-set at the peer-review round.

**Cross-product corner interpretation.** For Hanif, the four corners are interpreted as "sites of theoretical conflict" rather than "sites of evidence density." This re-interpretation is appropriate for the Theory Explorer persona but represents a departure from the Cross-Product Lead's standard interpretation, which uses corner selection to represent evidence coverage. This departure is flagged here so the team's Cross-Product Lead can assess whether it is permissible under the shared codebook.

**Inquiry dominance.** 66.0% of questions are tagged `inquiry`, reflecting Hanif's near-exclusive mode of settling open theoretical questions. The remaining cognitive_purpose values (deliberation, discovery, information-seeking) are underrepresented compared to the other corpora. This is structurally correct for the Theory Explorer chip but produces a corpus that would look pathological in any other persona's context.

---

## 6. Winnowing Record

No winnowing was required. All 50 questions satisfied the rubric minimums:

- All five sub-flavours have ≥5 questions: P7-mechanism-tracer (10), P7-rival-theorist (10), P7-underdetermination-prober (10), P7-warrant-auditor (10), P7-critical-test-seeker (10). All pass the ≥5 gate.
- Cognitive_purpose values: inquiry (33), deliberation (8), discovery (6), information-seeking (3). Persuasion is absent by design — a Theory Explorer in a long structural session does not load positions into debates; he resolves them. The Codebook Custodian should note this structural absence as a legitimate persona-driven gap, not a coverage failure.
- All four cross-product corners are populated.
- Total of 50 is within the 40–60 range.

The closest potential duplicate pair — H-Q-011 (ART vs. SRT side-by-side mechanism comparison) and H-Q-021 (whether the evidence base can adjudicate between ART and SRT) — ask structurally different questions: H-Q-011 asks what the theories predict differently; H-Q-021 asks whether the existing evidence is sufficient to decide between them. Both retained.

---

## 7. Final Coverage Summary

| Axis | Value | Count | % |
|------|-------|-------|---|
| **cognitive_purpose** | inquiry | 33 | 66.0% |
| | deliberation | 8 | 16.0% |
| | discovery | 6 | 12.0% |
| | information-seeking | 3 | 6.0% |
| | persuasion | 0 | 0.0% |
| **answer_shape** | Toulmin | 23 | 46.0% |
| | field-map | 12 | 24.0% |
| | procedure | 8 | 16.0% |
| | contrast-pair | 7 | 14.0% |
| | ranked-brief | 0 | 0.0% |
| **evidential_demand** | causal-with-mechanism | 24 | 48.0% |
| | mechanistic | 17 | 34.0% |
| | converging | 7 | 14.0% |
| | measurement-grade | 2 | 4.0% |
| | suggestive | 0 | 0.0% |
| **persona_fit** | P7-mechanism-tracer | 10 | 20.0% |
| | P7-rival-theorist | 10 | 20.0% |
| | P7-underdetermination-prober | 10 | 20.0% |
| | P7-warrant-auditor | 10 | 20.0% |
| | P7-critical-test-seeker | 10 | 20.0% |
| **source** | panel | 27 | 54.0% |
| | mining | 15 | 30.0% |
| | cross-product | 8 | 16.0% |

The corpus is inquiry-dominant (66.0%), which is structurally correct for a philosopher whose primary mode is settling open theoretical questions rather than filling known gaps. Causal-with-mechanism and mechanistic evidential demand together account for 82.0% of questions — the highest combined mechanistic demand of any of the three corpora — reflecting Hanif's governing question: "How do competing theoretical accounts explain these effects, and what experiment would distinguish between them?" The Toulmin answer shape (46.0%) and the field-map shape (24.0%) together cover 70.0% of questions; ranked-brief is entirely absent because Hanif is not choosing among options under brevity — he is adjudicating between theories under rigour. The complete absence of `suggestive` evidential demand and `persuasion` cognitive purpose, and of `ranked-brief` answer shape, defines this corpus as sharply as what it includes.
