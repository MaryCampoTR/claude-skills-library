---
name: ado-story-parser
description: >
  Normalise Azure DevOps (ADO) work items of varying quality into the
  ux-requirements-synthesizer intake schema. Use whenever the user provides
  an ADO work item, user story, feature, or any structured work item as input
  to a requirements or prototyping task. Handles incomplete AC, vague titles,
  missing context, and mixed-quality work item sets. Understands ADO-specific
  hierarchy (Epic → Feature → User Story → Task) and field structure.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: ADO Story Parser — Azure DevOps Work Item Normalisation

## Purpose
Azure DevOps work items arrive in wildly varying quality — from fully-formed
stories with detailed AC to single-line titles with no description. This skill
normalises any ADO work item format into clean, synthesizer-ready input without
inventing requirements that aren't there.

---

## ADO Terminology Reference

Always use ADO vocabulary when communicating with the user:

| ADO term | Do NOT use |
|---|---|
| Work item | Ticket |
| User Story | Story (acceptable shorthand), Issue |
| Acceptance Criteria (AC field) | Definition of Done |
| Active / Resolved / Closed / New | In Progress / Done / To Do |
| Iteration Path | Sprint (acceptable colloquially) |
| Tags | Labels |
| Parent | Epic / Feature (depending on level) |
| Child | Task / Sub-item |
| Feature | Initiative |

### ADO Hierarchy
```
Epic
  └── Feature
        └── User Story
              └── Task (implementation detail — not a UX concern)
```

- **Epic** — large strategic theme, rarely prototyped directly
- **Feature** — shippable capability, maps to a screen or flow
- **User Story** — primary unit for prototyping; contains AC
- **Task** — implementation sub-item; ignore for UX purposes
- **Bug** — existing behaviour defect; treat AC as reproduce → fix → verify

---

## Phase 1 — Work Item Intake

### Step 1: Inventory what you've been given

For each work item provided, record:

```
Work Item: [ID e.g. #12345]
Title: [as written]
Type: Epic | Feature | User Story | Bug | Task | Unknown
State: New | Active | Resolved | Closed | [other]
Iteration Path: [Sprint name / path if present]
Priority: [1–4 or label if present]
Tags: [if present]
Parent: [ID + title if present]
Children: [IDs if present]
Description quality: Rich | Partial | Minimal | Empty
AC field populated: Yes | No | Partial
Designs linked: Yes | No | Unknown
Dependencies / blocked by: [IDs if present]
```

If multiple work items are provided, inventory all before proceeding.

---

## Phase 2 — Quality Assessment

### Step 2: Score each work item

Rate each on three dimensions (High / Medium / Low):

**Clarity** — Is it clear what needs to be built?
**Completeness** — Are acceptance criteria present and testable?
**Context** — Is the "why" (user need / business goal) present?

```
[#ID] Clarity: H/M/L | Completeness: H/M/L | Context: H/M/L
→ Action: [Normalise directly | Needs gap-filling | Needs clarification from user]
```

Work items scored Low on Clarity always require user clarification before
synthesis. Do not invent intent for low-clarity work items.

### ADO-specific quality signals

**Good AC (in the AC field):**
- Written as "Given / When / Then" or bullet acceptance statements
- Each criterion is independently testable
- Covers happy path AND error/edge cases

**Weak AC patterns to flag:**
- AC field empty — description contains implied requirements (extract and mark [INFERRED])
- AC written as implementation ("Use a dropdown") → rewrite as behaviour
- AC written as design spec ("Button must be orange") → move to constraints
- AC field contains a single vague line ("Works as expected") → flag as [UNRESOLVED]
- AC exists only as child Tasks → extract Task titles as implied AC [INFERRED]

---

## Phase 3 — Normalisation

### Step 3: Rewrite each work item to standard format

```
## [#ID] [Normalised Title]
Type: [User Story | Feature | Bug]
Parent: [#ID Feature/Epic title if present]

### User Story
As a [actor],
I want to [goal],
so that [outcome].

[Mark any inferred element with [INFERRED]]

### Acceptance Criteria
- [ ] [criterion — testable, specific]
- [ ] [criterion] [INFERRED if not in original AC field]
- [ ] [criterion]

### Out of Scope (if stated in work item)
- [item]

### Dependencies
- [#ID or description]

### Gaps & Questions
- [UNRESOLVED] [specific question needed to complete this work item]
```

---

## Gap-Filling Rules

When AC is missing or incomplete, derive from the story + description using
these heuristics. Always mark as [INFERRED].

