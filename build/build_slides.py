#!/usr/bin/env python3
"""Build the course slide deck. Highly visual: every teaching slide is a component
(tile grid, process map, decision map, comparison table, native chart, stat row).
NO step-by-step procedures appear in the deck — those live in the Learner Guide
and the per-lab instruction PDFs."""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
REPO=os.path.dirname(HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2; from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4; from data_domain5 import DOMAIN5
from data_teaching import TEACHING
from data_teaching2 import TEACHING2
from deck_components import Deck, BLUE, TEAL, VIOLET, AMBER, GREY, INK, RED, GREEN
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5

D=Deck(C, os.path.join(REPO,"courseware","assets"))

def render(spec):
    """Dispatch a teaching spec to its visual component.

    Shapes (index 0 is always the kind):
      tile     (title, kicker, items, cols, size)
      process  (title, kicker, nodes, note)
      compare  (title, kicker, headers, rows, note)
      two_col  (title, kicker, left, right, _unused, lhead, rhead, size)
      big      (line1, line2, kicker)
      decision (title, question, yes, no, note)
      chart    (title, kind, categories, series, lens)
      stat     (title, kicker, stats, note)
      content  (title, kicker, items)
    """
    k=spec[0]
    if   k=="tile":    D.tile_grid(spec[1],spec[3],kicker=spec[2],cols=spec[4],size=spec[5])
    elif k=="cards":   D.cards3(spec[1],spec[3],kicker=spec[2])
    elif k=="process": D.process_map(spec[1],spec[3],kicker=spec[2],
                                     note=spec[4] if len(spec)>4 else None)
    elif k=="compare": D.compare_table(spec[1],spec[3],spec[4],kicker=spec[2],
                                       note=spec[5] if len(spec)>5 else None)
    elif k=="two_col": D.two_col(spec[1],spec[3],spec[4],kicker=spec[2],
                                 lhead=spec[6],rhead=spec[7],
                                 size=spec[8] if len(spec)>8 else 15)
    elif k=="big":     D.big_statement(spec[1],spec[2],spec[3])
    elif k=="decision":D.decision_map(spec[1],spec[2],spec[3],spec[4],
                                      kicker="DECISION RULE",
                                      note=spec[5] if len(spec)>5 else None)
    elif k=="chart":   D.chart_slide(spec[1],spec[2],spec[3],spec[4],
                                     lens=spec[5] if len(spec)>5 else None)
    elif k=="stat":    D.stat_row(spec[1],spec[3],kicker=spec[2],
                                  note=spec[4] if len(spec)>4 else None)
    elif k=="content": D.content(spec[1],spec[3],kicker=spec[2])
    else: raise ValueError(f"unknown teaching spec kind: {k}")


def traqom_slide():
    """Digital attendance as a numbered flow plus the conditions that govern it —
    never a bullet list (wsq-slides hard rule 1)."""
    D.flow_h("Digital Attendance (Mandatory)",[
      "Trainer displays the SSG digital attendance QR code",
      "Scan it with your phone camera",
      "Submit your attendance",
      "Repeat AM, PM and on assessment day"],
      kicker="TRAQOM · SSG DIGITAL ATTENDANCE",color=VIOLET)

def assessment_table(kicker):
    """The two instruments side by side, plus the conditions that apply to both."""
    D.compare_table("Assessment",
      ["","Written Assessment (WA)","Practical Performance (PP)"],
      [["Format","Short-answer questions (SAQ)","Hands-on practical tasks"],
       ["What it tests","Underpinning knowledge K1-K5","Practical ability A1-A8"],
       ["Duration","1 hour","1 hour"],
       ["Conditions","Open book, individual","Open book, individual"],
       ["Submission","On the LMS","On the LMS, with evidence"]],
      kicker=kicker,
      note="Open book: slides, Learner Guide and your completed lab files. "
           "75% attendance is required; a re-assessment and appeal process is available.")

def lab_process_map(a):
    """A four-stage process map per lab: the SHAPE of the work, not the clicks.

    Captions come from data_stages.STAGES — hand-authored complete phrases. They
    are never derived by truncating a step title, because a character chop leaves
    mid-phrase fragments ending on dangling function words.
    """
    from data_stages import STAGES
    caps = STAGES[a["num"]]
    labels = ["Prepare","Generate","Verify","Record"]
    nodes = list(zip(labels, caps))
    D.process_map(f"How Lab {a['num']:02d} Runs", nodes,
                  kicker=f"LAB {a['num']:02d} · PROCESS", color=TEAL,
                  note=f"The shape of the work. Full step-by-step is in the Learner Guide "
                       f"(Lab {a['num']:02d}) and the lab's instruction PDF.")

TRAQOM=["It is mandatory to take the AM, PM and Assessment digital attendance for WSQ-funded courses.",
        "The trainer or administrator displays the digital attendance QR code from the SSG portal.",
        "Scan the QR code with your mobile phone camera and submit your attendance.",
        "A minimum of 75% attendance is required to be eligible for assessment and funding."]
AFLOW=["TRAQOM survey — scan the QR code on the LMS",
       "Assessment digital attendance — scan the SSG QR",
       "Sit WA (SAQ) then PP — open book",
       "Submit your answers on the LMS",
       "Sign the Assessment Summary Record"]

# ============================================================ COVER + ADMIN
D.cover("COPILOT","MICROSOFT 365")
D.section("COURSE ADMINISTRATION","Welcome & Housekeeping","")
traqom_slide()
D.trainer_slide("YOUR TRAINER · GENERAL","Your Trainer",
  "General Trainer template —\nto be completed by the trainer",
  [("Name",""),("Title / Designation",""),("Qualifications",""),
   ("Areas of expertise",""),("Training & industry experience",""),("Contact","")],
  initials="?",accent=GREY)
D.trainer_slide("YOUR TRAINER",C.TRAINER,"Principal Trainer\nTertiary Infotech Academy Pte Ltd",
  [("Role","Principal Trainer, Tertiary Infotech Academy Pte Ltd"),
   ("Certification","Microsoft certified — Power Platform, Microsoft 365 and AI solutions."),
   ("Delivers","WSQ courses on Microsoft Copilot, Power Automate and automation."),
   ("Founder","Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
  initials="AA",accent=BLUE)
D.tile_grid("Let's Know Each Other",[
  ("Who you are","Your name, your organisation and the role you play in it."),
  ("What you repeat","The task you find yourself redoing most often each week."),
  ("What you want back","The hours you would reclaim if that task ran itself."),
  ("Where you want to get to","What you want to automate or produce faster after this week.")],
  kicker="ICE-BREAKER",cols=2,size=15)
D.tile_grid("Ground Rules",[
  "Set your mobile phone to silent mode.","Participate actively — no question is too small.",
  "Mutual respect: agree to disagree.","One conversation at a time.",
  "Be punctual; return from breaks on time.","75% attendance is required."],
  kicker="HOUSEKEEPING",cols=2,size=15)
D.tile_grid("Download Your Course Material",[
  ("LMS / TMS portal","lms-tms.tertiaryinfotech.com — sign in with the account issued to you."),
  ("Trainer slides","The deck used in class, as a PDF for reference."),
  ("Learner Guide","Every lab's full step-by-step procedure and prompts."),
  ("Lab files","Each lab folder holds its own data and instruction PDF."),
  ("Lesson Plan","The daily schedule and what is covered when."),
  ("Open book","You may use these materials during the assessment.")],
  kicker="COURSE REPOSITORY",cols=2,size=14)
D.tile_grid("What You Will Achieve",[
  ("Copilot for content","Produce verified business content in Word, PowerPoint, Excel and Outlook."),
  ("Feasibility scanning","Identify which work is worth automating, and what it would take."),
  ("Power Automate","Build flows that integrate Forms, Outlook, Excel and Approvals."),
  ("Copilot Studio agents","Design, ground, tool and publish agents that behave."),
  ("Integration","Connect automation to other systems over HTTP with a schema."),
  ("Testing and governance","Verify behaviour, gate consequential actions and diagnose failures.")],
  kicker="LEARNING OUTCOMES",cols=2,size=14)
D.tile_grid("Learning Outcomes",
  [(lo.split(":")[0], lo.split(":",1)[1].strip()) for lo in C.LEARNING_OUTCOMES],
  kicker="WSQ COURSE OUTCOMES",cols=1,size=14)
D.tile_grid("Lesson Plan — 5 Days, 8 Hours a Day",[
  (f"Day 1 — {C.DAY_THEMES[1]}","Topic 01 · Labs 01–05"),
  (f"Day 2 — {C.DAY_THEMES[2]}","Topic 02 · Labs 06–10"),
  (f"Day 3 — {C.DAY_THEMES[3]}","Topic 03 · Labs 11–15"),
  (f"Day 4 — {C.DAY_THEMES[4]}","Topic 04 · Labs 16–20"),
  (f"Day 5 — {C.DAY_THEMES[5]}","Topic 05 · Labs 21–25 + Assessment"),
  ("Daily timing","9:30am–6:30pm · 1-hour lunch · tea breaks within")],
  kicker="SCHEDULE",cols=2,size=14)
D.tile_grid("The Course Scenario",[
  ("Lumina Living Pte Ltd","A Singapore workspace-furniture company."),
  ("The Sustainable Workspace campaign","One connected scenario across all 25 labs."),
  ("Day 1–2","You create and verify the campaign's content."),
  ("Day 3–5","You automate the process behind it and put agents on it.")],
  kicker="ONE STORY, TWENTY-FIVE LABS",cols=2,size=15)
D.tile_grid("Briefing for Assessment",[
  ("Phones away","Place phones and other materials under the table or on the floor."),
  ("No recording","No photos or recording of assessment scripts, at any point."),
  ("No discussion","Work individually — no discussion once the assessment starts."),
  ("Black or blue pen","Use a black or blue pen for any hard-copy assessment."),
  ("No correction fluid","No liquid paper or correction tape; strike through instead."),
  ("Time is called","Scripts are collected when time is up — submit before then.")],
  kicker="BEFORE ASSESSMENT",cols=2,size=14)
assessment_table("FINAL ASSESSMENT")
D.flow_h("Assessment Flow",AFLOW,kicker="ON ASSESSMENT DAY")

# ============================================================ TOPICS
TOPIC_ACTS={t["num"]:[a for a in ACT if a["topic"]==t["num"]] for t in C.TOPICS}
CARD_COLORS=[BLUE,TEAL,VIOLET]
for ti,t in enumerate(C.TOPICS):
    n=t["num"]
    D.section(f"TOPIC {t['code']}", t["title"], t["code"], t["subtitle"])
    D.tile_grid(f"Key Concepts — Topic {t['code']}", t["concepts"],
                kicker=f"{t['days'].upper()} · WHAT THIS TOPIC COVERS", cols=2, size=14)
    acts=TOPIC_ACTS[n]
    third=(len(acts)+2)//3
    groups=[acts[i:i+third] for i in range(0,len(acts),third)][:3]
    while len(groups)<3: groups.append([])
    cards=[(CARD_COLORS[gi],
            f"Labs {g[0]['num']:02d}–{g[-1]['num']:02d}" if g else "—",
            [a["title"] for a in g] if g else ["—"]) for gi,g in enumerate(groups)]
    D.cards3(f"Hands-On Labs — Topic {t['code']}", cards, kicker="WHAT YOU WILL DO")
    # ---- teaching slides: concept pass, then the deepening pass ----
    for spec in TEACHING[n]: render(spec)
    D.brk("Tea Break","10 minutes")
    for spec in TEACHING2.get(n,[]): render(spec)
    # ---- labs: overview + acceptance only (NO steps in the deck) ----
    for a in acts:
        D.lab_overview(f"LAB {a['num']:02d}", a["title"], a["desc"], a["build"], a["apps"],
                       kicker=f"TOPIC {t['code']} · {a['level'].upper()}",
                       align=f"{a['km']} · {a['am']}", level=a['level'])
        lab_process_map(a)
        D.test_slide(a["title"], a["test"], kicker=f"LAB {a['num']:02d} · ACCEPTANCE")
    D.tile_grid(f"Recap — Topic {t['code']}",
                [(f"Lab {a['num']:02d}", a["objective"]) for a in acts],
                kicker="WHAT YOU CAN NOW DO", cols=2, size=13)
    if n<5: D.brk(f"End of Day {n}", "See you tomorrow", color=TEAL)

# ============================================================ CLOSE
D.section("WRAP-UP","Course Summary & Next Steps","")
D.tile_grid("What You Achieved",[
  ("Copilot for content","Verified business content in Word, PowerPoint, Excel and Outlook."),
  ("Feasibility scanning","Identified and scoped automation opportunities."),
  ("Power Automate","Built flows with triggers, actions, conditions and approvals."),
  ("Copilot Studio agents","Designed, grounded, tooled, orchestrated and published agents."),
  ("Integration","Connected automation over HTTP with a JSON schema."),
  ("Testing and governance","Tested behaviour, gated actions and diagnosed failures.")],
  kicker="LEARNING OUTCOMES",cols=2,size=14)
D.tile_grid("Taking This Back to Work",[
  ("Start with one process","Pick something repetitive, rule-based and time-consuming."),
  ("Write the prompt contract","Goal, context, source, expectation — every time."),
  ("Ground before you trust","An answer with no source is a draft, not a fact."),
  ("Gate the consequential step","Decide the boundary of agency before you build."),
  ("Keep the evidence","Prompt log, evidence register and run history."),
  ("Review the run history","Recurring failures are telling you about the design.")],
  kicker="NEXT STEPS",cols=2,size=14)
assessment_table("WRAP-UP · FINAL ASSESSMENT")
D.flow_h("Assessment Flow",AFLOW,kicker="ON ASSESSMENT DAY")
traqom_slide()
D.big_statement("Thank You!",
  "You can now create verified content with Copilot and automate the process behind it.",
  "SEE YOU IN CLASS",color=TEAL)

OUT=os.path.join(REPO,"courseware",f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
n=D.save(OUT)
print(f"Saved {OUT}  ({n} slides)")
