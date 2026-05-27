# User Journey Research Document
## P1 · Maya Chen · Undergraduate Explorer
**COGS 160 Spring 2026 · Track 4 Interaction Design**
**Research phase: Persona grounding & use-case definition**
**Document status: Pre-panel draft — findings to be validated by panel simulation**

---

## 1. Persona Reference Card

| Attribute | Value |
|---|---|
| Name | Maya Chen |
| Age | 19 |
| Year | Second-year undergraduate, UCSD |
| Primary device | M1 MacBook Air (desk/library); iPhone (transit) |
| Daily tools | ChatGPT, Google, iPhone Notes |
| Default competing tab | ChatGPT — query already typed before she opens K-Atlas |
| Session shape | 3–8 minutes, 1–2 pages, rare return visit |
| Arrival trigger | COGS class assignment directive, or Googled a term-paper topic |
| Jargon threshold | Bails within 5 seconds of first encountering undefined technical vocabulary |
| Knowledge floor | Does not know: "latent variable," "warrant," "construct," "affordance," "Bayesian," "EDA," "research front" |
| Mental model of K-Atlas | "A better-organised textbook with a search box" |
| Governing question | "What does the evidence actually say, and where are the gaps?" |
| Primary goal on arrival | Complete A0 — find and upload 10 experimental papers on assigned topic |

**Weighting constraint:** Maya is the plurality by visit count but the minority by depth. Fixes that serve Maya must not degrade the Researcher or Contributor experience. Where a conflict exists, a mode-switched or layered solution is required — not a global simplification.

---

## 2. Mental Model vs. System Reality

This section is the analytical core of the document. Every friction point in Maya's journey is a downstream consequence of the gap described here. Product recommendations that do not account for this gap will fail even if implemented perfectly.

### Maya's mental model
K-Atlas is a search engine with better organization than Google. The expected interaction loop is: **type a topic name → get a list of papers → download → cite**. She has no concept of a knowledge graph, epistemic layer, warrant chain, or construct taxonomy. She does not know that "construct" has an academic meaning distinct from its everyday meaning. She does not know what EDA, HRV, or NASA-TLX are. She does not know that her topic ("prospect-refuge") maps to a specific place in an academic taxonomy rather than being a searchable string.

### System reality
K-Atlas is a knowledge representation system built on a structured epistemic graph. Articles are indexed by cognitive/affective **construct** (Sustained Attention, Stress, Awe...) and **measuring instrument** (EDA, EEG, NASA-TLX...). Topic names like "prospect-refuge" are nodes within a taxonomy, not search terms. Assignment functionality requires authentication before any content is visible. Several workflow paths (topic hierarchy, workflow hub) require a live server to render. The site's opening description on `ka_home.html` explicitly states "K-Atlas is *not* a search engine" — which, while accurate, directly invalidates Maya's mental model before offering her any alternative frame.

### Translation requirements
The mental model gap generates a specific set of product obligations. These are not UX preferences — they are functional requirements for Maya to be able to use the system at all:

| Maya's frame | System's frame | Required translation |
|---|---|---|
| "Topic name" (e.g., "prospect-refuge") | Construct + taxonomy node | A topic-name → construct mapping, either via search alias or plain-language topic index |
| "Find papers" | Search by construct + instrument | A student-facing search mode that accepts natural-language topic names |
| "My assignment" | A0 — collect-articles-upload workflow | An assignment-aware entry point that surfaces A0 without requiring general site orientation first |
| "Is this paper good?" | Experimental article classification | A plain-language definition of what qualifies, inline, before she starts uploading |
| "Am I done?" | 10 qualifying uploads, A0 marked complete | An explicit, unambiguous completion state |

---

## 3. Jobs to Be Done

JTBD separates what Maya is hiring the product to accomplish from the features she would use to do it. This framing prevents design recommendations from being locked to the current feature set. Jobs are listed in priority order within each category.

### Functional jobs

**J1 (Primary) — Complete a required assignment without wasting time.**
*When I have a class assignment to collect experimental papers on a specific topic, I want to find 10 qualifying papers and upload them as fast as possible, so I can submit the assignment and move on to other work.*
This is the job that brings Maya to the site. Every other job is secondary to this one.

