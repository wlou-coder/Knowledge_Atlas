# Use Cases & User Journeys — P6 · Jamal Washington · Licensed Architect
## Track 4, Task 1 · COGS 160 Spring 2026 · Date: 2026-05-07

---

# PART I — USE CASES

---

## UC-P6-01 · Quick Spec Lookup — Space Designer

| Field | Value |
|-------|-------|
| **Actor** | P6 · Jamal Washington |
| **Sub-flavour** | P6-space-designer |
| **Corpus anchor** | J-Q-001 |
| **Goal** | Obtain an evidence-backed ceiling height specification for a hospital patient recovery room |
| **Trigger** | Structural engineer needs a ceiling height decision within 48 hours; Jamal has no literature on hand |
| **Entry workflow** | `design-decision` on `ka_home_practitioner.html` |
| **Expected answer shape** | ranked-brief |

**Preconditions**
- Jamal is in schematic design phase; space type is confirmed as Healthcare / inpatient recovery room
- He has navigated to `ka_home_practitioner.html` via the practitioner portal

**Main Success Scenario**
1. Jamal types "ceiling height hospital recovery room" into the `design-decision` search bar
2. System returns the **Ceiling Height** construct under the Spatial domain, with a sub-match on "healthcare inpatient" context
3. Practitioner summary card displays: recommended height range with an anxiety-reduction note and two clinical citations
4. Jamal expands the evidence tray: verifies that at least one study was conducted in a clinical (not laboratory) setting
5. Jamal copies the range and citations into his SD documentation in Bluebeam
6. Optionally triggers client-ready export as a one-page PDF card

**Extensions**
- 3a. Summary card shows only laboratory or office-setting evidence → Jamal expands evidence tray, notes the clinical-applicability gap, flags the decision as "professional judgment with partial evidence"
- 4a. Evidence tray shows only one study → system displays a thin-evidence indicator; Jamal treats as suggestive rather than converging and adds a caveat to his specification note
- 6a. Client-ready export is unavailable → Jamal manually pastes summary into a Bluebeam markup callout

**Postconditions**
- Jamal has a documentable specification decision with traceable citations
- Decision is defensible in a client meeting or peer review within 24 hours

**Adequacy condition (J-Q-001):** Fails if the answer does not give a specific dimension range and at least one citation from a healthcare (not office) context.

---

## UC-P6-02 · Pre-Meeting Client Brief — Client Briefer

| Field | Value |
|-------|-------|
| **Actor** | P6 · Jamal Washington |
| **Sub-flavour** | P6-client-briefer |
| **Corpus anchor** | J-Q-012 |
| **Goal** | Build a one-paragraph scientific case to justify acoustic treatment investment to a cost-conscious university client |
| **Trigger** | Client has pushed back on acoustic treatment line item; Jamal has a call in 20 minutes |
| **Entry workflow** | `client-brief` on `ka_home_practitioner.html` |
| **Expected answer shape** | Toulmin |

**Preconditions**
- Project type: Higher-education / classroom building
- Client is sceptical of the cost premium; Jamal needs a citable ROI framing
- He has 15–20 minutes before the call

**Main Success Scenario**
1. Jamal enters the `client-brief` workflow; selects space type: Educational / Classroom
2. Types "acoustic treatment classroom learning outcomes"
3. System returns a Toulmin-structured summary: claim (acoustic treatment improves comprehension), data (effect-size range from X studies), warrant (speech intelligibility is the mechanism), qualifier (applies to standard classroom size and occupancy), rebuttal (individual noise-sensitivity variation)
4. Jamal reads the one-paragraph summary; checks that at least one citation has an effect-size estimate
5. Uses the client-ready export to generate a formatted one-pager with citations
6. Attaches the export to the meeting invite agenda

**Extensions**
- 3a. System returns only a generic noise-cognition summary without educational-setting specificity → Jamal notes the scope limitation and qualifies his claim verbally on the call
- 4a. No effect-size estimate is present → Jamal flags this as a gap and uses the evidence tray to find the strongest available study
- 5a. Client-ready export is not formatted for a non-expert audience → Jamal pastes the summary into a plain email and reformats manually

