# Lab 10: Turn Meeting Notes into an Action Register

**Topic 02** · **Day 2** · **Intermediate** · **Teams, Word, Excel, Copilot** · **K2 · A2**

## Goal

The learner turns a supplied meeting-notes document into a decision log and an action register with named owners and due dates, then verifies every action against the source notes.

## Expected output

A meeting brief, a decision log, an action register and a reviewed follow-up message

![Lab 10 workflow](LAB-10-Workflow.png)

*Figure. Lab 10 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-10.xlsx` — Decision log and action register workbook
- `Teams-Meeting-Notes.docx` — The supplied meeting notes
- `LAB-10-Instructions.pdf` — printable detailed guide
- `LAB-10-Workflow.png` — the workflow diagram above

## Primary prompt

> From these meeting notes produce three things: a list of decisions made, a list of actions with an owner and a due date for each, and a list of unresolved questions. Quote the line that supports each decision. Do not create an action that nobody agreed to.

## Procedure

1. **Read the supplied meeting notes**

   Form your own view of what was decided before Copilot summarises it for you.

2. **Extract decisions, actions and open questions**

   Use the primary prompt so each of the three lists is separated.

3. **Verify each action against the source line**

   An action with no supporting line in the notes is an invention and must be removed.

4. **Assign an owner and a due date to every action**

   An action without a named owner and a date will not happen.

5. **Log unresolved questions separately**

   Open questions are not actions; conflating them hides the fact that a decision is still needed.

6. **Draft the follow-up message**

   Ask Copilot for a short message summarising decisions and actions for the attendees.

7. **Review and record the approval**

   Confirm every action and owner is correct, then log the reviewer in Acceptance_Check.

## Acceptance test

Every action in the register cites a supporting line from the notes and carries a named owner and due date, and unresolved questions are listed separately from actions.

## Evidence to retain

- Decision log, action register and the reviewed follow-up message.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*