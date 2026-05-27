# Stage B Shape-Fitting Log — Full Corpus
**Track 4 · Task 2 · COGS 160 Spring 2026**
*Corpus entering: 247 survivors from Stage A · Stage B rule: apply 5-shape decision table, write sketch, flag composites*

---

## Summary counts

| Metric | Count | Notes |
|--------|-------|-------|
| Total entering Stage B | 247 | From Stage A final pass |
| Shapes confirmed | 209 (85%) | Tagged shape matches decision table |
| Shapes reassigned | 38 (15%) | Tagged shape corrected by decision table |
| Composites flagged | 14 (6%) | ≥2 shapes plausible; single shape still chosen |

## Pre/post shape comparison (tagged entering → confirmed after Stage B)

| Shape | Tagged (entering Stage B) | Confirmed (Stage B) | Net Δ |
|-------|--------------------------|---------------------|-------|
| Toulmin | 67 | 91 | +24 |
| field-map | 36 | 35 | -1 |
| contrast-pair | 48 | 35 | -13 |
| ranked-brief | 50 | 43 | -7 |
| procedure | 46 | 43 | -3 |

**Key shift:** Toulmin rises (+24) because inquiry + mechanistic/causal-with-mechanism questions were frequently tagged as contrast-pair or field-map. The decision table specifies Toulmin whenever the evidential demand is mechanistic or causal-with-mechanism and the cognitive purpose is inquiry. Field-map, contrast-pair, ranked-brief, and procedure all shrink slightly as those reassignments flow to Toulmin.

---

## Decision table applied

The following 5-rule table was applied to each surviving row:

| Cognitive purpose | Evidential demand / other conditions | Confirmed shape |
|-------------------|--------------------------------------|-----------------|
| discovery | any | field-map |
| inquiry | causal-with-mechanism OR mechanistic | Toulmin |
| inquiry / persuasion | adversarial theoretical_commitment | Toulmin + mandatory rebuttal panel |
| deliberation | answer_shape = contrast-pair (2–4 options) | contrast-pair |
| deliberation | answer_shape = ranked-brief (5+ options) | ranked-brief |
| deliberation | answer_shape = procedure | procedure |
| persuasion | any | Toulmin (± rebuttal if adversarial) |
| information-seeking | any | respect existing shape (procedure / ranked-brief / field-map / contrast-pair) |
| inquiry | non-mechanistic, non-adversarial, existing shape is non-Toulmin | respect existing shape |

**Note on information-seeking:** The decision table in the task spec does not explicitly address information-seeking cognitive purpose. Information-seeking questions by nature do not build a Toulmin argument — they retrieve, rank, or navigate. The existing tagged shapes for information-seeking rows (procedure, ranked-brief, field-map) were therefore confirmed unless the purpose was mislabelled.

---

## Pass 1 — Confirmed shapes (batch decisions, 209/247)

The following batches were confirmed without shape change. Reasoning is given at the pattern level.

### Batch B-1 · P1 corpus (M-Q-prefix, most survivors)

**Rule applied:** information-seeking + procedure → confirmed procedure; deliberation + contrast-pair → confirmed contrast-pair; inquiry + converging + Toulmin → confirmed Toulmin; discovery + field-map → confirmed field-map.

P1 questions span all four purposes. The M-Q prefix is the student corpus — mix of P1-sceptic (procedure/navigational), P1-eager (Toulmin/field-map), P1-explorer (field-map/deliberation), P1-argbuilder (Toulmin/contrast-pair), P1-pragmatist (ranked-brief). Most confirmed. Exceptions: M-Q-012, M-Q-041, M-Q-042, M-Q-048, M-Q-050 (see reassigned below).

### Batch B-2 · P2 corpus (N-Q-prefix), confirmed subset

**Rule applied:** information-seeking + ranked-brief → confirmed ranked-brief (surveyor); deliberation + contrast-pair + converging → confirmed contrast-pair (arbiter); persuasion/inquiry + ranked-brief where demand is not causal-with-mechanism → confirmed for the non-advocate subset.