**Postconditions**
- Jamal enters the call with a one-paragraph scientific case, citations, and an effect-size anchor
- He can defend the acoustic investment without overstating the evidence

**Adequacy condition (J-Q-012):** Fails if the answer does not give an outcome (test scores, comprehension) with an effect size and does not suggest a cost-per-student framing.

---

## UC-P6-03 · Evidence Verification — Evidence Checker

| Field | Value |
|-------|-------|
| **Actor** | P6 · Jamal Washington |
| **Sub-flavour** | P6-evidence-checker |
| **Corpus anchor** | J-Q-023 |
| **Goal** | Verify whether the "green walls improve indoor air quality" claim is scientifically defensible before including it in a healthcare project specification |
| **Trigger** | A junior designer has included a green-wall air-quality claim in the project narrative; Jamal needs to verify before the narrative goes to the client |
| **Entry workflow** | `design-decision` on `ka_home_practitioner.html` |
| **Expected answer shape** | Toulmin |

**Preconditions**
- Project type: Healthcare
- The claim is currently in a draft project narrative as an unqualified assertion
- Jamal has 10 minutes before the narrative is due for client review

**Main Success Scenario**
1. Jamal searches "green wall indoor air quality healthcare"
2. System returns the **Living Plant Walls** construct under the Biophilia domain
3. Practitioner summary card: claim is marked as *mechanistic* (plausible mechanism, limited clinical evidence); VOC-reduction data is presented in m³/h with plant-density caveat
4. Jamal notes that the claim is technically supported but over-generalised in the junior designer's draft
5. Jamal revises the narrative: "green walls may reduce VOC concentrations under specific plant-density conditions; evidence is limited to laboratory settings"
6. Flags the revision with a source annotation in Bluebeam

**Extensions**
- 3a. System cannot distinguish living walls from artificial plant walls → Jamal notes this ambiguity and removes the air-quality claim entirely from the narrative
- 3b. Summary card flags that no healthcare-context study exists → Jamal downgrades the claim to "biophilic benefit" rather than "air quality improvement"

**Postconditions**
- The project narrative contains a qualified, defensible version of the claim
- Jamal has a documented evidence check he can cite if the client questions the change

**Adequacy condition (J-Q-023):** Fails if it does not give VOC-reduction data with plant density and does not distinguish living from artificial plant walls.

---

## UC-P6-04 · Specification Translation — Spec Translator

| Field | Value |
|-------|-------|
| **Actor** | P6 · Jamal Washington |
| **Sub-flavour** | P6-spec-translator |
| **Corpus anchor** | J-Q-031 |
| **Goal** | Determine the maximum RT60 and acoustic treatment type for a university lecture hall designed to maximise student attention |
| **Trigger** | Acoustical consultant is asking for the design team's evidence-based RT60 target; Jamal needs to provide a defensible number with a rationale |
| **Entry workflow** | `design-decision` on `ka_home_practitioner.html` |
| **Expected answer shape** | procedure |

**Preconditions**
- Project type: Higher-education / lecture hall, approximately 200-seat capacity
- Acoustical consultant has asked for the design team's preferred RT60 target and a treatment rationale
- Jamal needs to respond in the next 24 hours

**Main Success Scenario**
1. Jamal searches "lecture hall RT60 student attention"
2. System surfaces the **Acoustic Environment → Cognitive Performance** construct with a procedure-type answer
3. Summary card shows: recommended RT60 range (e.g. 0.6–0.8 s for a 200-seat hall), cited standard (ANSI S12.60), and treatment options (ceiling baffles, rear-wall absorption panels)
4. Jamal verifies the standard citation against the evidence tray; confirms the study is classroom-specific, not office
5. Jamal communicates the range and the standard citation to the acoustical consultant
6. Adds the citation to the project specification section in Revit

**Extensions**
- 3a. System gives an RT60 value but no treatment recommendation → Jamal searches specifically for "acoustic treatment lecture hall" and cross-references manually
- 3b. System cites only ANSI S12.60 without an empirical backing study → Jamal notes this is a standard-based (not evidence-based) recommendation and qualifies it accordingly

**Postconditions**
- Acoustical consultant has a documented evidence-based RT60 target
- Jamal has a citation he can include in the specification

