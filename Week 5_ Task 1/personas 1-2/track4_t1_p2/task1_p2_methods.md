# Task 1 Methods File — P2 · Dr. Nia Okafor · Environmental / Cognitive Neuroscientist
## Track 4, Task 1 · COGS 160 Spring 2026 · Charles Rivera
## Date: 2026-04-30

---

## 1. Overview

| Source | Questions in Corpus | % |
|--------|--------------------|----|
| Source 1 — LLM Panel | 20 | 35.7% |
| Source 2 — Literature Mining | 20 | 35.7% |
| Source 3 — Cross-Product Synthesis | 16 | 28.6% |
| **Total** | **56** | **100%** |

All 56 questions passed the canonical-value validator (no non-canonical axis tags). The corpus is within the 40–60 target range. No winnowing was necessary; the 56 raw questions satisfied all minimum requirements without reduction.

---

## 2. Source 1 — LLM Panel

### 2.1 Panel Configuration

| Panellist | Sub-Flavour | Orientation | Time Budget | Device |
|-----------|-------------|-------------|-------------|--------|
| Nia-Surveyor | P2-surveyor | Evidence provenance auditor — is the cortisol claim grounded in primary studies or a single review? | 8 min | 27″ iMac |
| Nia-Prober | P2-prober | Hypothesis tester — does the HPA–hippocampus–wayfinding chain hold across the cumulative evidence? | 20 min | 27″ iMac |
| Nia-Arbiter | P2-arbiter | Theory selector — does PP or ART better account for built-environment stress outcomes? | 12 min | 27″ iMac |
| Nia-Advocate | P2-advocate | Grant architect — build the strongest evidence case for chronic cortisol + pre-empt the self-selection defeater | 15 min | 27″ iMac |
| Nia-Frontiersman | P2-frontiersman | Frontier scout — find an IV × DV gap in the acoustic × hippocampal intersection she has not already mapped | 30 min | 27″ iMac |

### 2.2 Scenario Card Scaffold (Q1–Q4)

Each panellist received four scenario card questions derived from their sub-flavour context:

- **Q1** — What would the panellist type or click first? (entry action, maps to the most direct available path on the target page)
- **Q2** — What result would satisfy them? (adequacy threshold — what they would need to see to trust the answer)
- **Q3** — What would make the result feel insufficient? (failure mode — what triggers bail or loss of scientific confidence)
- **Q4** — What further question would they ask after receiving an initial answer? (follow-on question that reveals their underlying research goal)

### 2.3 Panel Run Record

| Field | Value |
|-------|-------|
| Run ID | Panel Run 01 |
| Date | 2026-04-30 |
| Target page | `ka_home_researcher.html` |
| Prompt file | `panel_prompt_nia_okafor.md` |
| Questions generated | 20 (4 per panellist × 5 panellists) |
| Falsifier Hypothesis 1 result | **Falsified** — 0 of 5 panellists reached their goal within time budget; all five encountered non-functional links or domain-agnostic card content |
| Falsifier Hypothesis 2 result | **Determined** — `page_serves_persona: partially`; vocabulary matches P2's expert frame but all six information cards serve static nature-domain content regardless of domain filter |

### 2.4 Panel Questions Retained After Winnowing

All 20 panel questions were retained. Rationale: all five sub-flavours represented (4 questions each), no semantic duplicates identified, and all five cognitive_purpose values covered across the 20 questions without any gap requiring supplementation from mining or cross-product sources.

---

## 3. Source 2 — Literature Mining

### 3.1 Data Source

`Knowledge_Atlas/data/ka_payloads/paper_pnus.json` — 760 papers with PNU summaries (`short_summary`, `science_summary.core_finding`, `theories`, `primary_topic`).

### 3.2 Papers Sampled