**J2 — Understand a concept quickly enough to participate in class.**
*When my TA names a concept I have never encountered, I want a plain-language explanation with at least one real study behind it, so I can follow the discussion and not look uninformed.*
This job brings Maya back for return visits when J1 does not. It is the second most common arrival trigger.

**J3 — Confirm that a source found elsewhere is credible enough to cite.**
*When I find a paper through Google or ChatGPT, I want a fast credibility signal on that specific paper, so I can cite it with confidence.*
Lower frequency than J1 and J2, but worth designing for because it represents an entry point the site does not currently surface at all.

### Emotional jobs

**J4 (Primary) — Feel like I am doing the assignment correctly.**
Maya is not primarily trying to learn. She is trying to avoid the anxiety of not knowing whether her output meets the standard. The product must provide explicit, step-by-step confirmation that she is on the right path at every stage. Ambiguity at any step generates the emotional signal that she is doing it wrong.

**J5 — Not feel excluded by the vocabulary.**
Every undefined technical term signals to Maya that the site was not built for her. That signal activates abandonment. The emotional job is not satisfaction — it is the absence of alienation. This is distinct from J4: J4 is about task confidence, J5 is about identity fit.

**J6 — Feel that her time was not wasted.**
Given a 3–8 minute window and a pre-loaded ChatGPT tab, the product must deliver something concrete and usable before Maya's patience budget runs out. Speed of payoff is as important as correctness of payoff.

### Social jobs

**J7 — Produce work that meets her instructor's standard.**
The product's output (uploaded papers, completion confirmation) must be legible and defensible to an instructor. Maya needs to be able to say "I used K-Atlas" and have that carry weight. If the output is ambiguous or looks incomplete, the social job fails even if the functional job technically succeeds.

**J8 — Be able to explain the process to a classmate in two sentences.**
If Maya succeeds, she will be asked by someone how she did it. If the path was too complex to describe simply, she will not be able to help — and her social recommendation of the product will fail along with it.

---

## 4. Use Cases

Use cases define the structured interaction contracts between Maya and the system. Each step specifies what Maya expects to see, what action she takes, what she expects to happen, what the site currently provides, where the expectation is violated, and what the bail risk is at that step.

**Bail risk scale:** Low = unlikely to cause abandonment · Medium = causes friction, some users abandon · High = causes a significant portion of users to abandon · Critical = the primary abandonment point for this disposition

---

### UC-01 · Complete A0 — Find and Upload 10 Experimental Papers
**Priority: Primary. All product research in this document is anchored to this use case.**

**Actor:** Maya Chen — any disposition (sceptic, eager, pragmatist all share this job)
**Trigger:** Assignment sheet or course page instructs her to go to K-Atlas and collect experimental papers
**Preconditions:** UCSD email address; assigned topic (prospect-refuge); no prior K-Atlas account; 3–8 minute time budget; ChatGPT tab already open with same query

---

**Step 1 · Navigate to K-Atlas**

- **Expects to see:** A normal website with a prominent search bar — the standard mental model for a research tool
- **Action:** Types URL from assignment sheet, or Googles "K-Atlas UCSD" / "Knowledge Atlas UCSD"
- **Expects to happen:** Lands on a page clearly built for COGS 160 students, with an obvious starting point
- **Current site state:** `ka_home.html` — first viewport contains the wordmark, a chip row ("160 Student / Researcher / Contributor / Practitioner / Theorist"), and an opening paragraph: *"Knowledge Atlas is not a search engine, a chatbot, or a literature database. It is a knowledge representation system..."*
- **Expectation gap:** The first sentence of the description explicitly denies what Maya expects the system to be ("not a search engine") before offering any alternative frame. The chip row exists and "160 Student" is correctly positioned first — but the alienating description appears above it in visual weight.
- **Bail risk — Sceptic: Critical.** The first sentence confirms her suspicion that the site is "academic decoration." She opens ChatGPT.
- **Bail risk — Eager: Low.** She reads the description trying to understand, then finds the chip.
- **Bail risk — Pragmatist: Medium.** She scrolls fast, finds the chip, and clicks without reading.

---

**Step 2 · Identify as a COGS 160 student**

