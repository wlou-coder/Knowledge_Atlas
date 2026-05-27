# Panel Run 01 — P2 · Dr. Nia Okafor · Environmental / Cognitive Neuroscientist
## Target page: ka_home_researcher.html
## Run date: 2026-04-30 · Prompt file: panel_prompt_nia_okafor.md

---

```json
{
  "panellist_id": "Nia-Surveyor",
  "sub_flavour": "P2-surveyor",
  "first_reaction_0_to_5s": "There's a topic filter and a mechanism chain right on the landing view — I need to click 'Noise & HPA Axis Stress' and see if actual primary studies come up, not just a claim.",

  "click_trace": [
    {
      "step": 1,
      "on_page_text": "Noise & HPA Axis Stress (93)",
      "action": "click",
      "expected": "A filtered list of ~93 papers on noise and cortisol, each showing author, year, sample size, and effect estimate.",
      "actual": "The domain checklist registers the selection and the six 'Of Potential Interest' cards update their text, but no paper list appears — the number 93 is decorative and there is no drill-down to the actual studies.",
      "reason": "93 studies is exactly what I need to evaluate provenance; I assumed the number was a live count linking to records."
    },
    {
      "step": 2,
      "on_page_text": "Grounding Score (CCI): 0.78 (moderate evidence)",
      "action": "hover",
      "expected": "A tooltip or expansion explaining what CCI means and how 0.78 was calculated from which papers.",
      "actual": "No tooltip appears. The score is static text with no definition or backing.",
      "reason": "As a reviewer I need to know the numerator — which specific studies constitute 'moderate' — not just a single number."
    },
    {
      "step": 3,
      "on_page_text": "Explore mechanisms →",
      "action": "click",
      "expected": "A page listing individual mechanism-chain studies with DOIs, sample sizes, and effect sizes.",
      "actual": "Nothing happens — the link appears non-functional or the destination page is not loaded in this snapshot.",
      "reason": "I need to follow the chain to primary sources."
    },
    {
      "step": 4,
      "on_page_text": "Article Search",
      "action": "click",
      "expected": "A search interface that accepts a query like 'cortisol open plan office' and returns filtered primary studies.",
      "actual": "Footer link — does not navigate within the page snapshot; destination unclear.",
      "reason": "Last attempt before switching back to PubMed."
    },
    {
      "step": 5,
      "on_page_text": "Evidence Browser",
      "action": "bail",
      "expected": "A browsable list of evidence records with DOIs.",
      "actual": "Footer link only; no navigation within this page.",
      "reason": "Eight minutes elapsed. Cannot verify primary-study provenance from this page. Returning to PubMed."
    }
  ],

  "friction_points": [
    {
      "step_ref": 1,
      "location_on_page": "Domain filter — Acoustic Design / Noise & HPA Axis Stress (93)",
      "verbatim_thought": "93 is exactly the number I need to interrogate, but clicking it does nothing useful — I cannot see a single one of those papers.",
      "severity": "catastrophic",
      "nielsen_heuristic": "visibility",
      "proposed_fix": "Make the paper-count badge a live link that opens a filtered evidence browser showing each paper's title, DOI, year, n, and primary effect size."
    },
    {
      "step_ref": 2,
      "location_on_page": "Neural Underpinnings card — Grounding Score (CCI): 0.78",
      "verbatim_thought": "What is CCI? How was 0.78 computed? From which 23 studies? I cannot cite a score I cannot reproduce.",
      "severity": "major",
      "nielsen_heuristic": "help",
      "proposed_fix": "Add a (?) tooltip on CCI that defines the metric, links the calculation method, and lists the contributing paper IDs."
    },
    {
      "step_ref": 3,
      "location_on_page": "Explore mechanisms → link",
      "verbatim_thought": "The link does nothing. If I cannot follow a mechanism chain to its supporting studies, the mechanism card is just an assertion.",
      "severity": "major",
      "nielsen_heuristic": "match",
      "proposed_fix": "Wire 'Explore mechanisms →' to a mechanism-pathway page that lists each chain link with supporting paper IDs and effect estimates."
    },
    {
      "step_ref": 4,
      "location_on_page": "Schema Status — 'Steps 1–2 confirmed in 23 studies'",
      "verbatim_thought": "Which 23 studies? Confirmed by whom? This is the most important claim on the page for my audit and I have no way to verify it.",
      "severity": "major",
      "nielsen_heuristic": "visibility",
      "proposed_fix": "Make '23 studies' a hyperlink or expandable list with paper IDs and the specific schema step each study supports."
    }
  ],

  "questions_generated": [
    {
      "q_id": "N-Q-001",
      "question": "How many primary studies — not reviews — does K-Atlas hold on noise-induced cortisol elevation in open-plan office settings, and what are their sample sizes and effect sizes?",
      "scenario_card_ref": "Q1",
      "adequacy_condition": "Answer is insufficient if it names only review papers, aggregates without individual study data, or omits any quantitative effect estimate.",
      "cognitive_purpose": "information-seeking",
      "answer_shape": "ranked-brief",
      "evidential_demand": "measurement-grade",
      "persona_fit": "P2-surveyor",
      "theoretical_commitment": "none",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Surveyor / Q1 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-002",
      "question": "What does the CCI Grounding Score of 0.78 actually mean — which papers went into that number, and is 0.78 considered strong or weak in this field?",
      "scenario_card_ref": "Q2",
      "adequacy_condition": "Answer is insufficient if it does not name the contributing studies, the formula for CCI, or a benchmark for interpreting 0.78.",
      "cognitive_purpose": "information-seeking",
      "answer_shape": "procedure",
      "evidential_demand": "converging",
      "persona_fit": "P2-surveyor",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Surveyor / Q2 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-003",
      "question": "If the only primary evidence for the cortisol–open-plan link comes from studies with N < 30, what does that do to the reliability of any claim built on that literature?",
      "scenario_card_ref": "Q3",
      "adequacy_condition": "Answer is insufficient if it does not address statistical power, replication likelihood, or the specific risk of small-N cortisol studies.",
      "cognitive_purpose": "inquiry",
      "answer_shape": "Toulmin",
      "evidential_demand": "mechanistic",
      "persona_fit": "P2-surveyor",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Surveyor / Q3 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-004",
      "question": "Are there any null results in the K-Atlas database for the noise–cortisol relationship that I should know about before I use this literature in a manuscript review?",
      "scenario_card_ref": "Q4",
      "adequacy_condition": "Answer is insufficient if it mentions only positive findings and does not check or report the absence of null results in the corpus.",
      "cognitive_purpose": "inquiry",
      "answer_shape": "contrast-pair",
      "evidential_demand": "converging",
      "persona_fit": "P2-surveyor",
      "theoretical_commitment": "adversarial",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Surveyor / Q4 / ka_home_researcher.html"
    }
  ],

  "what_they_wanted_instead": [
    "A drill-down from each topic tag's paper count to the actual paper records with DOIs and effect sizes.",
    "A definition and calculation trace for the CCI grounding score, accessible without leaving the page.",
    "A null-results filter alongside the supporting-evidence display."
  ],
  "satisfaction_rating": "complete_fail",
  "verdict_one_sentence": "The page tells me there are 93 studies on noise and HPA stress, but won't let me see a single one — that's exactly the provenance audit I came to do.",
  "goal_met_within_time_budget": false,
  "question_answered": false,
  "adequacy_met": false,
  "adequacy_reason": "The page displays claim summaries and aggregate scores without linking to the individual primary studies that would constitute an evidence audit."
}
```