**Adequacy condition (J-Q-031):** Fails if it gives an RT60 value without a surface-treatment recommendation or does not cite a standard (ANSI S12.60 or equivalent).

---

## UC-P6-05 · Mid-Meeting Fact-Check — Quick Lookup

| Field | Value |
|-------|-------|
| **Actor** | P6 · Jamal Washington |
| **Sub-flavour** | P6-quick-lookup |
| **Corpus anchor** | J-Q-041 |
| **Goal** | Retrieve the evidence-backed noise-level limit for a NICU, in under 2 minutes, during a live client meeting |
| **Trigger** | Client asks "what does the research say about noise in NICUs?" in a design review meeting; Jamal pulls up the Atlas on his phone |
| **Entry workflow** | `design-decision` — mobile quick-search |
| **Expected answer shape** | ranked-brief |

**Preconditions**
- Jamal is in a live client meeting; device is a phone; time budget is under 2 minutes
- Client is asking a specific factual question with clinical weight
- Jamal cannot bail or defer without losing credibility

**Main Success Scenario**
1. Jamal opens `ka_home_practitioner.html` on his phone; types "NICU noise level"
2. System returns a ranked-brief card immediately: dB(A) limit, cited guideline (AAP / WHO), named outcome (infant hearing / neurodevelopment)
3. Jamal reads the limit aloud to the client; mentions the guideline by name
4. Client is satisfied; meeting continues
5. Jamal bookmarks the card to add to the specification document after the meeting

**Extensions**
- 2a. System does not have a NICU-specific card and returns a generic "healthcare noise" card → Jamal reads the generic limit with a caveat ("our acoustical consultant will confirm the NICU-specific threshold")
- 2b. Mobile layout does not render the ranked-brief card cleanly → Jamal reads from the raw text summary

**Postconditions**
- Jamal has answered the client's question in real time without misrepresenting the evidence
- The NICU noise limit is flagged for inclusion in the specification

**Adequacy condition (J-Q-041):** Fails if it does not give a dB(A) limit from a clinical guideline and does not name the outcome measure.

---

# PART II — USER JOURNEYS

---

## UJ-P6-01 · Hospital Patient Room — Ceiling Height Specification

| Field | Value |
|-------|-------|
| **Persona** | P6 · Jamal Washington |
| **Entry question** | "What ceiling height should I specify for a hospital patient recovery room to reduce anxiety and support healing?" |
| **Corpus ID** | J-Q-001 |
| **Entry workflow** | `design-decision` |
| **Answer shape** | ranked-brief |
| **Evidential demand** | converging |
| **Sub-flavour** | P6-space-designer |
| **Time budget** | ~5 minutes |
| **Portal** | `ka_home_practitioner.html` |

---

### Part A — Stage Narrative

| Stage | Jamal's Action | System Response | Jamal's Thought | Pain Point | Opportunity |
|-------|---------------|----------------|-----------------|------------|-------------|
| **1. Entry** (0:00–0:45) | Opens `ka_home_practitioner.html`; selects `design-decision` workflow; types "ceiling height hospital patient room" | Search returns three construct matches: *Ceiling Height*, *Spatial Volume*, *Perceived Enclosure* | "Ceiling Height — that's the one. Let me see if it has healthcare context." | If space-type filter is not pre-applied, generic office results may appear first | Pre-filter by space type on entry; ask "what building type?" before showing results |
| **2. Construct Scan** (0:45–1:30) | Clicks *Ceiling Height* construct; reads practitioner summary card | Summary card: recommended range (e.g. 9–11 ft for inpatient), evidence quality badge (*converging*), two cited studies with setting icons | "Good — it shows clinical settings, not just labs. That's what I need for the client." | Badge system unclear if "converging" means 2 studies or 20 | Replace badge with explicit study count (e.g. "4 studies, 2 clinical settings") |
| **3. Evidence Engagement** (1:30–3:00) | Expands evidence tray; scans study list for clinical-setting flag; checks one citation for recency | Evidence tray shows 4 studies; 2 flagged as clinical; one from 2019, one from 2022 | "The 2022 study is in a general hospital ward — close enough. The 2019 one is a rehab unit." | Studies listed alphabetically, not by recency or clinical relevance | Sort evidence tray by recency by default; allow filter by setting type (clinical / lab / residential) |
| **4. Specification Decision** (3:00–4:00) | Notes the range (9–11 ft) and the two clinical citations; screenshots or copies for Bluebeam annotation | No new system interaction | "I'll spec 10 ft as the minimum and tell the structural team the research supports up to 11 ft if the floor plate allows." | No way to annotate or flag the specific range within the Atlas | Allow user to save a "practitioner note" alongside a construct |
| **5. Export / Close** (4:00–5:00) | Triggers client-ready export; downloads one-page PDF card | System generates a formatted card: construct, range, citations, evidence quality note, Atlas branding | "This is clean enough to attach to the specification document. I'll add it to the Bluebeam overlay." | Export template not editable; firm branding cannot be added | Allow logo and project-name customisation on export template |