- **Expects to see:** A clear "COGS 160 students, click here" affordance — a button, a banner, or a prominent role selector
- **Action:** Scans the page for anything that says "student" or "160"
- **Expects to happen:** One click routes her to a page built specifically for her role
- **Current site state:** Chip row with "160 Student" as the first option. Clicking a chip previews "a more relevant navbar and first actions before you register." The chip does not navigate — it previews.
- **Expectation gap:** Maya expects clicking her role to take her somewhere. Instead, clicking "160 Student" updates the navbar preview but keeps her on the same page. The action does not match the expected outcome. She may click it multiple times or look for a "go" button that does not exist.
- **Bail risk — Sceptic: High.** Clicks the chip, nothing happens the way she expected, reads it as the site being broken.
- **Bail risk — Eager: Low.** Reads the surrounding text, understands the chip is a preview, finds the "Enter Knowledge Atlas →" button or the student portal link.
- **Bail risk — Pragmatist: Medium.** Expects a navigation action; confused by the preview behavior; may look for a different entry point.

---

**Step 3 · Arrive on the student portal**

- **Expects to see:** A search bar, or an "your assignment is here" call to action at the top of the page
- **Action:** Lands on `ka_home_student_new.html`, scans the page top to bottom
- **Expects to happen:** Her task (A0) is immediately visible without scrolling
- **Current site state:** Hero section with heading "What does the evidence actually say about how environments affect people?" and subtitle "Start by exploring what's known, what's tentative, and what's genuinely unknown." Below: orientation checklist (4 items: read methodology guide, browse 3 "Did You Know" findings, explore topic hierarchy, complete A0). Below that: "Of Potential Interest" cards. Below that: "Your Journey Choices" grid containing the "Start A0" card.
- **Expectation gap:** Two violations. First, the hero question ("What does the evidence actually say...") is the site's governing question — it is not Maya's question. Maya's question is "where do I upload my papers?" The hero creates a mismatch between what the page announces and what Maya came to do. Second, A0 is item 4 in an orientation checklist and the second item in a journey grid — below the fold on most screens. Maya must scroll past content designed to orient her before she can access the task she came to complete.
- **Bail risk — Sceptic: Critical.** Does not scroll. Does not see A0. Closes the tab.
- **Bail risk — Eager: Low.** Reads the orientation checklist, understands the sequence, finds A0.
- **Bail risk — Pragmatist: Medium.** Scrolls fast, finds "Start A0" card, clicks it — but frustrated by the scroll distance.

---

**Step 4 · Understand what A0 requires**

- **Expects to see:** A plain-language statement: "find these kinds of papers, on this topic, and upload them here"
- **Action:** Reads the A0 journey card description ("Can I find 10 experimental articles on my assigned topic?") and clicks "Start A0 →"
- **Expects to happen:** Lands on the A0 page with clear instructions and an upload interface
- **Current site state:** Journey card text: *"Your first required assignment: find and upload experimental papers that match your research front."* The term "research front" is not defined anywhere on this page.
- **Expectation gap:** "Research front" is the system's internal taxonomy term for what Maya's assignment calls her "topic." This mapping is never stated. Maya knows she has a topic ("prospect-refuge"). She does not know what a "research front" is or whether it is the same thing. The first piece of assignment-specific language she encounters is already in the system's frame, not hers.
- **Bail risk — Sceptic: Medium.** Notes "research front" as further evidence the site is academic jargon. Suspicion deepens.
- **Bail risk — Eager: Low.** May Google "research front" or proceed assuming it means her topic.
- **Bail risk — Pragmatist: Low.** Ignores the unfamiliar term and clicks "Start A0."

---

**Step 5 · Encounter the authentication gate**

- **Expects to see:** The A0 upload interface — content, instructions, a place to start working
- **Action:** Clicks "Start A0 →" and is taken to `collect-articles-upload.html`
- **Expects to happen:** Arrives at the assignment and begins uploading
- **Current site state:** The page immediately shows: *"Sign in to access your article collection page"* with an email/password form. No A0 content is visible before authentication. No preview of what is behind the login wall. No indication of how long registration takes or what it requires.
- **Expectation gap:** Maya came to do an assignment. She is instead asked to create an account for a system she has not yet seen work for her. There is no trust basis for this request — she has not yet received any value from the product. The authentication gate arrives before any orientation, any preview, or any evidence that the system will serve her need.
- **Bail risk — Sceptic: Critical.** This is the highest-probability abandonment point for this disposition. ChatGPT requires no account. Google Scholar requires no account. K-Atlas does. She opens ChatGPT.
- **Bail risk — Eager: Low.** Has her UCSD email ready; registers and proceeds.
- **Bail risk — Pragmatist: High.** Will register only if she believes the system will save her time. No preview means no basis for that belief. Likely abandons.

