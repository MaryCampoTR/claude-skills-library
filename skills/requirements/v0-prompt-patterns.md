---
name: v0-prompt-patterns
description: >
  A pattern library of proven v0 prompt structures for common Saffron screen
  archetypes. Use when writing the v0 prompt section of a requirements spec,
  or when asked to produce a v0 prompt directly. Covers: form page, data table,
  dashboard, detail panel, empty/error states, modal flows, and navigation
  shells. Compose from patterns rather than writing from scratch every time.
version: 1.0.0
updated: 2026-03-27
relevant_roles:
  - design
  - engineering
owner: "@MaryCampoTR"
---

# SKILL: v0 Prompt Patterns — Saffron Screen Archetypes

## Purpose
Reusable, proven v0 prompt structures for the most common Saffron screen
types. Compose from these patterns to produce consistently high-quality
prompts with minimal variation between runs.

---

## Universal Preamble (include in EVERY v0 prompt)

```
Build using the Saffron Design System (Thomson Reuters).

Stack: React 18 + TypeScript + Tailwind CSS 3.4 (saf-* utilities) +
ShadCN/ui base components. Component imports from @saffron/core-components.

Fonts:
- Headings: Clario — font-family: var(--saf-font-family-heading), fallback: Georgia serif
- Body: Source Sans 3 — font-family: var(--saf-font-family-body), fallback: sans-serif
- Icons: Font Awesome 6 Sharp (light weight default, solid for emphasis)

Saffron token reminders:
- Focus rings: box-shadow: 0 0 0 2px #ffffff, 0 0 0 4px var(--saf-interactive-focus)
- Form field borders: CSS border (inside stroke). All other component borders: CSS outline (outside stroke).
- "Dark"/"Light" on components = visual intensity (not theme mode)
- Use appearance= not variant=. Use density= not size=.
- SafBadgeStatus: appearance="info" (NOT "informational")
- SafNumberField: instructionalText= (NOT helpText=)
- appearance="hero" = orange CTA (#D64000) — not destructive
- Primary brand colour: Racing Green #123021 (interactive-primary-default)
- Page background: var(--saf-bg-default) = #fcfcfc
```

---

## Pattern 1: Navigation Shell

Use for: Any screen that needs SafProductHeader + SafSidenav layout.
Compose this first, then layer content patterns on top.

```
## Navigation Shell

### SafProductHeader (top bar)
- Background: var(--saf-bg-inverse) [#212223 dark bar]
- Left: product logo/wordmark
- Center or right: primary nav links [SafNav]
- Right: SafButtonAvatar (user avatar + dropdown)
- Height: 56px (saf-17 spacing)

### SafSidenav (left sidebar)
- Width: 240px collapsed content area
- Background: var(--saf-bg-subtle) [#f7f7f7]
- Border-right: 1px solid var(--saf-border-subtle)
- Nav items: SafButtonInline or custom nav item pattern
- Active item: background var(--saf-interactive-primary-hover), text var(--saf-interactive-primary-active)
- Supports collapsible sections with SafDivider between groups

### MainContent
- Padding: p-saf-6 (24px all sides)
- Background: var(--saf-bg-default)
- Max-width: [specify or leave fluid]
```

---

## Pattern 2: Page Header

Use for: Top of any main content area. Title + primary actions.

```
## PageHeader
Layout: flex justify-between items-center, mb-saf-6

Left:
  - Page title: Clario medium, text-saf-2xl (28px), text-saf-text-heavy
  - Optional subtitle: Source Sans 3 regular, text-saf-sm (14px), text-saf-text-subtle
  - Optional SafBreadcrumb above the title

Right (action buttons — right-aligned):
  - Primary action: SafButton appearance=hero density=standard "[Label]"
    (use hero for the single most important CTA on the page)
  - Secondary action: SafButton appearance=secondary density=standard "[Label]"
  - Tertiary/destructive: SafButton appearance=tertiary density=standard "[Label]"
  - Max 3 buttons before overflow to SafMenu
```

---

## Pattern 3: Form Page

Use for: Create / edit / settings forms. Single column or two-column.

```
## Form Page

### Layout
- Max-width: 640px (single column) or 960px (two-column)
- Centered or left-aligned (specify)
- Section groups separated by SafDivider + section heading

### Form Section
- Section heading: Clario medium text-saf-lg (20px), mb-saf-4
- Fields: stack vertically, gap-saf-4 (16px) between fields
- Two-column grid: grid grid-cols-2 gap-saf-4 (use for related short fields)

### Field Pattern
Each field:
  SafTextField
    label="[Field Label]"        ← always present
    required={true/false}
    helpText="[guidance text]"   ← use when field needs explanation
    state="default"              ← default | invalid | success | disabled | readOnly
    placeholder="[placeholder]"

For dropdowns: SafSelect (static options) or SafCombobox (searchable / multi)
For numbers: SafNumberField (not SafTextField type=number)
For long text: SafTextArea
For toggles in forms: SafToggleSwitch (label left, toggle right)
For grouped choices: SafRadioGroup (mutually exclusive) or SafCheckboxGroup (multi-select)

### Validation States
On submit with errors:
  - Each invalid field: state="invalid" validationMessage="[specific error]"
  - SafAlert type="error" at top of form: "Please correct the errors below."

On successful save:
  - SafAlert type="success": "[Action] saved successfully."
  OR navigate away (specify which)

### Form Footer (SafButtonFooter)
  type="form"  ← F-pattern: primary buttons left, cancel/back right
  Left: SafButton appearance=primary "Save" + SafButton appearance=secondary "Save as Draft"
  Right: SafButtonInline "Cancel"
```

