# Lab 20: Publish an Agent to Microsoft Teams

**Topic 04** · **Day 4** · **Advanced** · **Copilot Studio, Microsoft Teams** · **K4 · A5**

## Goal

The learner publishes the grounded agent to Microsoft Teams, confirms the published version behaves as the test version did, and records the release decision and rollback plan.

## Expected output

A published agent available in Microsoft Teams with a recorded release decision

![Lab 20 workflow](LAB-20-Workflow.png)

*Figure. Lab 20 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-20.xlsx` — Release log and rollback-plan workbook
- `LAB-20-Instructions.pdf` — printable detailed guide
- `LAB-20-Workflow.png` — the workflow diagram above

## Primary prompt

> Summarise what changes when an agent is published to Teams: who can reach it, which version they get, what happens to my unpublished edits, and how I roll back a bad release.

## Procedure

1. **Re-run the acceptance tests before publishing**

   Publishing a failing agent makes the failure everyone's problem. The test set from Lab 16 is the release gate.

2. **Publish the agent**

   Use Publish in Copilot Studio. Users always receive the published version, never your latest unpublished edit.

3. **Add the Microsoft Teams channel**

   Under Channels choose Microsoft Teams and make the agent available, following the tenant's availability setting.

4. **Test the published agent inside Teams**

   Repeat two in-scope tests and one refusal test in Teams itself; the channel, not the test pane, is where users meet the agent.

5. **Confirm the refusal still holds after publishing**

   A refusal that works in the test pane but not in the channel is a release defect.

6. **Record the release decision**

   Log the version, the date, the tests that passed and the named approver in the Release_Log sheet.

7. **Write the rollback plan**

   State how the agent would be withdrawn or reverted, and who decides. A release without a rollback plan is not a controlled release.

## Acceptance test

The agent responds correctly inside Microsoft Teams, still refuses out-of-scope questions, and the release log records the version, tests, approver and rollback plan.

## Evidence to retain

- Teams transcript, release log and a credential-safe screenshot of the channel configuration.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*