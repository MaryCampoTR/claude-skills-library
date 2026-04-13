# Claude Skills Library

A shared library of Claude skill files for reuse across teams. Browse the catalog below to find skills, or contribute your own via pull request.

> **What is a skill?** A skill is a `.md` file you load into a Claude project to give it specialised behaviour — like a plugin. Each skill has a clear purpose, trigger conditions, and instructions for Claude to follow.

---

## 📖 Skills Catalog

<!-- CATALOG_START -->
### 🎨 Design

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [saffron-master](./skills/design/saffron-master.md) | Master Saffron Design System reference for TR. Authoritative source for tokens, components, and implementation guidance across React and HTML targets. Supersedes all other Saffron skills. | #design #engineering #product | @MaryCampoTR |
| [ui-designer](./skills/design/ui-designer.md) | Expert visual design craft and pixel-perfect implementation. Activates when building, styling, reviewing, or polishing any interface. | #design | @MaryCampoTR |
| [ux-designer](./skills/design/ux-designer.md) | Expert UX design thinking, user psychology, and experience strategy. Activates when building or reviewing any user-facing interface. | #design #product | @MaryCampoTR |
| [figma-ingestion](./skills/design/figma-ingestion.md) | Extract accurate component specs from Figma screenshots — no MCP or Dev Mode required. Output feeds into the requirements synthesizer. | #design #engineering | @MaryCampoTR |
| [frontend-design](./skills/design/frontend-design.md) | Create distinctive, production-grade frontend interfaces. Use when building web components, pages, artifacts, or any web UI. | #design #engineering | @MaryCampoTR |
| [agentic-ai-ux](./skills/design/agentic-ai-ux.md) | Apply Human-AI interaction UX principles to any feature involving AI-generated content, recommendations, or automated actions. | #design #product | @MaryCampoTR |

### 📋 Requirements

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [ux-requirements-synthesizer](./skills/requirements/ux-requirements-synthesizer.md) | Transform piecemeal UX inputs into complete, v0-ready requirement specs using Saffron vocabulary, tokens, and components. | #design #product | @MaryCampoTR |
| [session-kickoff](./skills/requirements/session-kickoff.md) | Automatically orchestrates a full UX requirements session from any input — transcripts, ADO items, Figma screenshots, or briefs. | #design #product | @MaryCampoTR |
| [transcript-parser](./skills/requirements/transcript-parser.md) | Parse messy meeting transcripts into clean, synthesizer-ready intent signals. Extracts decisions, pain points, open questions, and out-of-scope markers. | #design #product #strategy | @MaryCampoTR |
| [ado-story-parser](./skills/requirements/ado-story-parser.md) | Normalise Azure DevOps work items of any quality into the requirements synthesizer intake schema. | #design #product #engineering | @MaryCampoTR |
| [ux-design-principles](./skills/requirements/ux-design-principles.md) | Apply Staff Product Designer thinking to any UX spec or v0 prompt. Runs as a design critique layer before handoff. | #design | @MaryCampoTR |
| [user-context](./skills/requirements/user-context.md) | Capture and apply user context (persona, role, domain, sophistication) before synthesizing requirements. | #design #product | @MaryCampoTR |
| [spec-qa](./skills/requirements/spec-qa.md) | Final quality gate for any UX spec before handoff. Produces a binary READY / NOT READY verdict with a confidence score. | #design #product #engineering | @MaryCampoTR |
| [v0-prompt-patterns](./skills/requirements/v0-prompt-patterns.md) | A pattern library of proven v0 prompt structures for common Saffron screen archetypes. | #design #engineering | @MaryCampoTR |
| [v0-refinement](./skills/requirements/v0-refinement.md) | Diagnose v0 prototype output that missed the mark and produce targeted refinement prompts without starting over. | #design #engineering | @MaryCampoTR |

### 🏢 Brand

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [tr-brand-guidelines](./skills/brand/tr-brand-guidelines.md) | Enforces Thomson Reuters brand guidelines — Clario typeface, official color palette, and visual style rules — across HTML, React, Word (.docx), and PowerPoint (.pptx) artifacts. | #design #marketing #product | @BrittanyDiCosimoTR |

### 📝 Content

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [case-study](./skills/content/case-study.md) | Produces a polished, upper-management-ready Word (.docx) case study by interviewing the user section by section. Triggers on 'case study', 'UX case study', or requests to document a design initiative for stakeholders or portfolio. | #design #product #strategy | @MaryCampoTR |

<!-- CATALOG_END -->

---

## 🚀 How to Use a Skill

1. Navigate to the skill file you want
2. Click **Raw** and copy the full content
3. In your Claude project, go to **Project Instructions** and paste the skill content
4. That's it — Claude will now follow the skill's instructions in that project

---

## 🤝 Contributing

Want to add a skill or improve an existing one? See [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## 📁 Folder Structure

```
claude-skills-library/
├── README.md              ← You are here (catalog)
├── CONTRIBUTING.md        ← How to add/edit skills
├── skills/
│   ├── design/            ← UI/UX, Figma, Saffron, frontend
│   ├── requirements/      ← Specs, transcripts, ADO, v0 prompts
│   ├── brand/             ← TR brand guidelines
│   └── content/           ← Case studies, documents, writing
└── scripts/
    └── generate_catalog.py ← Auto-updates this catalog from skill front-matter
```