---

## Pattern 4: Data Table Page

Use for: List views, search results, admin tables.

```
## Data Table Page

### Toolbar (above table)
Layout: flex justify-between items-center, mb-saf-4

Left:
  - SafSearchField placeholder="Search [entity]..." width 280px
  - Filter chips: SafChip type=clickable per active filter
  - SafButtonInline "Clear all" (visible only when filters active)

Right:
  - Result count: Source Sans 3, text-saf-sm, text-saf-text-subtle "[n] results"
  - SafButton appearance=hero "Add [Entity]" (primary page action)
  - SafButtonIcon appearance=tertiary (export/download icon)

### Table
- Full width, border-collapse
- Header row: bg-saf-bg-subtle, Clario medium text-saf-xs (12px) uppercase
  tracking-wide, text-saf-text-subtle, border-b saf-border-strong
- Body rows: bg-saf-bg-default, hover:bg-saf-bg-subtle
  border-b saf-border-subtle
- Row height: 48px (standard density)
- Cell text: Source Sans 3 regular text-saf-sm, text-saf-text-strong
- Primary cell (name/title): text-saf-text-heavy, optionally SafAnchor if clickable
- Status cell: SafBadgeStatus appearance=[error|success|warning|info|neutral]
- Actions cell (right-aligned): SafButtonIcon appearance=tertiary per action
  (max 2–3 inline, overflow to SafMenu)

### Empty State
  Centered in table body area:
  - Icon: FA Sharp Light, 32px, text-saf-text-subtle
  - Heading: Clario medium text-saf-lg, text-saf-text-strong, "[No Entity] found"
  - Body: Source Sans 3 text-saf-sm, text-saf-text-subtle
    "[Contextual explanation — e.g. Try adjusting your search]"
  - CTA (if applicable): SafButton appearance=primary "[Add first Entity]"

### Loading State
  Replace table body rows with SafSkeleton:
  - 5 rows of: SafSkeleton height=16px, varying widths (60%, 80%, 40%, 90%, 50%)
  - Match column widths

### Pagination
  Layout: flex justify-between items-center, mt-saf-4
  Left: "Showing [n]–[n] of [total]" Source Sans 3 text-saf-sm text-saf-text-subtle
  Right: SafButton appearance=secondary density=compact "Previous" +
         page number indicators + SafButton appearance=secondary density=compact "Next"
```

---

## Pattern 5: Detail Panel / Drawer

Use for: Side panel that opens from a table row or list item click.

```
## Detail Panel (SafDrawer)

### Trigger
  Table row click OR SafButtonIcon on row

### Drawer
  SafDrawer
    side="right"
    width=480px (standard) or 640px (content-rich)

  Header:
    - Title: Clario medium text-saf-xl (24px), text-saf-text-heavy
    - Subtitle: Source Sans 3 text-saf-sm, text-saf-text-subtle
    - Close: SafButtonIcon appearance=tertiary icon=fa-xmark (top right)
    - Border-bottom: saf-border-subtle

  Body (scrollable):
    - Padding: p-saf-6
    - Sections separated by SafDivider
    - Labels: Clario medium text-saf-xs uppercase tracking-wide,
      text-saf-text-subtle, mb-saf-1
    - Values: Source Sans 3 regular text-saf-md, text-saf-text-strong
    - Status: SafBadgeStatus inline with label

  Footer (SafButtonFooter):
    type="default"  ← Z-pattern: secondary actions left, primary right
    Right: SafButton appearance=primary "Edit" +
           SafButton appearance=secondary "Close"
    Left: SafButton appearance=tertiary "Delete" (destructive — triggers confirm dialog)
```

---

## Pattern 6: Confirmation Dialog

Use for: Destructive actions, irreversible operations.

```
## Confirmation Dialog (SafDialog modal=true)

### Trigger
  Destructive button click (delete, remove, deactivate, etc.)

### Dialog
  Width: 480px, centered
  modal=true (backdrop blocks interaction)

  Header:
    - Title: Clario medium text-saf-lg, text-saf-text-heavy
      "[Action] [Entity]?" — e.g. "Delete Document?"
    - No close X for destructive actions (force explicit choice)

  Body:
    - Source Sans 3 regular text-saf-md, text-saf-text-strong
    - Explain what will happen: "This will permanently delete [entity name].
      This action cannot be undone."
    - SafAlert type="warning" if consequences are severe

  Footer (SafButtonFooter type="form"):
    Left: SafButton appearance=hero "[Confirm action]"
          ← hero for the destructive confirm (high-contrast, demands attention)
    Right: SafButtonInline "Cancel"
```