---

```json
{
  "panellist_id": "Nia-Prober",
  "sub_flavour": "P2-prober",
  "first_reaction_0_to_5s": "The mechanism chain is right there — noise → amygdala → cortisol → attention — but that's my hypothesis, not my question; I need to know where it breaks.",

  "click_trace": [
    {
      "step": 1,
      "on_page_text": "Hypothesis Test — Does the evidence support my prediction?",
      "action": "click",
      "expected": "An interface where I can enter a specific mechanism hypothesis and receive a structured warrant evaluation with defeaters.",
      "actual": "The button is present in the 'Choose Your Journey' section but does not navigate or open any functional workflow in this page snapshot.",
      "reason": "Hypothesis Test is the exact entry point the page advertises for my use case."
    },
    {
      "step": 2,
      "on_page_text": "DEFEATERS — Defeat Landscape",
      "action": "scroll",
      "expected": "A list of specific rebutting and undercutting defeaters for my noise–cortisol–hippocampus chain.",
      "actual": "The defeater card shows two defeaters for nature-restoration, not acoustic stress — no acoustic-specific defeaters are rendered even after I clicked the Acoustic Design filter.",
      "reason": "The defeater display appears to be a static example unconnected to my domain filter selection."
    },
    {
      "step": 3,
      "on_page_text": "Schema Status: Steps 1–2 confirmed in 23 studies; steps 2–3 tentative; steps 3–4 partially unknown.",
      "action": "hover",
      "expected": "A breakdown of which steps of my specific chain (noise → HPA → glucocorticoid receptor → place cells → wayfinding) are confirmed vs. tentative.",
      "actual": "The schema status text is fixed to a nature-restoration example; the acoustic domain filter did not update it.",
      "reason": "I need the schema status for the acoustic-cognitive chain, not the nature chain."
    },
    {
      "step": 4,
      "on_page_text": "View all defeaters →",
      "action": "click",
      "expected": "A comprehensive, filterable defeater database for acoustic stress research.",
      "actual": "Link appears non-functional in this snapshot.",
      "reason": "Defeaters are the most important feature for hypothesis testing and the link is dead."
    },
    {
      "step": 5,
      "on_page_text": "Acoustic Environment → Mechanism / Pathway",
      "action": "bail",
      "expected": "Some pathway evidence for the acoustic domain.",
      "actual": "Cannot navigate to it from this page; no clickable link to the acoustic mechanism pathway cell.",
      "reason": "20 minutes are up; the page cannot produce a mechanistic evaluation for my specific hypothesis chain."
    }
  ],

  "friction_points": [
    {
      "step_ref": 1,
      "location_on_page": "Choose Your Journey — Hypothesis Test button",
      "verbatim_thought": "The button exists but does nothing. A hypothesis-test workflow with no working entry point is not a workflow — it's a wireframe.",
      "severity": "catastrophic",
      "nielsen_heuristic": "match",
      "proposed_fix": "Make 'Test a Hypothesis →' open a modal or page where the user enters a free-text hypothesis and receives a structured warrant-plus-defeater evaluation filtered to the selected domain."
    },
    {
      "step_ref": 2,
      "location_on_page": "DEFEATERS — Defeat Landscape card",
      "verbatim_thought": "These defeaters are for nature restoration, not acoustic stress — my filter did nothing to this card.",
      "severity": "major",
      "nielsen_heuristic": "consistency",
      "proposed_fix": "Wire the Defeat Landscape card to the domain filter so defeaters update to reflect the selected topic."
    },
    {
      "step_ref": 3,
      "location_on_page": "Neural Underpinnings card — Schema Status",
      "verbatim_thought": "Steps 1–2 confirmed, 3–4 unknown — for nature restoration. I need this schema for my acoustic-hippocampal chain, not Ulrich's.",
      "severity": "major",
      "nielsen_heuristic": "flexibility",
      "proposed_fix": "Allow the Schema Status display to update to the user's selected domain and, ideally, to a user-specified mechanism chain."
    },
    {
      "step_ref": 4,
      "location_on_page": "View all defeaters → link",
      "verbatim_thought": "The most scientifically critical link on the page for me is broken.",
      "severity": "catastrophic",
      "nielsen_heuristic": "error_prevention",
      "proposed_fix": "Implement the defeater database behind this link with domain filter propagation."
    }
  ],

  "questions_generated": [
    {
      "q_id": "N-Q-005",
      "question": "What does the K-Atlas mechanism database show for the chain: broadband noise → sustained HPA activation → glucocorticoid receptor downregulation → hippocampal place-cell degradation → wayfinding error — which links are empirically confirmed and which are inferential?",
      "scenario_card_ref": "Q1",
      "adequacy_condition": "Answer is insufficient if it does not specify evidential status (confirmed / tentative / unknown) at each link and does not cite at least one study per confirmed link.",
      "cognitive_purpose": "inquiry",
      "answer_shape": "Toulmin",
      "evidential_demand": "causal-with-mechanism",
      "persona_fit": "P2-prober",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Prober / Q1 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-006",
      "question": "Has any study in K-Atlas used pharmacological glucocorticoid blockade during acoustic noise exposure to test whether the HPA pathway — and not some other stress pathway — is necessary for the cognitive impairment?",
      "scenario_card_ref": "Q2",
      "adequacy_condition": "Answer is insufficient if it does not address whether a pharmacological manipulation study exists or explicitly notes its absence.",
      "cognitive_purpose": "inquiry",
      "answer_shape": "contrast-pair",
      "evidential_demand": "causal-with-mechanism",
      "persona_fit": "P2-prober",
      "theoretical_commitment": "adversarial",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Prober / Q2 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-007",
      "question": "What are the strongest rebutting defeaters against the noise–hippocampus mechanism chain — which studies found no effect or an alternative mechanism?",
      "scenario_card_ref": "Q3",
      "adequacy_condition": "Answer is insufficient if it presents only supporting evidence; at least one falsifying or null-result study must be named.",
      "cognitive_purpose": "inquiry",
      "answer_shape": "field-map",
      "evidential_demand": "converging",
      "persona_fit": "P2-prober",
      "theoretical_commitment": "adversarial",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Prober / Q3 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-008",
      "question": "If the place-cell link in my chain is the weakest — because almost no built-environment studies use real-time hippocampal recording — what intermediate proxy measures does the field currently use, and how valid are they?",
      "scenario_card_ref": "Q4",
      "adequacy_condition": "Answer is insufficient if it does not name at least one proxy measure (e.g., virtual navigation error, fMRI BOLD in CA1/CA3) and discuss its construct validity.",
      "cognitive_purpose": "deliberation",
      "answer_shape": "procedure",
      "evidential_demand": "mechanistic",
      "persona_fit": "P2-prober",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Prober / Q4 / ka_home_researcher.html"
    }
  ],

  "what_they_wanted_instead": [
    "A mechanism-chain query interface where I can enter specific nodes (noise → HPA → place cells) and receive per-link evidence status.",
    "A defeater database that filters to my selected domain rather than displaying a static example.",
    "The Hypothesis Test workflow to be functional, not a placeholder button."
  ],
  "satisfaction_rating": "complete_fail",
  "verdict_one_sentence": "The page advertises hypothesis testing but delivers a static illustration — I cannot probe my actual mechanism chain.",
  "goal_met_within_time_budget": false,
  "question_answered": false,
  "adequacy_met": false,
  "adequacy_reason": "The Hypothesis Test entry point is non-functional, the defeater card is domain-agnostic, and no mechanism chain can be queried directly."
}
```

