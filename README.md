# Claude Skills Library

A shared library of Claude skill files for reuse across teams. Browse the catalog below to find skills, or contribute your own via pull request.

> **What is a skill?** A skill is a `.md` file you load into a Claude project to give it specialised behaviour — like a plugin. Each skill has a clear purpose, trigger conditions, and instructions for Claude to follow.

---

## 📖 Skills Catalog

<!-- CATALOG_START -->
### 🗂️ Admin

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [admin-generate-ado-description](./skills/admin/admin-generate-ado-description.md) | Generates a structured, Markdown-formatted Azure DevOps (ADO) work item description for design tasks — ready to paste directly into a work item. Use w... | #design #product | @MaryCampoTR |
| [admin-generate-meeting-invite](./skills/admin/admin-generate-meeting-invite.md) | Generates structured meeting invite content (description, agenda, and goals) ready to paste directly into a calendar invite or meeting request. Use wh... | #design #product #engineering #strategy | @MaryCampoTR |
| [admin-post-meeting-recap](./skills/admin/admin-post-meeting-recap.md) | Generates a ready-to-send Teams post-meeting recap with a summary, prioritised next steps with tagged owners, and a confirmation prompt. Use whenever ... | #design #product #engineering #strategy | @MaryCampoTR |
| [admin-pre-meeting-prep](./skills/admin/admin-pre-meeting-prep.md) | Generates a structured pre-meeting prep pack including research context, delegation opportunities with ready-to-send Teams messages, strategic questio... | #design #product #strategy | @MaryCampoTR |
| [admin-presentation-intro-framework](./skills/admin/admin-presentation-intro-framework.md) | Generates a meeting opening script and time-blocked agenda framework for professional presentations. Use whenever the user wants to prepare a talk tra... | #design #product #strategy | @MaryCampoTR |
| [admin-refine-response](./skills/admin/admin-refine-response.md) | Refines and polishes Teams messages for professional communication. Use whenever the user wants to write, draft, improve, or respond to a Microsoft Te... | #design #product #engineering #strategy | @MaryCampoTR |

### 🖥️ UX

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [ux-agentic-ai-prototype-review](./skills/ux/ux-agentic-ai-prototype-review.md) | Reviews and fixes HTML prototype code for agentic AI interfaces, producing improved copy-paste ready code and a prioritised change report. Use wheneve... | #design #engineering | @MaryCampoTR |
| [ux-generate-design-requirements](./skills/ux/ux-generate-design-requirements.md) | Accepts any mix of UX reference materials — transcripts, emails, screenshots, Figma exports, ADO work items, notes — and synthesizes them into a struc... | #design #product | @MaryCampoTR |

### 🎨 Design

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [agentic-ai-ux](./skills/design/agentic-ai-ux.md) | Apply Human-AI agent interaction UX principles to any feature spec or v0 prompt that involves AI-generated content, AI recommendations, automated acti... | #design #product | @MaryCampoTR |
| [figma-ingestion](./skills/design/figma-ingestion.md) | Extract accurate component specifications from Figma screenshots (no MCP, no Dev Mode required). Use whenever the user shares a Figma screenshot, expo... | #design #engineering | @MaryCampoTR |
| [frontend-design](./skills/design/frontend-design.md) | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, a... | #design #engineering | @MaryCampoTR |
| [saffron-master](./skills/design/saffron-master.md) | Master Saffron Design System reference skill for Thomson Reuters. Authoritative source for tokens, components, visual patterns, and implementation gui... | #design #engineering | @MaryCampoTR |
| [ui-designer](./skills/design/ui-designer.md) | Expert visual design craft, UI systems, and pixel-perfect implementation. Activates when building, styling, reviewing, or polishing any interface -- w... | #design | @MaryCampoTR |
| [ux-designer](./skills/design/ux-designer.md) | Expert UX design thinking, user psychology, and experience strategy. Activates when building, reviewing, or discussing any user-facing interface -- we... | #design #product | @MaryCampoTR |

### 📋 Requirements

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [ado-story-parser](./skills/requirements/ado-story-parser.md) | Normalise Azure DevOps (ADO) work items of varying quality into the ux-requirements-synthesizer intake schema. Use whenever the user provides an ADO w... | #design #product #engineering | @MaryCampoTR |
| [spec-qa](./skills/requirements/spec-qa.md) | Final quality gate for any UX requirements spec before it is handed off to v0, a stakeholder, or a development team. Run after ux-requirements-synthes... | #design #product #engineering | @MaryCampoTR |
| [transcript-parser](./skills/requirements/transcript-parser.md) | Parse and structure messy meeting transcripts into clean, synthesizer-ready intent signals. Use whenever the user provides a meeting transcript, call ... | #design #product #strategy | @MaryCampoTR |
| [user-context](./skills/requirements/user-context.md) | Capture and apply user context (persona, role, domain, sophistication level, task environment) before synthesizing requirements. Use at the start of a... | #design #product | @MaryCampoTR |
| [ux-design-principles](./skills/requirements/ux-design-principles.md) | Apply Staff Product Designer thinking to any UX requirements spec or v0 prompt. Use on every feature spec to ensure outputs reflect senior design judg... | #design | @MaryCampoTR |
| [ux-requirements-synthesizer](./skills/requirements/ux-requirements-synthesizer.md) | Transform piecemeal UX inputs (meeting transcripts, half-baked user stories, design artifacts) into complete, v0-ready requirement specs using Saffron... | #design #product | @MaryCampoTR |
| [v0-prompt-patterns](./skills/requirements/v0-prompt-patterns.md) | A pattern library of proven v0 prompt structures for common Saffron screen archetypes. Use when writing the v0 prompt section of a requirements spec, ... | #design #engineering | @MaryCampoTR |
| [v0-refinement](./skills/requirements/v0-refinement.md) | Diagnose v0 prototype output that missed the mark and produce targeted refinement prompts. Use when v0 has generated a prototype that is incomplete, i... | #design #engineering | @MaryCampoTR |

### 🏢 Brand

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [tr-brand-guidelines](./skills/brand/tr-brand-guidelines.md) | Enforces Thomson Reuters (TR) brand guidelines—Clario typeface, official color palette, and visual style rules—in all generated artifacts. Use this sk... | #design #marketing #product | @BrittanyDiCosimoTR |

### 📝 Content

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [case-study](./skills/content/case-study.md) | Use this skill whenever a user wants to create a UX or design case study document. Triggers include: mentions of 'case study', 'design case study', 'U... | #design #product #strategy | @MaryCampoTR |

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
