---
name: ux-requirements-synthesizer
description: >
  Transform piecemeal UX inputs (meeting transcripts, half-baked user stories,
  design artifacts) into complete, v0-ready requirement specs using Saffron
  Design System vocabulary, tokens, and components. Use when given any raw
  product/UX input and asked to produce a structured spec, prototype brief,
  or v0 prompt. Includes the full Saffron component map, 3-tier token system,
  v0 prompt template, ambiguity resolution rules, and a pre-delivery checklist.
version: 1.0.0
updated: 2026-03-27
relevant_roles:
  - design
  - product
owner: "@MaryCampoTR"
---

# SKILL: UX Requirements Synthesizer — Saffron Design System
**Version:** 1.0.0 | **Updated:** 2026-03-27  
**Purpose:** Transform piecemeal inputs (transcripts, user stories, design artifacts) into complete, v0-ready requirement specs that reference Saffron vocabulary, tokens, and components with zero ambiguity.

---

## Role
You are a Lead UX Designer's requirements synthesis engine. You receive messy inputs and produce structured, v0-ready specifications. You never invent design decisions — you apply what is in this skill file or flag gaps for the user.

---

## Intake Taxonomy

Classify each input before processing:

| Input Type | What to extract | Weight |
|---|---|---|
| **Meeting transcript** | User pain points, accepted/rejected ideas, open questions, implied flows | Medium — intent signal |
| **Half-baked user story** | Actor, goal, acceptance criteria (stated or implied), edge cases | High — functional signal |
| **Design artifact (screenshot/Figma)** | Layout intent, component names, visual hierarchy, interaction hints | High — visual signal |
| **Existing code/PRs** | Data shapes, prop names, API contracts, constraints | High — technical signal |
| **Verbal/Slack notes** | Priority signals, stakeholder opinions, out-of-scope markers | Low — context only |

---

## Required Output Schema

Every synthesized spec must include all sections below. Mark `[UNRESOLVED]` for anything that cannot be inferred from inputs — never guess.

```
## Feature: [Name]
### 1. Intent & Context
  - What problem is being solved
  - Who is the primary user
  - What triggers this flow
  - Success condition

### 2. User Stories (normalized)
  As a [actor], I want to [goal] so that [outcome].
  Acceptance criteria:
    - [ ] criterion 1
    - [ ] criterion 2

### 3. Screen Inventory
  [ScreenName]: [one-line purpose]
  Route: [path if known, else UNRESOLVED]

### 4. Component Spec (per screen)
  Per component:
    - Saffron component name (from vocabulary below)
    - Props and values (from component map below)
    - Content / copy
    - Conditional visibility rules

### 5. Interaction & State Map
  [Trigger] → [State change] → [Visual result]
  List all: empty state, loading, error, success, disabled, edge cases

### 6. Data Contract
  - Key data entities (shape, not implementation)
  - Which fields are required vs optional
  - Any async operations (loading/error states required)

### 7. Copy & Tone Notes
  - Button labels, field labels, error messages, empty states
  - Tone: [professional / conversational / instructional] — default: professional

### 8. Constraints & Out-of-Scope
  - Known constraints from inputs
  - Explicitly out of scope

### 9. Ambiguity Log
  - [UNRESOLVED] item 1 — question to ask
  - [UNRESOLVED] item 2 — question to ask

### 10. v0 Prompt (ready to paste)
  [See v0 Prompt Template section below]
```

---

## Saffron Design System Reference

### Tech Stack
- **React 18 + TypeScript + Vite 5**
- **Tailwind CSS 3.4** extended with `saf-*` utilities
- **ShadCN/ui** as base, overridden with Saffron tokens and vocabulary
- **Fonts:** Clario (headings, fallback: Georgia serif) · Source Sans 3 (body) · Font Awesome 6 Sharp (icons)
- **Component package:** `@saffron/core-components`

---

### Token Architecture (3-Tier)

**Tier 1 — Primitives** (never reference directly in components)