| paper_id | Title (truncated) | Topic | Theories |
|----------|-------------------|-------|----------|
| PDF-0914 | Architectural design and the brain: Effects of ceiling height and perceived enclosure | Spatial Form → Neural Activity | Neuroarchitecture, Ceiling Height, fMRI |
| PDF-0310 | A critical review on the impact of built environment on users' measured brain activity | Thermal & Air Quality → Neural Activity | Neuroarchitecture |
| PDF-0878 | Architectural Allostatic Overloading: Exploring a Connection between Architectural Form and Allostatic Overloading | Spatial Form → Stress Response | Neuroarchitecture, Allostatic Load, Neuroimmunology |
| PDF-0458 | A psychoacoustical approach to resolving office noise distraction | Social-Spatial → Cognitive Performance | (none listed) |
| PDF-0288 | Cells in human brain hippocampus responsible for location | Environmental Control → Social/Behavioral | Environmental psychology, Sense of belonging |

Selection criterion: papers identified by keyword search on `primary_topic`, `title`, and `theories` using keywords `['neuroarchitecture', 'cortisol', 'hippocam', 'fmri', 'open plan', 'open-plan', 'allostatic', 'place cell', 'entorhinal']`. 35 matches found; 5 selected as most directly engaging Dr. Okafor's domain (hippocampal/HPA mechanisms, built-environment stress, neural recording in or near real environments).

### 3.3 Mining Procedure

For each paper, the following steps were applied:

1. Read `pnu.short_summary` and `science_summary.core_finding` to identify the anchor question the paper's finding answers.
2. Phrase the anchor question explicitly in Dr. Okafor's expert voice (neuroarchitecture/HPA orientation).
3. Generate four follow-up questions she would ask after receiving the anchor answer, varying across sub-flavours and cognitive_purpose values.
4. Tag each question on all five axes using only canonical values.
5. Set `source: mining` and `provenance: [paper_id] / [short title] / paper_pnus.json`.
6. Record the anchor question in the `notes` field of the first question from that paper.

---

## 4. Source 3 — Cross-Product Synthesis

### 4.1 Data Source

`Knowledge_Atlas/data/ka_payloads/topic_hierarchy.json` — 102 IV × DV cells with paper counts.

### 4.2 Four Corners Selected

| Corner | IV Domain | DV Domain | Papers | Rationale |
|--------|-----------|-----------|--------|-----------|
| High/High | Acoustic Environment | Cognitive Performance | 22 | Most populated acoustic cell; canonical open-plan noise → cognition relationship |
| Low/Low | Spatial Form | Memory | 1 | Single paper; directly relevant to hippocampal/place-cell research; genuine frontier |
| High IV / Sparse DV | Acoustic Environment | Physiological Response | 12 | Acoustic IV well-studied (22 in cognition); cortisol/HRV DV underrepresented relative to cognitive outcomes |
| Sparse IV / Studied DV | Nature & Biophilia | Restoration / Recovery | 1 | ART is K-Atlas's featured restoration theory; single paper in cell despite theoretical prominence — likely a tagging-coverage problem |

### 4.3 Questions per Corner

4 questions per corner × 4 corners = 16 cross-product questions. High/High questions emphasise `converging` or `measurement-grade` evidential demand. Low/Low questions emphasise `suggestive` demand and `discovery` cognitive purpose. High IV / Sparse DV questions probe the asymmetry between acoustic cognitive research (22 papers) and acoustic physiological research (12 papers). Sparse IV / Studied DV questions interrogate whether the K-Atlas classification reflects a real literature gap or a tagging artefact in the ART/restoration domain.

---

## 5. Known LLM-Panel Limitations

**Single-page scope.** The panel reacted only to the `ka_home_researcher.html` snapshot. Features promised by nav links (Hypothesis Test, Compare Theories, View VOI map, Evidence Browser) were flagged as MISSING; their potential to satisfy P2 could not be evaluated.

**Inability to observe live UI interaction.** All click_trace outcomes are inferred from the static HTML source; JavaScript-rendered state changes (e.g., domain filter updating the six information cards) could not be verified.