---

**Step 6 · Search for papers on "prospect-refuge" (Core task — highest structural failure risk)**

- **Expects to see:** A search bar where she can type "prospect-refuge" and get a list of papers
- **Action:** Looks for a search interface; types or attempts to type "prospect-refuge" in any available input field
- **Expects to happen:** A list of papers about prospect-refuge theory appears, filterable or sortable by relevance
- **Current site state:** The article search interface (`ka_article_search.html`) is organized around three search modes: by Construct (dropdown: Sustained Attention, Working Memory Load, Emotional Arousal, Stress, Cognitive Load, Awe, Flow State, Fatigue, Vigilance Decrement, Spatial Navigation, Social Engagement, Sensory Overload, Restorative Attention, Hedonic Valence), by Instrument or Sensor (EDA, EEG, HRV, fMRI, NASA-TLX, PANAS...), or by both combined. "Prospect-refuge" does not appear in any dropdown. On the student portal, the topic checklist contains "Prospect & Refuge" under Spatial Form — but clicking this checkbox only "personalizes your experience" and does not link to papers or search results.
- **Expectation gap:** This is a product architecture gap, not a UX labeling problem. The search is built for users who know the academic taxonomy. Students receive their assignments in plain topic language. There is no bridge between the two frames. Maya cannot find papers on "prospect-refuge" using any currently available search path. The topic checklist on her portal contains her topic by name but connects to nothing actionable.
- **Bail risk — All dispositions: Critical.** This is the hardest wall in the entire journey. The Sceptic closes the tab in under 30 seconds. The Pragmatist tries one or two constructs, gets irrelevant results, and switches to Google Scholar. The Eager spends 3–4 minutes trying to deduce which construct maps to "prospect-refuge" (Spatial Navigation? Emotional Arousal? Neither is obvious) before giving up or making an arbitrary choice.
- **Design note:** The "Prospect & Refuge" checkbox in the student portal topic list is the closest the site comes to bridging this gap, but it is currently a dead end — it personalizes display without enabling search or paper discovery. This is the single highest-priority product gap in Maya's journey.

---

**Step 7 · Evaluate and upload individual papers**

- **Expects to see:** A drop zone or "upload" button, clear criteria for what qualifies, and immediate feedback per paper
- **Action:** Drags a PDF into the upload area or clicks to browse; pastes an APA citation when prompted
- **Expects to happen:** The paper is checked automatically and she sees a pass (✓) or fail (✗) with a reason
- **Current site state:** Upload interface accepts PDFs with parallel APA citation paste. Classification runs in real time with ✓/✗ result. The definition of "experimental article" is provided inline: *"papers that report original empirical studies with participants, data collection, and results."* Rejection messages provide a reason. The workflow also requires pasting APA citation text alongside the PDF — a two-step upload that Maya may not anticipate.
- **Expectation gap:** Two smaller gaps remain. First, the APA citation requirement adds a step Maya did not expect — she thought she was uploading PDFs, not also formatting citations. Second, rejection messages state why a paper fails but do not suggest what to search for instead. Maya must re-enter the search flow cold, without guidance.
- **Bail risk — Sceptic: Low** (if she reaches this step, the hardest walls are behind her). **Pragmatist: Medium** (APA formatting requirement is friction she resents). **Eager: Low** (will look up APA format if needed).

---

**Step 8 · Confirm A0 completion**

- **Expects to see:** A clear "you're done" signal with a count and a next step
- **Action:** Uploads her 10th qualifying paper
- **Expects to happen:** The system confirms she is finished and tells her what to do next
- **Current site state:** "Assignment 0 complete!" banner appears. Track selection options are surfaced (Track 1: Tagging, Track 2: Articles, Track 3: VR, Track 4: Interaction Design).
- **Expectation gap:** None significant. This step is adequately served. Completion state is explicit and the next step (choose a track) is immediately actionable.
- **Bail risk — All dispositions: Negligible.**

