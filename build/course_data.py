"""
SINGLE SOURCE OF TRUTH — Microsoft Copilot for Content Creation and Task Automation.

Every artifact (slide deck PPT, Lesson Plan LP, Learner Guide LG + Markdown mirror,
labs/ folder and the assessment) is generated from this module plus data_domainN.py,
so titles, lab numbering, learning outcomes, the schedule and the assessment can
never drift apart.

Day 1-2  Copilot for Content Creation  (Word, Excel, PowerPoint, Outlook)
Day 3-5  Copilot for Workflow and Agents (Power Automate, Copilot Studio)
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Microsoft Copilot for Content Creation and Task Automation"
SHORT_TITLE  = "Microsoft Copilot for Content Creation and Task Automation"
COURSE_CODE  = "TGS-2024042588"
VERSION      = "v1.0"
VERSION_DATE = "1 September 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 5
TRAINING_HOURS = 38
COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-copilot-for-power-automate.html"

# ------------------------------------------------------------------ outcomes
# Kept verbatim from the approved TGS course record so the courseware, the LMS
# record and the assessment all state the same four outcomes.
LEARNING_OUTCOMES = [
    "LO1: Identify opportunities and perform feasibility scans for dataverse and Power App applications.",
    "LO2: Utilise Business Flow and Power Automate to integrate functions across programs with API-level integration.",
    "LO3: Execute tests in Power Virtual Agent and Power BI to verify their functioning across platforms.",
    "LO4: Implement modifications to Power Platform with Power AI Builder and highlight technical issues.",
]

# Knowledge (K) and Ability (A) codes assessed by the WA and PP papers.
KNOWLEDGE = [
    ("K1", "Copilot grounding, the prompt contract and the human verification duty across Microsoft 365 apps."),
    ("K2", "Content-creation patterns for Word, PowerPoint, Excel and Outlook, and how evidence is traced to a source."),
    ("K3", "Business process automation: the Trigger to Actions to Output model, trigger families and action families."),
    ("K4", "Agent anatomy in Copilot Studio: instructions, knowledge, tools, skills and connected agents."),
    ("K5", "Integration, testing, security and the boundary of agency, including human-in-the-loop review gates."),
]
ABILITIES = [
    ("A1", "Scan a business workflow and identify feasible Copilot and Power Platform automation opportunities."),
    ("A2", "Produce verified business content with Copilot in Word, PowerPoint, Excel and Outlook."),
    ("A3", "Build Power Automate flows that integrate Forms, Outlook, Excel and Approvals."),
    ("A4", "Integrate a flow or agent with an external system over HTTP using a JSON schema."),
    ("A5", "Create and ground a Copilot Studio agent in approved knowledge and publish it to a channel."),
    ("A6", "Test an agent and a flow, verify refusals, and inspect run history to confirm behaviour."),
    ("A7", "Apply a human review gate so a consequential action requires a person before it takes effect."),
    ("A8", "Diagnose technical, data-quality and permission issues in an automation and record the fix."),
]

# ------------------------------------------------------------------ topics
# num, code, title, subtitle, weighting, concept bullets for the section
TOPICS = [
    dict(num=1, code="01",
         title="Copilot Foundations and Content Creation in Word and PowerPoint",
         subtitle="Grounding · responsible use · prompt design · drafting · presentation storytelling",
         weighting="Day 1",
         days="Day 1",
         concepts=[
            "Microsoft 365 Copilot combines your prompt with permitted work context; existing access permissions always still apply.",
            "The prompt contract states the goal, the context, the source and the expected output format, then verifies the result.",
            "Copilot proposes and the user disposes: the human checks evidence, tone, sensitivity and final release.",
            "Word turns approved evidence into a structured narrative; a reference document keeps the draft anchored to fact.",
            "PowerPoint converts an approved narrative into a decision-led story with one message per slide.",
            "Responsible AI principles — fairness, reliability, privacy, inclusiveness, transparency and accountability — govern every use.",
         ]),
    dict(num=2, code="02",
         title="Copilot for Excel and Outlook: Analysis and Communication",
         subtitle="Analysis-ready data · formulas · diagnostics · forecasting · inbox triage · controlled replies",
         weighting="Day 2",
         days="Day 2",
         concepts=[
            "Copilot analyses an Excel Table with one header row, one record per row and consistent data types.",
            "Analysis progresses from descriptive to diagnostic, then predictive and prescriptive questions.",
            "A suggested formula is a proposal: check its logic, references and edge cases before you accept it.",
            "Scenario modelling separates assumptions from formulas so base, downside and upside cases can be compared.",
            "Outlook Copilot triages a mailbox, summarises a thread and drafts a reply, but a person always sends it.",
            "Every quantitative claim must trace back to a named sheet and cell range before it is used in a decision.",
         ]),
    dict(num=3, code="03",
         title="Business Process Automation with Power Automate",
         subtitle="BPA · the Power Platform · triggers · actions · dynamic content · conditions · approvals",
         weighting="Day 3",
         days="Day 3",
         concepts=[
            "Business process automation replaces repeated manual handovers with a reliable, auditable flow.",
            "Every flow is Trigger then Actions then Output: something happens, steps run, a result is produced.",
            "The four trigger families are automated, instant, scheduled and business-process triggers.",
            "Dynamic content passes data from one step to the next; the run history shows exactly what each step received.",
            "A condition branches a flow so different inputs follow different paths.",
            "An approval action suspends the run until a named person responds, which is human-in-the-loop by design.",
         ]),
    dict(num=4, code="04",
         title="Designing and Building Copilot Studio Agents",
         subtitle="Workflow vs agent · instructions · knowledge · tools · skills · connected agents · publishing",
         weighting="Day 4",
         days="Day 4",
         concepts=[
            "A workflow follows a fixed path; an agent decides which step to take next from its instructions.",
            "An agent is made of instructions, knowledge, tools, skills and connected agents.",
            "Instructions shape behaviour but are not enforced; tools, schemas and approvals are what actually enforce limits.",
            "Grounding an agent in approved knowledge is what makes its answers citable and its refusals correct.",
            "A tool lets an agent act on a system; a connected agent delegates a task to another specialised agent.",
            "Publishing to a channel such as Microsoft Teams makes the agent available to real users.",
         ]),
    dict(num=5, code="05",
         title="Integrating, Testing, Securing and Optimising Agentic Automation",
         subtitle="Agent flows · HTTP · JSON schema · RAG · human review · testing · governance",
         weighting="Day 5",
         days="Day 5",
         concepts=[
            "An agent flow exposes automation to an agent, and an HTTP trigger exposes it to any external application.",
            "A JSON schema defines the request contract so an external caller and the flow agree on the data.",
            "Structured output turns a model response into named fields a flow can branch on reliably.",
            "Retrieval-augmented generation grounds answers in retrieved passages instead of model memory.",
            "The boundary of agency decides what an agent may do alone and what needs a person to approve.",
            "Testing means verifying correct answers, correct refusals and the run history behind both.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Copilot Foundations, Word and PowerPoint",
    2: "Copilot for Excel and Outlook",
    3: "Business Process Automation with Power Automate",
    4: "Copilot Studio Agents",
    5: "Integration, Testing, Security and Assessment",
}

# Which topics are taught on which day (used by the LP schedule + deck).
DAY_TOPICS = {1: [1], 2: [2], 3: [3], 4: [4], 5: [5]}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — hands-on Copilot and Power Platform tasks, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
