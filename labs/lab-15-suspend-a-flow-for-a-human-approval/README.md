# Lab 15: Suspend a Flow for a Human Approval

**Topic 03** · **Day 3** · **Advanced** · **Power Automate, Approvals, Outlook, Teams** · **K5 · A7**

## Goal

The learner builds a leave-application flow that pauses at an approval action, waits for a named approver's decision, and then takes a different action for an approved and a rejected outcome.

## Expected output

A leave-application flow that suspends until an approver responds and records the outcome

![Lab 15 workflow](LAB-15-Workflow.png)

*Figure. Lab 15 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-15.xlsx` — Approval design and outcome-evidence workbook
- `LAB-15-Instructions.pdf` — printable detailed guide
- `LAB-15-Workflow.png` — the workflow diagram above

## Primary prompt

> Explain what happens to a Power Automate run when it reaches a Start and wait for an approval action, how long it can wait, and how I should handle the approved and rejected outcomes.

## Procedure

1. **Create the leave-application form**

   Build a form capturing the applicant's name, email, leave type, start date, end date and reason.

2. **Create the flow and retrieve the answers**

   Use the Forms trigger and Get response details exactly as in Lab 12, so the approval has real data to show.

3. **Add Start and wait for an approval**

   Choose the Approvals action Start and wait for an approval, with Approval type Approve/Reject - First to respond. The run genuinely suspends here; it is not polling.

4. **Write a title and details the approver can act on**

   Insert the applicant name, dates and reason into the Details field so the approver does not have to look anything up.

5. **Assign the approver**

   Set Assigned To to the approver's address. Only a named person can respond, and their decision is recorded against them.

6. **Branch on the outcome**

   Add a Condition testing whether the Outcome dynamic value equals Approve, then send the applicant a confirmation on the If yes branch and a rejection with the approver's comments on the If no branch.

7. **Test both outcomes and inspect the timeline**

   Run it twice, approving once and rejecting once, then read the run history to see how long the run stayed suspended and when it resumed.

## Acceptance test

The run remains in a waiting state until the approver responds, then resumes down the branch matching the decision and emails the applicant the correct outcome.

## Evidence to retain

- Run histories for an approved and a rejected application, plus the two resulting emails.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*