P2-surveyor and P2-arbiter questions that ask 'how many / which is better' with converging demand confirmed as ranked-brief / contrast-pair respectively. P2-advocate persuasion questions and P2-prober mechanistic questions were largely reassigned (see below).

### Batch B-3 · P6 corpus (J-Q-prefix), confirmed subset

P6 practitioner questions (space-designer, spec-translator, quick-lookup, evidence-checker) are predominantly information-seeking + ranked-brief or procedure. These were confirmed by rule. P6-client-briefer persuasion questions J-Q-013 and J-Q-016 were reassigned (see below); J-Q-018 flagged composite.

### Batch B-4 · P7 corpus (H-Q-prefix), confirmed subset

P7-warrant-auditor, P7-underdetermination-prober, and P7-critical-test-seeker questions were largely confirmed (procedure and field-map for auditing workflows; Toulmin for warrant checks). P7-mechanism-tracer (field-map → Toulmin) and P7-rival-theorist (contrast-pair → Toulmin) sub-flavours were systematically reassigned — see reassignment section.

### Batch B-5 · P4 + P8 corpus (S-Q / D-Q prefix), confirmed subset

P4-submitter and P4-pipeline-tracker questions are predominantly procedure and ranked-brief for information-seeking — confirmed. P8-triage-operator, P8-epistemic-graph-reader, and P8-site-architect questions are information-seeking + ranked-brief or procedure — confirmed. Exceptions: S-Q-005 reassigned; D-Q-011 composite-flagged.

---

## Pass 2 — Reassigned shapes (38 questions)

Each reassignment is documented with the triggering rule and reasoning. Questions are grouped by the pattern that caused the mismatch.

### Pattern: deliberation + causal-with-mechanism → Toulmin corrected to contrast-pair

**Count:** 1 question(s)

**N-Q-010** (P2-arbiter)
- Question: *What is the Woodward-criterion discriminating test that would adjudicate between Predictive Processi*
- Tagged: `Toulmin` → Confirmed: `contrast-pair`
- Reasoning: `deliberation` = deliberation with tagged shape `Toulmin`. Deliberation asks 'which of these should I choose?' — a contrast-pair structure is correct for 2–4 options. The tagged shape implied a different structure not aligned with the deliberative cognitive purpose.

### Pattern: deliberation + converging → Toulmin corrected to contrast-pair

**Count:** 1 question(s)

**S-Q-005** (P4-epistemics-auditor)
- Question: *Can I see the full evidence chain behind a specific warrant — every contributing study, each study's*
- Tagged: `Toulmin` → Confirmed: `contrast-pair`
- Reasoning: `deliberation` = deliberation with tagged shape `Toulmin`. Deliberation asks 'which of these should I choose?' — a contrast-pair structure is correct for 2–4 options. The tagged shape implied a different structure not aligned with the deliberative cognitive purpose.

### Pattern: deliberation + suggestive → Toulmin corrected to contrast-pair

**Count:** 1 question(s)

**M-Q-048** (P1-pragmatist)
- Question: *Would improving the ventilation in a classroom actually change how much students participate or coll*
- Tagged: `Toulmin` → Confirmed: `contrast-pair`
- Reasoning: `deliberation` = deliberation with tagged shape `Toulmin`. Deliberation asks 'which of these should I choose?' — a contrast-pair structure is correct for 2–4 options. The tagged shape implied a different structure not aligned with the deliberative cognitive purpose.

### Pattern: deliberation + suggestive → field-map corrected to contrast-pair

**Count:** 1 question(s)

**M-Q-041** (P1-explorer)
- Question: *Why do we have almost no studies linking room geometry to memory — is the effect genuinely too small*
- Tagged: `field-map` → Confirmed: `contrast-pair`
- Reasoning: `deliberation` = deliberation with tagged shape `field-map`. Deliberation asks 'which of these should I choose?' — a contrast-pair structure is correct for 2–4 options. The tagged shape implied a different structure not aligned with the deliberative cognitive purpose.

### Pattern: discovery + converging → ranked-brief corrected to field-map

**Count:** 2 question(s)