---

### Part B — Page Sequence Specification

**Page 1 · Search / Entry**
- Component: Search bar + space-type selector
- Above the fold: Search bar (large, centred), space-type chip filter (Healthcare / Educational / Office / etc.), recent searches
- Interaction: User types query; space-type chip pre-filters results; autocomplete suggests construct names
- Exit trigger: User clicks a construct name in results

---

**Page 2 · Practitioner Summary Card — Ceiling Height (Healthcare)**
- Component: Practitioner summary card
- Above the fold:
  - Construct name: **Ceiling Height**
  - Space type badge: 🏥 Healthcare — Inpatient
  - Evidence quality badge: **Converging** (4 studies)
  - Recommended range: **9–11 ft (2.75–3.35 m)** for inpatient recovery rooms
  - Primary finding: Lower anxiety and perceived spaciousness associated with heights above 9 ft in clinical settings
  - Top two citations (inline, clickable)
  - Button: **Expand Evidence Tray** | Button: **Export Client Card**
- Below the fold: Mechanism note (1 sentence), scope qualifier, related constructs (Spatial Volume, Window-to-Wall Ratio)
- Interaction: "Expand Evidence Tray" reveals Page 3; "Export Client Card" triggers Page 4

---

**Page 3 · Evidence Tray (Expanded)**
- Component: Collapsible evidence tray within Page 2
- Above the fold (tray area):
  - Study table: Author / Year / Setting / N / Outcome / Effect Direction / Study Design
  - Filter chips: All | Clinical | Lab | Residential
  - Sort toggle: Recency | Relevance | Sample Size
- Study rows (4):
  - Study A (2022) — General hospital ward — n=120 — Anxiety (VAS) — ↓ — RCT
  - Study B (2019) — Rehab unit — n=64 — Perceived spaciousness (7-pt scale) — ↑ — Cross-sectional
  - Study C (2017) — Office (lab setting) — n=90 — Construal level — ↑ — Experiment
  - Study D (2015) — University lab — n=45 — Preference — ↑ — Survey
- Thin-evidence alert: not shown (4 studies clears the threshold)
- Interaction: User can click any study row to see abstract excerpt; clinical-setting studies visually distinguished (e.g. bold row or green left-border)

---

**Page 4 · Client-Ready Export**
- Component: Export modal / download
- Contents of generated PDF:
  - Header: *Evidence Summary — Ceiling Height · Healthcare / Inpatient*
  - Recommended range and plain-language rationale (2 sentences)
  - Two clinical citations in APA format
  - Evidence quality note: *"Based on 4 studies, 2 conducted in clinical settings. Evidence quality: converging."*
  - Footer: *Source: Knowledge Atlas · [date retrieved]*
- Format: Single A4/Letter page, printable, Atlas-branded
- Interaction: Download button; optional "Copy to clipboard" for Bluebeam paste

---

**Chinn-Brewer Rebuttal (embedded in Page 2, below the fold)**
- Anomaly: Studies C and D are laboratory (non-clinical) settings and may not generalise to inpatient populations
- Rebuttal type offered: **Peripheral reprocessing** — "The clinical studies (A, B) are sufficient to support a converging claim for inpatient settings; lab studies provide corroborating mechanism evidence but are not required for the specification decision."
- Reader action prompt: "Does this evidence base give you sufficient confidence to specify the 9–11 ft range for your project?" [Yes, with full confidence / Yes, with caveat / No, I need more clinical evidence]