| Category | Scale | Values |
|---|---|---|
| **Color — Named** | black, white, ash (#fcfcfc), graphite (#212223), focus (#0065ff) | — |
| **Color — Scales** | purple, red, green, gold, amber, lime, teal, racingGreen, orange, sky, gray | 100–800 steps |
| **Spacing** | saf-0→saf-23 | 0, 2, 4, 8, 12, 16, 20, 24, 32, 48, 64, 68, 80, 92px |
| **Font Size** | saf-xs→saf-5xl | 12, 14, 16, 20, 24, 28, 32, 40, 56px |
| **Font Weight** | light(300), regular(400), medium(500), semibold(600), bold(700) | — |
| **Border Radius** | saf-xs(4), saf-sm(8), saf-md(16), saf-xl(24), saf-circle(88) | px |
| **Shadow** | saf-1, saf-1-alt, saf-a11y-dark | — |

**Tier 2 — Semantic tokens** (what components reference — use these in specs)

| Token | CSS Variable | Resolved Value |
|---|---|---|
| **Text** | | |
| text-heavy | `--saf-text-heavy` | #212223 |
| text-strong | `--saf-text-strong` | #404040 |
| text-subtle | `--saf-text-subtle` | #666666 |
| text-knockout | `--saf-text-knockout` | #ffffff |
| **Background** | | |
| bg-default | `--saf-bg-default` | #fcfcfc |
| bg-subtle | `--saf-bg-subtle` | #f7f7f7 |
| bg-strong | `--saf-bg-strong` | #f2f2f2 |
| bg-stronger | `--saf-bg-stronger` | #e5e5e5 |
| bg-inverse | `--saf-bg-inverse` | #212223 |
| **Border** | | |
| border-subtle | `--saf-border-subtle` | #e5e5e5 |
| border-strong | `--saf-border-strong` | #d2d2d2 |
| border-stronger | `--saf-border-stronger` | #8a8a8a |
| **Interactive — Primary** (Racing Green brand) | | |
| interactive-primary-default | `--saf-interactive-primary-default` | #123021 |
| interactive-primary-hover | `--saf-interactive-primary-hover` | #edf2f0 |
| interactive-primary-active | `--saf-interactive-primary-active` | #1d4b34 |
| on-primary-default | `--saf-interactive-on-primary-default` | #f7f7f7 |
| **Interactive — Secondary** | | |
| interactive-secondary-default | `--saf-interactive-secondary-default` | #ffffff |
| on-secondary-default | `--saf-interactive-on-secondary-default` | #1d4b34 |
| **Interactive — Hero** (Orange CTA) | | |
| interactive-hero-default | `--saf-interactive-hero-default` | #D64000 |
| on-hero-default | `--saf-interactive-on-hero-default` | #ffffff |
| **Focus ring** | | |
| interactive-focus | `--saf-interactive-focus` | #0065ff (light) / #5aa3ed (dark) |
| **Status** | | |
| status-error-subtle / strong | `--saf-status-error-subtle/strong` | #ffeded / #dc0a0a |
| status-success-subtle / strong | `--saf-status-success-subtle/strong` | #eaffe5 / #387c2b |
| status-warning-subtle / strong | `--saf-status-warning-subtle/strong` | #fff8e5 / #ab3300 |
| status-info-subtle / strong | `--saf-status-info-subtle/strong` | #edf6ff / #0062c4 |
| status-neutral-subtle / strong | `--saf-status-neutral-subtle/strong` | #ededed / #404040 |
| **Anchor** | | |
| anchor-default/hover/active/visited | `--saf-anchor-*` | #0062c4 / #054688 / #032f5b / #9647d1 |
| **Disabled** | | |
| disabled-subtle / on-subtle | `--saf-disabled-subtle / --saf-disabled-on-subtle` | per theme |

**Tailwind utility mapping** — use `tw:` prefix in specs to indicate Tailwind class:
- `tw:text-saf-text-heavy` → `--saf-text-heavy`
- `tw:bg-saf-bg-subtle` → `--saf-bg-subtle`
- `tw:border-saf-border-strong` → `--saf-border-strong`
- `tw:text-saf-sm`, `tw:p-saf-4`, `tw:rounded-saf-xs`, `tw:shadow-saf-1`

---

### Typography System

| Category | Font | Sizes | Use |
|---|---|---|---|
| **Display** | Clario medium | 5xl (lg), 4xl (sm) | Hero headers |
| **Heading** | Clario medium | 4xl, 3xl, 2xl, xl, lg, md | Page/section titles |
| **Body** | Source Sans 3 regular/semibold | lg, md, sm, xs | All body copy |
| **Label Text** | Clario regular/medium | md, sm | Form labels |
| **Eyebrow** | Clario medium | md, sm | Section labels above headings |
| **Icon** | FA6 Sharp Light (default) / Solid (strong) / Brands | xs–2xl | Icons |

Line heights: standard body 1.5, bodySmall 1.35, heading 1.2 | compact body 1.35, bodySmall 1.2, heading 1.1

---

### Critical Vocabulary Rules

⚠️ **These rules prevent the most common spec errors:**

1. **`appearance` NOT `variant`** — Saffron uses `appearance` for visual style on most components. But verify per-component — it means different things in different contexts.
2. **`density: compact | standard` NOT `size: sm | md`** — Saffron sizing is always density-based.
3. **"Dark" / "Light" = visual intensity, NOT theme mode** — e.g. Badge `value: dark` means high-contrast solid fill. Never conflate with light/dark theme switching.
4. **Prop names are NOT consistent across components** — always reference the component map. e.g. `SafTextField` uses `helpText`; `SafNumberField` uses `instructionalText`.
5. **`hero` appearance = orange CTA** — not destructive. It is Saffron's primary call-to-action, NOT an error or danger action.
6. **Focus ring:** always `box-shadow: 0 0 0 2px #ffffff, 0 0 0 4px var(--saf-interactive-focus)` — never `outline` for focus.
7. **Borders:** Form fields use `border` (inside stroke). All other components use `outline` (outside stroke).

---

### Component Vocabulary

All 33 built components with their key props. **Always use these exact names and prop values.**

#### Buttons

**`SafButton`** — `@saffron/core-components`  
Props: `appearance: primary | secondary | tertiary | hero` · `density: standard | compact | large` · `iconOnly: boolean` (requires `aria-label`)  
States: default, hover, active, focus, disabled, loading  
Notes: `hero` = orange CTA. `primary` = racing green solid. `secondary` = outlined green. `tertiary` = ghost.

**`SafButtonIcon`** — icon-only button  
Props: `appearance: primary | secondary | tertiary | hero` · `density: standard | compact`  
Requires: `aria-label`

**`SafButtonEmbeddedIcon`** — icon button inside input fields (has left structural border)  
Props: `density: standard | compact | extra-compact` · includes tooltip on hover/focus  
3 sizes: 40×40 / 32×32 / 24×24

**`SafButtonInline`** — text link button  
Props: `size: sm | md | lg` · renders as `<button>` or `<a>` depending on `href`  
Always underlined. No bg, no border.

**`SafButtonAvatar`** — button with avatar  
Props: `density: standard | compact` · `badge?: ReactNode`

**`SafButtonFooter`** — layout component for form/dialog footers  
Props: `type: default | form` · `size`  
`default` = Z-pattern (anchor left, buttons right). `form` = F-pattern (buttons left, anchor right).

#### Form Inputs

**`SafTextField`** — standard text input  
Props: `state: default | invalid | success | disabled | readOnly` · `label` (required) · `helpText` · `validationMessage` · `required: boolean` · `optionalText`  
States: default, hover, focus, invalid, success, disabled, readOnly

**`SafTextArea`** — multi-line text input (inherits SafTextField props)

**`SafNumberField`** — numeric input with steppers  
Props: `state: default | invalid | disabled | readOnly` (**no success state**) · `instructionalText` (**not** helpText) · `label`  
Stepper: shows on hover/focus-within (error: focus-within only)

**`SafSearchField`** — search input  
Props: `state` · `helpText` · includes clear button and embedded icon support  

**`SafSelectTextField`** — select + text field combo

**`SafSelect`** — dropdown select  
Props: `state: default | invalid | success | disabled | readOnly` · `label` · `helpText` · `validationMessage`  
Dependencies: SafListbox + SafOption

**`SafListbox`** — list container (used inside SafSelect, SafCombobox)

**`SafOption`** — individual option item (supports single and multi-select checkbox mode)

**`SafCombobox`** — searchable select with multi-select chip support  
Props: `state` · `helpText` · multi-select shows "n items selected" placeholder  
Selected items render as `SafChip type=closable`  
Dependencies: SafListbox + SafOption + SafChip

**`SafCheckbox`** — single checkbox  
States: unchecked, checked, indeterminate, disabled, invalid

**`SafCheckboxGroup`** — group of checkboxes

**`SafRadio`** — single radio button  
States: unselected, selected, disabled, invalid

**`SafRadioGroup`** — group of radio buttons (uses SafRadioGroupContext)

**`SafToggleSwitch`** — toggle switch  
States: off, on, disabled

#### Feedback & Status

**`SafAlert`** — inline alert/notification  
Props: `type: error | success | warning | info | neutral` · `appearance: default | [others]`  
States: visible, dismissed

**`SafBadgeStatus`** — status badge  
Props: `appearance: error | success | warning | info | neutral`  
Note: prop value is `info` (NOT `informational`)

**`SafBadgeCounter`** — numeric counter badge

**`SafStatusDot`** — small status indicator dot

**`SafProgressRing`** — circular progress indicator

**`SafTooltip`** — tooltip (shows on hover and focus; NOT shown when disabled)

#### Navigation

**`SafBreadcrumb`** — breadcrumb navigation

**`SafAnchor`** — styled link/anchor  
States: default, hover, active, visited

**`SafAnchorCta`** — CTA link variant

#### Overlay

**`SafDialog`** — modal dialog  
Props: `modal: boolean`

**`SafDrawer`** — side drawer/panel

#### Content

**`SafChip`** — filter/selection chip  
Props: `type: clickable | closable | closable-with-icon`  
`clickable`: entire chip is button (secondary green tokens). `closable`: body is div, only SafChipClose is interactive (grey border). `closable-with-icon`: closable + leading icon slot.

**`SafAvatar`** — user avatar (24×24 in buttons, larger standalone)

**`SafCard`** — card container

**`SafDivider`** — horizontal/vertical divider

**`SafSkeleton`** — loading skeleton placeholder

#### Layout / Navigation Patterns

**`SafProductHeader`** — top product header bar

**`SafSidenav`** — side navigation

**`SafNav`** — navigation component

---

### Field Sizing Reference (confirmed from Figma)

| Density | Height | Padding |
|---|---|---|
| standard | h-10 (40px) | px-[12px] py-[8px] |
| compact | h-8 (32px) | px-[12px] py-[4px] |

Icon sizes within fields: stepper chevrons 12px (saf-xs) · label info icon 16px (saf-md) · validation icons 14px (saf-sm)

---

## v0 Prompt Template

Use this structure when writing the final v0 prompt in Section 10 of the output spec. Fill every token precisely.

```
Build a [screen name] using the Saffron Design System (Thomson Reuters).

## Stack
React 18 + TypeScript + Tailwind CSS 3.4 (with saf-* utilities) + ShadCN/ui base components.
Component imports: `@saffron/core-components`.
Fonts: Clario (var(--saf-font-family-heading)) for headings, Source Sans 3 (var(--saf-font-family-body)) for body, Font Awesome 6 Sharp for icons.

## Layout
[Describe the overall layout: sidebar + main, full-width, split pane, etc.]
[Reference SafProductHeader / SafSidenav / SafNav if needed]
[Specify max-width, padding, bg color via saf-* tokens]

## Screens & Components

### [ScreenName]
Purpose: [one line]

[ComponentName]
  - Saffron component: [SafButton, SafTextField, etc.]
  - Props: appearance=[value] density=[value] [other props]
  - Content: "[label text]"
  - Condition: [always visible | visible when X | hidden when Y]

[Repeat for each component]

## Interaction & States
- [Trigger] → [what changes] → [visual result using saf-* tokens]
- Empty state: [description]
- Loading state: [use SafSkeleton or SafProgressRing]
- Error state: [component state=invalid + validationMessage="[text]"]

## Data Shape
[List the key fields and types]

## Copy
- [Field label]: "[text]"
- [Button]: "[label]"
- [Error message]: "[text]"
- [Empty state]: "[text]"

## Constraints
[List what is NOT in scope]

## Saffron Token Reminders
- Focus rings: box-shadow: 0 0 0 2px #ffffff, 0 0 0 4px var(--saf-interactive-focus)
- Form field borders: CSS border (inside). All other borders: CSS outline (outside).
- "Dark"/"Light" on components = visual intensity, NOT theme mode.
- `appearance` NOT `variant`. `density` NOT `size`.
- SafBadgeStatus appearance="info" (NOT "informational").
- SafNumberField uses `instructionalText` (NOT helpText).
- hero appearance = orange CTA (#D64000), NOT destructive.
```

---

## Ambiguity Resolution Rules

When synthesizing from messy inputs, apply these rules:

**Infer these without asking:**
- Default density is `standard` unless compactness is mentioned
- Default button appearance for primary actions is `primary`
- Default text color is `text-heavy` (`#212223`)
- Default background is `bg-default` (`#fcfcfc`)
- If a form field is mentioned without a state, default is `default`
- If "required" is mentioned on a field, add `required: boolean = true`
- If a confirmation action is described, it's a `SafDialog` with `modal: true`
- Error, loading, and empty states are always required for async data — generate them even if not mentioned

**Always flag as `[UNRESOLVED]` and ask:**
- Specific copy/labels not present in the inputs
- Whether a data operation is async (affects loading/error states)
- Navigation destination after a completed action
- Whether a feature is in scope if inputs are contradictory
- Any destructive actions (need explicit confirmation pattern)
- Permission/role-based visibility of components

**Never invent:**
- Saffron component props or values not in this skill
- Token names not in this skill
- Business logic not present in any input
- API contracts

---

## Input Processing Workflow

1. **Classify all inputs** using the intake taxonomy above
2. **Extract intent** — what is the user trying to accomplish? What problem is solved?
3. **Normalize user stories** — rewrite to standard format with acceptance criteria
4. **Inventory screens** — list every screen/view implied by the inputs
5. **Map components per screen** — use Saffron vocabulary only
6. **Identify all states** — for every component and every screen
7. **Document data shape** — what data is needed, where does it come from?
8. **Extract copy** — every label, button, message, empty state
9. **Log ambiguities** — mark `[UNRESOLVED]` with a specific question
10. **Write v0 prompt** — use the template, reference saf-* tokens throughout

---

## Quality Checklist (run before delivering any spec)

- [ ] Every Saffron component name matches the vocabulary list exactly
- [ ] Every prop value is verified against the component map (no invented values)
- [ ] `appearance` used instead of `variant` where applicable
- [ ] `density` used instead of `size`
- [ ] All async operations have loading + error states specified
- [ ] Empty states are specified for all list/data views
- [ ] Focus rings specified as box-shadow pattern (not outline)
- [ ] No `[UNRESOLVED]` items in sections 1–8 (moved to section 9)
- [ ] v0 prompt includes stack declaration, Saffron token reminders, and copy
- [ ] "hero" appearance is used for primary CTA, not primary (unless it IS the brand green action)
- [ ] SafBadgeStatus uses `info` not `informational`
- [ ] SafNumberField uses `instructionalText` not `helpText`

---

## Notes on Saffron Versions (Baseline)

| Package | Version |
|---|---|
| Design Component Library | 3.20.0 |
| Design Token Library | 3.11.0 |
| Core Components Package | 3.18.0 |
| Core Styles Package | 3.8.0 |

Figma sources: Token Library `K79KnYrmEBddTS6k5wsrHp` · Component Library `9VuW5ptbYS7jfyHiuPpybR` (329 components, 64 categories)

