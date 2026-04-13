---
name: case-study
description: "Use this skill whenever a user wants to create a UX or design case study document. Triggers include: mentions of 'case study', 'design case study', 'UX case study', 'portfolio case study', requests to document a design initiative, project outcome, or design process for stakeholders or management review. Also trigger when a user mentions sections like 'the challenge', 'the solution', 'the outcome', 'design impact', or wants to write up a project for upper management, leadership review, or a design portfolio. Use this skill even if the user only mentions one section (e.g. \"help me write up the outcome of my project\") — it likely benefits from the full structured workflow."
---

# Case Study Document Skill

Produces a polished, upper-management-ready Word (.docx) case study document by
interviewing the user section by section, then generating a clean, corporate-formatted
document using the docx skill.

---

## Workflow

### Step 1: Introduce and Begin the Interview

Greet the user and explain you'll ask questions across 6 sections to build their case study.
Tell them they can skip any section — you'll insert a placeholder so they can fill it in later.
Also let them know they're welcome to **upload any existing documentation** (e.g. project briefs, research reports, design specs, retrospectives, or slide decks) — you'll pull relevant information from those files and use them to pre-fill answers, reducing how much they need to type.
Then proceed section by section. **Ask one section at a time.** Don't dump all questions at once.

If the user uploads documents, read them before starting the interview. For each section, use what you find in the documents to propose a draft answer, then ask the user to confirm, correct, or add to it rather than asking from scratch.

---

### Step 2: Section-by-Section Interview

Work through each section below in order. After the user responds, summarize what you've
captured and confirm before moving on. If a user skips a section or says they don't have
the info, note it and move on — you'll insert a placeholder in the doc.

---

#### Section 3.1 — The Challenge

Goal: A concise problem statement written for executive readers.

Ask the user:
- Who is the affected group? (e.g. customers, internal users, a specific segment)
- What problem did they face, and in what context or situation?
- What was the negative impact? (quantitative metrics preferred — drop-off rate, churn, etc.)
- What was the desired outcome of solving this?
- Any supporting evidence? (user feedback, support tickets, analytics, stakeholder observations)

**Formula to apply when writing this section:**
> [Affected group] faces [problem] when [context/situation], which results in [negative impact]. We need to [desired outcome] that addresses the issue faced by the user.

If metrics aren't available, use qualitative evidence instead and note it clearly.

---

#### Section 3.2 — The Solution

Goal: A short description of the work done, followed by 3–5 bullet points detailing the solution.

Ask the user:
- How long was the design process, and what was its goal?
- What were the key steps or design methods used? (e.g. user interviews, redesign, A/B tests, prototypes)
- Has this initiative launched yet, or is it still in progress?

**If launched:** Focus on concrete design actions and changes made.
**If in progress:** Focus on research, validation, stakeholder alignment, and artifacts delivered.

Write as: One sentence summary + 3–5 bullet points of key actions.

---

#### Section 3.3 — The Outcome

Goal: Measurable impact framed as increases in value or decreases in pain, with timeframe.

Ask the user:
- Has the initiative launched?
- What metrics improved? (activation rate, task completion, support tickets, churn, revenue, etc.)
- Over what timeframe were these measured?
- If not launched yet: any leading indicators? (usability test results, prototype validation, stakeholder sign-off)

**If launched:** Present as: "In the [timeframe] post-launch, the [initiative]:" + 3–5 bullet points.
**If in progress:** Document validation metrics, usability test results, and milestones achieved.
**If no metrics:** Note this clearly with placeholder, suggest proxy metrics or qualitative indicators.

Always look for opportunities to tie results to financial outcomes (call center deflection, revenue, churn reduction).

---

#### Section 3.4 — Visual Assets

Goal: List the visual artifacts that should accompany this case study.

Ask the user:
- What visual assets exist? (hi-fi designs, wireframes, UX flows, journey maps, research screenshots)
- Are there any research artifacts that were key to the solution? (research reports, CXO dashboards, heuristic tables)
- Can they describe or name the visuals so placeholders can be inserted?

**Note:** This skill inserts clearly labeled image placeholders in the document. The user will
need to manually insert actual images after downloading the .docx file.

---

#### Section 3.5 — Customer or Other Quotes

Goal: 2–3 verbatim (or lightly edited) quotes from customers or end users.

Ask the user:
- Do they have any customer, user, or stakeholder quotes?
- If yes, collect the quotes and who said them (role/segment is fine, no need for full names).
- Remind them: quotes should be short, punchy, and authentic — you can help tighten them while
  preserving meaning and tone.

If no quotes are available, insert a placeholder.

---

#### Section 3.6 — The Team

Goal: Credit everyone who contributed.

Ask the user:
- Who was the Design Director and Manager?
- Who were the design teammates?
- Were there cross-functional partners? (Product, Engineering, Research, Analytics, etc.)

---

### Step 3: Review & Confirm

Once all sections are collected, present a brief structured summary of everything captured.
Ask: "Does this look right? Anything you'd like to change before I create the document?"

Wait for confirmation before generating.

---

### Step 4: Generate the Word Document

