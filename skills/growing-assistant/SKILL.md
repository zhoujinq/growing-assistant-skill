---
name: growing-assistant
display_name: "成长助手 / Growing Assistant"
description: >
  A skill of skills: bootstrap a personal, growing AI assistant in any file-capable Agent.
  It interviews the user, creates a local assistant workspace (profile, rules, memory, docs,
  workflows, evals), runs one real workflow end-to-end, then turns corrections into rules
  and eval cases so the next run is better. Trigger: build my own assistant, personal AI,
  growing assistant, 会成长的数字助手, 个人助手, 助理工作流.
version: 0.1.0
last_updated: 2026-11-19
license: MIT
---

# Growing Assistant / 成长助手

> 这不是一个“帮你做某件事”的技能，是一个“帮你长出一个助手”的技能。
> 它先帮你搭好底座，再陪你跑通第一个工作流，最后把你的纠正变成规则和评测。

## What this is

A **meta-skill**: it does not replace your resume/email/weekly-review skill. It builds the workspace, memory, rules, and feedback loop that make those skills *yours* and *better over time*.

It is deliberately small:

- one local workspace,
- one first workflow,
- one correction loop,
- one effort switch.

No database server. No platform. No multi-agent ceremony.

## Hard rules

1. **One workflow at a time.** Do not scaffold five workflows before one works end-to-end.
2. **File-first.** Chat is not memory. Anything that must survive a new session goes into a file.
3. **Every fact cites a file.** Use `path#heading` or `path:line`. No source, no claim.
4. **Unknown is allowed.** Write `not in docs` or `待补`; never fill gaps with plausible guesses.
5. **Corrections become rules.** “I’ll remember” is not a mechanism. Write a rule + an eval case.
6. **Privacy is a hard gate.** Secrets, customer names, and company-internal data go in `private/`; public output must not contain them.
7. **Stop at gates.** G0–G3 exist to prevent a confident half-product.
8. **Build one loop, not a platform.** If a feature does not make the first loop more verifiable, cut it.

## Modes

| Mode | When | Output |
|---|---|---|
| `bootstrap` | New user / empty workspace | `assistant/` scaffold + `PROFILE.md` + first `WORKFLOW.md` |
| `run` | User gives a real task | `output/<date>-<task>/report.md` + `evidence.md` + `handoff.md` |
| `grow` | User corrects a result | new rule in `RULES.md` + new case in `evals/` + re-run |
| `export` | Workflow is stable | standalone `skills/<name>/SKILL.md` + a static case page |

If the user asks “build my assistant”, start at `bootstrap`. If they give a task and a workspace exists, go to `run`. If they say “that’s wrong / next time do X”, go to `grow`.

## The 5-step loop

### 1. Profile (5–8 questions)

Ask **one at a time**, with a recommended default. Stop when you can fill:

- who the user is and what they do,
- 3 current goals,
- one repeated task that wastes time,
- what “done” looks like for that task,
- what data/tools are allowed,
- what must never be shared,
- preferred language/tone,
- effort preference (fast vs thorough).

Write `PROFILE.md`. Do not ask for what is already in the repo.

### 2. Workspace

Create the file contract below. Use the script:

```bash
python scripts/init_assistant.py --root ./assistant --name "My Assistant"
```

The workspace is the state. If it is not on disk, it does not exist.

### 3. First workflow

Pick one task that is **frequent, painful, and verifiable**. Write `WORKFLOW.md`:

- trigger,
- inputs,
- steps,
- output contract,
- acceptance checks,
- stop conditions.

Run it once. Produce a real artifact, not a chat answer. If it cannot produce an artifact, pick another workflow.

### 4. Correction

Ask: “What exactly is wrong — fact, spec, or preference?”

- **Fact** → fix the source file / citation.
- **Spec** → change `WORKFLOW.md`.
- **Preference** → write a rule in `RULES.md`.

Then add one eval case to `evals/`. Re-run the same task. The second run must show the correction taking effect.

### 5. Effort

| Effort | Behaviour | Use when |
|---|---|---|
| `low` | answer directly; one pass | simple, reversible |
| `medium` | draft → self-check → revise once | normal work |
| `high` | solve → check → revise; keep best version; record evidence | high stakes / long tasks |

Record the effort level in the output. High effort without extra checks is just slower low effort.

## File contract

```text
assistant/
├─ PROFILE.md          # who, goals, constraints, preferences
├─ RULES.md            # durable rules, one per correction
├─ WORKFLOW.md         # the first workflow
├─ memory/             # dated notes, decisions, open loops
├─ docs/               # source material (read-only)
├─ workflows/          # additional workflows, one file each
├─ evals/              # good/bad cases, one file each
├─ output/             # dated task outputs
├─ skills/             # distilled standalone skills
└─ private/            # secrets/customer data; gitignored
```

## Gates

| Gate | Pass condition |
|---|---|
| **G0 Profile** | `PROFILE.md` has who/goals/constraints/privacy/preferences |
| **G1 Workflow** | `WORKFLOW.md` has inputs/output/steps/acceptance/stop |
| **G2 First run** | artifact + evidence + no uncited factual claim |
| **G3 Growth** | one new rule + one new eval case; second run passes |

Do not skip a gate because the user is in a hurry. A skipped gate is the most expensive shortcut.

## References

- `references/01-bootstrap.md` — questions + profile template
- `references/02-workspace.md` — file contract and naming
- `references/03-run.md` — run contract and acceptance
- `references/04-grow.md` — correction → rule → eval
- `references/05-export.md` — distill a workflow into a standalone skill + case page

## Definition of done (v0.1)

A new user can:

1. install the skill,
2. answer 5–8 questions,
3. get a workspace with profile/rules/workflow,
4. run one real task with a cited artifact,
5. correct one thing,
6. see the correction persist in a new session.

If any step needs the skill author to explain it, the skill is not done.
