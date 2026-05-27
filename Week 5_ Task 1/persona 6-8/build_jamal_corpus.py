import openpyxl
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side, GradientFill
)
from openpyxl.utils import get_column_letter

# ── colour palette ────────────────────────────────────────────────────────────
TEAL_DARK   = "1B6B6B"   # header bg
TEAL_MID    = "2E9E9E"   # sub-flavour header bg
TEAL_LIGHT  = "D6F0F0"   # alternating row A
WHITE       = "FFFFFF"
AMBER       = "FFF3CD"   # alternating row B
GOLD        = "B8860B"   # sub-flavour label font
BLACK       = "000000"

# ── helpers ───────────────────────────────────────────────────────────────────
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

# ── question data ─────────────────────────────────────────────────────────────
# Each tuple: (id, question, adequacy_condition, cognitive_purpose,
#              answer_shape, evidential_demand, persona_fit,
#              theoretical_commitment, source, provenance, notes)

rows = [
# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 1 · P6-space-designer  (J-Q-001 – J-Q-010)
# ──────────────────────────────────────────────────────────────────────────────
("J-Q-001",
 "What ceiling height should I specify for a hospital patient recovery room to reduce anxiety and support healing?",
 "Fails if it does not give a specific dimension range and at least one citation testing ceiling height in a healthcare (not office) context.",
 "information-seeking", "ranked-brief", "converging",
 "P6-space-designer",
 "Assumes ceiling height has a direct psycho-physiological effect on anxiety (Meyers-Levy construal-level framework).",
 "panel", "Panel-A · scenario-card-healthcare-inpatient",
 "Healthcare inpatient room; evidence-based design pitch context."),

("J-Q-002",
 "In a university classroom, does daylight on the left wall vs. the right wall matter for student attention?",
 "Fails if it does not distinguish unilateral from bilateral daylighting and cite at least one classroom study.",
 "inquiry", "contrast-pair", "suggestive",
 "P6-space-designer",
 "Presupposes directional lighting asymmetry affects attention; no strong prior theory committed.",
 "panel", "Panel-B · scenario-card-higher-ed-classroom",
 "Higher-ed classroom fit-out; orientation decision mid-SD."),

("J-Q-003",
 "For a hospital waiting room, what window-to-wall ratio does the research recommend to reduce patient-reported stress?",
 "Fails if it cites only office or residential studies and does not include a healthcare-context finding.",
 "information-seeking", "ranked-brief", "converging",
 "P6-space-designer",
 "Assumes visual access to outdoors reduces stress via ART or Ulrich SRT framework.",
 "mining", "template-biophilia-visual-access",
 ""),

("J-Q-004",
 "What STC rating between patient rooms prevents sleep disruption from corridor noise in a hospital?",
 "Fails if it gives an STC value without a study linking that threshold to sleep outcomes in a clinical setting.",
 "information-seeking", "procedure", "measurement-grade",
 "P6-space-designer",
 "Assumes acoustic separation is monotonically beneficial; does not engage with alarm-masking trade-offs.",
 "panel", "Panel-A · scenario-card-healthcare-inpatient",
 ""),

("J-Q-005",
 "What mix of enclosed vs. open seating in a student union supports both focused work and social interaction?",
 "Fails if it does not distinguish work type (individual vs. collaborative) or does not cite evidence from college-age users.",
 "deliberation", "contrast-pair", "converging",
 "P6-space-designer",
 "Assumes spatial segmentation mediates behavioural affordances (Gibson-style affordance theory).",
 "panel", "Panel-B · scenario-card-higher-ed-student-union",
 ""),

("J-Q-006",
 "Does wayfinding clarity in an outpatient clinic corridor affect patient anxiety — and is signage or spatial layout the more powerful lever?",
 "Fails if it does not compare wayfinding interventions (signage vs. spatial) with a clinical anxiety-outcome measure.",
 "deliberation", "contrast-pair", "mechanistic",
 "P6-space-designer",
 "Assumes wayfinding stress is separable from ambient environmental stress.",
 "cross-product", "IV:spatial[wayfinding-clarity] × DV:affect[anxiety] · low/low corner",
 ""),

("J-Q-007",
 "How much private office vs. open-plan should a research-lab building include to support both deep work and serendipitous collaboration?",
 "Fails if it does not name a ratio or range or does not distinguish disciplines (wet lab vs. computational).",
 "deliberation", "ranked-brief", "converging",
 "P6-space-designer",
 "Assumes spatial layout mediates cognitive performance and social interaction independently.",
 "panel", "Panel-C · scenario-card-research-facility",
 ""),

("J-Q-008",
 "For a pediatric oncology unit, what is the evidence for biophilic elements — plants, water features, natural materials — in reducing child-patient distress?",
 "Fails if it does not address the pediatric population specifically and conflates adult-stress proxies with child-distress outcomes.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P6-space-designer",
 "Assumes biophilic features trigger stress reduction via ANS pathway (Ulrich SRT).",
 "mining", "template-biophilia-stress-recovery",
 ""),

("J-Q-009",
 "Does resilient flooring in a hospital ICU actually reduce falls-per-unit, or is that a myth?",
 "Fails if it does not report both acoustic attenuation AND fall-outcome data together in a clinical setting.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P6-space-designer",
 "Assumes material hardness is the key variable; may not engage with footwear confound.",
 "panel", "Panel-A · scenario-card-healthcare-safety",
 ""),

("J-Q-010",
 "We are retrofitting a 1970s university library into a hybrid learning commons — what does the evidence say about lighting levels for sustained reading vs. collaborative work?",
 "Fails if it gives only one lux figure and does not differentiate by task type or user age.",
 "information-seeking", "contrast-pair", "measurement-grade",
 "P6-space-designer",
 "Assumes illuminance is the primary lighting variable; does not engage with spectrum or directionality.",
 "cross-product", "IV:color[lighting-level] × DV:cog[sustained-attention] · high/high corner",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 2 · P6-client-briefer  (J-Q-011 – J-Q-020)
# ──────────────────────────────────────────────────────────────────────────────
("J-Q-011",
 "I need to justify full-spectrum LED lighting over standard warm LED to a hospital client — what is the one-paragraph scientific case?",
 "Fails if it does not include a citable clinical study and does not name a measurable outcome the client will care about (sleep, mood, or recovery time).",
 "persuasion", "Toulmin", "converging",
 "P6-client-briefer",
 "Assumes circadian-rhythm disruption is the mechanism; client may be sceptical of circadian science.",
 "panel", "Panel-A · scenario-card-client-brief-lighting",
 ""),

("J-Q-012",
 "My higher-ed client is pushing back on the cost of acoustic treatment in classrooms — what does research say about learning outcomes vs. noise?",
 "Fails if it does not give an outcome (test scores, comprehension) with an effect size and does not mention a cost-per-student framing.",
 "persuasion", "Toulmin", "causal-with-mechanism",
 "P6-client-briefer",
 "Presupposes speech intelligibility is the bottleneck; does not engage with teacher-adaptation strategies.",
 "panel", "Panel-B · scenario-card-client-brief-acoustics",
 ""),

("J-Q-013",
 "The client wants to cut the courtyard from the hospital design for budget — what evidence can I show them about nature views and patient outcomes?",
 "Fails if it relies only on Ulrich 1984 and does not include more recent evidence from clinical settings beyond general surgery.",
 "persuasion", "ranked-brief", "converging",
 "P6-client-briefer",
 "Assumes nature views directly affect recovery (SRT/ART); does not distinguish mechanism.",
 "mining", "template-biophilia-visual-access-clinical",
 "Classic Ulrich study insufficient on its own; needs replication chain."),

("J-Q-014",
 "What ROI argument can I make to a university client for investing in high-quality daylighting in a new classroom building?",
 "Fails if it does not translate research into a financial proxy (energy + performance + retention) and cite at least one education-sector study.",
 "persuasion", "Toulmin", "converging",
 "P6-client-briefer",
 "Assumes daylighting benefits are robust enough to survive a cost-benefit argument; may not engage with glare trade-offs.",
 "panel", "Panel-B · scenario-card-client-brief-daylighting",
 ""),

("J-Q-015",
 "My healthcare client wants high-stimulation art in patient rooms — what is the science on whether that helps, is neutral, or harms recovery?",
 "Fails if it does not distinguish art types (abstract vs. representational, high-contrast vs. muted) or does not address patient-population specifics.",
 "inquiry", "contrast-pair", "converging",
 "P6-client-briefer",
 "Assumes visual complexity is the active variable in art-as-intervention.",
 "mining", "template-complexity-visual-arousal",
 ""),

("J-Q-016",
 "I am writing the evidence-based design narrative for a student wellness centre — what is the strongest three-sentence scientific case for biophilic elements?",
 "Fails if it does not offer citable claims with specific effects and does not distinguish cosmetic from functional biophilia.",
 "persuasion", "ranked-brief", "converging",
 "P6-client-briefer",
 "Assumes biophilic elements have separable, stackable effects (additive model).",
 "panel", "Panel-C · scenario-card-wellness-centre",
 ""),

("J-Q-017",
 "A hospital board is debating single-patient vs. double-occupancy rooms — what does the evidence say about infection rates AND patient satisfaction together?",
 "Fails if it reports infection and satisfaction separately without noting whether the trade-off has been studied in the same facilities.",
 "deliberation", "contrast-pair", "converging",
 "P6-client-briefer",
 "Assumes room configuration is the primary infection vector; may not engage with HVAC or staffing flow.",
 "panel", "Panel-A · scenario-card-room-configuration",
 ""),

("J-Q-018",
 "Can I claim our evidence-based design process reduces patient falls by X%? What is the honest range I can put in a marketing document?",
 "Fails if it does not give a range with confidence bounds and does not flag confounds (staffing, patient acuity) that make point estimates dishonest.",
 "persuasion", "Toulmin", "measurement-grade",
 "P6-client-briefer",
 "Assumes design is an isolable cause of fall rates; ignores operational confounds.",
 "panel", "Panel-A · scenario-card-marketing-claims",
 ""),

("J-Q-019",
 "My university client wants a case study showing good design improves student retention — does that literature exist, and is it credible?",
 "Fails if it confirms the literature without flagging selection bias (well-funded schools both build better and retain better).",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P6-client-briefer",
 "Assumes retention is separable from campus-quality signalling effect.",
 "cross-product", "IV:spatial[campus-design-quality] × DV:behav[enrollment-retention] · high/high corner",
 ""),

("J-Q-020",
 "Our firm's sustainability narrative claims biophilic elements reduce employee sick days — is that defensible, or is it overreach?",
 "Fails if it does not address absenteeism specifically and does not flag publication bias in the wellness-design literature.",
 "persuasion", "Toulmin", "causal-with-mechanism",
 "P6-client-briefer",
 "Assumes indoor environment quality directly mediates sick-building-syndrome outcomes.",
 "panel", "Panel-C · scenario-card-wellness-claims",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 3 · P6-evidence-checker  (J-Q-021 – J-Q-030)
# ──────────────────────────────────────────────────────────────────────────────
("J-Q-021",
 "Is there actually solid evidence that open-plan offices hurt productivity, or is that just trade-press lore?",
 "Fails if it does not distinguish open-plan types (activity-based vs. bullpen), cognitive work types, and primary research from secondary commentary.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P6-evidence-checker",
 "Assumes distraction is the primary mechanism; does not engage with social-facilitation as a confound.",
 "panel", "Panel-C · scenario-card-open-plan-sceptic",
 ""),

("J-Q-022",
 "We have been specifying terrazzo flooring in hospital lobbies for cleanability — is there any evidence it affects patient wayfinding or fall risk?",
 "Fails if it does not address contrast sensitivity at floor-wall interfaces and cite slip-resistance standards in clinical settings.",
 "information-seeking", "field-map", "suggestive",
 "P6-evidence-checker",
 "Assumes material properties have effects on safety independent of operational protocols.",
 "panel", "Panel-A · scenario-card-material-selection",
 ""),

("J-Q-023",
 "Is the 'green walls improve indoor air quality' claim actually supported — should I specify them for healthcare or is it marketing?",
 "Fails if it does not give VOC-reduction data (m³/h, plant density) and does not distinguish living walls from artificial plant walls.",
 "inquiry", "Toulmin", "mechanistic",
 "P6-evidence-checker",
 "Assumes phytoremediation is the active mechanism; does not engage with VOC production from plant substrate.",
 "mining", "template-biophilia-air-quality",
 ""),

("J-Q-024",
 "Does the evidence support circadian lighting protocols in hospital design, or are effect sizes too small to justify the cost premium?",
 "Fails if it does not give an effect size, a cost context, and a clinical outcome (sleep quality or delirium rates).",
 "deliberation", "contrast-pair", "causal-with-mechanism",
 "P6-evidence-checker",
 "Assumes circadian entrainment is the dominant mechanism for lighting effects in clinical populations.",
 "panel", "Panel-A · scenario-card-circadian-lighting",
 ""),

("J-Q-025",
 "I keep seeing 'resimercial' design cited as evidence-based for higher-ed — what is the actual research behind it, if any?",
 "Fails if it validates or dismisses without distinguishing which residential-style elements have been separately empirically tested.",
 "discovery", "field-map", "suggestive",
 "P6-evidence-checker",
 "Assumes style proxies for environmental-psychology constructs (comfort, perceived control).",
 "panel", "Panel-B · scenario-card-design-trend-check",
 ""),

("J-Q-026",
 "Colleagues recommend 'trauma-informed design' for our behavioural health unit — is that a clinical evidence base or a framework without data?",
 "Fails if it does not distinguish features with RCT or quasi-experimental support from those supported only by expert consensus or case reports.",
 "inquiry", "Toulmin", "converging",
 "P6-evidence-checker",
 "Assumes clinical trauma framework can be directly translated to spatial interventions.",
 "panel", "Panel-A · scenario-card-behavioural-health",
 ""),

("J-Q-027",
 "Does thermal comfort in classrooms measurably affect student test scores, or is this a correlation study that has not been replicated?",
 "Fails if it does not report replication status and does not note confounding variables (SES, teacher quality) in the stronger studies.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P6-evidence-checker",
 "Assumes thermal comfort is causally prior to cognitive performance (not mediated by arousal or motivation).",
 "mining", "template-thermal-cognitive-performance",
 ""),

("J-Q-028",
 "Is the evidence for acoustic comfort in libraries strong enough to justify sound-masking systems, or do they create more problems than they solve?",
 "Fails if it does not address speech-privacy vs. ambient-noise masking separately and does not cite a library (not office) study.",
 "deliberation", "contrast-pair", "converging",
 "P6-evidence-checker",
 "Assumes speech intelligibility is the key distraction mechanism in a library context.",
 "cross-product", "IV:sound[sound-masking] × DV:cog[distraction-resistance] · low/high corner",
 ""),

("J-Q-029",
 "Is the claim that wood surfaces reduce physiological stress substantiated, or is it an aesthetic preference dressed up as evidence?",
 "Fails if it does not cite a physiological stress measure (cortisol, HRV) specifically and does not distinguish solid timber from veneer or laminate.",
 "inquiry", "Toulmin", "mechanistic",
 "P6-evidence-checker",
 "Assumes material authenticity matters to psychophysiological response, not just appearance.",
 "mining", "template-material-wood-stress",
 ""),

("J-Q-030",
 "The WELL standard recommends specific view distances from workstations — is that derived from empirical research or from expert opinion?",
 "Fails if it does not identify the specific studies WELL cites for that parameter and evaluate their methodological quality.",
 "information-seeking", "field-map", "measurement-grade",
 "P6-evidence-checker",
 "Assumes WELL parameters are evidence-based rather than precautionary guidelines.",
 "panel", "Panel-C · scenario-card-standard-audit",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 4 · P6-spec-translator  (J-Q-031 – J-Q-040)
# ──────────────────────────────────────────────────────────────────────────────
("J-Q-031",
 "For a lecture hall designed for student attention, what is the maximum recommended RT60 and what acoustic treatment achieves it?",
 "Fails if it gives an RT60 value without a surface-treatment recommendation or does not cite a standard (ANSI S12.60 or equivalent).",
 "information-seeking", "procedure", "measurement-grade",
 "P6-spec-translator",
 "Assumes reverberation time is the primary acoustic variable for speech intelligibility.",
 "panel", "Panel-B · scenario-card-lecture-hall-acoustics",
 ""),

("J-Q-032",
 "What minimum illuminance (lux) should I specify for a hospital corridor to support safe night-time navigation without disrupting patient circadian rhythms?",
 "Fails if it does not give two lux levels (day vs. night) and does not cite a clinical study rather than general building code.",
 "information-seeking", "ranked-brief", "measurement-grade",
 "P6-spec-translator",
 "Assumes nighttime circadian disruption is the dominant harm; treats visual safety as a separate spec problem.",
 "mining", "template-circadian-lighting-clinical",
 ""),

("J-Q-033",
 "For a healthcare environment, what colour-temperature range (Kelvin) improves patient alertness during the day without inducing anxiety?",
 "Fails if it gives a single CCT value without a daytime/nighttime range and does not cite a healthcare-specific study.",
 "information-seeking", "procedure", "converging",
 "P6-spec-translator",
 "Assumes CCT is linearly related to arousal and anxiety; ignores individual variation.",
 "cross-product", "IV:color[color-temperature] × DV:affect[arousal-valence] · low/high corner",
 ""),

("J-Q-034",
 "What window-sill height in a hospital patient room gives a bed-bound patient a sufficient nature view — is there a research-based spec?",
 "Fails if it does not translate a view-angle calculation into a sill-height range based on bed/eye-level ergonomics.",
 "information-seeking", "procedure", "converging",
 "P6-spec-translator",
 "Assumes view content (nature vs. urban) is primary and sill height is purely instrumental.",
 "panel", "Panel-A · scenario-card-patient-room-view",
 ""),

("J-Q-035",
 "For a university study carrel, what evidence-based spec covers task-lighting illuminance, colour rendering (Ra), and directionality?",
 "Fails if it does not give Ra (CRI) and CCT alongside lux and does not address vertical vs. horizontal illuminance distinction.",
 "information-seeking", "procedure", "measurement-grade",
 "P6-spec-translator",
 "Assumes task lighting can be specified independently of ambient lighting.",
 "cross-product", "IV:color[task-lighting-quality] × DV:cog[reading-performance] · high/high corner",
 ""),

("J-Q-036",
 "We need glazing spec for a behavioural-health waiting room — what VLT balances daylight benefit against perceived privacy?",
 "Fails if it does not cite both a daylight study and a perceived-privacy study, and relies only on glazing product data.",
 "deliberation", "contrast-pair", "converging",
 "P6-spec-translator",
 "Assumes visual privacy and daylight are the two dominant competing variables; ignores acoustic privacy.",
 "panel", "Panel-A · scenario-card-behavioural-health-glazing",
 ""),

("J-Q-037",
 "Is there a minimum ceiling height for open-plan collaborative spaces that affects social comfort, and if so what is it?",
 "Fails if it gives a height without linking it to a study measuring social comfort specifically — not just spaciousness preference.",
 "information-seeking", "ranked-brief", "suggestive",
 "P6-spec-translator",
 "Assumes ceiling height has direct social effects independent of floor area (extension of Meyers-Levy construal framework).",
 "mining", "template-spatial-ceiling-height",
 ""),

("J-Q-038",
 "What outdoor surface-temperature limits should I specify for a hospital courtyard in a hot climate — is there evidence patients are harmed by radiant heat?",
 "Fails if it only cites ASHRAE thermal comfort standards without addressing patient vulnerability or clinical outcomes in outdoor hospital spaces.",
 "information-seeking", "procedure", "converging",
 "P6-spec-translator",
 "Assumes ASHRAE comfort model applies to immunocompromised patients (may not).",
 "cross-product", "IV:material[thermal-mass] × DV:physio[thermal-comfort] · high/low corner",
 ""),

("J-Q-039",
 "What CO2 concentration threshold in a health-science campus classroom corresponds to measurable cognitive decrements, and how does that translate into a ventilation-rate spec?",
 "Fails if it does not link a ppm threshold to a cognitive outcome measure and does not map that threshold to ACH or L/s/person.",
 "information-seeking", "procedure", "causal-with-mechanism",
 "P6-spec-translator",
 "Assumes CO2 is the active IAQ variable, not a proxy for other pollutants.",
 "mining", "template-IAQ-CO2-cognition",
 ""),

("J-Q-040",
 "What floor-to-ceiling glazing percentage in a hospital patient room maximises nature-view benefit without creating thermal discomfort or glare?",
 "Fails if it does not address the three-way trade-off (view, thermal, glare) with at least one study for each dimension.",
 "deliberation", "contrast-pair", "converging",
 "P6-spec-translator",
 "Assumes an optimal glazing percentage is calculable as a single figure rather than a climate-specific range.",
 "cross-product", "IV:spatial[window-to-wall-ratio] × DV:health[stress-recovery] · high/high corner",
 ""),

# ──────────────────────────────────────────────────────────────────────────────
# SUB-FLAVOUR 5 · P6-quick-lookup  (J-Q-041 – J-Q-050)
# ──────────────────────────────────────────────────────────────────────────────
("J-Q-041",
 "Quick — what is the research-backed noise-level recommendation for a hospital NICU to protect infant hearing and neurodevelopment?",
 "Fails if it does not give a dB(A) limit from a clinical guideline and does not name the outcome measure (hearing, neurological development, or length of stay).",
 "information-seeking", "ranked-brief", "measurement-grade",
 "P6-quick-lookup",
 "Assumes noise is the primary NICU environmental stressor; does not engage with light confound.",
 "panel", "Panel-A · scenario-card-NICU-quick",
 "Fast-lookup scenario; one paragraph answer expected."),

("J-Q-042",
 "I have two minutes before a client call — what is the one-liner on whether sit-stand desks improve cognitive productivity?",
 "Fails if it does not give a qualified yes/no with one citation and does not flag the task type (cognitive vs. physical) the result applies to.",
 "information-seeking", "ranked-brief", "converging",
 "P6-quick-lookup",
 "Assumes productivity is measurable and linearly affected by posture changes.",
 "panel", "Panel-C · scenario-card-quick-desk",
 ""),

("J-Q-043",
 "What does research say about single-loaded vs. double-loaded corridors for patient ambulation in hospital rehab units?",
 "Fails if it does not cite a study measuring steps or distance walked per day in a rehab setting — not just staff preference.",
 "inquiry", "contrast-pair", "mechanistic",
 "P6-quick-lookup",
 "Assumes corridor configuration directly mediates ambulatory behaviour (not just incentive or signalling).",
 "panel", "Panel-A · scenario-card-rehab-corridor",
 ""),

("J-Q-044",
 "Does the colour of a patient room wall affect mood or pain perception — is blue better than beige?",
 "Fails if it gives a colour recommendation without specifying hue, saturation, and value separately and without a pain or mood outcome in a clinical setting.",
 "information-seeking", "contrast-pair", "converging",
 "P6-quick-lookup",
 "Assumes hue is the primary variable; does not engage with lightness or chroma as independent effects.",
 "mining", "template-color-affect-clinical",
 ""),

("J-Q-045",
 "Is there solid evidence that biophilic features in a hospital reduce post-surgical opioid requirements, or is that cherry-picked from one study?",
 "Fails if it does not assess replication of the Ulrich 1984 finding and does not flag that modern pain-management protocols differ substantially.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P6-quick-lookup",
 "Assumes biophilic exposure has a direct analgesic effect (SRT); does not engage with placebo or expectation confound.",
 "panel", "Panel-A · scenario-card-pain-analgesia",
 ""),

("J-Q-046",
 "What visual complexity level — roughly what fractal dimension — do patients find most restorative in a healthcare waiting area?",
 "Fails if it does not give a fractal-dimension range (e.g. D ~1.3–1.5) and does not cite a healthcare or clinical-adjacent study.",
 "information-seeking", "ranked-brief", "converging",
 "P6-quick-lookup",
 "Assumes fractal complexity is the operative variable in perceived restorativeness (Taylor complexity model).",
 "cross-product", "IV:complexity[fractal-dimension] × DV:affect[perceived-restorativeness] · high/high corner",
 ""),

("J-Q-047",
 "Does providing outdoor views from a classroom improve student attendance or behaviour beyond academic performance effects?",
 "Fails if it conflates academic performance with behavioural outcomes and does not distinguish chronic absence from short-term engagement.",
 "inquiry", "Toulmin", "causal-with-mechanism",
 "P6-quick-lookup",
 "Assumes nature views reduce fatigue which mediates both performance and behavioural outcomes (ART pathway).",
 "cross-product", "IV:biophilia[nature-view] × DV:behav[attendance] · low/high corner",
 ""),

("J-Q-048",
 "For a student mental health clinic, what level of visual privacy in the waiting room is recommended — partial screening or full enclosure?",
 "Fails if it does not cite perceived stigma as the mechanism and does not address whether acoustic privacy is independent of visual privacy in the evidence.",
 "deliberation", "contrast-pair", "suggestive",
 "P6-quick-lookup",
 "Assumes visual privacy is the primary stigma-reduction variable; does not engage with acoustic or social-proximity confounds.",
 "panel", "Panel-B · scenario-card-mental-health-waiting",
 ""),

("J-Q-049",
 "Can I specify a Munsell lightness range for ICU walls that optimises both nurse visual acuity and patient perceived calm?",
 "Fails if it does not address the nurse vs. patient trade-off explicitly and does not cite a study measuring both outcomes.",
 "deliberation", "contrast-pair", "measurement-grade",
 "P6-quick-lookup",
 "Assumes nurse visual performance and patient affect are independently optimisable via the same surface specification.",
 "cross-product", "IV:color[wall-lightness] × DV:cog[visual-acuity] + DV:affect[calm] · high/low corner",
 ""),

("J-Q-050",
 "What does the science say about minimum corridor width in emergency departments for patient throughput — is there a threshold that improves flow without a full redesign?",
 "Fails if it gives a width without a simulation or observational study in an ED context and does not note patient acuity as a moderator.",
 "information-seeking", "procedure", "converging",
 "P6-quick-lookup",
 "Assumes spatial dimension directly mediates throughput; ignores staffing and triage-protocol confounds.",
 "panel", "Panel-A · scenario-card-ED-flow",
 ""),
]

# ── workbook build ─────────────────────────────────────────────────────────────
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "P6-Jamal-Corpus"

# column widths
col_widths = [10, 60, 55, 22, 20, 24, 22, 55, 16, 50, 40]
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

# ── header row ────────────────────────────────────────────────────────────────
ws.row_dimensions[1].height = 30
for col_idx, hdr in enumerate(HEADERS, 1):
    cell = ws.cell(row=1, column=col_idx, value=hdr)
    cell.fill        = hdr_fill(TEAL_DARK)
    cell.font        = Font(bold=True, color=WHITE, size=11)
    cell.alignment   = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border      = thin_border()

# sub-flavour label positions (row index in spreadsheet, 1-based data rows start at 2)
subflavour_map = {
    2:  "① SPACE-DESIGNER  — What should I do for this specific space type?",
    12: "② CLIENT-BRIEFER  — What is the scientific case I can put in front of a client?",
    22: "③ EVIDENCE-CHECKER — Does this design decision have real backing?",
    32: "④ SPEC-TRANSLATOR — How do I turn research findings into buildable specs?",
    42: "⑤ QUICK-LOOKUP  — One-paragraph answer needed right now.",
}

current_data_row = 2
for r_idx, row_data in enumerate(rows):
    # insert sub-flavour divider row if needed
    if current_data_row in subflavour_map:
        ws.row_dimensions[current_data_row].height = 22
        label_cell = ws.cell(row=current_data_row, column=1, value=subflavour_map[current_data_row])
        label_cell.fill      = hdr_fill(TEAL_MID)
        label_cell.font      = Font(bold=True, color=WHITE, size=10)
        label_cell.alignment = Alignment(vertical="center")
        label_cell.border    = thin_border()
        ws.merge_cells(start_row=current_data_row, start_column=1,
                       end_row=current_data_row, end_column=len(HEADERS))
        current_data_row += 1

    # alternating fill
    fill_color = TEAL_LIGHT if (r_idx % 2 == 0) else AMBER
    ws.row_dimensions[current_data_row].height = 80

    for col_idx, value in enumerate(row_data, 1):
        cell = ws.cell(row=current_data_row, column=col_idx, value=value)
        cell.fill      = hdr_fill(fill_color)
        cell.border    = thin_border()
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        # bold the id and question columns
        if col_idx in (1, 2):
            cell.font = Font(bold=(col_idx == 1), size=10)
        else:
            cell.font = Font(size=10)

    current_data_row += 1

# ── freeze panes ──────────────────────────────────────────────────────────────
ws.freeze_panes = "C2"

# ── auto-filter ───────────────────────────────────────────────────────────────
ws.auto_filter.ref = f"A1:{get_column_letter(len(HEADERS))}1"

# ── save ─────────────────────────────────────────────────────────────────────
out_path = "/sessions/confident-magical-goldberg/mnt/outputs/P6_Jamal_Washington_Question_Corpus.xlsx"
wb.save(out_path)
print(f"Saved → {out_path}")
print(f"Total question rows: {len(rows)}")
