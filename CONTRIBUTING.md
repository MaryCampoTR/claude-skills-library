# Contributing to the Claude Skills Library

Thanks for contributing! This guide covers everything you need to add a new skill or improve an existing one.

---

## Adding a New Skill

### 1. Create your skill file

Create a new `.md` file in the appropriate folder under `skills/`:

| Folder | Use for |
|--------|---------|
| `skills/design/` | UI/UX design, Figma, Saffron, visual tools |
| `skills/requirements/` | Specs, transcripts, ADO, v0 prompts |
| `skills/brand/` | Brand guidelines, visual identity |
| `skills/content/` | Case studies, documents, writing workflows |

Not sure where it fits? Put it in the closest category and note it in your PR — we'll sort it together.

### 2. Use the standard front-matter

Every skill file must start with this YAML block:

```yaml
---
name: your-skill-name
description: >
  One to three sentences. What does this skill do? When should Claude use it?
  Be specific about triggers — this text is used in the catalog.
version: 1.0.0
updated: YYYY-MM-DD
relevant_roles: [design, product, engineering, strategy, marketing]
owner: @your-github-handle
---
```

### 3. Structure your skill content

After the front-matter, follow this structure:

```markdown
# SKILL: Your Skill Name — Short Subtitle

## Purpose
What problem does this skill solve? Who is it for?

## When to Use
- Bullet list of trigger conditions
- Be specific — when should Claude load this?

## When NOT to Use
- Conditions where this skill doesn't apply

## Instructions
[The actual skill instructions for Claude]

## Output Format
What should Claude produce when this skill is active?

## Dependencies
List any other skills this one relies on, e.g. feeds into ux-requirements-synthesizer
```

### 4. Submit a pull request

- Branch name: `skill/your-skill-name` or `fix/skill-name-issue`
- PR title: `Add: your-skill-name` or `Update: skill-name — what changed`
- In the PR description, briefly explain: what the skill does, who it's for, and how you've tested it

The catalog (`README.md`) will auto-update when your PR is merged via GitHub Actions. You don't need to edit the catalog manually.

---

## Editing an Existing Skill

1. Edit the skill file directly
2. Bump the `version` in the front-matter (patch = `1.0.x`, minor change = `1.x.0`)
3. Update the `updated` date
4. Submit a PR with a clear description of what changed and why

---

## Skill Quality Standards

Before submitting, check:

- [ ] Front-matter is complete and valid YAML
- [ ] Description is specific enough to appear useful in the catalog
- [ ] "When to Use" and "When NOT to Use" sections are both present
- [ ] Skill has been tested in at least one real Claude session
- [ ] No confidential or proprietary content included (TR-internal concepts are fine; client data is not)

---

## Questions?

Open an issue or reach out to @MaryCampoTR on GitHub or Teams.
