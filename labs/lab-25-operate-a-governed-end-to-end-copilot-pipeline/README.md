# Lab 25: Operate a Governed End-to-End Copilot Pipeline

**Topic 05** · **Day 5** · **Capstone** · **Microsoft 365 Copilot, Power Automate, Copilot Studio, Outlook, Teams, Excel** · **K5 · A7,A8**

## Goal

The learner runs one request end to end through the whole solution built during the week, produces the content, routes it through the automation and the human gate, and assembles the governance evidence pack.

## Expected output

A complete pipeline run with content, automation, approval and a governance evidence pack

![Lab 25 workflow](LAB-25-Workflow.png)

*Figure. Lab 25 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-25.xlsx` — End-to-end pipeline and governance evidence workbook
- `LAB-25-Instructions.pdf` — printable detailed guide
- `LAB-25-Workflow.png` — the workflow diagram above

## Primary prompt

> Summarise this pipeline run for the governance record: what was requested, what Copilot generated, what was verified and by whom, which action required approval, who approved it and what the final outcome was. Flag anything that was released without a verification step.

## Procedure

1. **Restate the end-to-end process**

   Map the full path from the original request to the released output, naming the system that handles each stage.

2. **Run the content stage**

   Use Copilot to produce the required content, grounded in the approved source, exactly as in the Day 1 and Day 2 labs.

3. **Verify every claim before it enters the pipeline**

   Unverified content that enters an automated pipeline gets distributed faster, not checked more.

4. **Run the automation stage**

   Submit the request through the flow and confirm the log row and the notification both appear.

5. **Pass through the human review gate**

   Confirm the consequential step suspends for approval and record the approver's decision.

6. **Assemble the governance evidence pack**

   Collect the prompt log, the evidence register, the run identifiers, the approval record and the final output into one pack.

7. **Identify one improvement and one residual risk**

   State what you would change before this ran unattended, and the risk that would remain even then.

## Acceptance test

One request traverses content generation, verification, automation and human approval, and the evidence pack accounts for every stage with a named owner.

## Evidence to retain

- The complete governance evidence pack, including run identifiers and the approval record.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*