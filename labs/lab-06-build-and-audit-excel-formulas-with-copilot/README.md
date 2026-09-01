# Lab 06: Build and Audit Excel Formulas with Copilot

**Topic 02** · **Day 2** · **Foundation** · **Excel, Copilot** · **K2 · A2**

## Goal

The learner converts a flat range into an Excel Table, asks Copilot to add derived margin, conversion and status columns, then audits each generated formula against the assumptions sheet.

## Expected output

A formula-driven campaign table with revenue, margin, conversion, status and error controls

![Lab 06 workflow](LAB-06-Workflow.png)

*Figure. Lab 06 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-06.xlsx` — Campaign data, assumptions and controls workbook
- `LAB-06-Instructions.pdf` — printable detailed guide
- `LAB-06-Workflow.png` — the workflow diagram above

## Primary prompt

> In the Campaign_Data table add calculated columns for Margin, Margin_Percent, Conversion_Rate, Return_Rate and Target_Status. Use the thresholds in the Assumptions sheet, use structured references, and handle divide-by-zero safely. Explain each formula you add.

## Procedure

1. **Convert the data range into an Excel Table**

   Copilot analyses a Table far more reliably than a loose range, and structured references survive inserted rows.

2. **Confirm the data is analysis-ready**

   One header row, one record per row, consistent types and no merged cells.

3. **Ask Copilot to add the derived columns**

   Use the primary prompt so the thresholds come from Assumptions rather than being hard-coded.

4. **Audit every generated formula**

   Read each formula and confirm its logic, its references and its rounding before you accept it.

5. **Test the divide-by-zero and blank cases**

   A record with zero clicks or zero impressions must not produce an error value.

6. **Verify the control totals**

   Complete the Controls sheet: record count, blank keys and negative revenue must all match the expected values.

7. **Log each accepted formula and its reviewer**

   Record the formula, what it computes and who checked it in the Formula_Audit sheet.

## Acceptance test

Every derived column uses a checked structured-reference formula, no error values remain, and the Controls sheet matches the expected record count and zero exceptions.

## Evidence to retain

- Completed workbook with Formula_Audit, Controls and Acceptance_Check.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*