**Sycophancy risk.** LLM panels systematically generate questions that confirm the panellist's stated expertise. P2-prober and P2-arbiter questions may be biased toward sophisticated mechanism-chain queries and underrepresent the procedural or navigational questions a real researcher might also ask (e.g., "how do I export a BibTeX?").

**Sub-flavour skew from small panel size.** The 4 × 5 structure assigns exactly four questions per sub-flavour, artificially flattening what would in reality be a highly uneven distribution. A real P2-surveyor in a 25-minute journal-review session would generate far more questions than a P2-frontiersman in an exploratory afternoon.

**Voice drift in mining questions.** Mining questions were authored by the prompt author in Dr. Okafor's putative voice, not generated by the panel. Author bias is therefore present; the questions reflect the author's model of expert neuroarchitecture inquiry rather than real user utterances.

**Structural nature of cross-product questions.** Cross-product questions are generated from IV × DV cell coordinates and paper counts, not from reading the papers in those cells. Questions about what the 12-paper Acoustic × Physiological Response cell contains (e.g., the distribution of physiological outcome measures) cannot be verified from the topic_hierarchy.json alone; they require reading the actual papers.

---

## 6. Winnowing Record

No winnowing was required. All 56 questions satisfied the rubric minimums:

- All five sub-flavours have ≥5 questions: P2-surveyor (11), P2-prober (15), P2-arbiter (11), P2-advocate (7), P2-frontiersman (12). All pass the ≥5 gate.
- All five cognitive_purpose values are represented: information-seeking (7), inquiry (18), deliberation (11), persuasion (7), discovery (13).
- All four cross-product corners are populated with exactly 4 questions each.
- Total of 56 is within the 40–60 range.

The closest potential duplicate pair — N-Q-013 (chronic cortisol primary studies, P2-advocate) and N-Q-030 (validated biomarkers for allostatic overload, P2-surveyor) — ask about different constructs and map to different sub-flavours; both retained.

---

## 7. Final Coverage Summary

| Axis | Value | Count | % |
|------|-------|-------|---|
| **cognitive_purpose** | information-seeking | 7 | 12.5% |
| | inquiry | 18 | 32.1% |
| | deliberation | 11 | 19.6% |
| | persuasion | 7 | 12.5% |
| | discovery | 13 | 23.2% |
| **answer_shape** | Toulmin | 16 | 28.6% |
| | field-map | 9 | 16.1% |
| | procedure | 7 | 12.5% |
| | contrast-pair | 13 | 23.2% |
| | ranked-brief | 11 | 19.6% |
| **evidential_demand** | suggestive | 11 | 19.6% |
| | converging | 13 | 23.2% |
| | mechanistic | 12 | 21.4% |
| | causal-with-mechanism | 12 | 21.4% |
| | measurement-grade | 8 | 14.3% |
| **persona_fit** | P2-surveyor | 11 | 19.6% |
| | P2-prober | 15 | 26.8% |
| | P2-arbiter | 11 | 19.6% |
| | P2-advocate | 7 | 12.5% |
| | P2-frontiersman | 12 | 21.4% |
| **theoretical_commitment** | none | 8 | 14.3% |
| | topic-aware | 16 | 28.6% |
| | method-aware | 20 | 35.7% |
| | adversarial | 12 | 21.4% |
| **source** | panel | 20 | 35.7% |
| | mining | 20 | 35.7% |
| | cross-product | 16 | 28.6% |

The corpus is inquiry-heavy (32.1%), reflecting Dr. Okafor's primary cognitive mode as a hypothesis-testing researcher. Method-aware theoretical commitment is the dominant tag (35.7%), consistent with 15 years of fMRI lab experience and acute sensitivity to design confounds. Causal-with-mechanism and mechanistic evidential demands together account for 42.8% of questions, consistent with her governing question: "What does the cumulative evidence say about my hypothesis at the mechanism level?"