---

```json
{
  "panellist_id": "Nia-Arbiter",
  "sub_flavour": "P2-arbiter",
  "first_reaction_0_to_5s": "There's a 'Competing Theories' card — ART vs. SRT on evidence balance — that's close to what I need, but I'm looking for PP vs. ART, not SRT.",

  "click_trace": [
    {
      "step": 1,
      "on_page_text": "Which mechanism framework do you currently favor?",
      "action": "click",
      "expected": "Selecting 'Predictive Processing (PP)' would update the theory comparison card to show PP's predictions against ART on the same outcome variable.",
      "actual": "The radio button is clickable and registers 'Predictive Processing (PP)' as the selection, but the Competing Theories card content does not change — it still shows the ART vs. SRT comparison.",
      "reason": "I need the page to show me PP vs. ART, not ART vs. SRT — the prior selection is supposed to personalise the evidence layout."
    },
    {
      "step": 2,
      "on_page_text": "THEORY — Competing Theories — Compare theories →",
      "action": "click",
      "expected": "A theory comparison page where I can select PP and ART and see their differential predictions on cortisol and attention outcomes.",
      "actual": "Link does not function in this snapshot.",
      "reason": "This is the only direct theory-comparison interface on the page."
    },
    {
      "step": 3,
      "on_page_text": "Discriminating Test (Woodward): Pharmacological cortisol blockade during nature exposure.",
      "action": "scroll",
      "expected": "A discriminating test for PP vs. ART on acoustic outcomes (not nature exposure).",
      "actual": "The discriminating test displayed is fixed to ART vs. SRT for nature restoration. PP is not included in the comparison.",
      "reason": "I need the page to acknowledge PP exists as a theoretical option, not just the two legacy frameworks."
    },
    {
      "step": 4,
      "on_page_text": "Neuro Perspective",
      "action": "click",
      "expected": "A page that discusses neural mechanism frameworks including Predictive Processing as applied to built environments.",
      "actual": "Nav link in footer — does not navigate within this snapshot.",
      "reason": "PP is primarily a neural-level framework; the Neuro Perspective page might have what I need."
    },
    {
      "step": 5,
      "on_page_text": "Theory Explorer",
      "action": "bail",
      "expected": "A tool for comparing multiple theories head-to-head.",
      "actual": "Appears only in a footer test-suite row; not a functional link.",
      "reason": "12 minutes elapsed; no PP vs. ART comparison possible from this page."
    }
  ],

  "friction_points": [
    {
      "step_ref": 1,
      "location_on_page": "Prior Position panel — 'Which mechanism framework do you currently favor?'",
      "verbatim_thought": "I selected Predictive Processing and nothing changed. The page says it personalises the evidence layout — that's a false promise.",
      "severity": "catastrophic",
      "nielsen_heuristic": "consistency",
      "proposed_fix": "Wire the mechanism-framework selection to the Competing Theories card so that selecting PP updates the theory comparison to include PP's predictions against ART or SRT."
    },
    {
      "step_ref": 2,
      "location_on_page": "Competing Theories card — theory comparison table",
      "verbatim_thought": "ART vs. SRT is not the comparison I need. PP doesn't appear in the table at all — it's a known and increasingly prominent framework in this field.",
      "severity": "major",
      "nielsen_heuristic": "recognition",
      "proposed_fix": "Add PP as a third row in the theory comparison table with its coherence score and a discriminating-test prediction."
    },
    {
      "step_ref": 3,
      "location_on_page": "Discriminating Test — 'Pharmacological cortisol blockade during nature exposure'",
      "verbatim_thought": "This test distinguishes ART from SRT. I need a test that distinguishes PP from ART — those are different experiments.",
      "severity": "minor",
      "nielsen_heuristic": "flexibility",
      "proposed_fix": "Allow the discriminating test text to update based on which theory pair is selected, or show all pairwise tests in an expandable list."
    },
    {
      "step_ref": 4,
      "location_on_page": "Compare theories → link",
      "verbatim_thought": "If you're going to put 'Compare theories' on a researcher homepage, the link has to work.",
      "severity": "major",
      "nielsen_heuristic": "error_prevention",
      "proposed_fix": "Implement the Compare Theories destination page with a two-column format, theory selector dropdowns, and outcome-variable filter."
    }
  ],

  "questions_generated": [
    {
      "q_id": "N-Q-009",
      "question": "Does K-Atlas have evidence that Predictive Processing and Attention Restoration Theory make different predictions on cortisol trajectory in acoustic stress environments — and if so, which theory's prediction is better supported?",
      "scenario_card_ref": "Q1",
      "adequacy_condition": "Answer is insufficient if it presents only ART vs. SRT; PP must appear as a named theoretical option with at least one distinguishing prediction.",
      "cognitive_purpose": "deliberation",
      "answer_shape": "contrast-pair",
      "evidential_demand": "converging",
      "persona_fit": "P2-arbiter",
      "theoretical_commitment": "adversarial",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Arbiter / Q1 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-010",
      "question": "What is the Woodward-criterion discriminating test that would adjudicate between Predictive Processing and Attention Restoration Theory in built-environment stress research?",
      "scenario_card_ref": "Q2",
      "adequacy_condition": "Answer is insufficient if it does not name a specific experimental manipulation that would produce different outcomes under PP vs. ART.",
      "cognitive_purpose": "deliberation",
      "answer_shape": "Toulmin",
      "evidential_demand": "causal-with-mechanism",
      "persona_fit": "P2-arbiter",
      "theoretical_commitment": "adversarial",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Arbiter / Q2 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-011",
      "question": "How does the Salience Network Modulation framework — as it appears in K-Atlas — differ from Predictive Processing in its account of why noisy open-plan environments elevate cortisol?",
      "scenario_card_ref": "Q3",
      "adequacy_condition": "Answer is insufficient if it treats SN modulation and PP as equivalent or does not specify the mechanistic difference at the neural-systems level.",
      "cognitive_purpose": "deliberation",
      "answer_shape": "contrast-pair",
      "evidential_demand": "mechanistic",
      "persona_fit": "P2-arbiter",
      "theoretical_commitment": "topic-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Arbiter / Q3 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-012",
      "question": "Once I have identified which framework is better evidenced for acoustic stress, what does the K-Atlas VOI map say is the highest-value next experiment — the one that would most update prior beliefs?",
      "scenario_card_ref": "Q4",
      "adequacy_condition": "Answer is insufficient if it does not connect the VOI calculation to the theory comparison and name a specific study design.",
      "cognitive_purpose": "discovery",
      "answer_shape": "ranked-brief",
      "evidential_demand": "converging",
      "persona_fit": "P2-arbiter",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Arbiter / Q4 / ka_home_researcher.html"
    }
  ],

  "what_they_wanted_instead": [
    "Predictive Processing listed as a framework option in the theory comparison table alongside ART and SRT.",
    "The mechanism-framework radio button actually updating the theory card content.",
    "Discriminating tests displayed for all pairwise theory comparisons, not just ART vs. SRT."
  ],
  "satisfaction_rating": "complete_fail",
  "verdict_one_sentence": "The page promises personalised theory comparison but PP doesn't appear in the comparison table and the prior-setting does nothing.",
  "goal_met_within_time_budget": false,
  "question_answered": false,
  "adequacy_met": false,
  "adequacy_reason": "Predictive Processing is absent from the displayed theory comparison, and the prior-setting widget does not update the evidence layout as advertised."
}
```

