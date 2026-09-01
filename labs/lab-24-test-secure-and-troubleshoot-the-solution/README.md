# Lab 24: Test, Secure and Troubleshoot the Solution

**Topic 05** · **Day 5** · **Advanced** · **Power Automate, Copilot Studio, run history** · **K5 · A6,A8**

## Goal

The learner runs a structured test pass over the flows and agents built during the course, deliberately triggers failures, reads the run history to diagnose each one, and records the cause and the fix.

## Expected output

A completed test log and an issue register with a diagnosed cause and fix for every failure

![Lab 24 workflow](LAB-24-Workflow.png)

*Figure. Lab 24 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-24.xlsx` — Test log and issue register workbook
- `LAB-24-Instructions.pdf` — printable detailed guide
- `LAB-24-Workflow.png` — the workflow diagram above

## Primary prompt

> This flow run failed. Read the error, explain in plain English what went wrong, tell me which step caused it and what I should change. Distinguish a data problem from a permission problem from a configuration problem.

## Procedure

1. **Build the test pass from the acceptance criteria**

   Every lab in this course has a Test it criterion; those criteria are the test pass, not an afterthought.

2. **Test the happy path for each flow and agent**

   Confirm the expected outcome and record the run identifier as evidence.

3. **Trigger a data failure deliberately**

   Submit a malformed or empty value and observe how the flow behaves. An untested failure path is an unknown failure path.

4. **Trigger a permission failure deliberately**

   Remove or break a connection and read the resulting error, so you recognise it when it happens in production.

5. **Diagnose each failure from the run history**

   Open the failed step and read its inputs and outputs. The inputs usually show that the wrong data arrived, not that the action is broken.

6. **Classify the cause and record the fix**

   Log each issue in Issue_Register as a data, permission or configuration problem, with the fix applied and the retest result.

7. **Confirm the fix and retest**

   A fix is not complete until the failing case has been re-run and passes.

## Acceptance test

Every flow and agent has a recorded happy-path result, each deliberately triggered failure is diagnosed with a cause and a fix, and every fix has a passing retest.

## Evidence to retain

- Completed test log and issue register with run identifiers for each entry.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*