**N-Q-012** (P2-arbiter)
- Question: *Once I have identified which mechanistic framework is better evidenced for acoustic stress, what doe*
- Tagged: `ranked-brief` → Confirmed: `field-map`
- Reasoning: `discovery` = discovery specifies field-map. Discovery purpose means the persona is mapping the territory — identifying what has been studied, what gaps exist, what the landscape looks like. Tagged shape `ranked-brief` implies a navigational or comparative structure that presupposes more knowledge than the discovery purpose warrants.

**N-Q-020** (P2-frontiersman)
- Question: *Given a confirmed sparse cell in the acoustic × hippocampal-navigation space, what does the Spohn VO*
- Tagged: `ranked-brief` → Confirmed: `field-map`
- Reasoning: `discovery` = discovery specifies field-map. Discovery purpose means the persona is mapping the territory — identifying what has been studied, what gaps exist, what the landscape looks like. Tagged shape `ranked-brief` implies a navigational or comparative structure that presupposes more knowledge than the discovery purpose warrants.

### Pattern: discovery + suggestive → Toulmin corrected to field-map

**Count:** 1 question(s)

**M-Q-050** (P1-explorer)
- Question: *If thermal conditions and social behavior are barely connected in the literature, could the built en*
- Tagged: `Toulmin` → Confirmed: `field-map`
- Reasoning: `discovery` = discovery specifies field-map. Discovery purpose means the persona is mapping the territory — identifying what has been studied, what gaps exist, what the landscape looks like. Tagged shape `Toulmin` implies a navigational or comparative structure that presupposes more knowledge than the discovery purpose warrants.

### Pattern: discovery + suggestive → procedure corrected to field-map

**Count:** 2 question(s)

**M-Q-042** (P1-explorer)
- Question: *If the research on spatial form and memory is so thin, what would a well-designed study need to look*
- Tagged: `procedure` → Confirmed: `field-map`
- Reasoning: `discovery` = discovery specifies field-map. Discovery purpose means the persona is mapping the territory — identifying what has been studied, what gaps exist, what the landscape looks like. Tagged shape `procedure` implies a navigational or comparative structure that presupposes more knowledge than the discovery purpose warrants.

**N-Q-019** (P2-frontiersman)
- Question: *How do I distinguish a genuinely sparse cell — a real research gap — from a cell that is sparse only*
- Tagged: `procedure` → Confirmed: `field-map`
- Reasoning: `discovery` = discovery specifies field-map. Discovery purpose means the persona is mapping the territory — identifying what has been studied, what gaps exist, what the landscape looks like. Tagged shape `procedure` implies a navigational or comparative structure that presupposes more knowledge than the discovery purpose warrants.

### Pattern: discovery + suggestive → ranked-brief corrected to field-map

**Count:** 1 question(s)

**N-Q-039** (P2-frontiersman)
- Question: *Which architectural features beyond visual coherence — acoustic texture, thermal stability, olfactor*
- Tagged: `ranked-brief` → Confirmed: `field-map`
- Reasoning: `discovery` = discovery specifies field-map. Discovery purpose means the persona is mapping the territory — identifying what has been studied, what gaps exist, what the landscape looks like. Tagged shape `ranked-brief` implies a navigational or comparative structure that presupposes more knowledge than the discovery purpose warrants.

### Pattern: inquiry + causal-with-mechanism → contrast-pair corrected to Toulmin

**Count:** 5 question(s)

**N-Q-006** (P2-prober)
- Question: *Has any study used pharmacological glucocorticoid blockade during acoustic noise exposure to test wh*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `causal-with-mechanism` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain. (adversarial theory → rebuttal panel required)

**N-Q-055** (P2-prober)
- Question: *If the cortisol pathway is supposed to mediate both nature-induced restoration and noise-induced imp*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `causal-with-mechanism` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**H-Q-015** (P7-rival-theorist)
- Question: *Does embodied cognition theory predict different wayfinding outcomes from symbolic-map theories — an*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `causal-with-mechanism` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**H-Q-016** (P7-rival-theorist)
- Question: *How do biophilic design's evolutionary account and its cultural-learning account differ in what they*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `causal-with-mechanism` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**H-Q-018** (P7-rival-theorist)
- Question: *For noise-induced cognitive impairment, do the arousal model (Yerkes-Dodson) and the phonological-in*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `causal-with-mechanism` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