---

```json
{
  "panellist_id": "Nia-Advocate",
  "sub_flavour": "P2-advocate",
  "first_reaction_0_to_5s": "VOI targets of opportunity — this is close to what I need for a grant — but I need the strongest rebuttal architecture, not just ranked questions.",

  "click_trace": [
    {
      "step": 1,
      "on_page_text": "Noise & HPA Axis Stress (93)",
      "action": "click",
      "expected": "A filtered view of 93 studies on noise and cortisol with enough detail to distinguish longitudinal from acute designs.",
      "actual": "Topic filter registers the click and the page cards update their labels, but no study list appears; cannot distinguish longitudinal from acute designs.",
      "reason": "For an R01 Significance section, I need longitudinal cortisol studies specifically — acute studies will not survive reviewer scrutiny."
    },
    {
      "step": 2,
      "on_page_text": "DEFEATERS — Smith et al. (2023) found NO attention restoration in urban parks with high noise (>60 dB).",
      "action": "hover",
      "expected": "A DOI, sample size, and design summary for Smith et al. (2023) so I can assess how threatening this defeater is to my grant claim.",
      "actual": "No tooltip or expansion; Smith et al. (2023) is a name-drop with no link or metadata.",
      "reason": "I need to read the actual paper to assess whether its design is comparable to my claim (office noise, not urban parks)."
    },
    {
      "step": 3,
      "on_page_text": "VOI = 0.83: Does circadian disruption moderate the nature-stress restoration pathway?",
      "action": "scroll",
      "expected": "A VOI item specifically about chronic vs. acute cortisol elevation in office environments.",
      "actual": "The VOI items are locked to a nature-domain example and do not update to my acoustic filter selection.",
      "reason": "I need the highest-value experiment for my specific domain, not a generic example."
    },
    {
      "step": 4,
      "on_page_text": "Rebutting Defeater / Undercutting Defeater",
      "action": "scroll",
      "expected": "Pollock-framework defeaters for the noise–cortisol claim specifically.",
      "actual": "Defeaters shown are for nature restoration; no acoustic-domain defeaters are visible.",
      "reason": "I need the specific defeaters my grant reviewer will cite, not placeholders."
    },
    {
      "step": 5,
      "on_page_text": "View all defeaters →",
      "action": "bail",
      "expected": "A comprehensive defeater list filterable by domain.",
      "actual": "Link non-functional.",
      "reason": "15 minutes elapsed. Cannot locate chronic cortisol studies or acoustic-specific defeaters. Returning to PubMed."
    }
  ],

  "friction_points": [
    {
      "step_ref": 2,
      "location_on_page": "DEFEATERS card — 'Smith et al. (2023)'",
      "verbatim_thought": "A citation without a DOI or link is not useful for a grant — I cannot verify whether this study's design is comparable to mine.",
      "severity": "major",
      "nielsen_heuristic": "visibility",
      "proposed_fix": "Add DOI, year, journal, n, and a one-sentence design description as expandable metadata on every named study in the Defeat Landscape."
    },
    {
      "step_ref": 1,
      "location_on_page": "Domain filter — Acoustic Design / Noise & HPA Axis Stress (93)",
      "verbatim_thought": "93 studies and I cannot see whether any of them are longitudinal — that's the design distinction that decides whether my grant claim stands.",
      "severity": "catastrophic",
      "nielsen_heuristic": "visibility",
      "proposed_fix": "Add a study-design filter (acute / longitudinal / observational) visible once a domain is selected, so grant writers can isolate the design type they need."
    },
    {
      "step_ref": 3,
      "location_on_page": "VOI panel — static nature-domain examples",
      "verbatim_thought": "The VOI numbers are interesting but they're for the wrong domain — my domain filter selection did nothing here.",
      "severity": "major",
      "nielsen_heuristic": "consistency",
      "proposed_fix": "Bind all six information cards (Mechanism, Population, Theory, Defeaters, VOI, Evidence Architecture) to the user's domain filter selection so they update in sync."
    },
    {
      "step_ref": 4,
      "location_on_page": "Defeat Landscape — rebutting and undercutting defeaters",
      "verbatim_thought": "These defeaters are for nature restoration. I cannot use them in an R01 about office acoustics.",
      "severity": "major",
      "nielsen_heuristic": "consistency",
      "proposed_fix": "Wire the defeater card to the topic filter; display domain-appropriate defeaters."
    }
  ],

  "questions_generated": [
    {
      "q_id": "N-Q-013",
      "question": "What primary studies — with sample sizes and longitudinal designs — show that chronic, sustained noise exposure in open-plan offices elevates cortisol over weeks or months, not just acutely?",
      "scenario_card_ref": "Q1",
      "adequacy_condition": "Answer is insufficient if it names only acute-stress designs; at least one study tracking cortisol over ≥2 weeks must be cited, or the absence of such studies must be stated.",
      "cognitive_purpose": "persuasion",
      "answer_shape": "ranked-brief",
      "evidential_demand": "causal-with-mechanism",
      "persona_fit": "P2-advocate",
      "theoretical_commitment": "none",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Advocate / Q1 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-014",
      "question": "What is the best-documented defeater against the claim that open-plan noise chronically elevates cortisol, and how strong is it relative to the supporting evidence?",
      "scenario_card_ref": "Q2",
      "adequacy_condition": "Answer is insufficient if it does not characterise the defeater's design (sample size, study type) and compare its evidential weight to the supporting literature.",
      "cognitive_purpose": "persuasion",
      "answer_shape": "Toulmin",
      "evidential_demand": "converging",
      "persona_fit": "P2-advocate",
      "theoretical_commitment": "adversarial",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Advocate / Q2 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-015",
      "question": "How does the self-selection confound — where more stress-prone workers may disproportionately occupy open-plan desks — threaten the causal interpretation of the cortisol–open-plan association?",
      "scenario_card_ref": "Q3",
      "adequacy_condition": "Answer is insufficient if it does not name the specific design strategy (randomisation, multilevel modelling, natural experiment) that would address self-selection.",
      "cognitive_purpose": "persuasion",
      "answer_shape": "contrast-pair",
      "evidential_demand": "causal-with-mechanism",
      "persona_fit": "P2-advocate",
      "theoretical_commitment": "adversarial",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Advocate / Q3 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-016",
      "question": "Once I have the strongest available cortisol evidence, what is K-Atlas's VOI estimate for the next experiment that would most increase confidence in the chronic-cortisol causal claim?",
      "scenario_card_ref": "Q4",
      "adequacy_condition": "Answer is insufficient if the VOI estimate is not calibrated to the acoustic-cortisol domain and does not name a study design.",
      "cognitive_purpose": "persuasion",
      "answer_shape": "Toulmin",
      "evidential_demand": "measurement-grade",
      "persona_fit": "P2-advocate",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Advocate / Q4 / ka_home_researcher.html"
    }
  ],

  "what_they_wanted_instead": [
    "A study-design filter (acute / longitudinal) attached to the domain selector.",
    "DOIs and design summaries on every named study in the Defeat Landscape.",
    "VOI items that update to my selected domain, not locked to nature-restoration examples."
  ],
  "satisfaction_rating": "partial_fail",
  "verdict_one_sentence": "The defeat-landscape concept is exactly what I need for grant writing, but it shows me the wrong domain and won't link me to the actual papers.",
  "goal_met_within_time_budget": false,
  "question_answered": false,
  "adequacy_met": false,
  "adequacy_reason": "No longitudinal cortisol study can be located; the defeater card is domain-agnostic; no DOIs are provided for any named study."
}
```

