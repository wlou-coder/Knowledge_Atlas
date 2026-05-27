# Task 1 Methods File — P1 · Maya Chen · Undergraduate Explorer
**Track 4 · Spring 2026 COGS 160**
**Author:** Charles Rivera · cfrivera004@gmail.com
**Corpus file:** `maya_chen_question_corpus.xlsx`
**Total questions:** 50 (M-Q-001 through M-Q-050)
**Completed:** 2026-04-30

---

## 1. Overview

The corpus was generated from three sources as specified in Task 1: LLM panels (Source 1), literature mining (Source 2), and cross-product synthesis (Source 3). Each source was designed to surface a distinct region of Maya Chen's question space. The final 50-question corpus was winnowed from 99 candidate questions by applying the sub-flavour coverage constraint (≥5 questions per sub-flavour) and the cross-product corners requirement.

| Source | Questions in corpus | % of total |
|--------|--------------------:|------------|
| Panel (Source 1) | 14 | 28% |
| Mining (Source 2) | 20 | 40% |
| Cross-product (Source 3) | 16 | 32% |

---

## 2. Source 1 — LLM Panel

### 2.1 Panel configuration

A single panel of five AI agent variants was configured, each instantiating one sub-flavour of the P1 · Maya Chen persona. The panel was designed to serve a dual purpose: (1) UX friction inventory of the target page (D5 friction audit), and (2) Task 1 corpus generation. Both outputs were produced in the same run.

| Panellist | Sub-flavour | Orientation | Time budget | Device |
|-----------|------------|-------------|-------------|--------|
| Maya-Sceptic | P1-sceptic | Drive-By Evaluator — is this site worth my time? | 3 min | iPhone on bus |
| Maya-Eager | P1-eager | Conscientious Learner — I want to do this right | 8–15 min | MacBook Air at Geisel |
| Maya-Pragmatist | P1-pragmatist | Efficiency-Seeker — shortest path to done | 5 min | MacBook Air at home |
| Maya-ArgBuilder | P1-argbuilder | Thesis Defender — I have a position, I need evidence | 10 min | MacBook Air, draft open |
| Maya-Explorer | P1-explorer | Curious Connector — I want to understand the landscape | 20 min | MacBook Air between classes |

### 2.2 Scenario card scaffold (Scaffold 1.2)

Each panellist answered four scenario-card questions in Maya's voice:

- **Q1** — What would she type or click first?
- **Q2** — What result would satisfy her (adequacy condition)?
- **Q3** — What would make the result feel insufficient (failure mode)?
- **Q4** — What is one further question she would ask after receiving an initial answer?

Each Q1–Q4 response was tagged on all five corpus axes and added to the corpus with `source: panel`.

### 2.3 Panel run record

| Field | Value |
|-------|-------|
| Run ID | Panel Run 01 |
| Date | 2026-04-28 |
| Target page | `ka_home_student_new.html` (Student Explorer home) |
| Prompt file | `panel_prompt_maya_chen.md` |
| Questions generated | 20 (4 per panellist × 5 panellists) |
| Friction points logged | 15 (3 per panellist minimum) |
| Falsifier result | Hypothesis 1 FALSIFIED — 0 of 5 panellists met goal within time budget |

The panel run produced 20 candidate corpus questions (M-Q-044 through M-Q-063 in the pre-winnow numbering). After winnowing, 14 panel questions were retained in the final corpus.

### 2.4 Panel questions retained after winnowing

The 14 retained panel questions were selected to maximise sub-flavour balance and cognitive_purpose diversity. Priority was given to questions that (a) captured friction-specific failure modes unique to Maya's context, (b) covered cognitive_purpose values underrepresented by Sources 2 and 3, and (c) were phrased in unambiguously Maya-specific voice.

| Retained ID (pre-winnow) | Sub-flavour | Cognitive purpose | Rationale for retention |
|--------------------------|-------------|-------------------|------------------------|
| P1-Q-001 | P1-sceptic | information-seeking | Primary navigation failure — no search box |
| P1-Q-002 | P1-sceptic | information-seeking | Upload path — central G-05 friction point |
| P1-Q-008 | P1-sceptic | information-seeking | Zero-results recovery — no path offered |
| P1-Q-010 | P1-sceptic | information-seeking | Login gate — authentication cold-start (G-05) |
| P1-Q-011 | P1-sceptic | information-seeking | No onboarding entry — G-11 trigger condition |
| P1-Q-006 | P1-pragmatist | information-seeking | DOI visibility — citeability check |
| P1-Q-017 | P1-eager | inquiry | "What is prospect-refuge theory?" — definitional anchor |
| P1-Q-021 | P1-eager | inquiry | Evidence threshold — why empirical support matters |
| P1-Q-024 | P1-eager | deliberation | Kaplan vs. Appleton citation choice |
| P1-Q-030 | P1-eager | persuasion | Strength of evidence for evolved spatial preference |
| P1-Q-032 | P1-eager | persuasion | Strongest counter-argument — required for credible paper |
| P1-Q-033 | P1-argbuilder | persuasion | Both-sides evidence check |
| P1-Q-036 | P1-eager | discovery | Adjacent concepts she didn't know to look for |
| P1-Q-037 | P1-eager | discovery | Open questions in environmental psychology |

