---
name: admin-pre-meeting-prep
description: >
  Generates a structured pre-meeting prep pack including research context, delegation
  opportunities with ready-to-send Teams messages, strategic questions, and facilitation
  notes. Use this skill whenever the user wants to prepare for an upcoming meeting, build
  context before a stakeholder session, identify what to delegate before a sync, or plan
  how to navigate a difficult meeting. Triggers on phrases like "help me prep for",
  "I have a meeting about", "prepare me for", "what should I know before", "pre-meeting
  prep", "how should I approach this meeting", or any time the user shares meeting context
  and wants to walk in ready. Best for stakeholder meetings, design reviews, strategy
  sessions, and cross-functional alignment. Categorized under Admin utilities.
---

# Admin > Pre-Meeting Prep

Takes meeting context and produces a ready-to-use prep pack with four sections:
1. **Pre-Meeting Research & Context** — background and knowledge gaps to fill
2. **Delegation Opportunities** — tasks to assign with copy-paste Teams messages
3. **Questions to Ask** — strategic questions categorised by purpose
4. **Facilitation Notes** — talking points, friction navigation, success criteria

---

## Inputs to collect

| Input | Required? | Notes |
|---|---|---|
| Meeting purpose and topic | ✅ Required | Drives everything |
| Who's attending and your role | Recommended | Shapes questions, talking points, and delegation targets |
| Known agenda items / discussion points | Recommended | Drives questions and facilitation notes |
| Specific objectives or concerns | Recommended | Shapes success criteria and friction navigation |

If only the topic is provided, proceed with reasonable inferences — flag assumptions clearly.

---

## Output format

Produce all four sections in order. No preamble.

---

### Section 1: Pre-Meeting Research & Context

**What you should know going in:**
2–4 bullet points of relevant background on the topic, attendees, or organisational context.
Draw from what the user has provided. Where knowledge gaps exist that the user should fill
before the meeting, flag them explicitly:

> ⚠️ **Knowledge gap:** [What you don't know that could matter — and where/how to find it]
> e.g. "What decisions were made in the last design review for this feature? Check ADO or ask [relevant person]."

Keep this section factual and scannable. No padding.

---

### Section 2: Delegation Opportunities

Identify 1–3 tasks that could or should be handled by someone else before or after the meeting.
For each, provide a ready-to-send Teams message.

Format per delegation:

**Delegate to:** [Role or name if provided, otherwise "[Relevant teammate]"]
**Task:** [What needs doing and why it's relevant to the meeting]

> 💬 **Teams message (copy-paste ready):**
> Hey [name/team] — I have a [meeting topic] meeting [timeframe]. Could you [specific ask] before then? [Context sentence if needed.] Thanks

If no meaningful delegation opportunities exist, say so briefly and omit the messages:
*"No delegation opportunities identified for this meeting."*

---

### Section 3: Questions to Ask

Generate 6–10 strategic questions, categorised by purpose. Prioritise the top 3–4 with a ⭐.

Categories (use whichever apply):

**🎯 Clarifying** — questions to resolve ambiguity or confirm understanding
**📊 Strategic** — questions about direction, priority, or decisions
**🔍 Diagnostic** — questions to surface blockers, risks, or gaps
**🤝 Alignment** — questions to test or build shared understanding
**➡️ Forward-looking** — questions about next steps, ownership, timelines

Format:
- ⭐ [Question] *(category)*
- [Question] *(category)*

Top 3–4 starred questions should be the ones that matter most if time runs short.

---

### Section 4: Facilitation Notes

Three sub-sections:

**Key talking points**
2–4 bullet points — the things you most need to say or land in this meeting.
Written as points to make, not questions to ask.

**Friction navigation**
If the meeting has potential tension points (conflicting stakeholders, contested decisions,
unclear ownership), name them and suggest a brief approach:
> Potential friction: [what it is]
> Suggested approach: [one sentence on how to navigate it]

If no friction is anticipated, omit this sub-section.

**Success criteria**
2–3 specific, checkable outcomes that would make this meeting a success.
Written as: *"By the end of this meeting, we should have [X]."*

---

## Tone and style principles

- Prep packs are for the user's eyes only — direct, honest, and practical
- Flag knowledge gaps clearly rather than glossing over them
- Questions should be genuinely strategic, not obvious filler
- Delegation messages follow the same principles as `admin-refine-response`:
  50–100 words, no filler, professional but warm, ready to send without editing
- Success criteria should be concrete enough to actually check off, not vague
  ("aligned on the approach" is vague; "agreed on which flows go into the demo" is checkable)

---

## Process

1. Read all inputs.
2. Infer role and attendee dynamics where possible (e.g. if the user is presenting to
   senior stakeholders, weight strategic and alignment questions more heavily).
3. Generate all four sections in order.
4. Output sections directly — no meta-commentary between them.
5. Close with a single line:

   *Tip: Review this 15–20 minutes before the meeting, not the night before — it'll be fresher.*

---

## Relationship to other Admin skills

This skill prepares you **before** the meeting. Pair with:
- `admin-presentation-intro-framework` → to structure how you open and run it
- `admin-post-meeting-recap` → to document outcomes and next steps after
- `admin-refine-response` → if any delegation messages need further polish