Use the `docx` skill to produce the document. Follow all docx skill rules strictly.

#### Document Structure

```
Cover / Title Area
  - Case Study title (from project name) — TR Doc Title style
  - Subtitle: "Design Case Study"
  - Date (use today's date)

The Challenge    (TR Heading style)
The Solution     (TR Heading style)
The Outcome      (TR Heading style)
Visual Assets    (TR Heading style)
Customer & User Quotes (TR Heading style)
The Team         (TR Heading style)
```

#### Formatting Rules

**Fonts:**
- Headings & title: `Clario Medium` (majorHAnsi theme font)
- Body, bullets, subtitle, table, footer: `Clario`

**Page setup (A4, from TR_Document_style.docx):**
- Size: 11900 x 16840 DXA
- Margins: top=1463, right=814, bottom=1418, left=1006 DXA
- Content width: 10080 DXA
- Header distance: 567, footer distance: 340 DXA

**Color palette:**
- Title: `000000` black (bold)
- Eyebrow: `D64000` orange
- Section headings: `000000` black, NOT bold
- Body text: `000000` black
- Bullet/number markers: `D64000` orange
- Placeholder text: `AAAAAA` italic
- Footer text: `888888` grey

**Title block:**
- Eyebrow: "DESIGN CASE STUDY" — Clario Medium, 9pt (sz=18), `D64000`, all-caps, line=240
- Title: Clario Medium, 36pt (sz=72), black, bold, line=168
- Subtitle: must be exactly `"Design Case Study"` — do not append, modify, or embellish this string — Clario, 14pt (sz=28), `444444`
- Date: Clario bold, 11pt (sz=22), black, line=240

**Section headings:**
- Clario Medium, 20pt (sz=40), `000000` black, NOT bold
- No numbering prefix; suppress with `LevelFormat.NONE` reference
- Spacing: before=240, after=0, line=216

**Body text:**
- Clario, 10pt (sz=20), black
- Spacing: before=40, after=120, line=276

**Bullet points:**
- Bullet marker (`•`): color `D64000` orange — set via `style.run.color` in numbering config
- Bullet text: Clario, 10pt (sz=20), black — set per paragraph
- LevelFormat.BULLET, indent left=720, hanging=360
- Spacing: before=40, after=120

**Quotes:**
- Clario, 10pt (sz=20), italic, left indent 720 DXA
- Attribution: Clario, 9pt (sz=18), `555555`

**Image placeholders:**
- Single-cell table, border `CCCCCC`, bg `F9F9F9`, ShadingType.CLEAR
- Centered placeholder text: Clario, 9pt, `AAAAAA`, italic
- Caption below: Clario, 8pt, `888888`, italic
- Table width: CONTENT_W DXA

**Placeholder text (missing sections):**
- Clario, 10pt, italic, `AAAAAA`
- Format: `[ Placeholder: {instruction} ]`

**Page header:** None — no header on this document.

**Page footer:**
- Orange top rule: SINGLE, size 12, color `D64000`, space 4
- Left: "© 2026 Thomson Reuters" — Clario, 7pt (sz=14), `888888`
- Right: stacked TR logo — **mandatory, never skip**
  - Before generating the document, verify the logo exists by running: `ls /home/claude/tr-logo2.png`
  - If missing: stop and tell the user "The Thomson Reuters logo is missing at `/home/claude/tr-logo2.png`. Please upload it so I can include it in the footer." Do not generate the document without it.
  - If present: embed from `/home/claude/tr-logo2.png`, source dimensions 2640×879px, ~0.37in tall
    - FLOGO_H_EMU = 337820, FLOGO_W_EMU = round(337820 × 2640/879)
    - Convert to px: width = round(EMU / 914400 × 96), height = round(EMU / 914400 × 96)
- Tab stop RIGHT at CONTENT_W to push logo right

**Team table:**
- 2-column: Name | Role; width CONTENT_W, columnWidths [CONTENT_W/2, CONTENT_W/2]
- Header row: bg `D64000`, white bold text, Clario 9pt (sz=18)
- Body rows: all white, no alternating colour
- All cell borders: black SINGLE size 4
- Cell margins: top/bottom 80, left/right 120
- One row per person; parse "Name (Dept)" → name + role

#### docx-js Implementation Notes

- Always install: `npm install -g docx`
- Validate after creation: `python scripts/office/validate.py doc.docx`
- Never use `\n` — use separate Paragraph elements
- Never use `WidthType.PERCENTAGE` in tables — always DXA
- Tables need dual widths: `columnWidths` array AND per-cell `width`
- Use `ShadingType.CLEAR` for all shading, never `SOLID`
- PageBreak must live inside a Paragraph element
- Use `"Clario"` or `"Clario Medium"` explicitly as the font name for all text (never Calibri or Calibri Light)

---

### Step 5: Deliver

Save the file to `/mnt/user-data/outputs/case-study.docx` and present it to the user.

Tell the user:
- Where to manually insert images (Section 3.4 placeholders)
- Which sections have placeholders they should fill in
- That they can ask you to update any section and regenerate