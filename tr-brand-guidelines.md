---
name: tr-brand-guidelines
description: >
  Enforces Thomson Reuters (TR) brand guidelines—Clario typeface, official color palette, and visual style rules—in all generated artifacts. Use this skill whenever the user says "use TR branding," "apply TR brand guidelines," "make it on-brand," "TR style," or any similar phrasing. Also apply when the user asks for a dashboard, report, visualization, chart, HTML page, React component, Word document, .docx file, presentation, slide deck, or .pptx file and mentions TR, Thomson Reuters, or work context where TR branding would be expected. This skill covers HTML/CSS pages, React components, data visualizations/charts, Word documents (.docx), and presentations (.pptx).
---

# TR Brand Guidelines Skill

## Overview

When this skill is active, all generated artifacts (HTML, React, charts/data visualizations) must strictly follow TR's visual identity: the Clario typeface, the official color palette, and the layout and hierarchy rules below.

---

## Step 1: Load the Font

Before writing any artifact, read the font face declarations from:

```
references/clario-fonts.md
```

This file contains base64-embedded `@font-face` CSS for all 14 Clario variants (Air through Black, normal and italic). Copy the full CSS block into the `<style>` tag of every HTML artifact, or into the CSS-in-JS / stylesheet of every React component. **Never** reference Clario from a CDN or external URL — use only the embedded declarations from this file.

### Font weight reference

| Weight name | CSS font-weight |
|-------------|----------------|
| Air         | 100            |
| Thin        | 200            |
| Light       | 300            |
| Regular     | 400            |
| Medium      | 500            |
| Bold        | 700            |
| Black       | 900            |

### Typographic rules

- Set `font-family: 'Clario', sans-serif` as the global default on `body` or the root element.
- **Headings (H1–H2):** Clario Bold (700) or Black (900)
- **Subheadings / labels:** Clario Medium (500) or SemiBold (600 maps to Bold)
- **Body text:** Clario Regular (400)
- **Captions / metadata:** Clario Light (300)
- **Emphasis within text:** Clario Bold (700) + TR Orange (`#D64000`) — used together for in-line emphasis
- Do not use system fonts (Arial, Helvetica, etc.) anywhere in a branded artifact.

---

## Step 2: Apply the Color Palette

### Core colors

| Role | Name | Hex |
|------|------|-----|
| Primary text / headings on light bg | Black | `#000000` |
| Text / headings on dark bg | White | `#FFFFFF` |
| **Primary brand color** | TR Orange | `#D64000` |
| **Alternate primary / dark bg** | TR Racing Green | `#123121` |

### Accent colors

| Name | Hex | Typical use |
|------|-----|-------------|
| TR Dark Gold | `#E9B045` | Charts, highlights, badges |
| TR Dark Amber | `#D4792A` | Secondary chart series, warm accents |
| TR Dark Sky | `#0874E3` | Links, info states, cool accents |
| TR Dark Teal | `#4DB299` | Success states, data series |
| TR Dark Lime | `#8FCB64` | Positive indicators, data series |

### Background / surface colors

| Name | Hex | Paired accent |
|------|-----|--------------|
| TR Light Gold | `#FCF2DA` | Dark Gold |
| TR Light Amber | `#F8EADD` | Dark Amber |
| TR Light Sky | `#E3F1FD` | Dark Sky |
| TR Light Teal | `#E3F3EE` | Dark Teal |
| TR Light Lime | `#E1F4CD` | Dark Lime |

### Color usage rules

1. **Orange (`#D64000`) is the primary brand color.** Use it for primary CTAs, key data callouts, active states, and in-line bold emphasis.
2. **Racing Green (`#123121`) is a dark background option.** When used as a background, use White (`#FFFFFF`) for text. Ensure contrast ratio ≥ 4.5:1 for body text, ≥ 3:1 for large text.
3. **Light backgrounds pair with their matching Dark accent** (e.g., TR Light Sky background → TR Dark Sky text/icons). Do not mix light backgrounds with unrelated dark accents.
4. **Never place Orange text on Racing Green background** (or vice versa) without verifying contrast first — these combinations can fail WCAG AA.
5. For **chart color sequences**, use the accent set in order: Orange → Dark Sky → Dark Teal → Dark Gold → Dark Amber → Dark Lime. Avoid using Light palette colors for data series (insufficient contrast on white).
6. **Neutrals:** Use `#000000` / `#FFFFFF` for text. For borders and dividers, use `rgba(0,0,0,0.12)` on light backgrounds or `rgba(255,255,255,0.2)` on dark backgrounds.

---

## Step 3: Layout & Component Style Rules

### General