### Pattern: inquiry + converging → contrast-pair corrected to Toulmin

**Count:** 2 question(s)

**N-Q-004** (P2-surveyor)
- Question: *Are there any null results in the K-Atlas database for the noise–cortisol relationship that I should*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `converging` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain. (adversarial theory → rebuttal panel required)

**E-Q-002** (P3-theory-prober)
- Question: *Where does the evidence for Stress Recovery Theory (SRT) genuinely diverge from ART, and which studi*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `converging` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain. (adversarial theory → rebuttal panel required)

### Pattern: inquiry + converging → field-map corrected to Toulmin

**Count:** 1 question(s)

**N-Q-007** (P2-prober)
- Question: *What are the strongest rebutting defeaters against the noise–hippocampus mechanism chain — which stu*
- Tagged: `field-map` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `converging` demand specifies Toulmin. Field-map reveals the landscape of what has been studied; this question instead asks for the mechanism behind a specific claim — that requires a warrant-grounded Toulmin argument, not a territory survey. (adversarial theory → rebuttal panel required)

### Pattern: inquiry + mechanistic → contrast-pair corrected to Toulmin

**Count:** 9 question(s)

**N-Q-025** (P2-prober)
- Question: *The systematic review (PDF-0310) shows EEG dominates the neuroarchitecture method mix — what specifi*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**N-Q-026** (P2-prober)
- Question: *The vmPFC–amygdala pathway described for green space exposure in the neural review — does any study *
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain. (adversarial theory → rebuttal panel required)

**E-Q-005** (P3-theory-prober)
- Question: *What's an honest account of whether predictive processing accounts of architectural experience make *
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**E-Q-012** (P3-theory-prober)
- Question: *According to the CREA1 template, what environmental attributes are associated with DMN/ECN coupling *
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain. (adversarial theory → rebuttal panel required)

**J-Q-043** (P6-quick-lookup)
- Question: *What does research say about single-loaded vs. double-loaded corridors for patient ambulation in hos*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**H-Q-011** (P7-rival-theorist)
- Question: *How do Kaplan's ART and Ulrich's SRT explain the same natural-environment effects, and what predicti*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**H-Q-013** (P7-rival-theorist)
- Question: *For ceiling-height effects on abstraction, are the operationalist account and the Meyers-Levy constr*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**H-Q-014** (P7-rival-theorist)
- Question: *In the colour-attention literature, do the valence-activation model and the ecological-valence theor*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

**H-Q-020** (P7-rival-theorist)
- Question: *Is spatial complexity best accounted for by isovist metrics, fractal dimension, or perceived order-c*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain.

### Pattern: inquiry + mechanistic → field-map corrected to Toulmin

**Count:** 5 question(s)

**H-Q-001** (P7-mechanism-tracer)
- Question: *What is the full mechanistic chain from exposure to natural fractals to reduced physiological stress*
- Tagged: `field-map` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin. Field-map reveals the landscape of what has been studied; this question instead asks for the mechanism behind a specific claim — that requires a warrant-grounded Toulmin argument, not a territory survey.

**H-Q-003** (P7-mechanism-tracer)
- Question: *In ceiling-height effects on abstract thinking, is the proposed mechanism a change in cognitive cons*
- Tagged: `field-map` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin. Field-map reveals the landscape of what has been studied; this question instead asks for the mechanism behind a specific claim — that requires a warrant-grounded Toulmin argument, not a territory survey.

**H-Q-004** (P7-mechanism-tracer)
- Question: *What is the mechanism chain by which acoustic distraction impairs reading comprehension — phonologic*
- Tagged: `field-map` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin. Field-map reveals the landscape of what has been studied; this question instead asks for the mechanism behind a specific claim — that requires a warrant-grounded Toulmin argument, not a territory survey.

