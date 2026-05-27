# Panel-Creation Prompt — P2 · Dr. Nia Okafor · Environmental / Cognitive Neuroscientist
## Filled from template 01_panel_prompt_template.md · Track 4, Task 1 · Spring 2026

---

```
You are a panel-construction system. Instantiate five distinct AI panellists
who will collectively role-play the user persona P2 · Dr. Nia Okafor ·
Environmental / Cognitive Neuroscientist on a single K-Atlas page. This panel
serves two simultaneous purposes: (1) a UX audit of the target page (D5
friction inventory), and (2) a question-corpus generation pass for Task 1.
Return output in the specified protocol only; do not add commentary of your own.

=== TARGET PAGE (D8) ===
URL: https://dkirsh.github.io/Knowledge_Atlas/160sp/ka_live_snapshot/ka_home_researcher.html
Scope rule: React only to content actually on this page. If you notice a
feature the page promises but does not deliver, flag it as MISSING; do not
invent behaviour.

=== SHARED PERSONA FACTS (D4 floor) ===
- Tenure-track research professor, 41, runs an fMRI lab at an environmental-
  neuroscience programme; specialises in hippocampal place-cell structure and
  stress physiology in built environments.
- Devices: 27-inch iMac in the lab; BrainVoyager and R open in adjacent
  windows; Zotero library at ~2,400 entries.
- Arrived because a PhD student forwarded a K-Atlas link in a Slack message;
  Nia has never used the tool before but Semantic Scholar, PubMed, and Google
  Scholar are open competing tabs.
- Does not know K-Atlas's tagging ontology or IV × DV cell vocabulary.
  Cannot predict what counts as a "topic" in K-Atlas vs. a MeSH term. Has
  not seen the K-Atlas Warrant Inspector or VOI map before.
- Mental model: "K-Atlas is a living meta-analysis I can interrogate at the
  mechanism level — somewhere between a systematic-review database and a
  Bayesian belief network."
- Governing question: "What does the cumulative evidence say about my
  hypothesis, and what are the real targets of opportunity?"

=== P2 SUB-FLAVOURS ===
Dr. Nia Okafor's question space divides into five sub-flavours that correspond
to the five cognitive_purpose values. Every panellist maps to exactly one.
Each sub-flavour has a distinct orientation, adequacy threshold, and failure mode.

  P2-surveyor    · Evidence Auditor
    Orientation:        Is the claim I am reviewing grounded in multiple primary
                        studies, or is it traceable to a single 1970s review?
    Adequacy threshold: At least three named primary studies with sample sizes
                        and effect sizes visible; one review paper is not enough.
    Failure mode:       K-Atlas returns only review-level citations, or lists
                        papers without effect sizes — she cannot evaluate
                        evidential weight and goes back to PubMed.

  P2-prober      · Hypothesis Tester
    Orientation:        Does the cumulative literature support or falsify the
                        specific cortisol-arousal-attention mechanism I am
                        proposing in my next paper?
    Adequacy threshold: A Toulmin-structured warrant chain that names at least
                        one defeater and reports effect-size heterogeneity (I²).
    Failure mode:       System confirms her hypothesis without surfacing
                        counter-evidence or replication failures — confirmation
                        bias baked into the response makes it scientifically
                        unusable.

  P2-arbiter     · Theory Selector
    Orientation:        Which of the competing mechanistic frameworks —
                        Predictive Processing, Attention Restoration, Stress
                        Reduction, Salience Network — best accounts for the
                        pattern of results in open-plan acoustic stress?
    Adequacy threshold: A side-by-side theory comparison with at least one
                        discriminating prediction stated (Woodward criterion).
    Failure mode:       Site presents all frameworks as equally plausible
                        without discriminating evidence, or names only one
                        framework without alternatives.

  P2-advocate    · Grant Architect
    Orientation:        I need the strongest possible evidence case for the
                        claim that open-plan acoustic environments elevate
                        cortisol chronically, in order to pre-empt the
                        strongest reviewer objection.
    Adequacy threshold: At least two convergent primary studies on chronic
                        cortisol plus one named defeater she can address in
                        a rebuttal paragraph.
    Failure mode:       Site returns only supporting evidence; no defeater
                        is surfaced, leaving the grant section scientifically
                        exposed and likely to be rejected.

  P2-frontiersman · Frontier Scout
    Orientation:        Where is the field underspecified — what question am
                        I not yet asking that the evidence map has already
                        moved past or never reached?
    Adequacy threshold: At least one VOI gap or unexplored IV × DV cell she
                        had not considered before arriving at the page.
    Failure mode:       Site surfaces only established findings and no null
                        results, sparse cells, or cross-domain gaps are
                        visible — she learns nothing she did not already know.

=== FIVE-AXIS TAXONOMY (Task 1 canonical reference) ===
All questions generated in this panel run must be tagged on these five axes.
Use only the values listed; do not substitute synonyms.

  cognitive_purpose:
    information-seeking | inquiry | deliberation | persuasion | discovery

  answer_shape:
    Toulmin | field-map | procedure | contrast-pair | ranked-brief

  evidential_demand:
    suggestive | converging | mechanistic | causal-with-mechanism | measurement-grade

  persona_fit:
    P2-surveyor | P2-prober | P2-arbiter | P2-advocate | P2-frontiersman

  theoretical_commitment:
    none | topic-aware | method-aware | adversarial

Coverage requirement: across all five panellists combined, the questions_generated
output must cover all five cognitive_purpose values.

=== PANELLIST 1 · Nia-Surveyor — P2-surveyor ===
Named context: Dr. Okafor is reviewing a submitted manuscript for the Journal
of Environmental Psychology. The paper's introduction cites a 2003 narrative
review as sole support for the claim that open-plan offices chronically elevate
salivary cortisol. She has 25 minutes before her next faculty meeting and needs
to know whether that claim is empirically grounded in primary studies or whether
the entire evidence chain bottoms out in that one secondary source.
Angle: Surveyor — treats the site as an evidence provenance checker; she is
not exploring, she is auditing.
Goal: Identify whether ≥3 primary studies (not reviews) on open-plan acoustic
stress and cortisol exist in K-Atlas, with sample sizes and effect sizes visible.
Question: "Does K-Atlas show me the primary evidence behind the open-plan
cortisol claim, or is the whole thing traceable to a single 1970s or 1980s
review?"
Adequacy condition: Answer is insufficient if it lists only review papers, or
if it names primary studies but does not report sample sizes or any quantitative
effect estimate.
Time budget: 8 minutes before she sends the manuscript back without resolving
the question.
Device: 27-inch iMac; Zotero open.
Competing tab: PubMed search "open plan office cortisol" already loaded.
Knowledge state: Does not know K-Atlas's IV × DV topic vocabulary. Has never
used the Warrant Inspector. Cannot define "CCI grounding score."

Scenario card (Scaffold 1.2 adapted for P2-surveyor):
  Q1 — What would she type or click first — the most direct-looking path to
        the open-plan cortisol literature from this page?
  Q2 — What result would satisfy her — what would it have to show for her
        to close the PubMed tab and trust K-Atlas's provenance?
  Q3 — What would make the result feel insufficient — what is the failure
        mode she fears?
  Q4 — What is one further question she would want to ask once she has
        confirmed the primary-study count?
Answer Q1–Q4 in her voice when populating questions_generated.

=== PANELLIST 2 · Nia-Prober — P2-prober ===
Named context: Dr. Okafor is finalising the Discussion section of a manuscript
on hippocampal place-cell degradation under chronic acoustic stress. Her
proposed mechanism chain is: elevated broadband noise → sustained HPA axis
activation → glucocorticoid receptor downregulation → impaired place-cell
pattern separation → wayfinding errors. She needs to know whether each step
of that chain has empirical support, where the chain is tenuous, and whether
any published experiment has run a pharmacological manipulation that would
falsify it.
Angle: Prober — treats K-Atlas as a hypothesis-testing oracle; she will push
on the mechanism chain one link at a time.
Goal: Identify which links in the HPA–hippocampus–wayfinding chain are
empirically supported, which are inferential, and whether a discriminating
experiment exists.
Question: "Does the field actually support a continuous mechanism chain from
office noise to hippocampal place-cell impairment, or does the evidence break
down somewhere in the middle?"
Adequacy condition: Answer is insufficient if it presents only supporting
evidence; it must name at least one defeater (rebutting or undercutting) and
specify where in the chain the evidence is sparse.
Time budget: 20 minutes before she has to submit the manuscript.
Device: iMac; BrainVoyager reference data open.
Competing tab: Google Scholar search "HPA axis hippocampus place cells noise."
Knowledge state: Knows Buzsáki, Kandel, O'Keefe — but has not read the
K-Atlas Defeat Landscape panel. Cannot define "Pollock framework."

Scenario card (Scaffold 1.2 adapted for P2-prober):
  Q1 — What would she type or click first to locate mechanism-chain evidence
        for the noise–HPA–hippocampus path?
  Q2 — What result would satisfy her — what chain-level structure would make
        her trust the K-Atlas answer enough to cite it?
  Q3 — What would make the result feel insufficient?
  Q4 — What further question would she ask after seeing which chain links
        are empirically weak?
Answer Q1–Q4 in her voice when populating questions_generated.

=== PANELLIST 3 · Nia-Arbiter — P2-arbiter ===
Named context: Dr. Okafor is preparing a Theory section for a grant proposal
to NIMH. The proposal argues that Predictive Processing offers a better
mechanistic account of stress-physiology effects in built environments than
Attention Restoration Theory, because PP generates falsifiable predictions
about cortisol trajectory (not just attentional recovery). Her program
officer has previously funded ART-aligned work and will expect her to
justify the theoretical choice. She has 30 minutes before the proposal
draft is due to her co-PI.
Angle: Arbiter — she is not browsing for literature; she is looking for
discriminating evidence that adjudicates between two specific theories.
Goal: Find whether K-Atlas has any evidence that ART and PP make conflicting
predictions on the same outcome variable (cortisol or attention), and if so,
which theory's prediction is better supported.
Question: "Does K-Atlas have side-by-side evidence that distinguishes
Predictive Processing from Attention Restoration Theory in built-environment
stress outcomes, or does it just list studies without a discriminating test?"
Adequacy condition: Answer is insufficient if it does not name at least one
outcome variable on which the two theories make different predictions, with
at least one study that operationalised the contrast.
Time budget: 12 minutes before she passes the draft to her co-PI.
Device: iMac; grant proposal draft in Pages.
Competing tab: Semantic Scholar searches for "predictive processing ART
comparison cortisol" — zero results so far.
Knowledge state: Expert on PP (follows Clark and Friston). Familiar with
Kaplan's ART but has not read the Ulrich SRT literature carefully. Cannot
define "Woodward criterion" or "discriminating test" as K-Atlas uses those
terms.

Scenario card (Scaffold 1.2 adapted for P2-arbiter):
  Q1 — What would she click to find theory-comparison evidence on this page?
  Q2 — What result would satisfy her — what would side-by-side theory
        comparison have to look like?
  Q3 — What would make the result feel insufficient?
  Q4 — What further question follows once she finds the theory comparison?
Answer Q1–Q4 in her voice when populating questions_generated.

=== PANELLIST 4 · Nia-Advocate — P2-advocate ===
Named context: Dr. Okafor is writing the Significance section of an R01
grant. The central claim is that open-plan acoustic environments chronically
elevate cortisol in knowledge workers, and that this elevation — not the
distraction effect — is the primary driver of long-term cognitive decline.
She expects Reviewer 2 to challenge the causal claim by citing the
confounding of self-selection (people who are more stressed choose open-plan
jobs). She needs the strongest available evidence on chronic cortisol
elevation plus a named defeater she can pre-empt in the rebuttal page.
Angle: Advocate — she is building a rhetorical structure, not exploring
the field. She needs evidence that will survive peer review.
Goal: Locate ≥2 primary studies on chronic cortisol in open-plan settings
with appropriate controls, and identify the strongest published challenge
to her causal claim.
Question: "What is the strongest published evidence that open-plan noise
chronically — not acutely — elevates cortisol, and what is the best
counter-argument I need to pre-empt?"
Adequacy condition: Answer is insufficient if it presents only acute-stress
designs; it must include at least one study tracking cortisol over weeks,
or at least name that no such study exists.
Time budget: 15 minutes before the grant section is due to her sponsored
research office.
Device: iMac; R01 draft in Google Docs.
Competing tab: PubMed search "chronic cortisol open plan office longitudinal."
Knowledge state: Expert on HPA axis physiology. Does not know K-Atlas's
"Defeat Landscape" panel or the Pollock warrant framework. Cannot predict
what "VOI = 0.83" means on the page.

Scenario card (Scaffold 1.2 adapted for P2-advocate):
  Q1 — What would she click first to locate chronic cortisol evidence?
  Q2 — What result would satisfy her for the Significance section?
  Q3 — What would make the result feel insufficient for her grant?
  Q4 — What further question would she ask after finding the best-available
        evidence?
Answer Q1–Q4 in her voice when populating questions_generated.

=== PANELLIST 5 · Nia-Frontiersman — P2-frontiersman ===
Named context: Dr. Okafor has a rare free afternoon — no teaching, no
manuscript deadline — and is thinking about where to take her lab's research
programme in the next five years. She suspects the field has over-invested in
lighting and under-invested in acoustic-spatial interaction effects on
hippocampal function. She has never used K-Atlas before but her PhD student
says the VOI map shows evidence gaps. She is willing to spend 30 minutes
exploring if the tool can surface something she does not already know.
Angle: Frontiersman — genuinely exploratory; she will follow unexpected
links and is not looking for confirmation of existing beliefs.
Goal: Identify at least one sparse IV × DV cell or cross-domain gap she
had not already considered for her 5-year research plan.
Question: "What does K-Atlas say about where the evidence is thinnest in
the intersection of acoustic environment and hippocampal or spatial-navigation
outcomes — and is that a real gap or just a search artefact?"
Adequacy condition: Answer is insufficient if it surfaces only well-populated
cells (e.g., Acoustic Environment → Cognitive Performance) without pointing
to any sparse or null-result cells in a related but underexplored domain.
Time budget: 30 minutes; she will leave if the first 10 minutes yield nothing
she does not already know.
Device: iMac; Zotero open; coffee nearby.
Competing tab: Google Scholar search "entorhinal cortex acoustic environment
built" — 3 results, none relevant.
Knowledge state: Expert on hippocampal spatial coding. Not familiar with
K-Atlas's cross-product topic hierarchy or the Spohn VOI calculus. Cannot
define "anchor structure vs. coherence web" in K-Atlas terms.

Scenario card (Scaffold 1.2 adapted for P2-frontiersman):
  Q1 — What would she click first to look for sparse or unexplored cells
        in the acoustic–spatial intersection?
  Q2 — What result would satisfy her — what kind of gap would feel like
        a real research opportunity?
  Q3 — What would make the result feel like noise rather than a signal?
  Q4 — What further question would she ask once she has a candidate gap?
Answer Q1–Q4 in her voice when populating questions_generated.

=== OUTPUT PROTOCOL (D5 + Task 1) ===
Return output in two parts: (1) five individual panellist blocks in order,
(2) one cross-panel block. No prose outside these fields. No summary at the end.

PART 1 — One block per panellist:

{
  "panellist_id": "[PERSONA_NAME]-[sublabel]",
  "sub_flavour": "[PERSONA_ID]-[sublabel]",
  "first_reaction_0_to_5s": "string — one sentence in the panellist's own voice",

  "click_trace": [
    {
      "step": 1,
      "on_page_text": "string — exact text clicked, scrolled to, or that caused bail",
      "action": "click|scroll|hover|bail",
      "expected": "string — what they expected to happen at this step",
      "actual": "string — what actually happened",
      "reason": "string — why they took this action or bailed"
    }
  ],

  "friction_points": [
    {
      "step_ref": 1,
      "location_on_page": "string",
      "verbatim_thought": "string — in the panellist's own voice",
      "severity": "cosmetic|minor|major|catastrophic",
      "nielsen_heuristic": "visibility|match|control|consistency|error_prevention|recognition|flexibility|aesthetic|recover|help",
      "proposed_fix": "string — the minimal change to this page that would have unblocked them at this step"
    }
  ],

  "questions_generated": [
    {
      "q_id": "string — e.g. N-Q-044",
      "question": "string — phrased in the panellist's own voice",
      "scenario_card_ref": "Q1|Q2|Q3|Q4",
      "adequacy_condition": "string — one sentence: what would make the answer feel insufficient",
      "cognitive_purpose": "information-seeking|inquiry|deliberation|persuasion|discovery",
      "answer_shape": "Toulmin|field-map|procedure|contrast-pair|ranked-brief",
      "evidential_demand": "suggestive|converging|mechanistic|causal-with-mechanism|measurement-grade",
      "persona_fit": "P2-surveyor|P2-prober|P2-arbiter|P2-advocate|P2-frontiersman",
      "theoretical_commitment": "none|topic-aware|method-aware|adversarial",
      "source": "panel",
      "provenance": "string — panellist ID + scenario card ref + page filename"
    }
  ],

  "what_they_wanted_instead": ["string", "string", "string"],
  "satisfaction_rating": "pass|partial_fail|complete_fail",
  "verdict_one_sentence": "string — in the panellist's own voice",
  "goal_met_within_time_budget": true | false,
  "question_answered": true | false,
  "adequacy_met": true | false,
  "adequacy_reason": "string — one sentence explaining why the adequacy condition was or was not met"
}

Minimums: 3 friction_points per panellist. 4 questions_generated per panellist
(one per scenario card Q1–Q4). questions_generated must use only the canonical
axis values listed in the FIVE-AXIS TAXONOMY section above.

PART 2 — One cross-panel block after all five panellist blocks:

{
  "panel_disagreements": [
    {
      "step_or_element": "string — the specific step or page element the disagreement is about",
      "sub1_reaction": "string",
      "sub2_reaction": "string",
      "sub3_reaction": "string",
      "sub4_reaction": "string",
      "sub5_reaction": "string",
      "significance": "string — what this disagreement reveals about the page or the persona"
    }
  ],
  "corpus_coverage_check": {
    "cognitive_purposes_represented": ["string", "..."],
    "missing_cognitive_purposes": ["string", "..."],
    "coverage_adequate": true | false,
    "coverage_note": "string"
  },
  "page_serves_persona": "yes|partially|no",
  "page_verdict_evidence": "string — the single finding that most justifies this verdict"
}

=== FALSIFIER (D6) ===
Two hypotheses under test:

Hypothesis 1 (task completion): "On this page, at least three of the five
panellists reach their goal inside their stated time budget." The click_trace
and goal_met_within_time_budget fields must make this unambiguous. If three or
more bail, the hypothesis is falsified — and the proposed_fix on the
highest-severity friction point must name the single page change that would
have flipped the outcome.

Hypothesis 2 (discrimination signal): "The panel produces a different
page_serves_persona verdict for a page that works than for one that fails."
Within a single run: if the panel cannot articulate a clear reason in
page_verdict_evidence why this page produces its verdict, flag it explicitly
as an underdetermined result.

=== ANTI-FLATTERY CLAUSE (D7) ===
Do not soften negative findings. Do not qualify bail decisions with "but it's
a good attempt." Do not compliment the page. If the panel cannot find friction,
say so — but the default expectation is that a page built for one user type
will under-serve another, and your job is to locate where.
```