---

## 3. Source 2 — Literature Mining

### 3.1 Data source

Mining was conducted against `Knowledge_Atlas/data/ka_payloads/paper_pnus.json` (760 papers with PNU artifacts) and `question_bank.json` (130 pre-curated research questions). These files served as the equivalent of the PNU template library described in the task specification.

The paper selection criterion was theoretical relevance to Maya's assignment topic: prospect-refuge theory, spatial form, and environmental wellbeing. Papers were identified by filtering on the `theories` field and `primary_topic` field across the 760-paper corpus.

### 3.2 Papers sampled

Five sources were mined. For each, the question the PNU/template *answers* was identified first, then 4 follow-up questions were generated in Maya's voice — questions a person would ask having just received that answer.

| Source ID | Title (abbreviated) | K-Atlas topic | Theories |
|-----------|--------------------|--------------|----|
| PDF-0865 | Evidence for prospect-refuge theory: a meta-analysis | Spatial Form → Aesthetic Preference | Prospect-Refuge Theory |
| PDF-0868 | [Stress recovery in prospect vs. non-prospect environments] | Spatial Form → Stress Response | Prospect-Refuge Theory, ART, SRT |
| PDF-0864 | Perceived openness and ability to see without being seen | Spatial Form → Aesthetic Preference | Prospect-Refuge Theory, Environmental Preference |
| PDF-0914 | Architectural design and the brain: ceiling height and enclosure (fMRI) | Spatial Form → Neural Activity | Neuroarchitecture, Prospect-Refuge, fMRI |
| SQ-093 | Prospect-conferring elements and approach motivation | question_bank.json | Prospect-Refuge, approach-avoidance |

### 3.3 Mining procedure

For each sampled paper:

1. Read the `pnu.short_summary` and `science_summary.core_finding` fields from `paper_pnus.json`.
2. Identified the primary question the paper's finding answers (the "anchor question").
3. Generated 4 follow-up questions in Maya's voice — the questions a second-year UCSD student would ask after receiving the anchor answer.
4. Tagged each question on all five corpus axes.
5. Set `source: mining` and `provenance: <paper_id> / <short title> / paper_pnus.json`.

This produced 20 mining questions (4 per source × 5 sources).

---

## 4. Source 3 — Cross-Product Synthesis

### 4.1 Data source

Cross-product questions were generated from `Knowledge_Atlas/data/ka_payloads/topic_hierarchy.json`, which contains 102 realised IV × DV cells drawn from 9 independent-variable domains and 18 dependent-variable domains across 760 papers.

### 4.2 Four corners selected

Corners were defined by paper count within each IV × DV cell — a proxy for how thoroughly the research community has explored that combination.

| Corner | IV domain | DV domain | Papers in cell | Rationale |
|--------|-----------|-----------|---------------|-----------|
| High/High | Acoustic Conditions | Cognitive Performance | 22 | Dense, well-replicated literature; questions can demand converging evidence |
| Low/Low | Spatial Form | Memory | 1 | Virtually unstudied; questions surface gaps and design-study needs |
| Low/High | Natural and Biophilic Conditions | Restoration / Recovery | 1 | Well-theorised (ART, SRT) but sparse empirical grounding indoors |
| High/Low | Thermal and Air Conditions | Social / Behavioral | 1 | High IV literature overall, but the social outcome DV is uncharted |

### 4.3 Questions per corner

Four questions were generated per corner (16 total), following the cross-product question form: *"How does [IV] affect [DV], possibly moderated by [Z]?"* Questions at the high/high corner carry higher evidential demand (converging, measurement-grade); questions at low/low and high/low corners carry suggestive demand, reflecting the sparse literature.

| Corner | Questions generated | Evidential demand distribution |
|--------|--------------------|-|
| High/High (Acoustic × Cog. Perf.) | M-Q-039 to M-Q-042 | converging (3), measurement-grade (1) |
| Low/Low (Spatial Form × Memory) | M-Q-043 to M-Q-046 | suggestive (4) |
| Low/High (Biophilic × Restoration) | M-Q-047 to M-Q-050 | converging (2), mechanistic (1), suggestive (1) |
| High/Low (Thermal × Social) | M-Q-035 to M-Q-038 | suggestive (3), converging (1) |

