# Lab 16: Design a Scoped Agent Before You Build It

**Topic 04** · **Day 4** · **Foundation** · **Copilot Studio, Excel** · **K4 · A1**

## Goal

The learner produces an agent design canvas that states the job the agent does, what it must refuse, the knowledge it may use, the actions it may take and the tests that will prove it behaves.

## Expected output

An agent design canvas, a knowledge register, a risk-and-control table and ten acceptance tests

![Lab 16 workflow](LAB-16-Workflow.png)

*Figure. Lab 16 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-16.xlsx` — Agent design canvas, knowledge register and test workbook
- `Procurement-Policy.docx` — The approved procurement policy used as knowledge
- `LAB-16-Instructions.pdf` — printable detailed guide
- `LAB-16-Workflow.png` — the workflow diagram above

## Primary prompt

> Help me scope an agent that answers staff questions about our procurement policy. List the questions it should answer, the questions it must refuse, the knowledge it needs, and the actions it should never take on its own. Ask me for anything you need to know.

## Procedure

1. **State the one job the agent does**

   An agent with one clear job can be tested; an agent that does everything can only be hoped for. Write it as a single sentence in the Design_Canvas sheet.

2. **Separate a workflow from an agent**

   If the path is always the same, build a flow. Choose an agent only when the next step genuinely depends on what the user says.

3. **List what the agent must refuse**

   Write the out-of-scope questions explicitly. An agent with no stated refusals will answer everything, including things it should not.

4. **Register the knowledge sources**

   Record each approved source in Knowledge_Register with its owner. Note that a source you do not add is a source the agent cannot cite.

5. **Decide the boundary of agency**

   For each candidate action, record whether the agent may do it alone, may do it with a human gate, or may never do it.

6. **Identify the risks and the control for each**

   For every risk, name the control. A control the model cannot reach beats an instruction you asked it to follow.

7. **Write ten acceptance tests**

   Write ten concrete test cases with the expected outcome, including at least three that must be refused.

## Acceptance test

The canvas states one job, lists explicit refusals, registers every knowledge source with an owner, and carries ten acceptance tests of which at least three expect a refusal.

## Evidence to retain

- Completed design canvas, knowledge register, risk-and-control table and test list.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*