---

## Pattern 7: Empty & Error States

Use these consistently across all data regions.

```
## Empty State (no data)
  Centered, padding p-saf-12
  - Icon: FA Sharp Light, 40px, color: var(--saf-text-subtle)
  - Heading: Clario medium text-saf-xl, text-saf-text-strong
  - Body: Source Sans 3 text-saf-sm, text-saf-text-subtle, max-width 320px centered
  - CTA: SafButton appearance=primary (if user can create data)
         SafButton appearance=secondary (if user should go elsewhere)

## Error State (data fetch failed)
  Centered, padding p-saf-12
  - SafAlert type="error" "[Entity] could not be loaded."
  - SafButton appearance=secondary "Try again" (triggers retry)
  - SafButtonInline "Contact support" (secondary escape)

## Loading State
  Use SafSkeleton components matching the shape of the content they replace:
  - Text line: SafSkeleton height=14px width=[varies]
  - Heading: SafSkeleton height=24px width=40%
  - Avatar: SafSkeleton height=32px width=32px rounded-saf-circle
  - Card: SafSkeleton height=120px width=100% rounded-saf-sm
  - Table row: 5× SafSkeleton height=16px per row, staggered widths
  Animate: pulse (Tailwind animate-pulse)
```

---

## Pattern 8: Form Modal

Use for: Quick-create or quick-edit actions that don't warrant a full page.

```
## Form Modal (SafDialog modal=true)

### Trigger
  SafButton appearance=primary/hero "Add [Entity]"

### Dialog
  Width: 560px (compact form) or 640px (longer form)

  Header:
    - Title: Clario medium text-saf-lg, text-saf-text-heavy "[Add/Edit Entity]"
    - Close: SafButtonIcon appearance=tertiary icon=fa-xmark (top right)
    - Border-bottom: saf-border-subtle

  Body (scrollable if needed):
    - Padding: p-saf-6
    - Fields: SafTextField/SafSelect etc. — gap-saf-4 between fields
    - Validation: per-field state=invalid + validationMessage
    - SafAlert type=error at top if submission fails

  Footer (SafButtonFooter type="form"):
    Left: SafButton appearance=primary "Save [Entity]"
          SafButton appearance=secondary "Save & Add Another" (if applicable)
    Right: SafButtonInline "Cancel"
```

---

## Pattern 9: Filter Bar

Use for: Pages where data can be filtered by multiple dimensions.

```
## Filter Bar
  Layout: flex flex-wrap gap-saf-2, padding py-saf-3 border-b saf-border-subtle
  Background: var(--saf-bg-subtle)

  Filter controls (left-aligned):
    - SafSelect for each categorical filter
      density=compact, label=[filter name], width=160–200px
    - SafCombobox for multi-select filters
      density=compact
    - SafSearchField for text search (if separate from main search)
      density=compact, width=200px

  Active filter chips (below or inline):
    - SafChip type=closable per active filter value
    - Label: "[Filter]: [Value]"
    - On close: removes that filter

  Right-aligned:
    - SafButtonInline "Clear all filters" (visible only when ≥1 filter active)
    - Result count: text-saf-sm text-saf-text-subtle
```

---

## Composition Guide

Most screens are composed from 2–4 patterns:

| Screen type | Patterns to compose |
|---|---|
| List / admin page | Navigation Shell + Page Header + Data Table + Empty/Error States |
| Create / edit page | Navigation Shell + Page Header + Form Page |
| Dashboard | Navigation Shell + Page Header + Data Region (cards) + Empty/Error States |
| Record detail | Navigation Shell + Page Header + Detail Panel |
| Settings page | Navigation Shell + Page Header + Form Page (multiple sections) |
| Wizard / multi-step | Navigation Shell + Page Header (with step indicator) + Form Page + Form Modal |

---

## v0-Specific Tips

1. **Name every component explicitly** — v0 performs better with `SafButton appearance=primary` than "a green button"
2. **Specify layout with Tailwind** — use saf-* spacing utilities; v0 maps these correctly when the theme is set
3. **Include all states in one prompt** — list default, loading, empty, and error states upfront; v0 won't add them unless asked
4. **Copy matters** — real placeholder text produces better output than "Lorem ipsum"
5. **One screen per prompt** — complex multi-screen flows produce better results when broken into one prompt per screen
6. **Reference patterns by name** — "use the Data Table pattern with a Filter Bar" is faster than re-specifying everything
7. **Specify responsive behaviour explicitly** if needed — v0 defaults to desktop; mobile adaptations need to be stated
