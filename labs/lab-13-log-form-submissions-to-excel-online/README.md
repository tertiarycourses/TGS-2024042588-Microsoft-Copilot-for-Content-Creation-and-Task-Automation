# Lab 13: Log Form Submissions to Excel Online

**Topic 03** · **Day 3** · **Intermediate** · **Power Automate, Microsoft Forms, Excel Online, OneDrive** · **K3 · A3**

## Goal

The learner extends the enquiry flow so each submission also writes a row into a named Excel table, producing an auditable log alongside the email acknowledgement.

## Expected output

An enquiry flow that both emails the requester and appends a row to an Excel log table

![Lab 13 workflow](LAB-13-Workflow.png)

*Figure. Lab 13 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-13.xlsx` — Flow design and verification workbook
- `Enquiry-Log.xlsx` — Workbook containing the formatted EnquiryLog table
- `LAB-13-Instructions.pdf` — printable detailed guide
- `LAB-13-Workflow.png` — the workflow diagram above

## Primary prompt

> I want every Microsoft Forms submission to be appended as a row in an Excel table stored in OneDrive. Tell me what the workbook must contain before the action will work, and what each field of the Add a row into a table action needs.

## Procedure

1. **Prepare the Enquiry Log workbook**

   Upload the supplied Enquiry Log.xlsx to OneDrive for Business. It already contains a formatted table named EnquiryLog with the columns Timestamp, Name, Email, Tel and Message.

2. **Understand why a named table is required**

   The Excel Online connector can only write into a formatted table, not a plain sheet range. A worksheet without a table will not appear in the Table dropdown.

3. **Open the flow from Lab 12 and add a step**

   Add a new action after Get response details so both the log row and the email use the same retrieved answers.

4. **Add Add a row into a table**

   Choose the Excel Online (Business) action Add a row into a table. Set Location to OneDrive for Business, Document Library to OneDrive, File to Enquiry Log.xlsx and Table to EnquiryLog.

5. **Map each column to its dynamic value**

   Map Name, Email, Tel and Message from Get response details. For Timestamp use the expression utcNow() entered in the expression tab.

6. **Order the steps deliberately**

   Write the log row before sending the email so a delivery failure still leaves an auditable record of the enquiry.

7. **Test and verify both outputs**

   Submit the form, then confirm the run succeeded, a new row appeared in EnquiryLog and the confirmation email arrived.

## Acceptance test

A single form submission produces one new row in the EnquiryLog table with all five columns populated, and one confirmation email.

## Evidence to retain

- The updated Excel log showing the new row, plus the successful run history.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*