*(IDs reflect final renumbered corpus; corners appear in non-sequential order due to winnowing sort.)*

---

## 5. Known LLM-Panel Limitations

The following limitations are acknowledged for honest documentation as required by the Task 1 rubric.

**L-01 — Single page, single run.** Panel Run 01 evaluated only `ka_home_student_new.html`. The student home page is the most friction-heavy page for Maya's use case, but her question space also spans `ka_article_search.html` and the upload interface. Questions generated from a single-page run underweight mid-session and recovery questions. Mitigation: Sources 2 and 3 were used to supply the remaining question space without page dependency.

**L-02 — LLM panel cannot observe live UI behaviour.** The panellists were given the static HTML source of the target page. They cannot observe JavaScript rendering, animation, or network-dependent content (topic pages that require a live server). Known failures such as UC-02 (topic pages blank without server) and G-11 (DYK card routing bug) were injected into the prompt as explicit known gaps rather than discovered by the panel. Questions about these gaps may understate real-world friction for a user who does not receive this briefing.

**L-03 — Sycophancy and anti-flattery enforcement.** LLM agents have a known tendency to soften negative evaluations. The panel prompt included an explicit anti-flattery clause (D7) requiring that bail decisions not be qualified and that negative findings not be softened. Despite this, the language in panellist outputs should be treated as conservative; real-world friction is likely higher than the panel records.

**L-04 — Sub-flavour coverage skew.** Without an explicit P1-argbuilder and P1-explorer in the panel configuration, early drafts of the corpus had zero deliberation, persuasion, and discovery questions from Source 1. The solution was to add two additional panellists. This means persuasion and discovery coverage in Source 1 comes entirely from two panellists rather than being distributed across the full panel — a structural concentration risk.

**L-05 — Question voice drift.** Mining questions (Source 2) are phrased in Maya's voice but are generated from paper summaries written for a research audience. Some mining questions may carry implicit method-awareness that a real second-year undergraduate would not possess. These are flagged with `theoretical_commitment: method-aware` in the corpus; instructors should treat these as edge-of-persona rather than core-persona questions.

**L-06 — Cross-product questions are structurally generated, not observed.** Source 3 questions follow a formula (IV × DV × moderator) and do not emerge from observing Maya navigate or ask questions. They cover the logical space of the topic hierarchy but may not reflect questions Maya would spontaneously generate in a real session. They are most useful as coverage ballast for cognitive_purpose values (discovery, deliberation) underrepresented in Sources 1 and 2.

---

## 6. Winnowing Record

The raw candidate pool of 99 questions was reduced to 50 by the following procedure:

1. **Keep all cross-product questions (16).** Required for corners coverage.
2. **Keep all mining questions (20).** Highest specificity to Maya's assignment topic (prospect-refuge); not reproducible from the panel alone.
3. **Select 14 panel questions** by applying two gates in order:
   - *Sub-flavour coverage gate:* each sub-flavour must have ≥5 questions in the final corpus after all sources are combined. P1-sceptic and P1-pragmatist had zero representation from Sources 2 and 3, so panel questions for these sub-flavours were kept first.
   - *Cognitive_purpose gap gate:* persuasion and discovery were underrepresented after Sources 2 and 3; panel questions filling those gaps were kept next.
4. **Reject 49 panel questions** that were redundant with retained questions, off-persona (too general), or duplicated a cognitive_purpose already well-covered.

The winnowing left the corpus at exactly 50 questions with all five sub-flavours and all five cognitive_purpose values represented.

---

## 7. Final Coverage Summary

| Axis | Value | n | % |
|------|-------|---|---|
| **cognitive_purpose** | information-seeking | 14 | 28% |
| | inquiry | 19 | 38% |
| | deliberation | 8 | 16% |
| | persuasion | 4 | 8% |
| | discovery | 5 | 10% |
| **persona_fit** | P1-sceptic | 6 | 12% |
| | P1-eager | 15 | 30% |
| | P1-pragmatist | 5 | 10% |
| | P1-argbuilder | 13 | 26% |
| | P1-explorer | 11 | 22% |
| **evidential_demand** | suggestive | 19 | 38% |
| | converging | 21 | 42% |
| | mechanistic | 7 | 14% |
| | measurement-grade | 3 | 6% |
| **source** | panel | 14 | 28% |
| | mining | 20 | 40% |
| | cross-product | 16 | 32% |
