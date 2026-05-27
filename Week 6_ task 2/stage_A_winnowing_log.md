# Stage A Winnowing Log — Full Corpus
**Track 4 · Task 2 · COGS 160 Spring 2026**
*Corpus: COGS160_Task1_Question_Corpus.xlsx · 292 rows entering · 247 surviving*

---

## Summary counts

| Pass | Starting | Dropped / Backlogged | Surviving | Attrition |
|------|----------|----------------------|-----------|-----------|
| 0 — Pre-winnow | 292 | — | 292 | — |
| 1 — Deduplicate | 292 | 25 dropped | 267 | 8.6% |
| 2 — Adequacy gate | 267 | 0 dropped | 267 | 0% |
| 3 — Persona-fit gate | 267 | 20 to backlog | 247 | 7.5% |
| 4 — Coverage balance | 247 | 0 dropped; gaps noted | 247 | — |
| **Final working corpus** | | | **247** | **15.4% total** |

Note on Pass 1 attrition: the ~30% expected rate assumes many near-duplicates. This corpus has lower exact-tag duplication because the `theoretical_commitment` field is highly specific per contributor — many questions that seem similar carry different theoretical framings and would in fact produce different journeys. The actual deduplication rate (8.6%) reflects this. The "same journey" test catches the 25 cases below where both tags *and* answering path are genuinely identical.

---

## Pass 1 — Deduplicate (292 → 267, −25)

**Rule:** Two questions are duplicates if they share all five tags (cognitive_purpose, answer_shape, evidential_demand, persona_fit, theoretical_commitment) AND would be answered by the same journey. In all cases below, the merged entry credits both source IDs.

---

### Group D-1 · P1-argbuilder · deliberation / contrast-pair / converging
**Keep:** M-Q-017 · **Drop:** M-Q-033

- **M-Q-017:** "Where does the meta-analysis say the evidence is weakest — what is the strongest counter-argument I'd need to address?"
- **M-Q-033:** "Is the evidence for prospect-refuge theory in buildings the same as in natural landscapes, or weaker?"

**Reasoning:** Both are argbuilder questions asking for the weakest point in the evidence base to prepare a counter-argument. M-Q-033 is a specific instantiation of M-Q-017 within one theory. A contrast-pair journey answering M-Q-017 would necessarily answer M-Q-033. Tags are identical. Merge: keep M-Q-017, credit M-Q-033 in provenance.

---

### Group D-2 · P1-argbuilder · inquiry / Toulmin / converging
**Keep:** M-Q-019 · **Drop:** M-Q-031, M-Q-043

- **M-Q-019:** "Is there actual evidence that being in an open natural setting with clear sightlines reduces stress — or is that just intuition?"
- **M-Q-031:** "Do spaces with elevated platforms or big panoramic windows actually make people stay longer — and is that backed by data?"
- **M-Q-043:** "Does being near plants or natural materials inside a building actually restore your focus, or is that anecdote?"

**Reasoning:** All three are argbuilder Toulmin questions asking for evidential backing for a biophilic/restorative effect in architectural contexts. The warrant structure is identical: claim (environment type → outcome), data (primary studies), backing (converging evidence base). The specific environment varies but the journey is the same: retrieve primary evidence, assess quality, surface the claim + warrant. Merge all three into M-Q-019.

---

### Group D-3 · P1-argbuilder · inquiry / contrast-pair / converging
**Keep:** M-Q-023 · **Drop:** M-Q-025

- **M-Q-023:** "Is prospect or refuge the more important element — does the evidence show one matters more than the other?"
- **M-Q-025:** "Does the evidence say more windows equals better, or is it really about the VIEW — the depth, the content, not the aperture?"

**Reasoning:** Both frame an argbuilder contrast-pair question testing which of two architectural variables drives the outcome. M-Q-025 is a restatement of M-Q-023 at a finer grain (windows vs. view = a subset of prospect-refuge). A contrast-pair journey for M-Q-023 subsumes M-Q-025. Merge: keep M-Q-023.

---

