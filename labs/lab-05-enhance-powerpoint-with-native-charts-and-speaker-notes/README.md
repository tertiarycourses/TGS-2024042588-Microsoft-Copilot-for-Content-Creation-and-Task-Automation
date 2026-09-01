# Lab 05: Enhance PowerPoint with Native Charts and Speaker Notes

**Topic 01** · **Day 1** · **Intermediate** · **PowerPoint, Excel, Copilot** · **K2 · A2**

## Goal

The learner replaces picture-charts with native editable PowerPoint charts driven by the workbook, then generates and verifies speaker notes that match what each chart actually shows.

## Expected output

A polished deck with native trend, contribution and variance charts plus verified speaker notes

![Lab 05 workflow](LAB-05-Workflow.png)

*Figure. Lab 05 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-05.xlsx` — Chart plan and source data workbook
- `Lumina-Living-Leadership-Deck-Draft.pptx` — Draft deck to be enhanced
- `LAB-05-Instructions.pdf` — printable detailed guide
- `LAB-05-Workflow.png` — the workflow diagram above

## Primary prompt

> Review this deck against the attached workbook. For each data slide, tell me which chart type communicates the message most honestly, what the axis and units should be, and what a presenter should say. Flag any chart whose visual impression overstates the underlying numbers.

## Procedure

1. **Identify every slide that makes a quantitative claim**

   List them in Chart_Plan with the message each slide is meant to deliver.

2. **Choose the honest chart type for each message**

   Trend over time is a line; contribution is a bar or stacked bar; variance against target is a clustered bar.

3. **Insert native PowerPoint charts driven by the workbook figures**

   A native chart keeps its data editable and auditable; a pasted image cannot be checked.

4. **Label axes, units and the source on every chart**

   An unlabelled axis is where a misleading chart hides.

5. **Ask Copilot to draft speaker notes for each data slide**

   Then verify each note against the chart; a note that overstates the data is a defect.

6. **Check for visual exaggeration**

   Confirm that no axis is truncated in a way that overstates a difference.

7. **Complete the Acceptance_Check**

   Every chart must be native, labelled, sourced and consistent with its speaker note.

## Acceptance test

Every data slide carries a native, labelled chart traceable to the workbook, and each speaker note states only what its chart actually shows.

## Evidence to retain

- Enhanced deck, workbook with Chart_Plan, and the verified speaker notes.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*