import re

# Skill metadata map — relevant_roles and owner for each existing skill
SKILL_META = {
    # Design category
    "agentic-ai-ux":              (["design", "product"],                    "@MaryCampoTR"),
    "figma-ingestion":            (["design", "engineering"],                "@MaryCampoTR"),
    "frontend-design":            (["design", "engineering"],                "@MaryCampoTR"),
    "ui-designer":                (["design"],                               "@MaryCampoTR"),
    "ux-designer":                (["design", "product"],                    "@MaryCampoTR"),
    "saffron-master":             (["design", "engineering"],                "@MaryCampoTR"),
    # Requirements category
    "ado-story-parser":           (["design", "product", "engineering"],     "@MaryCampoTR"),
    "session-kickoff":            (["design", "product"],                    "@MaryCampoTR"),
    "spec-qa":                    (["design", "product", "engineering"],     "@MaryCampoTR"),
    "transcript-parser":          (["design", "product", "strategy"],        "@MaryCampoTR"),
    "user-context":               (["design", "product"],                    "@MaryCampoTR"),
    "ux-design-principles":       (["design"],                               "@MaryCampoTR"),
    "ux-requirements-synthesizer":(["design", "product"],                    "@MaryCampoTR"),
    "v0-prompt-patterns":         (["design", "engineering"],                "@MaryCampoTR"),
    "v0-refinement":              (["design", "engineering"],                "@MaryCampoTR"),
    # Brand category
    "tr-brand-guidelines":        (["design", "marketing", "product"],       "@BrittanyDiCosimoTR"),
    # Content category
    "case-study":                 (["design", "product", "strategy"],        "@MaryCampoTR"),
}

import os, sys

skills_dir = "skills"

for category in os.listdir(skills_dir):
    cat_path = os.path.join(skills_dir, category)
    if not os.path.isdir(cat_path):
        continue
    for filename in os.listdir(cat_path):
        if not filename.endswith(".md"):
            continue
        skill_name = filename.replace(".md", "")
        if skill_name not in SKILL_META:
            print(f"  ⚠️  No metadata defined for {skill_name} — skipping")
            continue

        roles, owner = SKILL_META[skill_name]
        filepath = os.path.join(cat_path, filename)
        content = open(filepath).read()

        # Skip if already has relevant_roles
        if "relevant_roles" in content:
            print(f"  ✓  Already has metadata: {skill_name}")
            continue

        # Build the fields to insert
        roles_yaml = "\n  - ".join(roles)
        insert = f"relevant_roles:\n  - {roles_yaml}\nowner: \"{owner}\"\n"

        # Insert before the closing --- of frontmatter
        updated = re.sub(r'(\n---\n)', f'\n{insert}---\n', content, count=1)

        open(filepath, "w").write(updated)
        print(f"  ✅  Updated: {skill_name}")