---

**UC-01 Postconditions:**
- 10 experimental papers uploaded and classified as qualifying
- A0 marked complete in the system
- Maya knows her next step

**UC-01 Critical path summary:**
Steps 1, 5, and 6 are the primary abandonment points. Step 6 (the search gap) is a structural product problem that will block the majority of Maya-type users regardless of how well Steps 1–5 are served. Fixing Steps 1 and 5 without fixing Step 6 reduces friction but does not produce task completion.

---

### UC-02 · Look Up a Research Concept for Exam Prep
**Priority: Secondary**

**Actor:** Maya Chen — Eager or Pragmatist disposition most likely
**Trigger:** TA or instructor names a concept in class ("know these for the midterm"); Maya looks it up after lecture
**Preconditions:** Maya has a specific term (e.g., "prospect-refuge theory," "attention restoration theory"); she needs understanding, not papers; device: MacBook Air or iPhone; time budget: 10–15 minutes; no competing tab — she is intentionally trying to learn

---

**Step 1 · Arrive with a concept name in hand**

- **Expects to see:** A search bar she can type the concept name into
- **Action:** Lands on the student portal or global home; looks for a search bar or a "concepts" / "topics" section in the navigation
- **Expects to happen:** Types "prospect-refuge theory" and receives a plain-language explanation
- **Current site state:** The student portal navigation contains: Home, Methods, Sitemap. No persistent search bar is available on the student portal. The global nav on `ka_home.html` does not surface a concept-level search for students. A search link (`⌕ Search`) appears in the COGS 160 course nav but links to `ka_search.html` — a global search not tailored to plain-language concept lookup.
- **Expectation gap:** There is no prominently available search affordance on the student portal that accepts concept names. The "Sitemap" and "Methods" links do not suggest concept discovery. Maya must either deduce that the topic hierarchy exists or find the search by trial and navigation.
- **Bail risk — Sceptic: High.** No search bar visible on arrival; opens Google instead.
- **Bail risk — Eager: Medium.** Will explore navigation options; may find the topic hierarchy or global search.
- **Bail risk — Pragmatist: High.** No immediate path to concept; uses Google.

---

**Step 2 · Navigate to the concept**

- **Expects to see:** A topic index or search results page listing named concepts
- **Action:** Clicks through Sitemap, or navigates to `ka_topic_hierarchy.html` or `ka_topics.html`
- **Expects to happen:** Finds "prospect-refuge" in a list organized by name and clicks through to a description
- **Current site state:** `ka_topic_hierarchy.html` requires a live server to load topic data. Without a running local server, the page renders with "0 Papers shown / 0 IV root families / 0 Topic nodes" — blank. `ka_topics.html` similarly pulls from a live data layer. The student portal topic checklist has "Prospect & Refuge" listed under Spatial Form — but clicking it only sets a preference, it does not navigate.
- **Expectation gap:** The topic discovery infrastructure exists conceptually (hierarchy, topics pages) but is not functional in a static or unauthenticated context. The only place "Prospect & Refuge" appears by name on a working page is the student portal topic checklist, where it is a dead-end preference setter. Maya has no functional path to concept content.
- **Bail risk — All dispositions: Critical.** The infrastructure for this use case does not function without a live server. This is a product availability gap, not a UX gap.

---

**Step 3 · Read a plain-language concept description**

- **Expects to see:** A paragraph explaining what the concept is in accessible language, with the key claim stated up front
- **Action:** Reads the concept page
- **Expects to happen:** Understands the concept well enough to explain it in one sentence
- **Current site state:** Cannot be reached via the paths available to Maya in a static or unauthenticated context. Assessment blocked by Step 2 failure.
- **Expectation gap:** Cannot assess.
- **Bail risk:** Not applicable — UC-02 fails at Step 2 for most Maya-type users.

---

**Step 4 · Find at least one supporting study**

- **Expects to see:** A list of papers she can reference — titles, authors, brief description
- **Action:** Looks for a "papers" or "studies" section on the concept page
- **Expects to happen:** Sees studies listed with enough information to cite one
- **Current site state:** Article cards on topic pages (when accessible) show title, article type, abstract, and DOI. This step would be adequately served if Steps 2–3 were functional.
- **Expectation gap:** Conditional on Step 2 being resolved. If the topic page is reachable, this step works.
- **Bail risk:** Low — if reached.

