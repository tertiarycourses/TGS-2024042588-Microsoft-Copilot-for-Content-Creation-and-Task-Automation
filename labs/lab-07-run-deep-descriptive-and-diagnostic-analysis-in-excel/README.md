# Lab 07: Run Deep Descriptive and Diagnostic Analysis in Excel

**Topic 02** · **Day 2** · **Intermediate** · **Excel, Copilot** · **K2 · A2**

## Goal

The learner uses Copilot to summarise performance, segment it by region, channel and product, isolate anomalies, and write management findings that each cite the cells they came from.

## Expected output

A diagnostic workbook with a KPI summary, segment analysis, an anomaly log and management findings

![Lab 07 workflow](LAB-07-Workflow.png)

*Figure. Lab 07 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-07.xlsx` — Campaign data, KPI summary and anomaly log workbook
- `LAB-07-Instructions.pdf` — printable detailed guide
- `LAB-07-Workflow.png` — the workflow diagram above

## Primary prompt

> Analyse the Campaign_Data table. Give me a KPI summary, then break performance down by Region, Channel and Product. Identify the three largest drivers of the gap against Target_Revenue and list any records that look anomalous, with the reason. Cite the columns you used.

## Procedure

1. **Ask the descriptive question first**

   Establish what happened — totals, averages and trend — before asking why.

2. **Segment the results**

   Break the totals down by Region, Channel and Product to find where the variance actually sits.

3. **Ask the diagnostic question**

   Ask Copilot which segments drive the gap against target and what evidence supports that.

4. **Isolate anomalies and record them**

   Log each anomalous record in Anomaly_Log with the reason it was flagged.

5. **Distinguish a cause from a correlation**

   A segment that moves with the gap is not automatically its cause; note what further evidence would be needed.

6. **Write management findings with citations**

   Each finding states the observation, the evidence cells and the recommended action.

7. **Complete the Acceptance_Check**

   Every finding must cite the sheet and range it came from.

## Acceptance test

The workbook holds a KPI summary, a segment breakdown, a populated anomaly log, and findings that each cite the sheet and range supporting them.

## Evidence to retain

- Completed diagnostic workbook and the management findings sheet.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*