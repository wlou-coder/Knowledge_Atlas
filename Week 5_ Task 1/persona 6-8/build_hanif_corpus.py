import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ── palette ───────────────────────────────────────────────────────────────────
INDIGO_DARK   = "2C2C6E"   # header bg
INDIGO_MID    = "4A4A9E"   # sub-flavour divider
LAVENDER_LIGHT= "E8E8F8"   # alt row A
WARM_WHITE    = "FAFAF5"   # alt row B
WHITE         = "FFFFFF"
AMBER         = "FFF3CD"

def hdr_fill(hex_color): return PatternFill("solid", fgColor=hex_color)
def thin_border():
    s = Side(style="thin", color="BBBBBB")
    return Border(left=s, right=s, top=s, bottom=s)

HEADERS = [
    "id", "question", "adequacy_condition",
    "cognitive_purpose", "answer_shape", "evidential_demand",
    "persona_fit", "theoretical_commitment",
    "source", "provenance", "notes"
]

rows = [
# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 1 · P7-mechanism-tracer  (H-Q-001 – H-Q-010)
# ──────────────────────────────────────────────────────────────────────────────
("H-Q-001",
 "What is the full mechanistic chain from exposure to natural fractals to reduced physiological stress — and at which step does the evidence break down?",
 "Fails if it does not specify at least three levels of the mechanism (distal → intermediate → proximate) and does not identify the evidential gap at each level.",
 "inquiry", "field-map", "mechanistic",
 "P7-mechanism-tracer",
 "Assumes mechanisms are decomposable and hierarchically organised (Machamer-Darden-Craver MDC framework).",
 "panel", "Panel-A · scenario-card-fractal-mechanism",
 "Entry via mechanism-trace workflow; Hanif wants the full causal chain, not a summary."),

("H-Q-002",
 "Is the restorative effect of nature environments mediated by reduced sympathetic activation, or does cortical attention recovery precede the autonomic change — and what does the evidence say about temporal order?",
 "Fails if it does not adjudicate temporal ordering (neural vs. autonomic) with at least one study measuring both streams in sequence.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-mechanism-tracer",
 "Presupposes ART's directed-attention account and Ulrich SRT predict different temporal orderings of the same mediators.",
 "panel", "Panel-A · scenario-card-ART-SRT-mechanism-order",
 ""),

("H-Q-003",
 "In ceiling-height effects on abstract thinking, is the proposed mechanism a change in cognitive construal, a proprioceptive schema shift, or something else — and which level has empirical support?",
 "Fails if it does not distinguish mechanism proposals and does not cite evidence for each level separately.",
 "inquiry", "field-map", "mechanistic",
 "P7-mechanism-tracer",
 "Assumes Meyers-Levy construal-level account but probes whether mechanism is cognitive or embodied.",
 "mining", "template-spatial-ceiling-height-mechanism",
 ""),

("H-Q-004",
 "What is the mechanism chain by which acoustic distraction impairs reading comprehension — phonological interference, attentional capture, or arousal modulation?",
 "Fails if it does not identify the competing mechanistic proposals and cite at least one study for each that tests the specific pathway.",
 "inquiry", "field-map", "mechanistic",
 "P7-mechanism-tracer",
 "Presupposes the irrelevant-sound-effect literature; probes whether mechanism is specific to verbal material or general to attention.",
 "mining", "template-sound-reading-comprehension",
 ""),

("H-Q-005",
 "When biophilic elements reduce cortisol in hospital patients, what is the intermediary — visual engagement, uncertainty reduction, or direct parasympathetic activation?",
 "Fails if it does not identify the causal intermediate and cite a study manipulating the purported intermediate while holding other variables constant.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-mechanism-tracer",
 "Assumes Ulrich's affective appraisal model; probes whether visual engagement is necessary or whether any uncertainty reduction would work.",
 "panel", "Panel-B · scenario-card-biophilia-cortisol",
 ""),

("H-Q-006",
 "What mechanism explains the wayfinding-stress link — does spatial disorientation produce anxiety, or does anxiety-driven attentional narrowing impair wayfinding?",
 "Fails if it does not address the directionality of the causal arrow with appropriate study designs (e.g. induced-anxiety paradigm vs. disorientation paradigm).",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-mechanism-tracer",
 "Assumes stress and wayfinding are separable constructs; probes which is cause and which is consequence.",
 "cross-product", "IV:spatial[wayfinding-clarity] × DV:affect[anxiety] · mechanism-level interrogation",
 ""),

("H-Q-007",
 "In the colour-mood literature, is the mechanism a direct psychophysiological response, a learned cultural association, or a context-priming effect — and are these empirically separable?",
 "Fails if it does not provide separate evidence for each mechanism type and does not note studies that attempt to dissociate them.",
 "inquiry", "field-map", "mechanistic",
 "P7-mechanism-tracer",
 "Agnostic between nativist and cultural accounts of colour-affect links; seeks dissociation evidence.",
 "mining", "template-color-affect-mechanism",
 ""),

("H-Q-008",
 "In IAQ studies showing CO₂ effects on decision-making, is the mechanism metabolic (direct CO₂ effects on CNS), attentional (discomfort distraction), or arousal-mediated — and can the evidence distinguish these?",
 "Fails if it does not specify which mechanism each study tested and whether any design controlled for participant awareness of CO₂ levels.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-mechanism-tracer",
 "Assumes CO₂ has independent direct effects; probes whether expectancy awareness mediates (confound vs. cause).",
 "panel", "Panel-C · scenario-card-CO2-mechanism",
 ""),

("H-Q-009",
 "For thermal comfort effects on cognitive performance, does heat impair peripheral processing first or central executive function — and which direction does the evidence lean?",
 "Fails if it does not specify at which cognitive level (WM, attention, processing speed) the effect is first observed and does not compare hot vs. cold conditions separately.",
 "inquiry", "field-map", "mechanistic",
 "P7-mechanism-tracer",
 "Assumes a bottom-up (peripheral → central) model of thermal impairment; tests whether this ordering is correct.",
 "mining", "template-thermal-cognitive-mechanism",
 ""),

("H-Q-010",
 "When daylight improves circadian entrainment in hospital patients, is the mechanism photonic (melanopsin-driven), social-schedule-driven, or motivation-driven — and how does the Atlas handle this tripartite uncertainty?",
 "Fails if it does not identify all three candidate mechanisms and does not flag whether the Atlas carries a mechanism-underdetermination annotation for this pathway.",
 "discovery", "field-map", "causal-with-mechanism",
 "P7-mechanism-tracer",
 "Assumes melanopsin photobiology as the dominant framework; probes whether social and motivational accounts are eliminated.",
 "cross-product", "IV:color[daylight] × DV:physio[circadian-entrainment] · mechanism-trace corner",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 2 · P7-rival-theorist  (H-Q-011 – H-Q-020)
# ──────────────────────────────────────────────────────────────────────────────
("H-Q-011",
 "How do Kaplan's ART and Ulrich's SRT explain the same natural-environment effects, and what predictions do they make that actually differ?",
 "Fails if it does not produce a side-by-side mechanism comparison and does not name at least one prediction where the theories diverge.",
 "inquiry", "contrast-pair", "mechanistic",
 "P7-rival-theorist",
 "Takes ART and SRT as genuine competitors rather than complementary accounts.",
 "panel", "Panel-A · scenario-card-ART-vs-SRT",
 "Core entry question for theory-comparison matrix workflow."),

("H-Q-012",
 "Does predictive processing / active inference offer a better mechanistic account of environmental preference than SRT and ART — and what evidence would adjudicate?",
 "Fails if it does not identify what predictive processing predicts that ART/SRT do not, and does not cite a study that could in principle discriminate.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-rival-theorist",
 "Leans toward PP as a potential unifying framework; tests whether it has distinctive empirical content over existing theories.",
 "panel", "Panel-A · scenario-card-PP-vs-ART",
 ""),

("H-Q-013",
 "For ceiling-height effects on abstraction, are the operationalist account and the Meyers-Levy construal-level account saying the same thing in different words — or do they make different predictions?",
 "Fails if it does not identify at least one prediction that one account makes and the other does not.",
 "inquiry", "contrast-pair", "mechanistic",
 "P7-rival-theorist",
 "Distinguishes semantic equivalence (same prediction, different vocabulary) from substantive theoretical difference.",
 "panel", "Panel-B · scenario-card-construal-vs-operationalism",
 ""),

("H-Q-014",
 "In the colour-attention literature, do the valence-activation model and the ecological-valence theory make different empirical predictions about which hues facilitate which cognitive tasks?",
 "Fails if it conflates valence with arousal and does not identify a specific task-colour pairing that the theories predict differently.",
 "inquiry", "contrast-pair", "mechanistic",
 "P7-rival-theorist",
 "Presupposes that both theories are individually coherent and empirically discriminable (not co-extensive).",
 "mining", "template-color-attention-rival-theories",
 ""),

("H-Q-015",
 "Does embodied cognition theory predict different wayfinding outcomes from symbolic-map theories — and if so, what spatial design feature would reveal the difference?",
 "Fails if it does not specify the spatial feature on which the theories give opposing predictions.",
 "inquiry", "contrast-pair", "causal-with-mechanism",
 "P7-rival-theorist",
 "Takes embodied cognition and symbolic-map accounts as genuine competitors in wayfinding, with different design implications.",
 "panel", "Panel-B · scenario-card-embodied-vs-map-wayfinding",
 ""),

("H-Q-016",
 "How do biophilic design's evolutionary account and its cultural-learning account differ in what they predict about cross-cultural variation in nature-environment responses?",
 "Fails if it does not describe what cross-cultural pattern would support the evolutionary account and what pattern would support the cultural-learning account.",
 "inquiry", "contrast-pair", "causal-with-mechanism",
 "P7-rival-theorist",
 "Takes Kellert-Wilson evolutionary account and cultural-learning account as empirically distinguishable via cross-cultural designs.",
 "mining", "template-biophilia-evolutionary-vs-cultural",
 ""),

("H-Q-017",
 "Is fractal-complexity preference better explained by low-level visual fluency or high-level restorative engagement — and are there studies that test the dissociation?",
 "Fails if it does not describe a study design that could dissociate perceptual from cognitive-restoration processing and cite one that actually attempts this.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-rival-theorist",
 "Treats fluency account (Reber et al.) and restorative engagement (Kaplan) as distinct explanatory levels, not reducible to each other.",
 "cross-product", "IV:complexity[fractal-dimension] × DV:affect[restorativeness] · rival-account corner",
 ""),

("H-Q-018",
 "For noise-induced cognitive impairment, do the arousal model (Yerkes-Dodson) and the phonological-interference model predict different patterns across task types — and which pattern does the evidence favour?",
 "Fails if it does not specify which task types each model differentially predicts to be impaired and does not cite studies designed to discriminate.",
 "inquiry", "contrast-pair", "causal-with-mechanism",
 "P7-rival-theorist",
 "Treats arousal-based and phonological-interference accounts as mechanistically distinct with different task-specificity signatures.",
 "panel", "Panel-C · scenario-card-noise-arousal-interference",
 ""),

("H-Q-019",
 "For the window-view-and-recovery effect, is the operative variable visual access to nature per se, or the affective valence of what is viewed — and how do the rival accounts cash out the difference?",
 "Fails if it does not specify a study manipulating affective valence of view content independently of nature-vs-built and does not report whether any such study exists.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-rival-theorist",
 "Distinguishes biophilic specificity (nature is special) from affective-valence account (positive content is the operative variable).",
 "mining", "template-biophilia-valence-vs-nature-specificity",
 ""),

("H-Q-020",
 "Is spatial complexity best accounted for by isovist metrics, fractal dimension, or perceived order-complexity balance — and do these measures agree on which environments are actually complex?",
 "Fails if it does not give an example of an environment where the three metrics disagree and does not cite evidence on which best predicts human preference or restoration.",
 "inquiry", "contrast-pair", "mechanistic",
 "P7-rival-theorist",
 "Treats isovist geometry, fractal mathematics, and perceived balance as distinct theoretical commitments with different empirical implications.",
 "cross-product", "IV:complexity[spatial-complexity-metrics] × DV:affect[preference] · rival-metrics corner",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 3 · P7-underdetermination-prober  (H-Q-021 – H-Q-030)
# ──────────────────────────────────────────────────────────────────────────────
("H-Q-021",
 "Is the current evidence base sufficient to adjudicate between ART and SRT, or is the dataset structurally underdetermined between them?",
 "Fails if it gives a verdict without identifying what specific study design would produce underdetermination-breaking data.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-underdetermination-prober",
 "Treats underdetermination as a non-trivial epistemic state requiring a specific adjudication design, not merely 'more research needed'.",
 "panel", "Panel-A · scenario-card-ART-SRT-underdetermination",
 ""),

("H-Q-022",
 "When the Atlas reports that 'nature exposure reduces cortisol', which specific theoretical account does that claim belong to — and can the claim be stated without committing to one account?",
 "Fails if it does not identify the theoretical commitment embedded in the cortisol claim's warrant and does not say whether a theory-neutral formulation is possible.",
 "inquiry", "Toulmin", "mechanistic",
 "P7-underdetermination-prober",
 "Assumes Quinean holism: observational claims inherit theoretical commitments from the framework generating them.",
 "panel", "Panel-A · scenario-card-theory-neutral-claim",
 ""),

("H-Q-023",
 "For colour temperature and alertness, is the evidence underdetermined between a direct photobiological account and a placebo/expectancy account?",
 "Fails if it does not describe what a blinded lighting study would need to look like and whether any such study exists.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-underdetermination-prober",
 "Takes expectancy effects as a genuine rival to direct photobiological accounts — not merely a nuisance variable to control away.",
 "cross-product", "IV:color[color-temperature] × DV:cog[alertness] · underdetermination corner",
 ""),

("H-Q-024",
 "Does the fractal-preference literature suffer from underdetermination because both the evolutionary and fluency accounts predict preference for D ≈ 1.3–1.5 — and are there discriminating predictions at the tails?",
 "Fails if it does not identify whether the two accounts make any discriminating predictions at the distribution tails.",
 "inquiry", "Toulmin", "mechanistic",
 "P7-underdetermination-prober",
 "Takes evolutionary and processing-fluency accounts as co-extensional on the central range, requiring dissociation at extremes.",
 "mining", "template-complexity-fractal-underdetermination",
 ""),

("H-Q-025",
 "When multiple converging studies all support biophilic design, does their convergence actually increase confirmation if they all share the same methodological family (self-report in laboratory)?",
 "Fails if it does not address whether shared method variance produces spurious convergence and cite at least one methodologically diverse study.",
 "inquiry", "Toulmin", "converging",
 "P7-underdetermination-prober",
 "Treats methodological coherentism as a potential source of confirmation bias; draws on Quinean epistemology and Laudan's methodological critique.",
 "panel", "Panel-A · scenario-card-convergence-illusion",
 "Key epistemological concern for coherentist: convergence within paradigm ≠ cross-paradigm confirmation."),

("H-Q-026",
 "In the daylighting-and-learning literature, is the evidence underdetermined between a direct light-quality account and a confound with school socioeconomic quality?",
 "Fails if it does not describe what study design (e.g. within-school randomisation) would break the confound and whether any such design has been run.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-underdetermination-prober",
 "Presupposes that SES confounds are empirically distinguishable from causal light effects with the right design.",
 "panel", "Panel-B · scenario-card-daylighting-SES-confound",
 ""),

("H-Q-027",
 "Can the Atlas distinguish between environments that are genuinely restorative and those that are merely preferred — and is that a theoretical distinction or an empirical one?",
 "Fails if it does not identify operational criteria distinguishing restoration from preference and does not say whether the Atlas's template system encodes this distinction.",
 "discovery", "field-map", "mechanistic",
 "P7-underdetermination-prober",
 "Assumes restoration and preference are separable constructs; tests whether the Atlas's taxonomy makes this distinction operational.",
 "panel", "Panel-A · scenario-card-restoration-vs-preference",
 ""),

("H-Q-028",
 "Is the evidence for thermal comfort effects on productivity underdetermined between a direct thermal-physiology account and an arousal-mediated attention account?",
 "Fails if it does not describe an experiment dissociating core body temperature change from arousal-mediated attention effects.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-underdetermination-prober",
 "Takes direct physiological and arousal-mediation accounts as distinct, with different implications for design intervention.",
 "mining", "template-thermal-underdetermination",
 ""),

("H-Q-029",
 "When the Atlas marks a warrant as 'converging', how does it handle the possibility that all converging studies inherit a shared theoretical assumption from the original paradigm?",
 "Fails if it does not describe the Atlas's procedure for flagging paradigm-level theoretical assumptions spanning a body of converging evidence.",
 "discovery", "field-map", "converging",
 "P7-underdetermination-prober",
 "Applies Lakatosian critique: convergence within a research programme does not confer cross-programme confirmation.",
 "panel", "Panel-C · scenario-card-atlas-epistemology",
 "Meta-question about the Atlas's own epistemic infrastructure."),

("H-Q-030",
 "In studies where nature exposure improves mood and reduces cognitive fatigue simultaneously, is it evidentially possible to determine which effect is primary — or are they jointly produced by a common cause?",
 "Fails if it does not describe a mediation-analysis design that could distinguish sequential vs. common-cause models and cite whether one exists.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P7-underdetermination-prober",
 "Treats mood-improvement and fatigue-recovery as potentially distinct outcomes with separate causal histories (not assuming tight coupling).",
 "cross-product", "IV:biophilia[nature-exposure] × DV:affect[mood] + DV:cog[fatigue] · common-cause corner",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 4 · P7-warrant-auditor  (H-Q-031 – H-Q-040)
# ──────────────────────────────────────────────────────────────────────────────
("H-Q-031",
 "What is the full Toulmin warrant structure of the Atlas's claim that 'high-complexity environments impair focused cognitive work'? Identify data, warrant, backing, qualifier, and rebuttal explicitly.",
 "Fails if the analysis conflates warrant with data or does not identify scope conditions (qualifier) that bound the claim.",
 "inquiry", "Toulmin", "mechanistic",
 "P7-warrant-auditor",
 "Applies Toulmin's argument structure as an analytic tool; treats every Atlas claim as having distinct backing and warrant components.",
 "panel", "Panel-C · scenario-card-warrant-audit-complexity",
 ""),

("H-Q-032",
 "In the Atlas's treatment of ART, what is the backing for the directed-attention-fatigue warrant — experimental evidence, neuroimaging, or theoretical stipulation?",
 "Fails if it does not distinguish empirical backing from stipulative backing and does not provide a citable source for the identified backing type.",
 "inquiry", "Toulmin", "mechanistic",
 "P7-warrant-auditor",
 "Draws the distinction between empirical warrant-backing and theoretical postulation as backing — a key epistemological distinction in Toulmin.",
 "panel", "Panel-A · scenario-card-ART-warrant-backing",
 ""),

("H-Q-033",
 "For the Atlas's claim about wood surfaces and stress reduction, what qualifier restricts the claim's generalisability — is the evidence limited to Japanese participants, to laboratory settings, or to both?",
 "Fails if it does not identify the specific population and setting restrictions and does not assess whether those restrictions are stated in the Atlas.",
 "information-seeking", "Toulmin", "converging",
 "P7-warrant-auditor",
 "Treats scope conditions as constitutive of a claim's epistemic content, not mere caveats to be mentioned and forgotten.",
 "mining", "template-material-wood-warrant-scope",
 ""),

("H-Q-034",
 "What is the rebuttal condition for the Atlas's claim that open-plan offices reduce spontaneous collaboration — is there a documented condition under which the effect reverses?",
 "Fails if it does not identify a published finding where open-plan increased collaboration and does not assess whether it meets the bar for a genuine Toulmin rebuttal.",
 "inquiry", "Toulmin", "converging",
 "P7-warrant-auditor",
 "Treats rebuttal conditions as empirical (requiring actual data), not just logical possibilities.",
 "panel", "Panel-C · scenario-card-open-plan-rebuttal",
 ""),

("H-Q-035",
 "For the claim that biophilic exposure reduces post-surgical opioid use, what is the qualifier — does it hold across surgical types, patient ages, and hospital settings, or is it restricted to the original narrow sample?",
 "Fails if it does not assess the Ulrich 1984 study's replication scope specifically and does not note whether later studies widened the qualifier.",
 "information-seeking", "Toulmin", "causal-with-mechanism",
 "P7-warrant-auditor",
 "Treats the Ulrich 1984 study as the anchor; question probes whether the qualifier has been empirically expanded across three decades.",
 "mining", "template-biophilia-opioid-warrant-scope",
 ""),

("H-Q-036",
 "Does the Atlas's warrant for ceiling-height effects on abstract thinking rest on a single experimental paradigm — and if so, what epistemically follows about its confidence level?",
 "Fails if it does not identify the paradigm dependency and does not give a principled account of why single-paradigm warrants carry reduced epistemic weight.",
 "inquiry", "Toulmin", "converging",
 "P7-warrant-auditor",
 "Applies a multiplism criterion: a claim's confidence depends on methodological diversity of its backing studies.",
 "panel", "Panel-B · scenario-card-ceiling-height-warrant-audit",
 ""),

("H-Q-037",
 "What is the logical form of the Atlas's claim that 'acoustic masking reduces distraction in open offices' — is it a universal, statistical, or dispositional generalisation, and does the Atlas mark this distinction?",
 "Fails if it does not identify the logical form of the generalisation and does not assess whether the Atlas's confidence tags encode the universal/statistical/dispositional distinction.",
 "discovery", "field-map", "mechanistic",
 "P7-warrant-auditor",
 "Draws the universal/statistical/dispositional distinction from the ceteris paribus laws literature as relevant to environmental psychology claims.",
 "panel", "Panel-C · scenario-card-masking-generalisation-form",
 ""),

("H-Q-038",
 "When the Atlas assigns 'measurement-grade' evidential demand to a circadian lighting claim, what specific psychometric or metrological criteria is it applying — and are those criteria stated?",
 "Fails if it does not identify specific measurement criteria (reliability, validity, calibration standard) being applied and does not assess whether they are stated or merely assumed.",
 "information-seeking", "field-map", "measurement-grade",
 "P7-warrant-auditor",
 "Treats 'measurement-grade' as a specific epistemological category requiring calibration against an independent standard, not merely 'high quality evidence'.",
 "mining", "template-circadian-measurement-warrant",
 ""),

("H-Q-039",
 "For the colour-temperature-and-mood claim, what backing does the Atlas provide for the warrant — neuroimaging, physiological measurement, self-report, or behavioural — and does the backing type affect the warrant's epistemic authority?",
 "Fails if it does not distinguish backing types and does not give a principled account of whether the type changes the warrant's epistemic status.",
 "inquiry", "Toulmin", "converging",
 "P7-warrant-auditor",
 "Applies an ordered hierarchy of backing types (neuroimaging > physiological > behavioural > self-report) — tests whether Atlas encodes this.",
 "cross-product", "IV:color[color-temperature] × DV:affect[mood] · warrant-backing corner",
 ""),

("H-Q-040",
 "Is the qualifier for the Atlas's acoustic-distraction-and-reading claim stated in a way that covers real-world classroom populations, or does it only licence the claim for laboratory participants doing phonological tasks?",
 "Fails if it does not specify population and task restrictions in the original studies and does not say whether those restrictions invalidate the Atlas's application to classroom design.",
 "inquiry", "Toulmin", "converging",
 "P7-warrant-auditor",
 "Treats ecological validity as a constitutive feature of warrant generalisability, not an optional annotation.",
 "mining", "template-sound-classroom-warrant-scope",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 5 · P7-critical-test-seeker  (H-Q-041 – H-Q-050)
# ──────────────────────────────────────────────────────────────────────────────
("H-Q-041",
 "What experimental design would definitively distinguish ART from SRT — what manipulation, what DV, and what result pattern would falsify one but not the other?",
 "Fails if it does not name a specific DV, a specific manipulation, and a specific result pattern — not just 'more research needed'.",
 "deliberation", "procedure", "causal-with-mechanism",
 "P7-critical-test-seeker",
 "Assumes both theories are falsifiable and empirically distinguishable, not merely semantic variants of the same claim.",
 "panel", "Panel-A · scenario-card-ART-SRT-critical-test",
 ""),

("H-Q-042",
 "What critical test would determine whether ceiling-height effects on abstract thinking are driven by cognitive construal or by embodied proprioceptive experience?",
 "Fails if it does not name a manipulation that dissociates construal from proprioception (e.g. virtual environment maintaining normal proprioception but altering perceived height).",
 "deliberation", "procedure", "causal-with-mechanism",
 "P7-critical-test-seeker",
 "Takes construal-level and embodied accounts as generating different predictions about virtual vs. physical manipulation.",
 "panel", "Panel-B · scenario-card-ceiling-critical-test",
 ""),

("H-Q-043",
 "What experiment would determine whether wood surfaces reduce stress via aesthetic preference or via a direct psychophysiological channel — and has anything close been run?",
 "Fails if it does not describe an experimental design controlling for preference while manipulating material identity independently, and does not report whether any such study exists.",
 "deliberation", "procedure", "mechanistic",
 "P7-critical-test-seeker",
 "Treats aesthetic preference and direct psychophysiology as distinguishable causal pathways requiring a dissociation design.",
 "mining", "template-material-wood-critical-test",
 ""),

("H-Q-044",
 "What study design would establish whether fractal preference is innate or learned — and does the cross-cultural fractal literature come anywhere near answering it?",
 "Fails if it does not describe what a developmental or cross-cultural design would need to control for and does not evaluate existing cross-cultural data against that standard.",
 "deliberation", "procedure", "causal-with-mechanism",
 "P7-critical-test-seeker",
 "Presupposes that innate and learned accounts make different developmental and cross-cultural predictions, testable in principle.",
 "panel", "Panel-A · scenario-card-fractal-innate-vs-learned",
 ""),

("H-Q-045",
 "What is the critical test between a colour-affect account based on evolutionary valence (red = danger) and one based on cultural conditioning — and does any study in the Atlas approach this design?",
 "Fails if it does not describe a specific test population (e.g. culturally isolated group with independent colour ecology) and does not evaluate any existing study against this criterion.",
 "deliberation", "procedure", "causal-with-mechanism",
 "P7-critical-test-seeker",
 "Takes evolutionary and cultural-conditioning accounts as making different cross-cultural predictions, in principle testable.",
 "mining", "template-color-evolutionary-vs-cultural-test",
 ""),

("H-Q-046",
 "What experiment would show whether the open-plan office distraction effect is driven by auditory interruption, social-monitoring anxiety, or loss of perceived control — and which is currently best-supported?",
 "Fails if it does not describe a factorial design separating the three candidate causes and does not name the current best-supported candidate with a citation.",
 "deliberation", "procedure", "causal-with-mechanism",
 "P7-critical-test-seeker",
 "Treats the three mechanisms as empirically distinguishable and not jointly necessary or sufficient.",
 "panel", "Panel-C · scenario-card-open-plan-critical-test",
 ""),

("H-Q-047",
 "What critical test would establish whether biophilic environments improve mood via positive affect induction or via stress-state reduction — and are these operationally the same thing?",
 "Fails if it does not identify whether positive affect induction and stress reduction are operationally distinguishable via opposing valence/arousal profiles and does not cite a study testing both.",
 "deliberation", "procedure", "causal-with-mechanism",
 "P7-critical-test-seeker",
 "Treats Fredrickson's broaden-and-build (positive affect) and Ulrich's SRT (stress reduction) as distinct causal pathways with different design implications.",
 "cross-product", "IV:biophilia[nature-exposure] × DV:affect[positive-affect] vs DV:affect[stress-reduction] · critical-test corner",
 ""),

("H-Q-048",
 "What experimental design would falsify the prediction that circadian lighting protocols improve hospital patient outcomes — and is the absence of such a design a sign of paradigm entrenchment?",
 "Fails if it does not describe a pre-registered null-hypothesis study with adequate power and does not assess whether any adversarial study has been run.",
 "deliberation", "procedure", "measurement-grade",
 "P7-critical-test-seeker",
 "Applies Popperian falsificationism as a diagnostic; probes whether the circadian-design community is generating genuinely risky predictions.",
 "panel", "Panel-A · scenario-card-circadian-falsification",
 ""),

("H-Q-049",
 "What is the Duhem-Quine problem for the WELL building standard — which auxiliary assumptions could be revised to protect core circadian or cognitive claims from disconfirmation?",
 "Fails if it does not identify at least two specific auxiliary assumptions in WELL that could absorb a disconfirmatory finding and does not assess whether WELL's revision history shows this pattern.",
 "discovery", "field-map", "mechanistic",
 "P7-critical-test-seeker",
 "Applies the Duhem-Quine thesis explicitly: any design standard embeds auxiliary assumptions, and disconfirmation is always deflectable.",
 "panel", "Panel-C · scenario-card-WELL-Duhem-Quine",
 "A uniquely Hanif question — no other persona would frame a design standard through Duhem-Quine."),

("H-Q-050",
 "In the restorative-environment literature, has any study been designed to fail — i.e., to test a condition where ART or SRT would predict no effect but an alternative account would predict an effect?",
 "Fails if it does not identify at least one adversarial study design from the literature and does not assess whether its null result was published or suppressed.",
 "discovery", "field-map", "causal-with-mechanism",
 "P7-critical-test-seeker",
 "Treats adversarial design as a methodological value criterion; questions whether the field's design culture is confirmatory-biased.",
 "panel", "Panel-A · scenario-card-adversarial-restoration",
 "Closing epistemological question — about the field's culture, not just any single claim."),
]

# ── workbook build ─────────────────────────────────────────────────────────────
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "P7-Hanif-Corpus"

col_widths = [10, 62, 57, 22, 20, 24, 26, 57, 16, 52, 45]
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws.row_dimensions[1].height = 30
for col_idx, hdr in enumerate(HEADERS, 1):
    cell = ws.cell(row=1, column=col_idx, value=hdr)
    cell.fill      = hdr_fill(INDIGO_DARK)
    cell.font      = Font(bold=True, color=WHITE, size=11)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border    = thin_border()

subflavour_map = {
    2:  "① MECHANISM-TRACER — Trace the full causal chain; find where it breaks down",
    13: "② RIVAL-THEORIST — How do competing accounts explain the same effect?",
    24: "③ UNDERDETERMINATION-PROBER — Can the evidence actually adjudicate between rivals?",
    35: "④ WARRANT-AUDITOR — What is the logical structure of this Atlas claim?",
    46: "⑤ CRITICAL-TEST-SEEKER — What experiment would falsify one account but not the other?",
}

current_data_row = 2
for r_idx, row_data in enumerate(rows):
    if current_data_row in subflavour_map:
        ws.row_dimensions[current_data_row].height = 22
        label_cell = ws.cell(row=current_data_row, column=1,
                             value=subflavour_map[current_data_row])
        label_cell.fill      = hdr_fill(INDIGO_MID)
        label_cell.font      = Font(bold=True, color=WHITE, size=10)
        label_cell.alignment = Alignment(vertical="center")
        label_cell.border    = thin_border()
        ws.merge_cells(start_row=current_data_row, start_column=1,
                       end_row=current_data_row, end_column=len(HEADERS))
        current_data_row += 1

    fill_color = LAVENDER_LIGHT if (r_idx % 2 == 0) else AMBER
    ws.row_dimensions[current_data_row].height = 90

    for col_idx, value in enumerate(row_data, 1):
        cell = ws.cell(row=current_data_row, column=col_idx, value=value)
        cell.fill      = hdr_fill(fill_color)
        cell.border    = thin_border()
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.font      = Font(bold=(col_idx == 1), size=10)

    current_data_row += 1

ws.freeze_panes = "C2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(HEADERS))}1"

out_path = "/sessions/confident-magical-goldberg/mnt/outputs/P7_Hanif_Raza_Question_Corpus.xlsx"
wb.save(out_path)
print(f"Saved → {out_path}")
print(f"Total question rows: {len(rows)}")