**H-Q-007** (P7-mechanism-tracer)
- Question: *In the colour-mood literature, is the mechanism a direct psychophysiological response, a learned cul*
- Tagged: `field-map` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin. Field-map reveals the landscape of what has been studied; this question instead asks for the mechanism behind a specific claim — that requires a warrant-grounded Toulmin argument, not a territory survey.

**H-Q-009** (P7-mechanism-tracer)
- Question: *For thermal comfort effects on cognitive performance, does heat impair peripheral processing first o*
- Tagged: `field-map` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` demand specifies Toulmin. Field-map reveals the landscape of what has been studied; this question instead asks for the mechanism behind a specific claim — that requires a warrant-grounded Toulmin argument, not a territory survey.

### Pattern: inquiry + mechanistic → procedure corrected to Toulmin

**Count:** 1 question(s)

**N-Q-032** (P2-prober)
- Question: *If chronic architectural prediction-error activates the anterior insula repeatedly, at what temporal*
- Tagged: `procedure` → Confirmed: `Toulmin`
- Reasoning: `inquiry` + `mechanistic` specifies Toulmin. A procedure answers 'how to do X'; this question asks for the mechanistic explanation of an effect — a theoretical claim requiring warrant and backing, not a sequence of steps.

### Pattern: persuasion + causal-with-mechanism → contrast-pair corrected to Toulmin

**Count:** 1 question(s)

**N-Q-015** (P2-advocate)
- Question: *How does the self-selection confound — where more stress-prone workers may disproportionately occupy*
- Tagged: `contrast-pair` → Confirmed: `Toulmin`
- Reasoning: `persuasion` + `causal-with-mechanism` demand specifies Toulmin by decision table rule. A contrast-pair structure addresses 'which of A or B' but the question requires a claim + warrant + backing structure at mechanistic evidential depth. Contrast-pair is the shape for *deliberation* between options; this question is *inquiry* seeking a mechanistic answer, which requires the full Toulmin warrant chain. (adversarial theory → rebuttal panel required)

### Pattern: persuasion + causal-with-mechanism → ranked-brief corrected to Toulmin

**Count:** 1 question(s)

**N-Q-013** (P2-advocate)
- Question: *What primary studies — with sample sizes and longitudinal designs — show that chronic, sustained noi*
- Tagged: `ranked-brief` → Confirmed: `Toulmin`
- Reasoning: `persuasion` + `causal-with-mechanism` specifies Toulmin. Ranked-brief lists items in priority order, but this question asks for a persuasive claim backed by causal-with-mechanism evidence — a Toulmin structure (claim + warrant + backing + rebuttal) is the appropriate shape. (adversarial theory → rebuttal panel required)

### Pattern: persuasion + converging → ranked-brief corrected to Toulmin

**Count:** 3 question(s)

**M-Q-012** (P1-sceptic)
- Question: *Are there papers that support my argument, or only ones that complicate it?*
- Tagged: `ranked-brief` → Confirmed: `Toulmin`
- Reasoning: `persuasion` + `converging` specifies Toulmin. Ranked-brief lists items in priority order, but this question asks for a persuasive claim backed by causal-with-mechanism evidence — a Toulmin structure (claim + warrant + backing + rebuttal) is the appropriate shape. (adversarial theory → rebuttal panel required)

**J-Q-013** (P6-client-briefer)
- Question: *The client wants to cut the courtyard from the hospital design for budget — what evidence can I show*
- Tagged: `ranked-brief` → Confirmed: `Toulmin`
- Reasoning: `persuasion` + `converging` specifies Toulmin. Ranked-brief lists items in priority order, but this question asks for a persuasive claim backed by causal-with-mechanism evidence — a Toulmin structure (claim + warrant + backing + rebuttal) is the appropriate shape. (adversarial theory → rebuttal panel required)

**J-Q-016** (P6-client-briefer)
- Question: *I am writing the evidence-based design narrative for a student wellness centre — what is the stronge*
- Tagged: `ranked-brief` → Confirmed: `Toulmin`
- Reasoning: `persuasion` + `converging` specifies Toulmin. Ranked-brief lists items in priority order, but this question asks for a persuasive claim backed by causal-with-mechanism evidence — a Toulmin structure (claim + warrant + backing + rebuttal) is the appropriate shape. (adversarial theory → rebuttal panel required)

---

## Pass 3 — Composites flagged (14 questions)

A composite is flagged when ≥2 shapes are plausible for a question. A single shape is still confirmed (the primary fit); the composite note indicates what secondary structure the shape sketch should acknowledge.

**Protocol for composite questions:** The shape sketch for each flagged question must include a note on the secondary shape, explaining why the primary shape was chosen and what the secondary shape would add if the question were split.

**M-Q-046** (P1-argbuilder) — confirmed: `contrast-pair`
- Question: *Is nature-induced restoration the same psychological process as stress relief, or are attention reco*
- Composite note: Potential Toulmin composite: causal-with-mechanism demand implies warrant-backing structure beyond simple comparison
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**N-Q-008** (P2-prober) — confirmed: `procedure`
- Question: *If the place-cell link in my chain is the weakest — because almost no built-environment studies use *
- Composite note: Potential ranked-brief composite: question implies ordering beyond step-following
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**N-Q-010** (P2-arbiter) — confirmed: `contrast-pair`
- Question: *What is the Woodward-criterion discriminating test that would adjudicate between Predictive Processi*
- Composite note: Potential Toulmin composite: causal-with-mechanism demand implies warrant-backing structure beyond simple comparison
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**N-Q-011** (P2-arbiter) — confirmed: `contrast-pair`
- Question: *How does the Salience Network Modulation framework — as it appears in K-Atlas — differ from Predicti*
- Composite note: Potential Toulmin composite: causal-with-mechanism demand implies warrant-backing structure beyond simple comparison
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**N-Q-023** (P2-frontiersman) — confirmed: `field-map`
- Question: *Does the degree of enclosure-induced aMCC activation documented in architectural fMRI studies intera*
- Composite note: Potential Toulmin composite: adversarial theoretical_commitment implies embedded rebuttal slot in the map
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**N-Q-039** (P2-frontiersman) — confirmed: `field-map`
- Question: *Which architectural features beyond visual coherence — acoustic texture, thermal stability, olfactor*
- Composite note: Potential Toulmin composite: adversarial theoretical_commitment implies embedded rebuttal slot in the map
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**N-Q-047** (P2-arbiter) — confirmed: `procedure`
- Question: *What study design would best populate the Spatial Form × Memory cell — a virtual navigation paradigm*
- Composite note: Potential ranked-brief composite: question implies ordering beyond step-following
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**E-Q-002** (P3-theory-prober) — confirmed: `Toulmin`
- Question: *Where does the evidence for Stress Recovery Theory (SRT) genuinely diverge from ART, and which studi*
- Composite note: Potential field-map composite: question probes the territory as well as the claim
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**J-Q-006** (P6-space-designer) — confirmed: `contrast-pair`
- Question: *Does wayfinding clarity in an outpatient clinic corridor affect patient anxiety — and is signage or *
- Composite note: Potential Toulmin composite: causal-with-mechanism demand implies warrant-backing structure beyond simple comparison
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**J-Q-018** (P6-client-briefer) — confirmed: `Toulmin`
- Question: *Can I claim our evidence-based design process reduces patient falls by X%? What is the honest range *
- Composite note: Potential procedure composite: persuasion question contains procedural element
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**J-Q-024** (P6-evidence-checker) — confirmed: `contrast-pair`
- Question: *Does the evidence support circadian lighting protocols in hospital design, or are effect sizes too s*
- Composite note: Potential Toulmin composite: causal-with-mechanism demand implies warrant-backing structure beyond simple comparison
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**H-Q-046** (P7-critical-test-seeker) — confirmed: `procedure`
- Question: *What experiment would show whether the open-plan office distraction effect is driven by auditory int*
- Composite note: Potential ranked-brief composite: question implies ordering beyond step-following
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**H-Q-050** (P7-critical-test-seeker) — confirmed: `field-map`
- Question: *In the restorative-environment literature, has any study been designed to fail — i.e., to test a con*
- Composite note: Potential Toulmin composite: adversarial theoretical_commitment implies embedded rebuttal slot in the map
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

**D-Q-011** (P8-epistemic-graph-reader) — confirmed: `field-map`
- Question: *Show me the current state of the ART-vs-SRT underdetermination node in the epistemic graph — has any*
- Composite note: Potential Toulmin composite: adversarial theoretical_commitment implies embedded rebuttal slot in the map
- Team note: If the journey splits naturally at the composite point, consider adding a second question in Stage C targeted at the secondary shape. Do not force the primary shape to do double duty — acknowledge the secondary structure in the shape sketch and flag for targeted generation.

---

## Persona-level shape distribution after Stage B

| Persona | n | Toulmin | field-map | contrast-pair | ranked-brief | procedure | Notes |
|---------|---|---------|-----------|---------------|--------------|-----------|-------|
| P1-argbuilder | 9 | 3 | 0 | 3 | 3 | 0 |  |
| P1-eager | 12 | 6 | 3 | 1 | 2 | 0 |  |
| P1-explorer | 9 | 1 | 6 | 2 | 0 | 0 | 2 reassigned: procedure→field-map, Toulmin→field-map (discovery purpose) |
| P1-pragmatist | 5 | 1 | 0 | 2 | 2 | 0 |  |
| P1-sceptic | 2 | 1 | 0 | 0 | 0 | 1 |  |
| P2-advocate | 6 | 6 | 0 | 0 | 0 | 0 | 2 reassigned ranked-brief/contrast-pair → Toulmin (persuasion purpose) |
| P2-arbiter | 9 | 0 | 1 | 5 | 1 | 2 |  |
| P2-frontiersman | 8 | 0 | 8 | 0 | 0 | 0 | 3 reassigned ranked-brief/procedure → field-map (discovery purpose) |
| P2-prober | 10 | 9 | 0 | 0 | 0 | 1 | 5 reassigned contrast-pair/procedure/field-map → Toulmin (mechanistic demand) |
| P2-surveyor | 9 | 3 | 1 | 0 | 3 | 2 |  |
| P3-construct-validity | 3 | 0 | 0 | 1 | 1 | 1 |  |
| P3-cross-product | 3 | 1 | 1 | 1 | 0 | 0 |  |
| P3-literature-mapper | 1 | 0 | 1 | 0 | 0 | 0 |  |
| P3-theory-prober | 4 | 4 | 0 | 0 | 0 | 0 |  |
| P4-dispute-filer | 2 | 0 | 0 | 0 | 0 | 2 |  |
| P4-epistemics-auditor | 2 | 0 | 0 | 1 | 0 | 1 |  |
| P4-pipeline-tracker | 2 | 0 | 0 | 0 | 0 | 2 |  |
| P4-submitter | 6 | 0 | 0 | 1 | 0 | 5 |  |
| P5-adjudicator | 4 | 0 | 0 | 1 | 0 | 3 |  |
| P5-assignment-designer | 4 | 0 | 0 | 0 | 1 | 3 |  |
| P5-cohort-monitor | 3 | 0 | 0 | 0 | 2 | 1 |  |
| P5-reporter | 1 | 0 | 0 | 0 | 0 | 1 |  |
| P6-client-briefer | 10 | 8 | 0 | 2 | 0 | 0 | 2 reassigned ranked-brief → Toulmin (persuasion purpose) |
| P6-evidence-checker | 10 | 5 | 3 | 2 | 0 | 0 |  |
| P6-quick-lookup | 10 | 3 | 0 | 3 | 3 | 1 |  |
| P6-space-designer | 10 | 2 | 0 | 4 | 3 | 1 |  |
| P6-spec-translator | 10 | 0 | 0 | 2 | 2 | 6 |  |
| P7-critical-test-seeker | 10 | 0 | 2 | 0 | 0 | 8 |  |
| P7-mechanism-tracer | 10 | 9 | 1 | 0 | 0 | 0 | All 5 confirmed Toulmin (were field-map) — see reassignments |
| P7-rival-theorist | 10 | 10 | 0 | 0 | 0 | 0 | 6/10 reassigned contrast-pair → Toulmin; adversarial confirmed Toulmin + rebuttal |
| P7-underdetermination-prober | 10 | 8 | 2 | 0 | 0 | 0 |  |
| P7-warrant-auditor | 10 | 8 | 2 | 0 | 0 | 0 |  |
| P8-epistemic-graph-reader | 9 | 2 | 4 | 0 | 3 | 0 |  |
| P8-quality-controller | 7 | 1 | 0 | 0 | 6 | 0 |  |
| P8-site-architect | 8 | 0 | 0 | 4 | 2 | 2 |  |
| P8-triage-operator | 9 | 0 | 0 | 0 | 9 | 0 | All ranked-brief; review 2–3 for procedure candidates in Stage C |

---

## Team fitting-critique notes

These are items the team should discuss before the Stage B submission is finalised:

**1. P7-rival-theorist reassignment (6 items: H-Q-011 through H-Q-020).**
Six questions in the rival-theorist sub-flavour were tagged as contrast-pair but confirm as Toulmin because the cognitive_purpose is inquiry + mechanistic demand. The team should consider whether these questions are genuinely *inquiry* (seeking the best mechanistic account) or *deliberation* (choosing between two frameworks to use). If the intent is deliberation, the contrast-pair tag should be restored and a ranked-brief used where the rival accounts are explicitly weighed. If the intent is inquiry into which account the evidence actually supports, Toulmin with mandatory rebuttal panel is correct.

**2. P7-mechanism-tracer reassignment (5 items: H-Q-001/003/004/007/009).**
All five mechanism-tracer questions were tagged as field-map but confirm as Toulmin. Field-map is appropriate when the persona is surveying the territory; Toulmin is appropriate when the persona is asking for a specific mechanism chain. The mechanism-tracer sub-flavour by definition asks for a causal chain — Toulmin is the right shape. The team should verify this is consistent with how this sub-flavour was defined.

**3. P8-triage-operator: all ranked-brief.**
Nine questions, all ranked-brief. As noted in Stage A, some of these (specifically those about 'how should I handle X?') are better served by procedure. Recommend reviewing D-Q-001, D-Q-002, D-Q-003 for procedure reassignment before Stage C.

**4. Hannah's P3 questions: all confirmed, but thin sub-flavours still gap.**
E-Q-002, E-Q-005, E-Q-012 (theory-prober, contrast-pair → Toulmin), and the 3 construct-validity + 3 cross-product survivors, all confirmed their corrected shapes. The coverage gap flagged in Stage A remains: P3-literature-mapper has 1 question and both P3 cross-product gap corners (high/low, high/high) are unfilled. Targeted generation should happen before Stage C, or these gaps should be explicitly acknowledged in the submission.

**5. Composite questions: do not split without a new Stage A pass.**
All 14 composite questions have a primary shape confirmed. If the team decides to split any composite into two questions (one per shape), those new questions must go through a mini Stage A pass (adequacy gate + persona-fit check) before being added to the Stage C corpus.

---

## Coverage check after Stage B

| Shape | Count | % | Status |
|-------|-------|---|--------|
| Toulmin | 91 | 37% | ✓ Healthy |
| field-map | 35 | 14% | ✓ Healthy |
| contrast-pair | 35 | 14% | ✓ Healthy |
| ranked-brief | 43 | 17% | ✓ Healthy |
| procedure | 43 | 17% | ✓ Healthy |

All five shapes are represented in the confirmed corpus. Field-map (35) and contrast-pair (35) are the thinnest — both at 14%. This is expected: field-map is a discovery-purpose shape and the corpus skews toward inquiry; contrast-pair is a deliberation-purpose shape and many deliberation questions were moved to Toulmin after the decision-table correction. No shape is at a gap level (<10 questions).

---

*End of Stage B log. Next step: Stage C — Name Defeaters (citable falsifying studies, alternative explanations, scope conditions, embedded theoretical commitments) for each surviving question. Due Friday 8 May 2026.*