---

```json
{
  "panellist_id": "Nia-Frontiersman",
  "sub_flavour": "P2-frontiersman",
  "first_reaction_0_to_5s": "VOI map, sparse cells, targets of opportunity — this page was designed for someone like me; let me see if it actually shows me a gap I don't already know.",

  "click_trace": [
    {
      "step": 1,
      "on_page_text": "Acoustic Design (3) — Noise & HPA Axis Stress (93) / Soundscapes & Restoration (41) / Speech Intelligibility (37)",
      "action": "click",
      "expected": "A topic-filtered view where I can also see which IV × DV cross-product cells have 0–1 papers — the genuine sparse frontier.",
      "actual": "The acoustic filter activates and the six cards update labels. No sparse-cell map is visible; the topic list shows only populated cells.",
      "reason": "I wanted to see not just where the evidence IS but where it ISN'T — the zero-count cells."
    },
    {
      "step": 2,
      "on_page_text": "VOI = 0.83: Does circadian disruption moderate the nature-stress restoration pathway?",
      "action": "scroll",
      "expected": "VOI items for acoustic × hippocampal / spatial-navigation intersections.",
      "actual": "VOI items are static nature-domain examples; not updated by my filter.",
      "reason": "I specifically want to know if acoustic × spatial-navigation is a VOI gap."
    },
    {
      "step": 3,
      "on_page_text": "View VOI map →",
      "action": "click",
      "expected": "A full VOI map across all IV × DV cells showing which cells have low evidence density and high expected value of a new study.",
      "actual": "Link non-functional.",
      "reason": "A VOI map across all cells is exactly the kind of landscape survey I came for."
    },
    {
      "step": 4,
      "on_page_text": "Evidence Architecture — Acoustic Perception: WEB structure — 15 studies mutually support with no single anchor.",
      "action": "scroll",
      "expected": "A web-structure breakdown that shows which specific acoustic sub-topics are in the web and which are peripheral singletons.",
      "actual": "A single summary sentence — no visual map, no expandable list of the 15 studies, no way to see which nodes are peripheral.",
      "reason": "Peripheral nodes in the acoustic web are the most likely candidates for underexplored frontiers."
    },
    {
      "step": 5,
      "on_page_text": "Evidence Browser",
      "action": "click",
      "expected": "A browsable evidence database sortable by IV × DV cell and paper count, so I can find the cells with 1–2 papers.",
      "actual": "Footer link only; non-functional in this snapshot.",
      "reason": "30 minutes. Found one interesting thing (WEB structure for acoustics) but no actual sparse cells visible."
    }
  ],

  "friction_points": [
    {
      "step_ref": 1,
      "location_on_page": "Domain filter — topic checklist",
      "verbatim_thought": "The checklist shows me where evidence exists, not where it doesn't. I need a zero-count display — the empty cells are more interesting than the full ones.",
      "severity": "major",
      "nielsen_heuristic": "visibility",
      "proposed_fix": "Add a 'Show sparse cells (≤2 papers)' toggle to the topic filter that reveals IV × DV combinations with few or no studies."
    },
    {
      "step_ref": 2,
      "location_on_page": "VOI panel",
      "verbatim_thought": "These VOI numbers are calibrated to nature-restoration, not acoustics — changing my filter should have changed these.",
      "severity": "major",
      "nielsen_heuristic": "consistency",
      "proposed_fix": "Compute and display domain-appropriate VOI items when the filter changes."
    },
    {
      "step_ref": 3,
      "location_on_page": "View VOI map → link",
      "verbatim_thought": "A full VOI map across all cells is the single most valuable feature K-Atlas could offer a frontier-seeking researcher, and it's behind a dead link.",
      "severity": "catastrophic",
      "nielsen_heuristic": "match",
      "proposed_fix": "Implement the VOI map as an interactive grid of all IV × DV cells colour-coded by evidence density and expected VOI, with click-through to cell records."
    },
    {
      "step_ref": 4,
      "location_on_page": "Evidence Architecture — web structure sentence",
      "verbatim_thought": "I know acoustics has a web structure — what I don't know is which nodes in the web are singleton papers clinging on at the periphery. That's where the frontiers are.",
      "severity": "minor",
      "nielsen_heuristic": "recognition",
      "proposed_fix": "Expand the Evidence Architecture card to show a mini-network diagram with peripheral (low-degree) nodes labelled."
    }
  ],

  "questions_generated": [
    {
      "q_id": "N-Q-017",
      "question": "What IV × DV cross-product cells in K-Atlas sit at the intersection of acoustic environment and spatial-navigation or hippocampal outcomes — and how many papers populate each?",
      "scenario_card_ref": "Q1",
      "adequacy_condition": "Answer is insufficient if it does not report the paper count for each relevant cell and distinguish cells with ≥5 papers from those with ≤2.",
      "cognitive_purpose": "discovery",
      "answer_shape": "field-map",
      "evidential_demand": "suggestive",
      "persona_fit": "P2-frontiersman",
      "theoretical_commitment": "none",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Frontiersman / Q1 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-018",
      "question": "Is there any published evidence connecting continuous acoustic stress in built environments to entorhinal cortex grid-cell disruption — or is this a completely unstudied intersection?",
      "scenario_card_ref": "Q2",
      "adequacy_condition": "Answer is insufficient if it does not explicitly confirm whether such studies exist in the K-Atlas corpus or state that the cell is empty.",
      "cognitive_purpose": "discovery",
      "answer_shape": "field-map",
      "evidential_demand": "suggestive",
      "persona_fit": "P2-frontiersman",
      "theoretical_commitment": "topic-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Frontiersman / Q2 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-019",
      "question": "How do I distinguish a genuinely sparse cell — a real research gap — from a cell that is sparse only because K-Atlas's tagging missed relevant papers that are indexed under different MeSH terms?",
      "scenario_card_ref": "Q3",
      "adequacy_condition": "Answer is insufficient if it does not address the tagging-coverage problem and suggest at least one cross-validation strategy.",
      "cognitive_purpose": "discovery",
      "answer_shape": "procedure",
      "evidential_demand": "suggestive",
      "persona_fit": "P2-frontiersman",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Frontiersman / Q3 / ka_home_researcher.html"
    },
    {
      "q_id": "N-Q-020",
      "question": "Given a confirmed sparse cell in the acoustic × hippocampal-navigation space, what does the Spohn VOI calculus say the expected information gain from a single new fMRI study in that cell would be?",
      "scenario_card_ref": "Q4",
      "adequacy_condition": "Answer is insufficient if it does not operationalise expected information gain relative to current evidence state, even approximately.",
      "cognitive_purpose": "discovery",
      "answer_shape": "ranked-brief",
      "evidential_demand": "converging",
      "persona_fit": "P2-frontiersman",
      "theoretical_commitment": "method-aware",
      "source": "panel",
      "provenance": "Panel Run 01 / Nia-Frontiersman / Q4 / ka_home_researcher.html"
    }
  ],

  "what_they_wanted_instead": [
    "A sparse-cell view or zero-count toggle showing IV × DV combinations with ≤2 papers.",
    "A functional VOI map interactive grid across all cells.",
    "VOI items that update to my domain filter selection."
  ],
  "satisfaction_rating": "partial_fail",
  "verdict_one_sentence": "The page's vocabulary is exactly right for me — VOI, sparse cells, anchor vs. web — but none of the links work and the filter does not update the cards.",
  "goal_met_within_time_budget": false,
  "question_answered": false,
  "adequacy_met": false,
  "adequacy_reason": "No sparse IV × DV cells are visible on the page, the VOI map link is non-functional, and the domain filter does not update VOI content."
}
```

