#!/usr/bin/env python3
"""Generate the Lesson Plan (LP) DOCX in the WSQ house format.

Each training day totals exactly 480 instructional minutes (8 hours), 9:00am-6:00pm
with a 1-hour lunch excluded; tea breaks are counted within the 8 hours.
"""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
REPO=os.path.dirname(HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2; from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4; from data_domain5 import DOMAIN5
import prodoc
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5
ASSETS=os.path.join(REPO,"courseware","assets")
BRAND=prodoc.BRAND; DARK=prodoc.DARK; GREY=prodoc.GREY

# --------------------------------------------------- day schedules (480 min each)
DAY_TRAINING_MIN   = 480          # Days 1-4: a full 8 instructional hours
ASSESSMENT_MIN     = 120          # WA 60 + PP 60 on the final day
# The TGS record for this course is 38 training hours + 2 assessment hours, so the
# final day carries whatever training minutes remain after four full days.
LAST_DAY_TRAINING  = C.TRAINING_HOURS*60 - DAY_TRAINING_MIN*(C.DAYS-1)   # = 360

def _clock(start_min):
    h,m=divmod(start_min,60); return f"{h}:{m:02d}"
def _span(start_min,dur):
    return f"{_clock(start_min)}-{_clock(start_min+dur)}", start_min+dur

def day_rows(day):
    """One day's schedule, built on a running clock so the times always add up.

    House window is 9:30am-6:30pm with a 1-hour lunch (tertiary-lesson-plan
    SKILL.md). Days 1-4 carry 480 instructional minutes. Day 5 carries
    LAST_DAY_TRAINING training minutes plus the 120-minute assessment, so the
    course totals exactly 38 training hours + 2 assessment hours. Lunch is
    excluded from the instructional total; tea breaks are counted within it.
    """
    t={t_["num"]:t_ for t_ in C.TOPICS}[day]
    labs=[a for a in ACT if a["day"]==day]
    lab_lo=labs[0]["num"]; lab_hi=labs[-1]["num"]
    last=(day==C.DAYS)
    budget = LAST_DAY_TRAINING if last else DAY_TRAINING_MIN

    # Fixed elements of every day, then the lab time is whatever remains.
    open_m, tea1, tea2 = 20, 10, 10
    close_m = 30 if last else 40              # recap (+ assessment admin on day 5)
    concept = 70
    lab_budget = budget - (open_m+tea1+tea2+close_m+concept)
    # Split the lab budget across four blocks (two paired, then three singles).
    b1 = lab_budget*80//280                    # morning paired block
    b2 = lab_budget*90//280
    b3 = lab_budget*70//280
    b4 = lab_budget - (b1+b2+b3)               # remainder keeps the total exact

    rows=[]; t0=9*60+30       # house window: 9:30am start, 6:30pm finish
    sp,t0=_span(t0,open_m)
    rows.append((sp,f"{open_m} min",
        "Welcome, AM digital attendance (TRAQOM), objectives for the day" if day==1
        else f"Day {day-1} recap, AM digital attendance (TRAQOM), objectives for the day",
        "Facilitated briefing","Admin"))
    sp,t0=_span(t0,concept)
    rows.append((sp,f"{concept} min",f"Topic {t['code']}: {t['subtitle']}",
        "Concept briefing with visual models and worked examples",f"Topic {t['code']}"))
    sp,t0=_span(t0,tea1); rows.append((sp,f"{tea1} min","Tea break","Break","—"))
    sp,t0=_span(t0,b1)
    rows.append((sp,f"{b1} min",f"Lab {lab_lo:02d} and Lab {lab_lo+1:02d}",
        "Demonstration then individual hands-on practice",f"Labs {lab_lo:02d}-{lab_lo+1:02d}"))
    lunch_start=t0; t0+=60
    rows.append((f"{_clock(lunch_start)}-{_clock(t0)}","—",
        "Lunch (1 hour, not counted in the instructional hours)","Break","—"))
    sp,t0=_span(t0,b2)
    rows.append((sp,f"{b2} min",f"Lab {lab_lo+2:02d}: {labs[2]['title']}",
        "Guided hands-on practice with acceptance check",f"Lab {lab_lo+2:02d}"))
    sp,t0=_span(t0,b3)
    rows.append((sp,f"{b3} min",f"Lab {lab_lo+3:02d}: {labs[3]['title']}",
        "Guided hands-on practice with acceptance check",f"Lab {lab_lo+3:02d}"))
    sp,t0=_span(t0,tea2); rows.append((sp,f"{tea2} min","Tea break","Break","—"))
    sp,t0=_span(t0,b4)
    rows.append((sp,f"{b4} min",
        f"Lab {lab_hi:02d}: {labs[4]['title']}" + (" (capstone)" if last else ""),
        "Individual hands-on practice" if last else "Guided hands-on practice with acceptance check",
        f"Lab {lab_hi:02d}"))
    if last:
        sp,t0=_span(t0,20)
        rows.append((sp,"20 min","Course recap and briefing for assessment","Facilitated briefing","Admin"))
        sp,t0=_span(t0,10)
        rows.append((sp,"10 min","Assessment digital attendance (TRAQOM) and TRAQOM survey","Admin","Admin"))
        sp,t0=_span(t0,60)
        rows.append((sp,"60 min","Written Assessment (WA) — SAQ, open book","Individual assessment","Assessment"))
        sp,t0=_span(t0,60)
        rows.append((sp,"60 min","Practical Performance (PP) — open book","Individual assessment","Assessment"))
    else:
        sp,t0=_span(t0,close_m)
        rows.append((sp,f"{close_m} min",
            f"Topic {t['code']} recap, Q&A, PM digital attendance (TRAQOM)","Facilitated review","Recap"))
    return rows

def instructional_minutes(rows):
    tot=0
    for _,dur,_,_,_ in rows:
        if dur.endswith("min"): tot+=int(dur.split()[0])
    return tot

def build():
    doc=Document()
    st=doc.styles["Normal"]; st.font.name="Arial"; st.font.size=Pt(11)
    for s in doc.sections:
        s.top_margin=Inches(0.9); s.bottom_margin=Inches(0.9)
        s.left_margin=Inches(1.0); s.right_margin=Inches(1.0)
    prodoc.style_headings(doc)
    prodoc.add_cover_page(doc,"LESSON PLAN",C.TITLE,C.VERSION.lstrip("v"),
        org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
        course_code=C.COURSE_CODE)
    prodoc.add_version_control(doc,[
        (C.VERSION.lstrip("v"), C.VERSION_DATE,
         "First release of the five-day lesson plan covering Copilot for content creation "
         "(Days 1-2) and Copilot for workflow and agents (Days 3-5), aligned to the v1.0 deck, "
         "Learner Guide and the WA/PP assessment.", C.TRAINER)])
    prodoc.add_toc(doc)

    doc.add_heading("Course Overview",level=1)
    doc.add_paragraph(
        f"{C.TITLE} is a five-day, {C.TRAINING_HOURS}-hour WSQ programme. Days 1 and 2 build the "
        "ability to create verified business content with Microsoft 365 Copilot in Word, PowerPoint, "
        "Excel and Outlook. Days 3 to 5 build the ability to automate the process behind that content "
        "with Power Automate and Copilot Studio agents, and to integrate, test, secure and govern the "
        "result. All twenty-five labs follow one connected scenario — Lumina Living Pte Ltd and its "
        "Sustainable Workspace campaign — so each day builds on the last.")
    t=doc.add_table(rows=0,cols=2); t.style="Table Grid"
    for k,v in [("Course Code",C.COURSE_CODE),
                ("Training Duration",f"{C.TRAINING_HOURS} hours across {C.DAYS} days"),
                ("Assessment","WA (SAQ) 60 minutes; PP 60 minutes — both open book"),
                ("Mode of Delivery","Classroom, instructor-led, with individual hands-on labs"),
                ("Trainer",C.TRAINER),
                ("Class Size","Maximum 20 learners"),
                ("Attendance","A minimum of 75% attendance is required for assessment and funding")]:
        c=t.add_row().cells
        c[0].text=""; r=c[0].paragraphs[0].add_run(k); r.bold=True; r.font.size=Pt(10)
        c[1].text=""; r2=c[1].paragraphs[0].add_run(v); r2.font.size=Pt(10)
    doc.add_paragraph()

    doc.add_heading("Learning Outcomes",level=1)
    for lo in C.LEARNING_OUTCOMES: doc.add_paragraph(lo,style="List Bullet")

    doc.add_heading("Assessed Knowledge and Abilities",level=1)
    doc.add_paragraph("The Written Assessment covers every knowledge statement (K) and the Practical "
                      "Performance covers every ability statement (A).")
    t=doc.add_table(rows=0,cols=2); t.style="Table Grid"
    hr=t.add_row().cells
    for i,h in enumerate(["Code","Statement"]):
        hr[i].text=""; r=hr[i].paragraphs[0].add_run(h)
        r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        prodoc._shade_cell(hr[i],"1F6FEB")
    for code,txt in list(C.KNOWLEDGE)+list(C.ABILITIES):
        c=t.add_row().cells
        c[0].text=""; r=c[0].paragraphs[0].add_run(code); r.bold=True; r.font.size=Pt(9.5)
        c[1].text=""; r2=c[1].paragraphs[0].add_run(txt); r2.font.size=Pt(9.5)
    doc.add_paragraph()

    doc.add_heading("Daily Schedule",level=1)
    for day in range(1,C.DAYS+1):
        rows=day_rows(day)
        doc.add_heading(f"Day {day}: {C.DAY_THEMES[day]}",level=2)
        mins=instructional_minutes(rows)
        doc.add_paragraph(f"Scheduled learning and assessment time excluding lunch: {mins} minutes "
                          f"({mins//60} hours).")
        t=doc.add_table(rows=0,cols=5); t.style="Table Grid"; t.alignment=WD_TABLE_ALIGNMENT.CENTER
        hr=t.add_row().cells
        for i,h in enumerate(["Time","Duration","Topic / Activity","Method","Reference"]):
            hr[i].text=""; r=hr[i].paragraphs[0].add_run(h)
            r.bold=True; r.font.size=Pt(9); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
            prodoc._shade_cell(hr[i],"1F6FEB")
        for row in rows:
            c=t.add_row().cells
            for i,v in enumerate(row):
                c[i].text=""; rr=c[i].paragraphs[0].add_run(str(v)); rr.font.size=Pt(9)
        doc.add_paragraph()

    doc.add_heading("Topic-by-Topic Delivery Guide",level=1)
    for tp in C.TOPICS:
        labs=[a for a in ACT if a["topic"]==tp["num"]]
        doc.add_heading(f"Topic {tp['code']}: {tp['title']}",level=2)
        doc.add_paragraph(tp["subtitle"])
        doc.add_paragraph("Key concepts delivered:")
        for c_ in tp["concepts"]: doc.add_paragraph(c_,style="List Bullet")
        doc.add_paragraph("Hands-on labs:")
        for a in labs:
            doc.add_heading(f"Lab {a['num']:02d}: {a['title']}",level=3)
            doc.add_paragraph(
                f"Alignment: {a['km']} · {a['am']}. Level: {a['level']}. Apps: {a['apps']}. "
                f"Learner output: {a['build']}. Acceptance: {a['test']}")

    doc.add_heading("Assessment Plan",level=1)
    doc.add_paragraph(C.ASSESSMENT["written"],style="List Bullet")
    doc.add_paragraph(C.ASSESSMENT["practical"],style="List Bullet")
    doc.add_paragraph("Both instruments are open book: learners may use the slides, the Learner Guide "
                      "and their completed lab files.",style="List Bullet")
    doc.add_paragraph(C.ASSESSMENT["note"],style="List Bullet")
    doc.add_paragraph("Learners who are assessed Not Yet Competent may be re-assessed in accordance "
                      "with the organisation's assessment policy. An appeal process is available.",
                      style="List Bullet")

    doc.add_heading("Resources Required",level=1)
    for r_ in ["A Windows laptop per learner with a supported browser.",
               "A Microsoft 365 account with a Microsoft 365 Copilot licence.",
               "Access to Power Automate and Copilot Studio in the course Power Platform environment.",
               "The course lab files, one folder per lab, distributed through the LMS.",
               "Projector or large display for demonstrations.",
               "The slide deck, Learner Guide and Lesson Plan available on the LMS."]:
        doc.add_paragraph(r_,style="List Bullet")

    prodoc.add_page_numbers(doc); prodoc.enable_update_fields(doc)
    out=os.path.join(REPO,"courseware",f"LP-{C.SHORT_TITLE}.docx")
    doc.save(out); print("Saved",out)
    for d in range(1,C.DAYS+1):
        print(f"  Day {d}: {instructional_minutes(day_rows(d))} instructional minutes")

if __name__=="__main__": build()