| Story type | Standard AC to infer |
|---|---|
| Any form / data entry | Validation rules, required fields, success state, error state |
| Any list / data view | Empty state, loading state, pagination or scroll behaviour |
| Any action button | Confirmation step (if destructive), success feedback, error feedback |
| Any navigation | Active state, breadcrumb update, back behaviour |
| Any search / filter | No-results state, clear/reset behaviour |
| Any async operation | Loading indicator, timeout/error handling |
| Any modal / dialog | Close behaviour (ESC, backdrop click, X button), focus trap |
| Any Bug work item | Steps to reproduce, expected vs actual behaviour, verified-fixed state |

Do not infer AC beyond these standard patterns without explicit content
from the work item. Flag anything else as [UNRESOLVED].

---

## Phase 4 — Hierarchy & Theme Detection

### Step 4: Reconstruct the ADO hierarchy context

If parent/child relationships are visible, map them:

```
Epic: [#ID title]
  Feature: [#ID title]
    User Stories:
      - [#ID title] ← current item(s)
      - [#ID title]
```

Use this to:
- Understand scope (a Story under a large Feature may be one of many)
- Identify sibling stories that should be prototyped together
- Flag if a Story's scope seems too large (should be split into a Feature)

### Step 5: Group work items by feature theme (if multiple provided)

```
Feature / Theme: [name]
Work Items: [IDs]
Shared context: [what they have in common]
Suggested prototyping sequence: [ordered list]
```

Recommended prototyping sequence:
1. Navigation shell and layout (if applicable)
2. Primary happy-path flows
3. Validation and error states
4. Edge cases and empty states
5. Secondary flows

---

## Phase 5 — Structured Output

### Step 6: Produce the ADO Parse Report

```
## ADO Work Item Parse Report
Work items processed: [count]
Total [INFERRED] items: [count]
Total [UNRESOLVED] items: [count]

### ADO Hierarchy Map
[Step 4 output]

### Normalised Work Items
[One normalised block per work item — Step 3 format]

### Feature Groupings
[Step 5 output if multiple work items]

### Recommended Prototyping Sequence
[Ordered list]

### Ambiguity Log
[All [UNRESOLVED] items consolidated, with owning work item ID]

### Synthesizer Handoff Summary
Ready for synthesis: [#IDs]
Blocked (needs clarification): [#IDs + what's needed]
```

---

## Phase 6 — Handoff to Synthesizer

Parsed work items feed into ux-requirements-synthesizer as follows:

- Normalised user stories → Section 2 (User Stories)
- Inferred AC → Section 2 acceptance criteria (marked [INFERRED])
- Gaps/questions → Section 9 (Ambiguity Log)
- Out of scope → Section 8 (Constraints & Out-of-Scope)
- Prototyping sequence → Section 3 (Screen Inventory) ordering

---

## Common ADO Anti-Patterns & How to Handle Them

| Anti-pattern | How to handle |
|---|---|
| AC field empty, requirements buried in description | Extract from description, mark [INFERRED], note source |
| AC written as Task list ("Dev: build API", "QA: test flow") | Ignore Task-level items; derive functional AC [INFERRED] |
| Feature-level item with no child Stories | Treat as a Story; flag that it may need splitting [UNRESOLVED] |
| Story title is a technical task ("Refactor search component") | Flag as likely Task not Story; clarify UX scope [UNRESOLVED] |
| Multiple features bundled in one Story | Split into sub-stories; note the split explicitly |
| Story written from system POV ("System shall...") | Rewrite as user POV; flag if intent unclear |
| Bug work item mixed with feature work in AC | Separate bug AC (reproduce → fix → verify) from feature AC |
| Iteration Path missing | Note as [UNRESOLVED] if priority/sequencing is needed |
| Tags used for scope/status ("MVP", "Blocked") | Capture tags and factor into constraints or ambiguity log |
| Parent Feature is vague or missing | Note missing context; infer from Story title if possible |

---

## Rules

1. **Never invent business logic** — only infer standard UX patterns (loading, error, empty)
2. **Low-clarity work items need user input** — do not synthesise from a title alone
3. **Mark every inference** — [INFERRED] on every AC, story element, or gap-fill not in the original
4. **Use ADO terminology** when communicating with the user — work item not ticket, AC field not comments
5. **One story per work item** — if a work item contains multiple stories, split and note the split
6. **Respect the hierarchy** — a Feature is not a Story; don't prototype a Feature as if it's a single screen
7. **Tasks are implementation detail** — ignore child Tasks for UX purposes unless they reveal missing AC
8. **Dependencies are blocking** — if Story B depends on Story A, note this in the prototyping sequence