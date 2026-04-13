---
name: saffron-master
description: >
  Master Saffron Design System reference skill for Thomson Reuters. Authoritative
  source for tokens, components, visual patterns, and implementation guidance
  across both React (v0/prototyping) and HTML (Web Components) targets. Use
  whenever building, speccing, or reviewing any Saffron-based UI. Supersedes
  all other floating Saffron skills in the organisation. Token values and
  component props derived from the actual saffron-prototype-theme repo
  (token dictionary v1.0.0, baseline component library 3.20.0).
version: 1.0.0
updated: 2026-03-27
---

# Saffron Design System — Master Skill
**Authoritative source.** Derived from the actual `saffron-prototype-theme`
repo (`saffron-token-dictionary.json` + `saffron-component-map.json`).

---

## ⚠️ Known Issues with Other Saffron Skills in Circulation

Before using any other Saffron skill you find in the organisation, check
it against these known discrepancies. If a skill conflicts with this file,
this file wins — it is derived from the actual repo.

| Issue | Affected skill | Detail |
|---|---|---|
| **Wrong CSS variable prefix** | `saffron_skill.zip` (visual guidelines) | Uses `--saffron-*` prefix. Correct prefix is `--saf-*`. Do not use `--saffron-*` variables. |
| **Wrong semantic colour values** | `saffron_skill.zip` | success = `#2a9d50` (wrong, should be `#387c2b`), error = `#d62f00` (wrong, should be `#dc0a0a`) |
| **Wrong compact button height** | `saffron_skill.zip` | States 34px. Correct value from repo is 32px. |
| **Wrong border radius values** | `saffron_skill.zip` | States xs=2px, sm=4px, md=8px. Correct: xs=4px, sm=8px, md=16px. |
| **Wrong visited link colour** | `saffron_skill.zip` | States racing green 600. Correct: purple #9647d1. |
| **Invented spacing values** | `saffron_skill.zip` | Contains `--saffron-spacing-7: 28px` which doesn't exist in the Saffron scale. |
| **Stale CDN versions** | `saffron-html.skill` | References core-components 3.12.0 and styles 3.6.1. Current baseline: 3.18.0 / 3.8.0. |
| **Missing hero button** | Both floating skills | Neither documents `appearance=hero` (orange CTA, #D64000). This is a core Saffron pattern. |

---

## Implementation Targets

Saffron has two distinct implementation paradigms. Be explicit about which
you are working in — they use different syntax and different token names.

| Target | When to use | Component syntax | Token prefix |
|---|---|---|---|
| **React** (v0 / prototyping) | v0 prompts, React prototypes, this skill suite | `SafButton`, `SafTextField` etc. | `--saf-*` |
| **HTML / Web Components** | Standalone HTML prototypes, CDN-based delivery | `<saf-button>`, `<saf-text-field>` etc. | `--saf-color-*` (CDN) |

---

## Visual Design Philosophy

Saffron's character: **professional, trustworthy, enterprise-grade, with
subtle warmth from the racing green palette.**

Five guiding principles: **purposeful · human-centered · efficient ·
intuitive · dynamic**

**What to avoid:**
- Bright or vibrant colours — Saffron uses muted, sophisticated tones
- Playful or casual aesthetics — keep it professional
- Overly rounded corners — subtle 4px–16px radius only
- Dramatic shadows — keep elevation subtle
- Generic fonts — always Clario + Source Sans 3
- Inconsistent spacing — always multiples of 4px
- Missing focus states — non-negotiable
- More than one primary CTA per page section

---

## Token Architecture (3-Tier)

**Tier 1 — Primitives.** Raw palette values. Never reference directly
in components or specs.

**Tier 2 — Semantic tokens.** Contextual roles. Always use these.

**Tier 3 — Component tokens.** Per-component overrides (product-header,
avatar, etc.).

---

## Tier 1: Primitive Tokens (reference only)

### Colour Palette

**Named:**
- black `#000000` · white `#ffffff` · ash `#fcfcfc` · graphite `#212223`
- focus `#0065ff` · hidden `#ffffff03` · overlay `#0000004d`

**Scales (100–800):**

| Scale | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 |
|---|---|---|---|---|---|---|---|---|
| **racingGreen** | #f5f7f6 | #edf2f0 | #ccd9d2 | #a1b2a9 | #6e8178 | #50665b | #1d4b34 | #123021 |
| **gray** | #f7f7f7 | #f2f2f2 | #ededed | #e5e5e5 | #d2d2d2 | #8a8a8a | #666666 | #404040 |
| **sky** | #edf6ff | #e3f1fd | #a6d2ff | #5aa3ed | #0874e3 | #0062c4 | #054688 | #032f5b |
| **red** | #ffeded | #ffbfbf | #ff8080 | #dc0a0a | #a10707 | — | — | — |
| **green** | #eaffe5 | #c9ffbf | #87cc7a | #387c2b | #214a1a | — | — | — |
| **orange** | #f8eadd | #efb399 | #e68c66 | #de6633 | #D64000 | #ab3300 | #802600 | #561a00 |
| **gold** | #fff8e5 | #fcf0da | #fde8c2 | #f2d08f | #e9b045 | #cf962a | #a6761c | #5d461c |
| **purple** | #F4E5FF | #e3bfff | #9647D1 | #621f95 | #351a6e | — | — | — |
| **amber** | #fff7f0 | #f8eadd | #f2ddc9 | #f0bf95 | #f0a05b | #d4792a | #aa4f00 | #553011 |
| **teal** | #f0f7f5 | #e3f3ee | #cfe5e0 | #add9cf | #91c9bd | #4db299 | #307a68 | #24594c |

### Typography Primitives

**Font families:**
- Clario — `--saf-font-family-clario` (headings, labels, UI)
- Source Sans 3 — `--saf-font-family-source-sans-3` (body, content, data)
- Font Awesome 6 Sharp — `--saf-font-family-fa-sharp` (icons)
- Font Awesome 6 Brands — `--saf-font-family-fa-brands` (brand icons)

**Font sizes:** xs=12px · sm=14px · md=16px · lg=20px · xl=24px · 2xl=28px · 3xl=32px · 4xl=40px · 5xl=56px

**Font weights:** light=300 · regular=400 · medium=500 · semibold=600 · bold=700

**Line heights (standard density):** body=1.5 · bodySmall=1.35 · heading=1.2
**Line heights (compact density):** body=1.35 · bodySmall=1.2 · heading=1.1

### Spacing Scale

| Token | CSS Variable | Value |
|---|---|---|
| saf-0 | `--saf-spacing-0` | 0px |
| saf-05 | `--saf-spacing-05` | 2px |
| saf-1 | `--saf-spacing-1` | 4px |
| saf-2 | `--saf-spacing-2` | 8px |
| saf-3 | `--saf-spacing-3` | 12px |
| saf-4 | `--saf-spacing-4` | 16px |
| saf-5 | `--saf-spacing-5` | 20px |
| saf-6 | `--saf-spacing-6` | 24px |
| saf-8 | `--saf-spacing-8` | 32px |
| saf-12 | `--saf-spacing-12` | 48px |
| saf-16 | `--saf-spacing-16` | 64px |
| saf-17 | `--saf-spacing-17` | 68px |
| saf-20 | `--saf-spacing-20` | 80px |
| saf-23 | `--saf-spacing-23` | 92px |

Note: saf-7 (28px) does NOT exist. saf-10 (40px) does NOT exist in the
scale — use saf-spacing-10 only if confirmed from Figma.

### Border Radius

| Token | Value |
|---|---|
| saf-xs | 4px |
| saf-sm | 8px |
| saf-md | 16px |
| saf-xl | 24px |
| saf-circle | 88px |

### Shadows / Elevation

| Level | Value | Use |
|---|---|---|
| level-1 | `0 1px 2px 0 rgba(0,0,0,0.16)` | Cards, small raised elements |
| level-1-alt | `0 2px 8px 2px rgba(31,31,31,0.10)` | Alternate card elevation |
| a11y-on-dark | `0 0 0 1px #FFFFFF` | Accessibility on dark backgrounds |
| **Focus ring** | `0 0 0 2px #ffffff, 0 0 0 4px var(--saf-interactive-focus)` | ALL interactive elements |

### Transitions

- Standard: `0.2s ease` (most interactions)
- Quick: `0.15s ease` (micro-interactions)
- Smooth: `0.3s ease` (deliberate, larger changes)

---

## Tier 2: Semantic Tokens (use these in all specs and code)

### Text

| Role | CSS Variable | Value |
|---|---|---|
| text-heavy | `--saf-text-heavy` | #212223 |
| text-strong | `--saf-text-strong` | #404040 |
| text-subtle | `--saf-text-subtle` | #666666 |
| text-knockout | `--saf-text-knockout` | #ffffff |

### Background

| Role | CSS Variable | Value |
|---|---|---|
| bg-default | `--saf-bg-default` | #fcfcfc |
| bg-subtle | `--saf-bg-subtle` | #f7f7f7 |
| bg-strong | `--saf-bg-strong` | #f2f2f2 |
| bg-stronger | `--saf-bg-stronger` | #e5e5e5 |
| bg-inverse | `--saf-bg-inverse` | #212223 |

### Border

| Role | CSS Variable | Value |
|---|---|---|
| border-subtle | `--saf-border-subtle` | #e5e5e5 |
| border-strong | `--saf-border-strong` | #d2d2d2 |
| border-stronger | `--saf-border-stronger` | #8a8a8a |

### Interactive — Primary (Racing Green)

| Role | CSS Variable | Value |
|---|---|---|
| primary-default | `--saf-interactive-primary-default` | #123021 |
| primary-hover | `--saf-interactive-primary-hover` | #edf2f0 |
| primary-active | `--saf-interactive-primary-active` | #1d4b34 |
| on-primary-default | `--saf-interactive-on-primary-default` | #f7f7f7 |
| on-primary-hover | `--saf-interactive-on-primary-hover` | #1d4b34 |
| on-primary-active | `--saf-interactive-on-primary-active` | #ffffff |
| border-primary-default | `--saf-interactive-border-primary-default` | #123021 |

### Interactive — Secondary

| Role | CSS Variable | Value |
|---|---|---|
| secondary-default | `--saf-interactive-secondary-default` | #ffffff |
| secondary-hover | `--saf-interactive-secondary-hover` | #edf2f0 |
| secondary-active | `--saf-interactive-secondary-active` | #1d4b34 |
| on-secondary-default | `--saf-interactive-on-secondary-default` | #1d4b34 |
| border-secondary-default | `--saf-interactive-border-secondary-default` | #1d4b34 |

### Interactive — Tertiary (Ghost)

| Role | CSS Variable | Value |
|---|---|---|
| tertiary-default | `--saf-interactive-tertiary-default` | #ffffff03 (transparent) |
| tertiary-hover | `--saf-interactive-tertiary-hover` | #edf2f0 |
| on-tertiary-default | `--saf-interactive-on-tertiary-default` | #1d4b34 |

### Interactive — Hero (Orange CTA)

| Role | CSS Variable | Value |
|---|---|---|
| hero-default | `--saf-interactive-hero-default` | #D64000 |
| hero-hover | `--saf-interactive-hero-hover` | (racingGreen-200 bg) |
| on-hero-default | `--saf-interactive-on-hero-default` | #ffffff |

⚠️ Hero = orange CTA. It is NOT destructive. It is the strongest call-to-action.

### Focus

| Role | CSS Variable | Value |
|---|---|---|
| focus | `--saf-interactive-focus` | #0065ff (light) / #5aa3ed (dark) |

**Focus ring pattern (apply to ALL interactive elements):**
```css
box-shadow: 0 0 0 2px #ffffff, 0 0 0 4px var(--saf-interactive-focus);
```
Never use `outline` for focus rings — always `box-shadow`.

### Status Colours

⚠️ These are the authoritative values from the token dictionary.
Do not use values from other floating skills — they are wrong.

| Status | Subtle CSS Var | Subtle Value | Strong CSS Var | Strong Value |
|---|---|---|---|---|
| error | `--saf-status-error-subtle` | #ffeded | `--saf-status-error-strong` | #dc0a0a |
| success | `--saf-status-success-subtle` | #eaffe5 | `--saf-status-success-strong` | #387c2b |
| warning | `--saf-status-warning-subtle` | #fff8e5 | `--saf-status-warning-strong` | #ab3300 |
| info | `--saf-status-info-subtle` | #edf6ff | `--saf-status-info-strong` | #0062c4 |
| neutral | `--saf-status-neutral-subtle` | #ededed | `--saf-status-neutral-strong` | #404040 |

### Anchor

| State | CSS Variable | Value |
|---|---|---|
| default | `--saf-anchor-default` | #0062c4 |
| hover | `--saf-anchor-hover` | #054688 |
| active | `--saf-anchor-active` | #032f5b |
| visited | `--saf-anchor-visited` | #9647d1 (purple) |

⚠️ Visited links are purple — not green. Other skills have this wrong.

### Disabled

| Role | CSS Variable |
|---|---|
| disabled-subtle | `--saf-disabled-subtle` |
| disabled-on-subtle | `--saf-disabled-on-subtle` |
| disabled-strong | `--saf-disabled-strong` |
| disabled-on-strong | `--saf-disabled-on-strong` |
| disabled-border-default | `--saf-disabled-border-default` |

---

## Typography System

| Category | Font | Sizes | Use |
|---|---|---|---|
| Display | Clario medium | 5xl (56px), 4xl (40px) | Hero headers |
| Heading | Clario medium | 4xl–md (40px→16px) | Page and section titles |
| Body | Source Sans 3 regular/semibold | lg–xs (20px→12px) | All body copy, data |
| Label Text | Clario regular/medium | md (16px), sm (14px) | Form labels |
| Eyebrow | Clario medium | md, sm | Section labels above headings |
| Icon (default) | FA6 Sharp Light | xs–2xl | Default icons |
| Icon (strong) | FA6 Sharp Solid | xs–2xl | Emphasis icons |
| Icon (brand) | FA6 Brands Regular | xs–2xl | Brand/social icons |

---

## Field Sizing (confirmed from Figma)

| Density | Height | Padding |
|---|---|---|
| standard | 40px | px-[12px] py-[8px] |
| compact | **32px** ← (not 34px) | px-[12px] py-[4px] |

---

## Critical Vocabulary Rules

1. **`appearance=` not `variant=`** — for visual style on most components
2. **`density=` not `size=`** — for sizing (React target)
3. **"Dark"/"Light" on components = visual intensity, not theme mode**
4. **`hero` = orange CTA (#D64000), not destructive**
5. **Prop names are NOT consistent across components** — verify each one
6. **`--saf-*` prefix only** — never `--saffron-*`
7. **Borders:** form fields = CSS `border` (inside). All others = CSS `outline` (outside)
8. **Focus:** always `box-shadow` double-ring, never `outline`

---

## React Component Reference (v0 / prototyping target)

All components from `@saffron/core-components`. Baseline: 3.20.0.

### Buttons

| Component | Key props | Notes |
|---|---|---|
| `SafButton` | `appearance: primary\|secondary\|tertiary\|hero` · `density: standard\|compact\|large` · `iconOnly: boolean` | iconOnly requires aria-label |
| `SafButtonIcon` | `appearance` · `density` | Requires aria-label |
| `SafButtonEmbeddedIcon` | `density: standard\|compact\|extra-compact` | Used INSIDE input fields, has border-l |
| `SafButtonInline` | `size: sm\|md\|lg` | Renders as `<button>` or `<a>` (href). Always underlined |
| `SafButtonAvatar` | `density` · `badge?: ReactNode` | Avatar always 24×24px circular |
| `SafButtonFooter` | `type: default\|form` | default=Z-pattern, form=F-pattern |

### Form Inputs

| Component | Key props | States | Notes |
|---|---|---|---|
| `SafTextField` | `label` · `helpText` · `validationMessage` · `required` · `optionalText` | default, hover, focus, invalid, success, disabled, readOnly | Uses `helpText` |
| `SafTextArea` | inherits SafTextField | same | Multi-line |
| `SafNumberField` | `label` · `instructionalText` · `state` | default, hover, focus, invalid, disabled, readOnly | Uses `instructionalText` NOT `helpText`. No success state. |
| `SafSearchField` | `state` · `helpText` | — | Includes clear button |
| `SafSelect` | `label` · `helpText` · `validationMessage` · `state` | default→readOnly | Depends: SafListbox + SafOption |
| `SafSelectTextField` | — | — | Select + text field combo |
| `SafCombobox` | `state` · `helpText` | — | Searchable. Multi-select chips = SafChip closable. Depends: SafListbox + SafOption + SafChip |
| `SafListbox` | — | — | Container for options |
| `SafOption` | — | — | Single/multi-select mode |
| `SafCheckbox` | — | unchecked, checked, indeterminate, disabled, invalid | — |
| `SafCheckboxGroup` | — | — | Group wrapper |
| `SafRadio` | — | unselected, selected, disabled, invalid | — |
| `SafRadioGroup` | — | — | Uses SafRadioGroupContext |
| `SafToggleSwitch` | — | off, on, disabled | — |

### Feedback & Status

| Component | Key props | Notes |
|---|---|---|
| `SafAlert` | `type: error\|success\|warning\|info\|neutral` · `appearance` | States: visible, dismissed |
| `SafBadgeStatus` | `appearance: error\|success\|warning\|info\|neutral` | Use `info` NOT `informational` |
| `SafBadgeCounter` | — | Numeric counter |
| `SafStatusDot` | — | Small coloured dot |
| `SafProgressRing` | — | Circular progress |
| `SafTooltip` | — | Shows on hover + focus. NOT shown when disabled. |

### Content & Layout

| Component | Key props | Notes |
|---|---|---|
| `SafChip` | `type: clickable\|closable\|closable-with-icon` | clickable=button, closable=div+SafChipClose |
| `SafAvatar` | — | 24×24px in buttons, larger standalone |
| `SafCard` | — | Card container |
| `SafDivider` | — | Horizontal/vertical |
| `SafSkeleton` | — | Loading placeholder |

### Navigation & Overlay

| Component | Key props | Notes |
|---|---|---|
| `SafBreadcrumb` | — | — |
| `SafAnchor` | — | States: default, hover, active, visited |
| `SafAnchorCta` | — | CTA link variant |
| `SafDialog` | `modal: boolean` | modal=true traps focus |
| `SafDrawer` | — | Side panel |
| `SafProductHeader` | — | Top product bar |
| `SafSidenav` | — | Left nav |
| `SafNav` | — | Navigation component |

### Component Dependency Chains
Always build dependencies before parents:
- SafSelect → SafListbox → SafOption
- SafCombobox → SafListbox → SafOption + SafChip
- SafButtonFooter → SafAnchor (or SafButtonInline)

---

## HTML / Web Component Reference (CDN target)

Use this section when building standalone HTML prototypes (not v0/React).

### CDN Setup (updated to current baseline)

```html
<link rel="stylesheet"
  href="https://saffron.int.thomsonreuters.com/cdn/styles/3.8.0/index.css" />

<script type="importmap">
{
  "imports": {
    "@saffron/config":
      "https://saffron.int.thomsonreuters.com/cdn/config/1.1.11/es5/index.js",
    "@saffron/date-fns":
      "https://saffron.int.thomsonreuters.com/cdn/date-fns/4.1.3/index.js",
    "@saffron/core-components":
      "https://saffron.int.thomsonreuters.com/cdn/code/3.18.0/es5/index.js",
    "tslib": "https://esm.sh/tslib",
    "@microsoft/fast-web-utilities": "https://esm.sh/@microsoft/fast-web-utilities@4",
    "@floating-ui/dom": "https://esm.sh/@floating-ui/dom@1",
    "tabbable": "https://esm.sh/tabbable@6"
  }
}
</script>

<script type="module">
  import { SafButton, SafTextField, SafSelect } from '@saffron/core-components';
  SafButton(); SafTextField(); SafSelect();
  // Register only components you use
</script>
```

⚠️ The floating `saffron-html.skill` referenced 3.12.0 / 3.6.1 — those
are stale. Use 3.18.0 / 3.8.0 above.

### Web Component Syntax

```html
<!-- Buttons -->
<saf-button appearance="primary">Save</saf-button>
<saf-button appearance="secondary">Cancel</saf-button>
<saf-button appearance="tertiary">Learn more</saf-button>
<saf-button appearance="hero">Get started</saf-button>
<saf-button icon-only appearance="tertiary" aria-label="Search">
  <saf-icon icon-name="search"></saf-icon>
</saf-button>

<!-- Form controls -->
<saf-text-field label="Email" placeholder="Enter email" required></saf-text-field>
<saf-select label="Country">
  <saf-option value="us">United States</saf-option>
</saf-select>
<saf-checkbox>I agree to terms</saf-checkbox>
<saf-radio-group label="Method" name="method">
  <saf-radio value="a">Option A</saf-radio>
</saf-radio-group>

<!-- Layout -->
<saf-container centered="true">...</saf-container>
<saf-layout-grid>
  <saf-layout-grid-item xs="12" md="6">...</saf-layout-grid-item>
</saf-layout-grid>
<saf-flex direction="row" gap="md" align="center" justify="space-between">
  ...
</saf-flex>

<!-- Cards & data -->
<saf-card>
  <saf-text variant="heading-3" slot="header">Title</saf-text>
  <p>Content</p>
  <saf-button slot="footer">Action</saf-button>
</saf-card>
<saf-badge appearance="success">Active</saf-badge>
<saf-progress-ring></saf-progress-ring>
<saf-progress-bar value="60" max="100"></saf-progress-bar>

<!-- Overlays -->
<saf-dialog id="myDialog">
  <saf-text variant="heading-2" slot="header">Title</saf-text>
  <p>Content</p>
  <saf-button slot="footer" appearance="primary">Confirm</saf-button>
</saf-dialog>
<saf-drawer position="right">
  <saf-text variant="heading-3" slot="header">Title</saf-text>
  <p>Content</p>
</saf-drawer>
<saf-tooltip content="Helpful tip"><saf-button>Hover</saf-button></saf-tooltip>
<saf-popover>
  <saf-button slot="trigger">Options</saf-button>
  <saf-menu>
    <saf-menu-item>Edit</saf-menu-item>
    <saf-menu-item>Delete</saf-menu-item>
  </saf-menu>
</saf-popover>

<!-- Navigation -->
<saf-breadcrumb>
  <saf-breadcrumb-item><a href="/">Home</a></saf-breadcrumb-item>
  <saf-breadcrumb-item>Current</saf-breadcrumb-item>
</saf-breadcrumb>
<saf-pagination current="3" total="10"></saf-pagination>
<saf-tabs>
  <saf-tab>Overview</saf-tab>
  <saf-tab-panel>Overview content</saf-tab-panel>
</saf-tabs>

<!-- Typography -->
<saf-text variant="heading-1">Page Title</saf-text>
<saf-text variant="heading-2">Section</saf-text>
<saf-text variant="body">Regular text</saf-text>
<saf-text variant="body-small">Small text</saf-text>
<saf-text weight="bold">Bold</saf-text>
<saf-text color="muted">Muted</saf-text>

<!-- Icons -->
<saf-icon icon-name="search"></saf-icon>
<saf-icon icon-name="download"></saf-icon>
```

### Web Component Sizing Vocabulary
In the Web Component API, sizing uses `size` attribute (not `density`):
- `size="small"` = compact equivalent
- `size="medium"` = standard equivalent (default)
- `size="large"` = large

### Workspace Pattern (split-pane)
```html
<saf-workspace-pattern initial-size="50"
  scrollable-primary="false" scrollable-secondary="false">
  <saf-windows slot="primary" addable="true">
    <saf-window closeable="false">Primary</saf-window>
    <saf-window-panel><!-- left content --></saf-window-panel>
  </saf-windows>
  <saf-windows slot="secondary" addable="false">
    <saf-window closeable="false">Secondary</saf-window>
    <saf-window-panel><!-- right content --></saf-window-panel>
  </saf-windows>
</saf-workspace-pattern>
```

### Chat Pattern
```html
<saf-chat>
  <saf-message-box user="AI" timestamp="10:30 AM">
    Hello! How can I help you?
  </saf-message-box>
  <div slot="footer">
    <saf-button-embedded>
      <saf-text-field label="Enter a message"></saf-text-field>
      <saf-button appearance="tertiary" icon-only type="submit">
        <saf-icon icon-name="send"></saf-icon>
      </saf-button>
    </saf-button-embedded>
  </div>
</saf-chat>
```

---

## Icon Reference (FA6 Sharp)

Used as `<saf-icon icon-name="...">` (HTML) or via FA class in React.

**Actions:** add · subtract · close · download · upload · edit · search ·
zoom-in · zoom-out · show · hide · send · calendar · expand · collapse ·
link · print · save · share · filter · copy · trash · delete · pin · chat · setting

**Navigation:** chevron-right · chevron-left · chevron-up · chevron-down ·
arrow-right · arrow-left · arrow-up · arrow-down · refresh · sort · undo ·
redo · home · menu · go-to-first · go-to-last

**Status:** error · alert · information · success · checkmark · warning ·
question · thumbs-up · thumbs-down

**Objects:** user · users · folder · document · lock · clock · phone ·
location · bell · bell-mute · dollar-sign · star · heart

---

## Saffron Version Baseline

| Package | Version |
|---|---|
| Design Component Library (Figma) | 3.20.0 |
| Design Token Library (Figma) | 3.11.0 |
| Core Components (npm/CDN) | 3.18.0 |
| Core Styles (npm/CDN) | 3.8.0 |

Figma sources:
- Token Library: `K79KnYrmEBddTS6k5wsrHp`
- Component Library: `9VuW5ptbYS7jfyHiuPpybR` (329 components, 64 categories)