- Prefer clean, minimal layouts with generous whitespace.
- Border radius: `4px` for cards/containers, `2px` for inputs and buttons, `50%` for avatar/badge circles.
- Box shadows: use sparingly — `0 1px 3px rgba(0,0,0,0.12)` for subtle card elevation.
- No gradients except subtle `linear-gradient` overlays on Racing Green hero sections (dark-to-transparent, max 30% opacity).

### Buttons

- **Primary button:** Background `#D64000`, text `#FFFFFF`, Clario Bold, no border.
- **Secondary button:** Border `1.5px solid #D64000`, text `#D64000`, background transparent.
- **Dark-surface button:** Background `#FFFFFF`, text `#123121`, Clario Bold.
- Hover states: darken background by ~10% (`#B83800` for primary orange).

### Data visualizations / charts

- Load Chart.js or D3 as needed; do not use external brand-unaware defaults.
- Override all default chart colors with the TR accent palette (see color sequence above).
- Chart titles: Clario Bold 700, `#000000`.
- Axis labels: Clario Regular 400, `#000000` at 85% opacity.
- Gridlines: `rgba(0,0,0,0.08)`, 1px.
- Tooltips: background `#123121`, text `#FFFFFF`, Clario Regular.
- Legends: Clario Light 300.

### React-specific

- Define a `TR_COLORS` constant object at the top of the file for clean reuse:

```js
const TR_COLORS = {
  orange: '#D64000',
  green: '#123121',
  white: '#FFFFFF',
  black: '#000000',
  darkGold: '#E9B045',
  darkAmber: '#D4792A',
  darkSky: '#0874E3',
  darkTeal: '#4DB299',
  darkLime: '#8FCB64',
  lightGold: '#FCF2DA',
  lightAmber: '#F8EADD',
  lightSky: '#E3F1FD',
  lightTeal: '#E3F3EE',
  lightLime: '#E1F4CD',
};
```

- Inject Clario `@font-face` declarations via a `<style>` tag rendered at the root of the component.
- Use inline styles or Tailwind utility classes — never assume a global stylesheet exists.

---

## Word Documents (.docx)

Word does not support embedded custom fonts the same way HTML does — Clario will only render on machines where the font is installed. Apply TR branding through color, structure, and style overrides instead, which travel with the file on all systems.

### Font handling in Word

- Set the **default document font to Clario** — it is installed on all TR machines.
- Use `font: 'Clario'` on all `TextRun` and style definitions. Map TR typographic intent as follows:

| TR Role | docx-js setting |
|---------|----------------|
| H1 (major heading) | Clario, size 40, bold |
| H2 (section heading) | Clario, size 28, bold |
| H3 (sub-section) | Clario, size 24, bold |
| Body text | Clario, size 24 (12pt), regular |
| Captions / metadata | Clario, size 20 (10pt), regular |
| Emphasis | Clario, bold + TR Orange color |

- For recipients outside TR who may not have Clario installed, recommend exporting to PDF to lock in font rendering.

### Color in Word

Use TR hex values (without `#`) in all `color`, `fill`, and `shading` properties:

```javascript
const TR = {
  orange:     'D64000',
  green:      '123121',
  white:      'FFFFFF',
  black:      '000000',
  darkGold:   'E9B045',
  darkAmber:  'D4792A',
  darkSky:    '0874E3',
  darkTeal:   '4DB299',
  darkLime:   '8FCB64',
  lightGold:  'FCF2DA',
  lightAmber: 'F8EADD',
  lightSky:   'E3F1FD',
  lightTeal:  'E3F3EE',
  lightLime:  'E1F4CD',
};
```

### TR Word document structure conventions

**Cover / header block:**
- Use a Racing Green (`123121`) shaded paragraph as the document header or cover band.
- Place the TR org/department name as white (`FFFFFF`) text, eyebrow-style (small, light weight).
- Place the document title as large bold black text immediately below.
- Add a TR Orange (`D64000`) paragraph border-bottom as a divider beneath the cover block.

**Section headings:**
- H1: Black (`000000`), bold, with a TR Orange bottom border on the paragraph for visual separation.
- H2: Racing Green (`123121`), bold — signals a major sub-section.
- H3: TR Orange (`D64000`), bold — signals a sub-topic or named item.

**Tables:**
- Header row: Racing Green fill (`123121`), white text, with a TR Orange right-side accent border on the label column.
- Alternating body rows: TR Light Gold (`FCF2DA`) and white (`FFFFFF`).
- All borders: light gray (`DDDDDD`), single-line, 1pt. Never use default blue Word table borders.
- Always use `ShadingType.CLEAR` (never `SOLID`) to prevent black backgrounds.

**Callout / pull-quote blocks:**
- Left border: TR Orange (`D64000`), thick (size 16), single style.
- Background: TR Light Gold (`FCF2DA`) shading.
- Text: italic, regular weight, dark gray (`444444`).