---

## UJ-P6-02 · University Client — Acoustic Treatment Justification

| Field | Value |
|-------|-------|
| **Persona** | P6 · Jamal Washington |
| **Entry question** | "My higher-ed client is pushing back on the cost of acoustic treatment in classrooms — what does the research say about learning outcomes vs. noise?" |
| **Corpus ID** | J-Q-012 |
| **Entry workflow** | `client-brief` |
| **Answer shape** | Toulmin |
| **Evidential demand** | causal-with-mechanism |
| **Sub-flavour** | P6-client-briefer |
| **Time budget** | ~15 minutes (pre-meeting prep) |
| **Portal** | `ka_home_practitioner.html` |

---

### Part A — Stage Narrative

| Stage | Jamal's Action | System Response | Jamal's Thought | Pain Point | Opportunity |
|-------|---------------|----------------|-----------------|------------|-------------|
| **1. Entry — Client Brief Mode** (0:00–1:00) | Opens `client-brief` workflow; selects space type: Educational / Classroom; types "acoustic treatment learning outcomes noise" | Workflow landing page presents a brief-builder: "Who is your client?" — [Board / Facilities / Faculty / Developer]; Jamal selects *Board* | "Board audience — I need the financial angle, not the mechanism." | Workflow does not adjust output for audience type; same summary regardless | `client-brief` workflow should accept audience type and surface cost-per-student framing for Board audience |
| **2. Toulmin Summary Load** (1:00–3:00) | System loads a Toulmin-structured answer | **Claim:** Acoustic treatment in classrooms improves speech intelligibility and comprehension. **Data:** 3 meta-analyses; effect sizes 0.3–0.6 SD on comprehension tests. **Warrant:** Speech intelligibility is the primary cognitive bottleneck in noisy classrooms. **Qualifier:** Standard classroom size (< 30 students); RT60 > 0.8 s triggers the effect. **Rebuttal:** Teacher voice amplification partially compensates without treatment. | "Good — the effect sizes are there. I can build a cost-per-student argument from this." | Toulmin diagram is not visually rendered; it is plain text | Render Toulmin diagram as an SVG with each node labelled and clickable |
| **3. Evidence Expansion** (3:00–6:00) | Expands evidence tray; looks specifically for a study with a cost or ROI framing | Evidence tray: 5 studies; none has a direct cost-per-student analysis; closest is a UK government review citing £X per-pupil improvement in attainment | "I'll have to do the cost translation myself. I know the acoustic treatment cost per room; I can divide by seat count." | Atlas does not translate evidence into cost-per-unit framing | Practitioner summary card could include a "financial translation" note: "If acoustic treatment costs $X per room and the classroom holds N students, cost per student is $Y — compare against the estimated comprehension benefit." |
| **4. Rebuttal Review** (6:00–9:00) | Reads the rebuttal panel: teacher amplification as a rival intervention | Rebuttal: "Voice amplification systems cost ~$2,000 per room and can achieve 15–20 dB SNR improvement without structural treatment; however, amplification does not address reverberation." Chinn-Brewer response options shown | "I can use this — acoustic treatment addresses reverberation; amplification does not. Two different problems." | Rebuttal is informative but Jamal may not know how to position it in a client conversation | Provide a "client language version" of the rebuttal: one plain-English sentence suitable for a board-level audience |
| **5. Export and Call Prep** (9:00–15:00) | Exports client-ready card; assembles talking points | PDF card: claim, effect sizes, two citations, one sentence on the amplification alternative | "This is enough for the call. I'll open with the effect-size range and the qualifier — they can't argue with the 30-student threshold because our classrooms are all under 28 seats." | No talking-points generator; Jamal has to construct his own script from the Toulmin summary | Offer a "practitioner talking points" export mode: 3–5 bullet points in plain language, ordered for a board conversation |

---

### Part B — Page Sequence Specification