---

**UC-02 Critical finding:**
This use case is currently not completable for most Maya-type users. The concept discovery infrastructure requires a live server to function. Until that dependency is resolved — either by making the topic layer work in an authenticated-but-static context, or by building a lightweight plain-language concept index that does not depend on live data — UC-02 represents a failed product promise.

---

### UC-03 · Explore What Research Says on a Topic of Personal Interest
**Priority: Tertiary — serendipitous engagement**

**Actor:** Maya Chen — Eager disposition
**Trigger:** Heard something interesting in lecture or in conversation; 5–10 free minutes; not driven by a deadline
**Preconditions:** No specific assignment; intrinsically motivated by curiosity; willing to click around; time budget 5–10 minutes

---

**Step 1 · Arrive with curiosity but no specific goal**

- **Expects to see:** Something that catches her attention within 15 seconds — a striking claim, a surprising statistic, a question she has not thought about
- **Action:** Lands on the student portal, scans the page without a specific target
- **Expects to happen:** Something stops her scrolling and makes her want to know more
- **Current site state:** Hero section leads with the governing question ("What does the evidence actually say about how environments affect people?"). Below the checklist, the "Of Potential Interest" section contains four cards: a "Did You Know" finding (rotating, plain-language, e.g., "Natural light improves sleep — workers with adequate natural light report 46 more minutes of sleep per night"), a "Topic Spotlight" card, a "Gap Alert" card, and a "New This Week" card.
- **Expectation gap:** Small. The "Did You Know" card is the strongest match for this use case — it is written in plain language, makes a specific surprising claim, and cites a study. The "Gap Alert" card ("Only 1 research front and limited experimental coverage...") is written in system-internal language that would not resonate with Maya. The "Topic Spotlight" card ("7 research fronts and 760 articles") uses metrics Maya has no frame for.
- **Bail risk: Low.** The "Did You Know" card provides genuine value for this disposition. Risk is that Maya sees it as trivia rather than evidence of the site's depth.

---

**Step 2 · Follow a finding**

- **Expects to see:** A page that expands on the specific finding she just read
- **Action:** Clicks "Explore this finding →" on the "Did You Know" card
- **Expects to happen:** Lands on a page specifically about that finding — more context, the study, related findings
- **Current site state:** The "Explore this finding →" CTA on the "Did You Know" card links to `ka_home.html` — the global site home, not the specific finding. The link is a site-level CTA, not a content-specific one.
- **Expectation gap:** This is a broken promise. The CTA says "explore this finding" but delivers the global home. Maya clicked expecting depth on a specific claim and landed on a page she may have already been on. This is a high-severity mismatch between the CTA's implied contract and its actual destination.
- **Bail risk: High.** The broken link terminates the curiosity loop. Clicking "explore this finding" and landing somewhere unrelated is jarring enough to cause abandonment.
- **Design note:** This is a small fix with outsized impact on UC-03. Routing the "Did You Know" CTA to the relevant topic or article page would make this step work. The content likely exists — the routing does not.

---

**Step 3 · Go deeper or discover related content**

- **Expects to see:** Related findings, more context on the same topic, a thread she can follow
- **Action:** Reads more, clicks a related link, or checks another card
- **Expects to happen:** A connected thread of interesting content that rewards continued exploration
- **Current site state:** Unreachable for the "Did You Know" card due to Step 2 routing failure. The "Topic Spotlight" and "Gap Alert" cards link to `ka_topics.html` and `ka_gaps.html` respectively — both require live data to render meaningfully.
- **Expectation gap:** The serendipitous exploration loop is broken at Step 2 and does not recover. The only card that works (Did You Know) routes to a dead end. The other cards route to data-dependent pages.
- **Bail risk: Critical — but moot.** Maya has already left at Step 2.

---

**UC-03 Critical finding:**
This use case has the best content setup of the three (the "Did You Know" card is genuinely good for this persona) but is killed by a single routing error. The fix is targeted and low-effort. This is the highest ROI improvement available for UC-03: fix the CTA destination on the "Did You Know" card.

---

## 5. Gap Analysis

