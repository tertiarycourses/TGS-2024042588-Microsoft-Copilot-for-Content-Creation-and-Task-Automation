# Lab 23: Add a Human Review Gate to an Agent Action

**Topic 05** · **Day 5** · **Advanced** · **Copilot Studio, Power Automate, Teams Approvals** · **K5 · A7**

## Goal

The learner takes an agent that can trigger a consequential action and inserts an approval gate, so the model may propose the action but only a named person can release it.

## Expected output

An agent whose consequential action is suspended until a named person approves it

![Lab 23 workflow](LAB-23-Workflow.png)

*Figure. Lab 23 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-23.xlsx` — Boundary-of-agency and approval-test workbook
- `LAB-23-Instructions.pdf` — printable detailed guide
- `LAB-23-Workflow.png` — the workflow diagram above

## Primary prompt

> Review this proposed action and summarise for the approver: what is being requested, the amount, the vendor, which policy rule applies and what your recommendation is. Present it as a decision, not as a completed action.

## Procedure

1. **Identify the consequential action**

   Decide which single step in the process would be expensive or embarrassing to get wrong. That is the step that needs the gate.

2. **Rank the controls honestly**

   A control the model cannot reach beats a rule you asked it to follow, and neither is the same as a name someone typed into a text box.

3. **Insert an approval before the action**

   In the agent flow, place a Start and wait for an approval action before the step that has real effect.

4. **Send the approval to Microsoft Teams**

   Route the approval to Teams so the approver receives it where they work and the decision is recorded against them.

5. **Give the approver enough to decide**

   Include the request, the amount, the applicable rule and the recommendation, so approving does not require a separate investigation.

6. **Write an audit row regardless of the outcome**

   Log every request, approved or rejected, so the record does not depend on the decision that was made.

7. **Test an approval, a rejection and an edge case**

   Include a case the agent would plausibly get wrong, and confirm the gate stops it even when the agent's reasoning looked sound.

## Acceptance test

The consequential action never completes without a recorded approval, a rejection stops it cleanly, and an audit row exists for every request regardless of outcome.

## Evidence to retain

- Approval and rejection run histories, the Teams approval cards and the audit log rows.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*