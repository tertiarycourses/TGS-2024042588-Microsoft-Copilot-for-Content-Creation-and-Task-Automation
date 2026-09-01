# Lab 12: Build a Trigger and Actions Flow from Microsoft Forms

**Topic 03** · **Day 3** · **Foundation** · **Power Automate, Microsoft Forms, Outlook** · **K3 · A3**

## Goal

The learner creates a Microsoft Form, builds an automated cloud flow that starts on submission, retrieves the answers and sends a personalised confirmation to the address the requester entered.

## Expected output

A working Forms-to-email flow that acknowledges every enquiry automatically

![Lab 12 workflow](LAB-12-Workflow.png)

*Figure. Lab 12 workflow — the four stages and the artifact produced.*

## Files

- `Lumina-Living-Lab-12.xlsx` — Flow design and run-verification workbook
- `LAB-12-Instructions.pdf` — printable detailed guide
- `LAB-12-Workflow.png` — the workflow diagram above

## Primary prompt

> Describe the trigger and actions I need so that when someone submits a Microsoft Form, the person who submitted it receives a personalised confirmation email. Name the exact connector actions and explain why the response details step is needed.

## Procedure

1. **Create the Course Enquiry Form**

   At forms.office.com create a form named Course Enquiry Form with four required Text questions: Name, Email, Tel and Message, with Long answer enabled on Message.

2. **Create an automated cloud flow**

   At make.powerautomate.com choose Create, then Automated cloud flow, name it Lab 12 - Form Email Confirmation, and pick the Microsoft Forms trigger When a new response is submitted.

3. **Point the trigger at your form**

   Set Form Id to Course Enquiry Form. The trigger fires once per submission and carries only a Response Id, not the answers.

4. **Add Get response details**

   Add the Microsoft Forms action Get response details, set Form Id again, and set Response Id from dynamic content under the trigger. This is the step that actually fetches the answers.

5. **Add Send an email (V2)**

   Add the Office 365 Outlook action Send an email (V2). Set the To field from the form's Email answer using dynamic content, never by typing a value.

6. **Compose a personalised body**

   Insert the Name answer into the subject and body so the reply is addressed to the requester. A dynamic value must be inserted from the panel, never typed as text.

7. **Save, test and read the run history**

   Save the flow, submit the form once, then open the run history and confirm each step shows a green tick and the Outlook step shows the submitted address.

## Acceptance test

One form submission produces one successful run, and the confirmation email arrives at the address entered in the form rather than the flow owner's mailbox.

## Evidence to retain

- Flow run-history screenshot showing a successful run and the delivered confirmation email.

---

*Microsoft Copilot for Content Creation and Task Automation · TGS-2024042588 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*