Maps every identified gap across all three use cases to a severity rating, the relevant Nielsen heuristic, and a design implication. Severity is rated 1–5 (1 = minor friction · 5 = blocks task completion).

| ID | Use Case | Step | Gap Description | Sev. | Nielsen Heuristic | Design Implication |
|---|---|---|---|---|---|---|
| G-01 | UC-01 | Step 1 | First viewport of `ka_home.html` opens with "K-Atlas is *not* a search engine" — directly contradicts Maya's mental model before offering an alternative | 4 | H2 · Match between system and real world | Rewrite the opening description to lead with what the system *does for students*, not what it is not. Move epistemological framing below the fold. |
| G-02 | UC-01 | Step 2 | Clicking the "160 Student" chip is a preview action, not a navigation action — violates the expected click contract for a role selector | 3 | H1 · Visibility of system status; H4 · Consistency and standards | Make the chip a navigation action to the student portal, or add a clearly labeled "Go →" CTA immediately adjacent to the chip |
| G-03 | UC-01 | Step 3 | A0 is the 4th item in the orientation checklist and below the fold on first load — students must scroll past orientation content to reach their primary task | 4 | H3 · User control and freedom; H8 · Aesthetic and minimalist design | Surface A0 as the primary CTA on the student portal for first-time visitors. Orientation checklist should be secondary, not a gate. |
| G-04 | UC-01 | Step 4 | "Research front" used on the A0 journey card without definition — system taxonomy term used in student-facing context | 2 | H2 · Match between system and real world | Replace "research front" with "your assigned topic" or add an inline tooltip. |
| G-05 | UC-01 | Step 5 | Authentication required before any A0 content is visible — cold start with no preview of value | 4 | H3 · User control and freedom; H5 · Error prevention | Show a preview of the A0 interface (static, non-functional) before the login gate. Alternatively, defer authentication to the first upload action. |
| G-06 | UC-01 | Step 6 | No search path accepts "prospect-refuge" as a search term — article search is organized by academic construct/instrument taxonomy with no student-facing alias | 5 | H2 · Match between system and real world; H6 · Recognition over recall | **Critical.** Build a topic-name alias layer that maps student assignment language to constructs. Or: create a dedicated "A0 search" mode that accepts plain topic names and returns relevant papers. The "Prospect & Refuge" checkbox in the student topic list is the seed of this solution — it needs to become a search entry point. |
| G-07 | UC-01 | Step 7 | Paper rejection messages provide a reason but no next-step suggestion — Maya must re-enter the search flow cold | 2 | H9 · Help users recognize, diagnose, and recover from errors | Add "What to search for instead" guidance to each rejection message type. |
| G-08 | UC-01 | Step 7 | APA citation paste required alongside PDF upload — unexpected two-step workflow | 2 | H2 · Match between system and real world | Add contextual guidance: "Don't have the citation? Here's how to find it in 30 seconds." Or: auto-extract citation metadata from the PDF on upload. |
| G-09 | UC-02 | Step 1 | No persistent search bar on student portal; no obvious concept-lookup entry point | 4 | H6 · Recognition over recall | Add a plain-language concept search bar to the student portal. Label it "Look up a topic or concept." |
| G-10 | UC-02 | Step 2 | Topic hierarchy and topics pages require a live server to render — blank in static context | 5 | H1 · Visibility of system status | Build a lightweight static topic index that does not depend on live data. Even a plain HTML list of concept names with descriptions would close this gap. |
| G-11 | UC-03 | Step 2 | "Explore this finding →" CTA on the "Did You Know" card routes to `ka_home.html` instead of the specific finding | 4 | H4 · Consistency and standards; H2 · Match between system and real world | Route each "Did You Know" card CTA to the relevant topic or article page. If that page does not yet exist, link to the topic in the checklist as a temporary measure. |
| G-12 | UC-03 | Step 3 | "Gap Alert" and "Topic Spotlight" cards use system-internal metrics ("7 research fronts," "1 research front") without translation | 2 | H2 · Match between system and real world | Rewrite card descriptions to lead with a plain-language implication ("This is one of the best-studied topics on the site" / "This area is almost completely unstudied — yours could be one of the first papers here"). |

---

## 6. Success Criteria