**Page 1 · Client Brief Workflow Entry**
- Component: Workflow landing — `client-brief`
- Above the fold:
  - Heading: *Build a Client Evidence Brief*
  - Step 1: Space type selector (Educational / Healthcare / Office / etc.)
  - Step 2: Audience selector (Board / Facilities Director / Faculty / Developer / Other)
  - Step 3: Search bar — "What design decision are you justifying?"
- Interaction: User completes Steps 1–3 then submits; system loads Page 2 tailored to space type and audience

---

**Page 2 · Toulmin Answer — Acoustic Treatment in Classrooms**
- Component: Toulmin answer shape (visual SVG diagram + prose summary)
- Above the fold:
  - Toulmin SVG diagram:
    - **Data node:** "3 meta-analyses; comprehension effect sizes 0.3–0.6 SD"
    - **Claim node:** "Acoustic treatment improves comprehension in classrooms"
    - **Warrant node:** "Speech intelligibility is the primary cognitive bottleneck in noisy classrooms"
    - **Backing node:** "Irrelevant-sound-effect literature; ANSI S12.60 threshold studies"
    - **Qualifier node:** "Classrooms < 30 students; baseline RT60 > 0.8 s"
    - **Rebuttal node:** "Voice amplification partially substitutes but does not address reverberation"
  - One-paragraph prose summary (client-language version)
  - Evidence quality badge: **causal-with-mechanism** (mechanism is identified and supported)
  - Buttons: **Expand Evidence Tray** | **View Rebuttal Panel** | **Export Client Card**
- Below the fold: Related constructs (Reverberation Time, Speech Intelligibility, Open-Plan Acoustics)

---

**Page 3 · Evidence Tray (Expanded)**
- Study table: 5 studies; columns: Author / Year / Study Type / N / Setting / Outcome / Effect Size
  - Meta-analysis A (2021) — 42 studies — Classrooms globally — Comprehension — d = 0.45
  - RCT B (2018) — n=312 — UK primary schools — Attainment test score — +8 percentile points
  - Experiment C (2016) — n=88 — University lecture hall — Recall — d = 0.33
  - Review D (2020) — UK government — Cost per pupil: £180 per-pupil attainment gain
  - Study E (2014) — n=44 — Elementary classroom — Word recognition — d = 0.61
- Financial translation note (if audience = Board): *"At typical acoustic treatment costs of $15,000–25,000 per classroom (25–30 seats), cost per student seat is $500–1,000 — offset partially by measurable comprehension gains."*

---

**Page 4 · Chinn-Brewer Rebuttal Panel**
- Component: Rebuttal panel (full width, exposed by default in `client-brief` mode)
- Anomaly presented: "Voice amplification systems achieve comparable SNR improvement at lower cost without structural intervention"
- Expert response (Atlas-authored): "Amplification improves signal level but does not reduce reverberation time; in rooms with RT60 > 0.8 s, reverberation continues to mask speech even with amplification. The two interventions address different acoustic problems."
- Client-language version: "A microphone system makes the teacher louder but does not stop sound from bouncing off hard surfaces. In a reverberant room, both are needed."
- Chinn-Brewer response options for Jamal:
  - *Acceptance* — "The rebuttal is valid; I will recommend both interventions"
  - *Reinterpretation* — "The rebuttal applies to a different acoustic problem; my recommendation stands for reverberation-dominated rooms"
  - *Rejection* — "The cost comparison is misleading; amplification is not a substitute in this context"
- Jamal's likely selection: **Reinterpretation**

---

**Page 5 · Client-Ready Export**
- PDF card contents (Board audience version):
  - Header: *Evidence Brief — Acoustic Treatment · Educational / Classroom*
  - Plain-language claim (1 sentence)
  - Effect-size range with plain translation: *"Students in acoustically treated classrooms scored 0.3–0.6 standard deviations higher on comprehension tests than students in untreated rooms — equivalent to approximately 1–2 months of additional learning."*
  - Two citations in accessible format (Author, Year, Journal)
  - Cost note (if financial translation is available)
  - Qualifier: *"Evidence applies to classrooms under 30 students with baseline reverberation times above 0.8 seconds."*
  - Footer: *Source: Knowledge Atlas · [date retrieved]*