**Dividers:**
- Use a paragraph bottom border in TR Orange (`D64000`), size 8, single style.
- Never use tables as horizontal rules — they render as empty boxes.

**Footers:**
- Use TR Racing Green text or TR Dark Gold (`E9B045`) for highlighted labels.
- Use tab stops for two-column footer layouts, not tables.

---

## Presentations (.pptx)

Use PptxGenJS to build TR-branded slide decks. The same color and type system applies as all other artifact types, adapted to slide layout conventions.

> **⚠️ Critical:** Never use `#` prefix on hex colors in PptxGenJS — it corrupts the file. Use bare hex strings only: `"D64000"` not `"#D64000"`.

### Color constants for PptxGenJS

```javascript
const TR = {
  orange:     'D64000',
  green:      '123121',
  white:      'FFFFFF',
  black:      '000000',
  darkGold:   'E9B045',
  darkAmber:  'D4792A',
  darkSky:    '0874E3',
  darkTeal:   '4DB299',
  darkLime:   '8FCB64',
  lightGold:  'FCF2DA',
  lightAmber: 'F8EADD',
  lightSky:   'E3F1FD',
  lightTeal:  'E3F3EE',
  lightLime:  'E1F4CD',
};
```

### Font

- Use `fontFace: 'Clario'` on all `addText()` calls — Clario is installed on all TR machines.
- Never use Arial, Calibri, or other system fonts in TR-branded decks.

| Slide element | fontFace | fontSize | bold |
|---------------|----------|----------|------|
| Slide title | Clario | 36–40pt | true |
| Section header | Clario | 22–26pt | true |
| Body / bullets | Clario | 14–16pt | false |
| Callout / stat | Clario | 48–72pt | true |
| Caption / label | Clario | 10–12pt | false |
| Eyebrow / tag | Clario | 10pt, charSpacing: 4 | false |

### Slide structure — "sandwich" pattern

Use a dark/light/dark structure across the deck:

- **Title slide:** Racing Green (`123121`) background, white title, TR Orange accent element.
- **Content slides:** White or TR Light palette background, black body text, TR Orange for emphasis.
- **Closing / section divider slides:** Racing Green background, white text — mirrors the title slide.

### Title slide recipe

```javascript
slide.background = { color: TR.green };

// TR Orange left accent bar
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: 0.18, h: 5.625,
  fill: { color: TR.orange }, line: { color: TR.orange }
});

// Eyebrow (org name)
slide.addText('Thomson Reuters', {
  x: 0.4, y: 1.6, w: 9, h: 0.4,
  fontFace: 'Clario', fontSize: 11, color: TR.darkGold,
  charSpacing: 4, margin: 0
});

// Main title
slide.addText('Presentation Title', {
  x: 0.4, y: 2.1, w: 8.5, h: 1.4,
  fontFace: 'Clario', fontSize: 40, bold: true, color: TR.white, margin: 0
});

// Subtitle / date
slide.addText('Subtitle or Date', {
  x: 0.4, y: 3.6, w: 8, h: 0.5,
  fontFace: 'Clario', fontSize: 16, color: 'rgba not supported — use CCCCCC', margin: 0
});
// Note: use muted light color for subtitle on dark bg, e.g. 'AAAAAA'
```

### Content slide recipe

```javascript
slide.background = { color: TR.white };

// Slide title
slide.addText('Section Title', {
  x: 0.5, y: 0.3, w: 9, h: 0.6,
  fontFace: 'Clario', fontSize: 28, bold: true, color: TR.black, margin: 0
});

// Orange underline accent — thin rectangle below title
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 0.95, w: 9, h: 0.04,
  fill: { color: TR.orange }, line: { color: TR.orange }
});

// Body text
slide.addText('Body content here.', {
  x: 0.5, y: 1.15, w: 9, h: 3.8,
  fontFace: 'Clario', fontSize: 15, color: TR.black, valign: 'top'
});
```

### Stat / callout card recipe

```javascript
// Card background
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.2, w: 2.8, h: 1.8,
  fill: { color: TR.lightSky }, line: { color: TR.lightSky }
});
// Top accent bar
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.2, w: 2.8, h: 0.07,
  fill: { color: TR.darkSky }, line: { color: TR.darkSky }
});
// Stat number
slide.addText('82%', {
  x: 0.5, y: 1.35, w: 2.8, h: 0.9,
  fontFace: 'Clario', fontSize: 52, bold: true, color: TR.darkSky,
  align: 'center', margin: 0
});
// Label
slide.addText('AI Engagement Score', {
  x: 0.5, y: 2.3, w: 2.8, h: 0.5,
  fontFace: 'Clario', fontSize: 11, color: TR.black,
  align: 'center', margin: 0
});
```

