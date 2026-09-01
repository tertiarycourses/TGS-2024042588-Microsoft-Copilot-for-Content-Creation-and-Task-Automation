"""Topic 1 (Day 1) — Copilot Foundations and Content Creation in Word and PowerPoint.

Scenario: Lumina Living Pte Ltd, a Singapore workspace-furniture company, is
launching its Sustainable Workspace campaign. Every lab in the course works on
this one connected scenario.
"""

DOMAIN1 = [
    dict(
        num=1, topic=1, day=1, level="Foundation",
        title="Set Up Microsoft 365 Copilot and Prompt Safely",
        objective="Identify where Copilot is available, how it is grounded, and the verification duty that comes with it",
        km="K1", am="A1",
        apps="Microsoft 365 Copilot Chat, Excel",
        desc="The learner confirms which Copilot surface they are licensed for, learns how grounding and permissions work, writes prompts using the four-part prompt contract, and records a review decision for every generated claim.",
        build="A completed setup, grounding and prompt-review register in Excel",
        services="Microsoft 365 Copilot Chat, Excel, Microsoft Graph grounding",
        prompt=("Summarise what Microsoft 365 Copilot can and cannot access on my behalf in this tenant. "
                "List the work data sources it may use, state that my existing permissions still apply, "
                "and give three limitations I should verify before trusting an answer. Do not invent features."),
        steps=[
            ("Confirm your Copilot surface and licence", "Open Microsoft 365 Copilot Chat and note whether the toggle shows Web or Work. Record the surface name in the Setup sheet, because grounding differs between them."),
            ("Establish how grounding works", "Ask Copilot the primary prompt. Copilot combines your prompt with permitted work context; it can never show you a file you could not already open yourself."),
            ("Write a prompt using the four-part contract", "Every prompt states the Goal, the Context, the Source and the Expectation. Record each of the four parts in the Prompt_Log sheet."),
            ("Re-run the prompt with an explicit source", "Attach or reference a specific file, then compare the grounded answer with the ungrounded one and note the difference."),
            ("Identify three claims that need verification", "Copy each claim into the Evidence_Register and record where it would be checked."),
            ("Record a review decision for every claim", "Mark each claim Verified, Corrected or Rejected. A claim that cannot be traced to a source is never released."),
            ("Complete the Acceptance_Check sheet", "Confirm the surface, the grounding source, three evidence-backed gaps and a verification status for every claim."),
        ],
        test="The register identifies the active Copilot surface, the grounding source, three evidence-backed gaps, and a verification status for every claim.",
        evidence="Completed workbook with Prompt_Log and Evidence_Register, plus a credential-safe screenshot of the Copilot surface.",
        files=[("Lumina-Living-Lab-01.xlsx", "Setup, prompt-log and evidence register workbook")],
    ),
    dict(
        num=2, topic=1, day=1, level="Foundation",
        title="Draft a Project Brief in Word from Excel Evidence",
        objective="Produce a governed business document in Word grounded in an approved data source",
        km="K2", am="A2",
        apps="Word, Excel, Copilot",
        desc="The learner uses Copilot in Word with a supplied template and workbook to draft a two-page launch brief, then traces every objective, milestone, risk and number back to the workbook.",
        build="A two-page launch brief with cited objectives, milestones, risks and open questions",
        services="Word Copilot, Excel, reference documents",
        prompt=("Draft a two-page project brief for the Sustainable Workspace campaign using the attached "
                "template and workbook. Include purpose, three measurable objectives, scope, milestones, "
                "budget, risks and open questions. Use only figures that appear in the workbook and mark "
                "anything uncertain as an open question."),
        steps=[
            ("Open the supplied brief template in Word", "Keep the template headings; they are the agreed structure for a Lumina Living brief."),
            ("Reference the workbook as the evidence source", "Use Copilot's reference-a-file option so the draft is grounded in the supplied numbers rather than invented ones."),
            ("Generate the first draft with the primary prompt", "Copilot drafts into the template structure. Treat the output as a proposal, not a finished document."),
            ("Check every number against the workbook", "Open the Brief_Data sheet and confirm each figure. Record the sheet and cell range for each one in Evidence_Register."),
            ("Rewrite any unsupported sentence as an open question", "A claim with no source does not become a fact by being well written; move it to the Open Questions section."),
            ("Tighten the tone for a leadership audience", "Ask Copilot to make the brief concise and decision-focused while keeping every cited figure unchanged."),
            ("Record the review decision and approver", "Complete Acceptance_Check so the brief has a named reviewer before it is circulated."),
        ],
        test="The brief fills every template heading, all figures trace to the workbook, and unsupported statements appear as open questions rather than claims.",
        evidence="Completed brief, workbook with Evidence_Register, and the named review decision.",
        files=[("Lumina-Living-Lab-02.xlsx", "Brief data and evidence register workbook"),
               ("Lumina-Living-Project-Brief-Template.docx", "Word brief template with the agreed headings")],
    ),
    dict(
        num=3, topic=1, day=1, level="Intermediate",
        title="Refine a Responsible Copilot Use Policy in Word",
        objective="Use Copilot to review, improve and simplify an existing governance document",
        km="K1", am="A2",
        apps="Word, Excel, Copilot",
        desc="The learner reviews a draft internal policy with Copilot, identifies gaps and ambiguities, rewrites the weak clauses, and produces a one-page staff quick-reference from the approved text.",
        build="An approved policy draft, an issue log and a staff quick-reference checklist",
        services="Word Copilot, Excel, document review",
        prompt=("Review the attached Responsible Copilot Use Policy. Identify unclear obligations, missing "
                "controls and any clause that a staff member could not act on. For each issue give the clause, "
                "the problem and a suggested rewrite. Do not add controls the organisation has not stated."),
        steps=[
            ("Open the supplied policy draft in Word", "Read it once yourself before asking Copilot; you need your own view to judge the suggestions."),
            ("Ask Copilot to critique the policy against the primary prompt", "Copilot returns issues with suggested rewrites. Log each one in the Issue_Log sheet."),
            ("Classify each issue by severity and owner", "Not every suggestion should be accepted; record Accept, Amend or Reject with a reason."),
            ("Rewrite the accepted clauses in place", "Ask Copilot to rewrite only the clauses you accepted, keeping the defined terms unchanged."),
            ("Check the policy still matches organisational reality", "A policy that promises a control the organisation does not operate is worse than no policy."),
            ("Generate a one-page staff quick-reference", "Ask Copilot to summarise the approved policy as a short do/do-not checklist in plain English."),
            ("Record the approval decision", "Complete Acceptance_Check with the reviewer and the date of approval."),
        ],
        test="Every logged issue has a decision and a rationale, the rewritten policy keeps its defined terms, and the quick-reference matches the approved text.",
        evidence="Revised policy, issue log with decisions, and the staff quick-reference.",
        files=[("Lumina-Living-Lab-03.xlsx", "Issue log and acceptance workbook"),
               ("Responsible-Copilot-Use-Policy-Draft.docx", "Draft policy to be reviewed")],
    ),
    dict(
        num=4, topic=1, day=1, level="Intermediate",
        title="Build a PowerPoint Story from Word and Excel",
        objective="Convert an approved brief and supporting data into a decision-led presentation",
        km="K2", am="A2",
        apps="PowerPoint, Word, Excel, Copilot",
        desc="The learner generates a leadership deck from the approved brief and workbook, checks every claim against its source, and ends the deck with a specific decision request.",
        build="An eight-slide leadership deck with one message per slide and a documented evidence map",
        services="PowerPoint Copilot, Word, Excel",
        prompt=("Create an eight-slide leadership presentation for the Sustainable Workspace campaign using "
                "the attached project brief and workbook. Build a decision-led story: context, customer need, "
                "campaign idea, target audience, timeline, budget, risks and approval request. Use concise "
                "slide titles that state the takeaway. Do not invent numbers."),
        steps=[
            ("Review the brief and the presentation data", "Complete the Evidence_Map before generating slides so you know what each slide must prove."),
            ("Open the supplied blank deck and confirm the 16:9 layout", "Retain the Lumina Living theme and footer so the deck matches house branding."),
            ("Create the outline with Copilot", "Generate the outline first and review it before slides are built; fixing a story at outline stage is far cheaper."),
            ("Check that every slide earns its place", "Each slide must answer why it matters or what decision is needed, or it should be cut."),
            ("Generate the presentation and replace generic imagery", "Swap stock imagery for editable shapes or approved visuals; never use a decorative chart."),
            ("Verify every number against the workbook", "Record slide number, source sheet and cell range in Evidence_Map for each quantitative claim."),
            ("Run an accessibility and legibility check", "Check title size, colour contrast, alt text and reading order before the deck is shared."),
        ],
        test="The deck contains eight coherent slides, all quantitative claims trace to the workbook, and the final slide asks for a specific decision.",
        evidence="Completed deck, workbook with Evidence_Map, and a credential-safe screenshot.",
        files=[("Lumina-Living-Lab-04.xlsx", "Presentation data and evidence map workbook"),
               ("Lumina-Living-Approved-Project-Brief.docx", "The approved brief from Lab 02"),
               ("Lumina-Living-Blank-Leadership-Deck.pptx", "Branded blank 16:9 deck")],
    ),
    dict(
        num=5, topic=1, day=1, level="Intermediate",
        title="Enhance PowerPoint with Native Charts and Speaker Notes",
        objective="Turn a draft deck into a presentation-ready story with verifiable native charts",
        km="K2", am="A2",
        apps="PowerPoint, Excel, Copilot",
        desc="The learner replaces picture-charts with native editable PowerPoint charts driven by the workbook, then generates and verifies speaker notes that match what each chart actually shows.",
        build="A polished deck with native trend, contribution and variance charts plus verified speaker notes",
        services="PowerPoint Copilot, native charts, Excel",
        prompt=("Review this deck against the attached workbook. For each data slide, tell me which chart type "
                "communicates the message most honestly, what the axis and units should be, and what a presenter "
                "should say. Flag any chart whose visual impression overstates the underlying numbers."),
        steps=[
            ("Identify every slide that makes a quantitative claim", "List them in Chart_Plan with the message each slide is meant to deliver."),
            ("Choose the honest chart type for each message", "Trend over time is a line; contribution is a bar or stacked bar; variance against target is a clustered bar."),
            ("Insert native PowerPoint charts driven by the workbook figures", "A native chart keeps its data editable and auditable; a pasted image cannot be checked."),
            ("Label axes, units and the source on every chart", "An unlabelled axis is where a misleading chart hides."),
            ("Ask Copilot to draft speaker notes for each data slide", "Then verify each note against the chart; a note that overstates the data is a defect."),
            ("Check for visual exaggeration", "Confirm that no axis is truncated in a way that overstates a difference."),
            ("Complete the Acceptance_Check", "Every chart must be native, labelled, sourced and consistent with its speaker note."),
        ],
        test="Every data slide carries a native, labelled chart traceable to the workbook, and each speaker note states only what its chart actually shows.",
        evidence="Enhanced deck, workbook with Chart_Plan, and the verified speaker notes.",
        files=[("Lumina-Living-Lab-05.xlsx", "Chart plan and source data workbook"),
               ("Lumina-Living-Leadership-Deck-Draft.pptx", "Draft deck to be enhanced")],
    ),
]