Measurable conditions under which K-Atlas can be said to serve Maya for each use case. These are the evaluation inputs for the heuristic audit phase (Week 5) and the baselines against which fix-sprint improvements are measured (Weeks 6–7).

### UC-01 · Complete A0

| ID | Criterion | Current baseline | Target |
|---|---|---|---|
| SC-01 | Maya reaches the A0 upload interface in N clicks from the global home | Est. 4–5 clicks (home → chip preview → student portal → scroll → journey card → A0 page) | ≤3 clicks |
| SC-02 | Maya can search for "prospect-refuge" by name and receive ≥1 result | 0 results — term not in any search path | ≥1 result |
| SC-03 | No undefined term above Grade 11 reading level appears in the first visible viewport of any page in the A0 flow | Violations at Steps 1, 4 ("research front") | 0 violations |
| SC-04 | Authentication is deferred until at least one page of A0 content is visible | Fails — gate is immediate | Authentication deferred to upload action |
| SC-05 | Paper rejection messages include a next-step suggestion | Fails — rejection gives reason only | Every rejection includes a suggested next action |
| SC-06 | Maya can complete A0 from cold start in ≤15 minutes, assuming papers are findable | Not measurable — Step 6 blocks completion | ≤15 minutes end-to-end |

### UC-02 · Look Up a Concept

| ID | Criterion | Current baseline | Target |
|---|---|---|---|
| SC-07 | A named concept (e.g., "prospect-refuge theory") is findable by that exact name within 2 clicks from the student portal | Fails — no functional path exists | Findable in ≤2 clicks |
| SC-08 | The first 150 words of any concept page are free of undefined jargon | Cannot assess — pages not reachable | 0 undefined terms in first 150 words |
| SC-09 | Each concept page references ≥1 citable study before any mechanism or warrant content | Cannot assess | ≥1 citable study in first viewport |

### UC-03 · Serendipitous Exploration

| ID | Criterion | Current baseline | Target |
|---|---|---|---|
| SC-10 | "Did You Know" CTA routes to a page specifically about the finding displayed | Fails — routes to `ka_home.html` | Routes to specific topic or article page |
| SC-11 | ≥2 of 4 "Of Potential Interest" cards link to pages that are accessible without a live server | Fails — all 4 cards link to data-dependent or home pages | ≥2 cards link to accessible content |
| SC-12 | A first-time visitor on the student portal can spend 5 minutes exploring without hitting a dead end or data-blank page | Fails — dead ends at Steps 2 and 3 | 0 dead ends in a 5-minute casual browse |

---

## 7. Open Research Questions

Questions the panel simulation and heuristic audit must be designed to answer. These are gaps in current knowledge — not findings.

**RQ-01:** Does the "160 Student" chip on `ka_home.html` get clicked before Maya abandons the page, or does the opening description cause her to leave first? What is the actual abandonment rate at Step 1? *(Addressable via panel UC-01 simulation, Step 1–2)*

**RQ-02:** When Maya encounters the orientation checklist on the student portal, does she read it as a required sequence (blocking A0 access) or as a parallel optional activity? Does this interpretation differ by disposition? *(Addressable via panel click-trace, Step 3)*

**RQ-03:** When the article search returns no results for "prospect-refuge," what alternative behavior emerges? Does Maya retry with different terms, does she look for help, or does she abandon immediately? Are there terms she would naturally try that might coincidentally return results? *(Addressable via panel alternative flow simulation, Step 6)*

**RQ-04:** Does the "Did You Know" card create genuine curiosity that extends Maya's session, or is it processed as decorative content and ignored on the path to A0? *(Addressable via panel click-trace, UC-03)*

**RQ-05:** What is the minimum intervention required at Step 6 to unblock Maya? Three candidates exist: (a) add "prospect-refuge" as a search alias for the relevant construct, (b) build a plain-language topic index that maps assignment topics to constructs, (c) create a dedicated "I'm doing A0" search mode that bypasses the construct taxonomy entirely. Which produces the least disruption to the Researcher experience? *(Requires cross-persona analysis — do not design without checking against P2/P3)*

---

*Linked panel prompt: `panel_prompt_maya_chen.md`*
*Target page for initial panel run: `ka_home_student_new.html`*
*Next revision: after panel simulation produces transcript data*
