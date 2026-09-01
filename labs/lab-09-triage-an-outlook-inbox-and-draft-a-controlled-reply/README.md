# Lab 09: Triage an Outlook Inbox and Draft a Controlled Reply

**Topic 02** · **Day 2** · **Intermediate** · **Outlook, Excel, Copilot** · **K2 · A2**

## Goal

The learner triages a supplied mail pack, summarises a long thread, verifies the summary against the original messages, and drafts one reply that is explicitly approved before it would be sent.

## Expected output

An inbox triage register, a verified thread summary and one approval-ready draft reply

![Lab 09 workflow](LAB-09-Workflow.png)

*Figure. Lab 09 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-09.xlsx` — Triage register and evidence workbook
- `Outlook-Thread-Pack.docx` — The supplied email thread pack
- `LAB-09-Instructions.pdf` — printable detailed guide
- `LAB-09-Workflow.png` — the workflow diagram above

## Primary prompt

> Summarise this email thread. List the decisions already made, the open questions, who owns each action and the dates committed. Flag anything where the thread contradicts itself. Do not infer agreement that was not stated.

## Procedure

1. **Triage the supplied thread pack**

   Classify each message as Action, Awaiting, Information or Archive in the Triage_Register.

2. **Summarise the longest thread with Copilot**

   Use the primary prompt so the summary separates decisions from open questions.

3. **Verify the summary against the original messages**

   Check each stated decision actually appears in the thread; a plausible summary is not a correct one.

4. **Record any contradiction the thread contains**

   Where two messages disagree, the summary must surface the conflict rather than resolve it silently.

5. **Draft one reply with Copilot**

   Set the tone and length explicitly, and state the facts the reply is allowed to assert.

6. **Verify recipients, facts and attachments**

   The human-send gate: check who is on the To and Cc lines before anything is sent.

7. **Record the approval decision**

   Log the reviewer and the decision in Acceptance_Check. The draft is not sent during the lab.

## Acceptance test

The triage register classifies every message, the thread summary matches the original messages, and the draft reply carries a named approver before any send.

## Evidence to retain

- Triage register, verified summary and the approved draft reply.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*