---

```json
{
  "panel_disagreements": [
    {
      "step_or_element": "Domain filter — paper count badges (e.g. Noise & HPA Axis Stress (93))",
      "sub1_reaction": "Catastrophic — the number looks like a link but is decorative; I cannot audit provenance.",
      "sub2_reaction": "Catastrophic — I need to drill into the mechanism chain studies; the count badge does nothing.",
      "sub3_reaction": "Cosmetic — I wasn't trying to get to individual papers; I wanted theory comparison.",
      "sub4_reaction": "Catastrophic — I cannot filter longitudinal from acute designs without paper-level access.",
      "sub5_reaction": "Major — I need zero-count cells, not just populated-count badges.",
      "significance": "The paper-count badge creates different severity failures depending on the panellist's goal: P2-surveyor and P2-advocate need paper-level drilldown; P2-frontiersman needs sparse-cell visibility; P2-arbiter doesn't need papers at all. The fix is the same — make counts live links — but the failure modes are distinct."
    },
    {
      "step_or_element": "Six information cards (Mechanism, Population, Theory, Defeaters, VOI, Architecture)",
      "sub1_reaction": "Partial pass — the mechanism card's language is correct but CCI is opaque.",
      "sub2_reaction": "Fail — the mechanism card uses a nature example, not my acoustic chain.",
      "sub3_reaction": "Catastrophic fail — PP is absent from the theory card; the prior-setting widget is inert.",
      "sub4_reaction": "Fail — the defeater card shows wrong-domain defeaters; no DOIs on named studies.",
      "sub5_reaction": "Partial pass — the VOI card vocabulary is right but content is wrong-domain.",
      "significance": "All five panellists encounter static, nature-restoration-locked card content despite different domain filter selections. This is the most systemic failure: the six cards appear domain-responsive but are not."
    },
    {
      "step_or_element": "Choose Your Journey — Hypothesis Test button",
      "sub1_reaction": "Did not click — went to topic filter first.",
      "sub2_reaction": "Catastrophic — it is the advertised entry point for my use case and it does nothing.",
      "sub3_reaction": "Did not click — used theory comparison card.",
      "sub4_reaction": "Did not click — went to defeaters.",
      "sub5_reaction": "Did not click — went to VOI.",
      "significance": "Only P2-prober reached the Hypothesis Test button, because it is the only panellist with a true hypothesis-test goal. The button's non-functionality is catastrophic specifically for this sub-flavour; the other panellists found other paths (also broken)."
    }
  ],
  "corpus_coverage_check": {
    "cognitive_purposes_represented": [
      "information-seeking",
      "inquiry",
      "deliberation",
      "persuasion",
      "discovery"
    ],
    "missing_cognitive_purposes": [],
    "coverage_adequate": true,
    "coverage_note": "All five cognitive_purpose values are represented across the 20 panel questions. P2-surveyor covers information-seeking (Q-001, Q-002) and inquiry (Q-003, Q-004). P2-prober covers inquiry (Q-005, Q-006, Q-007) and deliberation (Q-008). P2-arbiter covers deliberation (Q-009, Q-010, Q-011) and discovery (Q-012). P2-advocate covers persuasion (Q-013, Q-014, Q-015, Q-016). P2-frontiersman covers discovery (Q-017, Q-018, Q-019, Q-020). No gaps; mining pass can deepen rather than repair coverage."
  },
  "page_serves_persona": "partially",
  "page_verdict_evidence": "The page's conceptual architecture — mechanism chains, defeat landscape, VOI, anchor vs. web structure — maps precisely onto what a research neuroscientist needs; every feature label is correct and the vocabulary is expert-appropriate. But all six information cards serve static nature-restoration examples regardless of the domain filter, all interactive links (Explore mechanisms, Compare theories, View defeaters, View VOI map) are non-functional, and the Hypothesis Test entry point does nothing. The page serves P2 at the vocabulary level only, not at the function level."
}
```