### Group D-4 · P1-eager · deliberation / contrast-pair / converging
**Keep:** M-Q-009 · **Drop:** M-Q-036

- **M-Q-009:** "Should I cite the Kaplan paper or the Appleton paper for the definition of prospect-refuge?"
- **M-Q-036:** "Is studying with background music better or worse than silence for cognitive performance — what does the evidence say?"

**Reasoning:** These two questions are topically unrelated but share identical tags. Both are P1-eager deliberation/contrast-pair questions asking which of two options is better supported. The journey shape is the same (present two options, weight evidence for each, recommend). The tag collision is real; the topics are distinct but the journey template is identical. Per the deduplication rule — same tags AND same journey — we drop one. Keep M-Q-009 (prospect-refuge is more central to P1's domain); backlog M-Q-036 for a targeted generation pass if the music/cognition topic needs coverage.

---

### Group D-5 · P1-eager · inquiry / Toulmin / mechanistic
**Keep:** M-Q-020 · **Drop:** M-Q-027, M-Q-044

- **M-Q-020:** "Why does a forest clearing feel safer and calmer than a dense thicket — is there neuroscience behind it?"
- **M-Q-027:** "Does ceiling height actually change how I feel about a space in a measurable way, or does it just seem that way?"
- **M-Q-044:** "What actually makes an indoor environment feel restorative — is it the nature elements themselves, the light, the quiet?"

**Reasoning:** All three are P1-eager mechanistic Toulmin inquiries — the student wants to understand *why* an effect happens, not just *whether* it does. The journey in all three cases: find the mechanistic warrant, name the causal chain, surface backing studies. Topically different (prospect-refuge, ceiling height, restoration) but the journey is the same template. Keep M-Q-020 as the canonical form; note M-Q-027 and M-Q-044 as topic variants for targeted generation.

---

### Group D-6 · P1-explorer · inquiry / field-map / suggestive
**Keep:** M-Q-018 · **Drop:** M-Q-026, M-Q-039

- **M-Q-018:** "Has anyone actually tested prospect-refuge in indoor spaces like classrooms or libraries?"
- **M-Q-026:** "Are there spaces that have strong refuge but almost no prospect — like a cave or deep alcove?"
- **M-Q-039:** "Does the shape or layout of a room affect what you remember from being in it?"

**Reasoning:** All three are P1-explorer field-map questions: the student is mapping the conceptual territory, looking for what exists rather than testing a specific claim. The journey is the same: browse the space, surface what's known, reveal adjacent topics. Keep M-Q-018 (strongest prospect-refuge grounding); M-Q-039 introduces a different DV (memory) that could warrant its own targeted question in coverage balance.

---

### Group D-7 · P1-sceptic · information-seeking / procedure / suggestive
**Keep:** M-Q-001 · **Drop:** M-Q-002, M-Q-004, M-Q-005, M-Q-006

- **M-Q-001:** "Where do I go to search for papers?"
- **M-Q-002:** "How do I upload papers for my class assignment?"
- **M-Q-004:** "I searched for prospect-refuge and got nothing — what now?"
- **M-Q-005:** "I'm on a page that asks me to log in — do I need an account to see anything?"
- **M-Q-006:** "Nothing on this page makes sense — is there a 'start here' for students?"

**Reasoning:** All five are P1-sceptic procedural/navigational questions at the system entry point. They all reduce to the same journey: site onboarding for a student with low trust. Dropping four is arguably aggressive, since the *content* of M-Q-002 (upload) differs from M-Q-001 (search). However, the adequacy condition for all five is the same type (UI reachability within N clicks), and a single onboarding journey handles them in sequence. Merge to M-Q-001 and note the sub-steps in the shape sketch. A targeted generation pass could split "search access" from "upload access" into two discrete journeys if the site's architecture warrants it.

---

### Group D-8 · P2-advocate · persuasion / ranked-brief / causal-with-mechanism
**Keep:** N-Q-013 · **Drop:** N-Q-051

- **N-Q-013:** "What primary studies — with sample sizes and longitudinal designs — show chronic, sustained noise causes cortisol elevation?"
- **N-Q-051:** "For the grant I am writing on chronic cortisol elevation in open-plan offices, how many longitudinal studies exist, and what effect sizes are reported?"

**Reasoning:** Both are P2-advocate persuasion questions seeking a ranked brief of high-quality studies to build a grant argument. N-Q-051 is a specific instantiation of N-Q-013 with the office context named. The journey is the same: retrieve converging mechanistic studies, rank by design quality, surface effect sizes. Merge: keep N-Q-013.

---

### Group D-9 · P2-arbiter · deliberation / contrast-pair / mechanistic
**Keep:** N-Q-011 · **Drop:** N-Q-030

- **N-Q-011:** "How does the Salience Network Modulation framework as it appears in K-Atlas differ from the allostatic overload mechanism?"
- **N-Q-030:** "How does the allostatic overload mechanism proposed in the architectural neuroimmunology paper differ from the standard ART account?"

**Reasoning:** Both are P2-arbiter contrast-pair questions asking how two mechanistic accounts differ. The journey is the same: name the mechanisms, identify the differentiating prediction, assess which the evidence supports. Merge: keep N-Q-011 (more general framing); note N-Q-030's specific ART comparison in the provenance.

---

### Group D-10 · P2-frontiersman · discovery / field-map / suggestive
**Keep:** N-Q-023 · **Drop:** N-Q-035, N-Q-046, N-Q-053

- **N-Q-023:** "Does the degree of enclosure-induced aMCC activation documented in architectural fMRI studies predict individual differences in open-plan tolerance?"
- **N-Q-035:** "Has any study measured whether high-neuroticism workers in open-plan offices show elevated cortisol?"
- **N-Q-046:** "Given that architectural spatial form drives hippocampal place-cell encoding, why does the literature not yet connect this to layout-preference studies?"
- **N-Q-053:** "The Nature & Biophilia × Restoration/Recovery cell holds only one paper in K-Atlas — does that signal a real gap or just an indexing gap?"

**Reasoning:** All four are P2-frontiersman discovery field-map questions identifying gaps and unexplored territory. The journey in each case: map what's known, locate the gap, signal it as unexplored. Tags are identical. Keep N-Q-023 (most specific frontier question); note the other three as gap variants. N-Q-053 is particularly worth a targeted generation pass since it names a specific IV × DV cell gap.

---

### Group D-11 · P2-prober · inquiry / Toulmin / causal-with-mechanism
**Keep:** N-Q-005 · **Drop:** N-Q-044

- **N-Q-005:** "What does the K-Atlas mechanism database show for the chain: broadband noise → sustained HPA axis activation?"
- **N-Q-044:** "Is there a dose-response function for noise intensity (dB SPL) and executive function impairment?"

**Reasoning:** Both are P2-prober Toulmin inquiries asking for a causal-with-mechanism answer about noise. N-Q-044's dose-response framing is a specific variant of the mechanistic chain question in N-Q-005. The journey — find the warrant, trace the mechanism, surface the claim — is the same. Merge: keep N-Q-005.

---

### Group D-12 · P2-prober · inquiry / Toulmin / mechanistic
**Keep:** N-Q-022 · **Drop:** N-Q-033, N-Q-037, N-Q-048

- **N-Q-022:** "How does anterior midcingulate cortex activation in enclosed rooms connect to the threat-response literature?"
- **N-Q-033:** "What is the neural mechanism connecting trait neuroticism to elevated noise sensitivity?"
- **N-Q-037:** "Beyond the theoretical argument in the Pruitt-Igoe analysis, is there direct neuroimaging evidence?"
- **N-Q-048:** "Does the O'Keefe-Dostrovsky place-cell literature predict that open-plan spatial layouts disrupt navigation recall?"

**Reasoning:** All four are P2-prober mechanistic Toulmin questions chasing a neural mechanism. The journey is identical: retrieve the mechanism chain from the Atlas, assess the backing evidence, surface the claim. Keep N-Q-022 as the most general; note the others as topic variants for the shape sketch.

---

### Group D-13 · P2-prober · inquiry / contrast-pair / mechanistic
**Keep:** N-Q-025 · **Drop:** N-Q-052

- **N-Q-025:** "The systematic review shows EEG dominates the neuroarchitecture method mix — what does EEG uniquely capture that fMRI and EDA don't?"
- **N-Q-052:** "Do acoustic frequency spectrum characteristics (low-frequency hum vs. broadband noise vs. speech) have distinguishable EEG signatures?"

**Reasoning:** Both are P2-prober contrast-pair questions asking which method or signal distinguishes phenomena. N-Q-052 is a specific case of N-Q-025's broader method-comparison question. Merge: keep N-Q-025.

---

### Group D-14a · P2-surveyor · information-seeking / ranked-brief / measurement-grade (first pair)
**Keep:** N-Q-024 · **Drop:** N-Q-028

- **N-Q-024:** "What ceiling height threshold — in absolute meters — does K-Atlas identify as the breakpoint for construal-level effects?"
- **N-Q-028:** "Across the 52 original studies in the built-environment neural review, what is the modal sample size and what does that imply for power?"

**Reasoning:** Both are P2-surveyor measurement-grade ranked-brief queries asking for a specific quantitative threshold or summary statistic from the corpus. The journey — retrieve the numerical answer, give context, surface precision limits — is the same. Merge: keep N-Q-024.

---

### Group D-14b · P2-surveyor · information-seeking / ranked-brief / measurement-grade (second pair)
**Keep:** N-Q-001 · **Drop:** N-Q-029

- **N-Q-001:** "How many primary studies — not reviews — does K-Atlas hold on noise-induced cortisol elevation?"
- **N-Q-029:** "The architectural allostatic overloading paper is a conceptual review — what empirical studies does the Atlas actually index for the claim?"

**Reasoning:** Both ask the surveyor to count and distinguish primary from review evidence on a specific topic. Same journey: retrieve and count by study type, surface the gap between reviews and primary evidence. Merge: keep N-Q-001.

---

## Pass 2 — Adequacy gate (267 → 267, −0)

**Rule:** Drop any row whose adequacy condition cannot be articulated in one sentence after five minutes of team discussion.

**Result: zero drops.**

All 267 surviving rows have adequacy conditions that are articulable in one sentence. The majority use a "Fails if X, where X is specific" format — this is negative phrasing of a positive adequacy criterion, not a vague condition. A condition like "Fails if it does not report both acoustic attenuation AND fall-outcome data together, not separately" is fully articulable and specific; it just states the criterion as a falsifier rather than a satisfier.

**One note for the team:** 161 of the 267 rows use exclusively "Fails if..." framing with no positive adequacy statement. This is technically adequate but stylistically inconsistent with the researcher corpus exemplar, which states both what would satisfy and what would fail. Before Stage B, the team should consider harmonising the phrasing — not because anything fails the gate, but because the positive form is more useful when writing shape sketches.

---

## Pass 3 — Persona-fit gate (267 → 247, −20 to backlog)

**Rule:** Move any item the team would re-classify to a different persona to the next-pass backlog. Do not discard.

---

### Backlog destination: P7 (theorist, rival-theory focus)

**E-Q-006** → P7-backlog
- Current: P3-literature-mapper
- Question: "Where does the corpus currently have genuine underdetermination — cases where evidence is consistent with two competing accounts?"
- Reasoning: Underdetermination-mapping is the defining concern of P7-underdetermination-prober, not P3-literature-mapper. P3-Elena's literature-mapper sub-flavour is about identifying what has been studied and where the gaps are, not about adjudicating between competing theoretical accounts. This question belongs in H-prefix territory. Move to P7 backlog; consider as a targeted addition for the P7 persona if the underdetermination-prober sub-flavour has room.

---

### Backlog destination: P5 (instructor, student monitoring)

The following 17 D-Q questions (P8-student-pipeline-monitor and two P8-site-architect rows) are fundamentally about monitoring student progress, assessing student work quality, and deciding how to intervene — which is Marisol's (P5) domain, not the PI dashboard operator's (P8). P8 is concerned with the *epistemic health of the Atlas itself*; P5 monitors the *pedagogical pipeline of students contributing to it*. The distinction is real: P8 asks "is the knowledge base healthy?" while P5 asks "are the students doing their work correctly?"

| ID | Question (abbreviated) | Current sub-flavour |
|----|------------------------|---------------------|
| D-Q-004 | Which students across all four tracks have not submitted any work in the past 72 hours? | P8-triage-operator |
| D-Q-014 | Which PNU templates have the fewest backing studies — are those the same ones students are being assigned? | P8-epistemic-graph-reader |
| D-Q-021 | Which Track 4 student is furthest behind their expected milestone? | P8-student-pipeline-monitor |
| D-Q-022 | Are there student contributions submitted but not reviewed in more than 48 hours? | P8-student-pipeline-monitor |
| D-Q-023 | Is any student currently working on a template already processed? | P8-student-pipeline-monitor |
| D-Q-024 | Which Track 1 students have produced tagging outputs that consistently diverge from HITL? | P8-student-pipeline-monitor |
| D-Q-025 | Has any student submitted a Task 1 corpus where adequacy conditions are formulaically vague? | P8-student-pipeline-monitor |
| D-Q-026 | Are all four Track 4 students working on genuinely distinct personas? | P8-student-pipeline-monitor |
| D-Q-027 | Which students have not yet engaged with the researcher corpus as a calibration standard? | P8-student-pipeline-monitor |
| D-Q-028 | For Track 2 students, are any question-to-answer-shape fittings internally inconsistent? | P8-student-pipeline-monitor |
| D-Q-029 | Has any student's question corpus grown beyond 60 questions without a winnowing log? | P8-student-pipeline-monitor |
| D-Q-030 | Which students are on track to deliver Task 3 prototypes with a working Chinn-Brewer panel? | P8-student-pipeline-monitor |
| D-Q-032 | Has the Tagging_Contractor's tag-assignment accuracy drifted from the week-3 baseline? | P8-quality-controller |
| D-Q-037 | Are there claims where the warrant tag was assigned by a student and never HITL-reviewed? | P8-quality-controller |
| D-Q-040 | Has any student extraction or tagging work been incorporated without HITL review? | P8-quality-controller |
| D-Q-042 | How should the HITL adjudication queue be sorted on the PI dashboard? | P8-site-architect |
| D-Q-044 | Should the dashboard display individual student names and work states? | P8-site-architect |

**Reasoning (all 17):** The D-Q-032, D-Q-037, and D-Q-040 rows concern student tagging quality — the concern is not "is the Atlas correct?" but "did students do their work correctly?" which is grading/monitoring. D-Q-042 and D-Q-044 concern dashboard design choices that directly involve pedagogical transparency decisions. All 17 are better served by P5-Marisol's adjudicator and cohort-monitor sub-flavours. They are moved to the P5 next-pass backlog, not discarded.

---

### Backlog destination: P8 (site-architect / PI dashboard)

**N-Q-034** → P8-backlog
- Current: P2-arbiter
- Question: "In a study measuring cortisol in open-plan offices, how should I separate personality-moderated from direct environmental effects?"
- Reasoning: This is a methodological question about study design and parsing, not about adjudicating between two theoretical accounts in the Atlas. It reads as a P8-quality-controller or P8-site-architect concern (how should the Atlas index moderated vs. direct effects?) rather than a researcher adjudicating between two knowledge claims.

**N-Q-045** → P8-backlog
- Current: P2-frontiersman
- Question: "The Spatial Form × Memory cell holds only one paper in K-Atlas — what does that single study's methodology tell us about what kind of follow-up the Atlas should prioritise?"
- Reasoning: The second half of the question — "what kind of follow-up should the Atlas prioritise?" — is a site-architecture and curation question, not a researcher frontier question. The frontiersman persona asks "what's out there that hasn't been studied?" not "what should the site do about it?" The curation-priority framing belongs to P8-site-architect.

---

## Pass 4 — Coverage balance (247 surviving, gaps noted)

**Rule:** Inspect surviving items against the five axes and the four cross-product corners. Empty cells get targeted generation passes or written gap acknowledgements.

---

### Axis coverage across surviving corpus

**Cognitive purpose:** inquiry (89), information-seeking (63), deliberation (55), discovery (23), persuasion (17). Well-distributed across the top three. Discovery and persuasion are present but thin at the corpus level; this is expected since not all personas have strong discovery or persuasion needs.

**Answer shape:** Toulmin (67), ranked-brief (50), contrast-pair (48), procedure (46), field-map (36). All five shapes present. Field-map is the thinnest — this is worth noting for shape-fitting in Stage B, since many discovery questions may need to be fitted to field-map and the corpus may be under-generating them.

**Evidential demand:** converging (66), suggestive (50), measurement-grade (50), causal-with-mechanism (44), mechanistic (37). Reasonably balanced. Mechanistic is the thinnest; this is appropriate since mechanistic claims are the most demanding and not all questions reach that bar.

---

### Persona-level gaps (personas with fewer than 5 surviving questions)

These are flagged as genuine coverage gaps requiring either targeted generation or explicit written acknowledgement:

**P1-sceptic: 2 questions** (gap)
Only M-Q-001 (search entry) and one persuasion question survive. The sceptic sub-flavour needs at least a deliberation question (should I trust this?) and an information-seeking question (is there a guide?). Targeted generation pass recommended.

**P3-literature-mapper: 1 question** (gap — Hannah's corpus)
After moving E-Q-006 to backlog, only one question survives here. The literature-mapper sub-flavour needs at minimum a field-map question and a ranked-brief question. Targeted generation pass required. Note: this is Hannah's corpus — this gap is the most urgent to address.

**P3-cross-product: 3 questions** (gap — Hannah's corpus)
Below the threshold for cross-product corner coverage (low/low, low/high, high/low, high/high). Currently only low/low and low/high corners are covered. High/low and high/high need targeted additions.

**P3-construct-validity: 3 questions** (gap — Hannah's corpus)
Thin. Needs at least one measurement-grade question and one deliberation question to represent the construct-validity sub-flavour adequately.

**P3-theory-prober: 4 questions** (borderline — Hannah's corpus)
Just below threshold. One additional adversarial Toulmin question would bring this to a defensible level.

**P4-dispute-filer: 2 questions** (gap — Hannah's corpus)
The dispute-filing workflow needs at minimum: one procedure question (how do I file?) and one deliberation question (when should I dispute?). Currently only has 2 rows total.

**P4-epistemics-auditor: 2 questions** (gap — Hannah's corpus)
Same gap pattern. Needs at least a contrast-pair (how do I weigh two conflicting claims?) and an inquiry question.

**P4-pipeline-tracker: 2 questions** (gap — Hannah's corpus)
Needs a procedure question (how do I check status?) and an information-seeking question (where is my submission?).

**P5-reporter: 1 question** (gap)
Only one survivor. The reporter sub-flavour (Marisol generating institutional reports on cohort performance) needs procedure and ranked-brief questions at minimum.

**P5-cohort-monitor: 3 questions** (gap)
Thin. Needs an inquiry question and a deliberation question to round out the sub-flavour.

**P5-adjudicator and P5-assignment-designer: 4 each** (borderline)
Just below threshold. One targeted addition each would bring these to a defensible level.

---

### Cross-product corner coverage (Hannah's P3 corpus)

The cross-product framework (IV × DV at four specificity levels) was applied to P3 Elena's questions. Surviving coverage after Pass 3:

| Corner | Status | Notes |
|--------|--------|-------|
| low/low | ✓ Covered | E-Q-008 (isovist.openness × cog.creativity.divergent_thinking) |
| low/high | ✓ Covered | One surviving question |
| high/low | ✗ Gap | No surviving question covers a broad-IV × specific-DV pairing |
| high/high | ✗ Gap | No surviving question covers the broad-IV × broad-DV corner |

**Action required:** Two targeted generation passes for P3 — one high/low (e.g., "which category of spatial feature most reliably predicts specific cognitive outcome X?") and one high/high (e.g., "what does the field know broadly about how spatial environment shapes cognition?").

---

### Notable answer-shape gaps per persona

- **P3 (all sub-flavours):** No surviving persuasion questions. Elena's sub-flavours should include at least one adversarial-framed Toulmin with rebuttal panel (she is explicitly ART-sceptical). Targeted generation.
- **P4 (all sub-flavours):** No surviving discovery questions. Samira's contributor role does include an exploratory moment (what do I not know about the schema?). Consider one field-map addition.
- **P5 (all sub-flavours):** No surviving inquiry, persuasion, or discovery questions. Marisol's sub-flavours are heavily procedure and ranked-brief, which reflects her operational role — but the adjudicator sub-flavour should include at least one deliberation/contrast-pair question (how do I choose between two conflicting student submissions?).
- **P8-triage-operator:** 9 questions, all ranked-brief. No other shape represented. The triage operator has some procedure questions that should have been tagged as such (how do I handle a stalled item?). Review 2–3 rows for shape reassignment in Stage B.

---

## Backlog (20 items — do not discard)

| ID | Original persona | Backlog destination | Reason |
|----|-----------------|---------------------|--------|
| E-Q-006 | P3-literature-mapper | P7-underdetermination-prober | Underdetermination framing belongs to P7 |
| N-Q-034 | P2-arbiter | P8-quality-controller | Study-design advice = curation question, not researcher adjudication |
| N-Q-045 | P2-frontiersman | P8-site-architect | "What should the Atlas prioritise?" is curation, not researcher frontier |
| D-Q-004 | P8-triage-operator | P5-cohort-monitor | Student non-submission monitoring is instructor domain |
| D-Q-014 | P8-epistemic-graph-reader | P5-assignment-designer | Template-to-student assignment overlap is pedagogical |
| D-Q-021–030 | P8-student-pipeline-monitor | P5 (various sub-flavours) | All 10 concern student progress/quality — Marisol's domain |
| D-Q-032 | P8-quality-controller | P5-adjudicator | Student tagging accuracy = grading question |
| D-Q-037 | P8-quality-controller | P5-adjudicator | Unreviewed student warrant tags = assignment quality check |
| D-Q-040 | P8-quality-controller | P5-adjudicator | Bypassed HITL by student = pedagogical compliance |
| D-Q-042 | P8-site-architect | P5-adjudicator | Dashboard design for student visibility = pedagogical decision |
| D-Q-044 | P8-site-architect | P5-cohort-monitor | Individual vs. aggregate display = pedagogical transparency |

The P5 backlog items should be reviewed before Task 3: if Marisol's corpus (currently thin at 12 questions before Stage A) absorbs these 17 items with appropriate re-tagging, her persona will have substantially better coverage.

---

## Priority actions before Stage B

1. **Hannah (P3 + P4 + P5):** Generate two targeted P3 cross-product questions (high/low and high/high corners). Generate one additional P3-literature-mapper field-map question to replace E-Q-006. Generate one P4-dispute-filer procedure question and one P4-epistemics-auditor contrast-pair question.
2. **Team (Codebook Custodian):** Review the 17 backlogged D-Q student-monitoring questions and re-tag for P5. This would nearly double P5's surviving question count and close most of the P5 gaps.
3. **All:** Harmonise adequacy conditions from "Fails if..." to positive-plus-failure form before Stage B — the shape sketch requires knowing both what success looks like and what failure looks like.
4. **All:** Flag the P8-triage-operator shape uniformity issue (9 questions, all ranked-brief) for review in Stage B — some of these may need reassignment to procedure or contrast-pair.

---

*Winnowing log compiled for Track 4 Task 2 · COGS 160 Spring 2026*
*Full corpus: 292 → 247 surviving + 20 backlogged + 25 dropped*
