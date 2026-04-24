---
name: visual-quality-assurance
description: >
  Use when comparing a Figma design file against a live demo environment or screenshot to identify
  visual discrepancies. Triggers when QA is needed on UI implementation fidelity, design system
  compliance, or when flagging component/token violations against the Saffron design system.
version: "1.0.0"
updated: "2026-04-22"
relevant_roles: [design, engineering]
owner: "@Amirasallam2205"
---

# SKILL: Visual Quality Assurance — Design-to-Implementation Comparison

## Purpose

This skill enables systematic comparison between a Figma design source and a live demo environment (or screenshot fallback) to surface visual discrepancies, design system violations, and missed requirements. It is for designers and engineers who need a structured, prioritized bug report that distinguishes content issues, Saffron design system deviations, and requirement gaps.

## When to Use

- A Figma file and a demo URL (or screenshot) are both available for comparison
- QA is needed before a feature ships to verify implementation fidelity
- A stakeholder requests a visual audit of a built UI against its design
- Design system compliance needs to be checked (component usage, token application)
- Inconsistencies in spacing, color, typography, or component variants have been spotted and need formal documentation
- Demo URL is inaccessible — a screenshot of the implemented screen is an acceptable substitute

## When NOT to Use

- No Figma source is available (cannot establish design intent)
- The task is purely functional/behavioral testing, not visual
- The feature is in early wireframe/prototype stage not meant for pixel comparison
- The Figma file is marked as a draft by the designer

## Instructions

### Step 1 — Gather Inputs

Collect the following before starting:
1. **Figma file link** — share with "can view" access, or export frames as images
2. **Demo URL** — the live/staging environment to compare against
   - If URL is inaccessible, request a **screenshot** of the relevant screen(s)
3. **Screen / feature scope** — which page, flow, or component is in scope

### Step 2 — Side-by-Side Comparison

For each screen or component in scope:
1. Place Figma frame and demo screenshot side by side
2. Scan systematically in this order:
   - **Layout & spacing** — alignment, padding, margins, grid adherence
   - **Typography** — font family, size, weight, line height, letter spacing
   - **Color & tokens** — fill colors, border colors, background colors vs. Saffron tokens
   - **Component variants** — correct component used? correct state (default/hover/disabled)?
   - **Iconography** — correct icon, correct size, correct color
   - **Content** — labels, copy, placeholder text, empty states
   - **Responsive behavior** — if breakpoints are in scope

### Step 3 — Classify Each Discrepancy

Tag every finding with one (or more) of these themes:

| Theme | Definition |
|---|---|
| **Content** | Label, copy, or data does not match the design or agreed spec |
| **Saffron Design System** | Wrong component, variant, token, or pattern from the Saffron DS |
| **Requirement Gap** | A designed element is entirely missing from the implementation |
| **Layout / Spacing** | Spacing, alignment, or sizing deviates from design |
| **Typography** | Font, size, weight, or line height deviates |

### Step 4 — Assign Priority

Use this matrix:

| Priority | Criteria |
|---|---|
| **P1 — Critical** | Breaks brand, accessibility violation, completely wrong component, missing core UI element |
| **P2 — High** | Wrong Saffron token applied (e.g., wrong color semantic), wrong component variant, layout misalignment visible at a glance |
| **P3 — Medium** | Minor spacing deviation (<8px off), typography weight mismatch, icon size off |
| **P4 — Low** | Pixel-level polish, copy capitalization inconsistency, hover state mismatch |

### Step 5 — Flag Design System Violations Explicitly

For each Saffron DS violation, record:
- **Component name** (e.g., `Button/Primary` vs `Button/Secondary` used)
- **Token name** (e.g., `color.text.primary` used instead of `color.text.inverse`)
- **Expected vs. Actual** — what the Figma shows vs. what is implemented

### Step 6 — Compile Report

Produce a structured report (see Output Format below).

## Output Format

### VQA Report — [Screen / Feature Name]

**Date:** YYYY-MM-DD
**Figma Source:** [link or "Frame export provided"]
**Demo / Screenshot:** [URL or "Screenshot provided"]
**Reviewer:** [name or @handle]

---

#### Summary

| Theme | Count |
|---|---|
| Content | N |
| Saffron Design System | N |
| Requirement Gap | N |
| Layout / Spacing | N |
| Typography | N |
| **Total** | **N** |

---

#### Findings

For each finding:

```
ID: VQA-001
Priority: P2 — High
Theme: Saffron Design System
Location: [Component name / screen section]
Description: Button uses `Button/Secondary` but Figma specifies `Button/Primary`.
Expected: Button/Primary (Saffron token: color.action.primary)
Actual: Button/Secondary (color.action.secondary)
Screenshot ref: [attach or annotate]
```

---

#### Recommended Fix Order

List P1s first, then group P2s by theme to minimize engineering context-switching.

## Dependencies

- Requires access to Figma file (view permission) or exported frame images
- Requires Saffron Design System component and token documentation to validate DS findings
- Feeds into: `superpowers:requesting-code-review` (findings can be attached as review context)