### Chart colors

Always override default chart colors with the TR accent sequence:

```javascript
chartColors: [TR.orange, TR.darkSky, TR.darkTeal, TR.darkGold, TR.darkAmber, TR.darkLime]
```

Apply clean chart styling:

```javascript
{
  chartColors: ['D64000', '0874E3', '4DB299', 'E9B045', 'D4792A', '8FCB64'],
  chartArea: { fill: { color: 'FFFFFF' } },
  catAxisLabelColor: '666666',
  valAxisLabelColor: '666666',
  valGridLine: { color: 'EEEEEE', size: 0.5 },
  catGridLine: { style: 'none' },
  showLegend: true, legendPos: 'b',
  titleFontFace: 'Clario', titleFontSize: 14, titleColor: '000000',
}
```

### Section divider / closing slide recipe

```javascript
slide.background = { color: TR.green };

slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: 0.18, h: 5.625,
  fill: { color: TR.orange }, line: { color: TR.orange }
});

slide.addText('Section Title', {
  x: 0.4, y: 2.2, w: 9, h: 1.0,
  fontFace: 'Clario', fontSize: 36, bold: true, color: TR.white, margin: 0
});
```

### Tables in slides

```javascript
const tableData = [
  // Header row
  [
    { text: 'Column A', options: { fill: { color: TR.green }, color: TR.white, bold: true, fontFace: 'Clario', fontSize: 12 } },
    { text: 'Column B', options: { fill: { color: TR.green }, color: TR.white, bold: true, fontFace: 'Clario', fontSize: 12 } },
  ],
  // Alternating body rows — use TR.lightGold / TR.white
  [
    { text: 'Value', options: { fill: { color: TR.lightGold }, color: TR.black, fontFace: 'Clario', fontSize: 12 } },
    { text: 'Value', options: { fill: { color: TR.lightGold }, color: TR.black, fontFace: 'Clario', fontSize: 12 } },
  ],
];
slide.addTable(tableData, {
  x: 0.5, y: 1.2, w: 9,
  border: { pt: 0.5, color: 'DDDDDD' },
});
```

### What NOT to do in TR decks

- ❌ No accent lines under slide titles (use whitespace or the Orange rectangle bar instead)
- ❌ No default blue PowerPoint color scheme
- ❌ No Arial, Calibri, or other non-Clario fonts
- ❌ No `#` prefix on any hex color value
- ❌ No reused option objects across multiple `addShape`/`addText` calls (PptxGenJS mutates them — use factory functions)
- ❌ No gradients (not natively supported in PptxGenJS — use a flat TR color instead)
- ❌ No text-only slides — every slide needs at least one visual element (shape, chart, or icon)

---

## Checklist before returning any branded artifact

**HTML / React / Charts:**
- [ ] Clario `@font-face` CSS is embedded (from `references/clario-fonts.md`) — no system fonts used
- [ ] Global `font-family: 'Clario', sans-serif` applied to root element
- [ ] Only TR palette colors used (no arbitrary hex values)
- [ ] TR Orange used as the primary emphasis/action color
- [ ] Text on dark backgrounds uses `#FFFFFF`; Racing Green backgrounds checked for contrast
- [ ] Chart color sequence follows TR accent order (Orange → Sky → Teal → Gold → Amber → Lime)
- [ ] `TR_COLORS` constant present in React artifacts

**Presentations (.pptx):**
- [ ] `fontFace: 'Clario'` on every `addText()` call — no system fonts
- [ ] No `#` prefix on any hex color value
- [ ] Title and closing slides use Racing Green background with TR Orange left accent bar
- [ ] Content slides use white or TR Light palette background
- [ ] TR Orange used for accent bars, stat highlights, and emphasis
- [ ] Chart colors follow TR accent sequence (`chartColors` explicitly set)
- [ ] Tables use Racing Green header row, alternating TR Light Gold / white body rows
- [ ] No accent lines under slide titles
- [ ] Every slide has at least one visual element beyond text
- [ ] No option objects reused across multiple `addShape`/`addText` calls
- [ ] Default font set to Clario throughout (`font: 'Clario'` on all TextRuns and styles)
- [ ] H1 black bold, H2 Racing Green bold, H3 TR Orange bold
- [ ] Cover/header block uses Racing Green shading with white text
- [ ] TR Orange used for dividers (paragraph bottom borders), emphasis text, and callout left borders
- [ ] Tables use Racing Green header row, alternating TR Light Gold / white body rows
- [ ] All table shading uses `ShadingType.CLEAR` (never SOLID)
- [ ] Callout blocks use TR Light Gold background + TR Orange left border
- [ ] Font fallback note included (cover block or footer)
