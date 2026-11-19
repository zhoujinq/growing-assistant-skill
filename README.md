# Growing Assistant / 成长助手

> A skill of skills: give it to your Agent, answer 5–8 questions, and get a personal assistant that runs one real workflow and gets better after every correction.

**Demo page:** https://zhoujinq.github.io/growing-assistant-skill/

## What it is

Most “personal AI” setups are a prompt and a chat history. This skill builds the missing layer:

- a local workspace with profile, rules, memory, docs, workflows, evals;
- one real workflow running end-to-end;
- a correction loop that turns “that’s wrong” into a rule + an eval case;
- an effort switch: fast, normal, thorough.

It is not a chatbot. It is not a resume/email/weekly-review skill. It is the **bootstrap + growth loop** those skills need.

## The loop

```text
Profile → Workspace → First workflow → Correction → Effort
   ↑                                            │
   └──────────────── eval case ─────────────────┘
```

1. **Profile** — who, goals, one repeated task, acceptance, privacy, effort.
2. **Workspace** — `PROFILE.md`, `RULES.md`, `WORKFLOW.md`, `memory/`, `docs/`, `evals/`, `output/`, `skills/`.
3. **First workflow** — one real task, one artifact, one evidence file.
4. **Correction** — fact / spec / preference → rule + eval case; re-run.
5. **Effort** — `low` / `medium` / `high`; high must add checks, not just words.

## Install

### WorkBuddy

```bash
git clone https://github.com/zhoujinq/growing-assistant-skill.git
cp -r growing-assistant-skill/skills/growing-assistant ~/.workbuddy/skills/growing-assistant
```

Windows PowerShell:

```powershell
git clone https://github.com/zhoujinq/growing-assistant-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.workbuddy\skills" | Out-Null
Copy-Item -Recurse .\growing-assistant-skill\skills\growing-assistant "$env:USERPROFILE\.workbuddy\skills\growing-assistant"
```

Restart WorkBuddy; the skill will be available.

### skills CLI

```bash
npx skills@latest add zhoujinq/growing-assistant-skill --skill=growing-assistant
```

If the CLI is unavailable, use the git clone path above; it is the tested path (Python 3.11+, stdlib only).

## Quick start

```bash
cd skills/growing-assistant
python scripts/init_assistant.py --root ./assistant --name "My Assistant"
python scripts/lint_assistant.py --root ./assistant
python scripts/selftest.py
```

Then ask your Agent:

> Build my growing assistant. Start with the first workflow: `<your repeated task>`.

## What is inside

```text
skills/growing-assistant/
├─ SKILL.md
├─ references/        # bootstrap, workspace, run, grow, export
├─ templates/         # PROFILE / RULES / WORKFLOW / EVAL
├─ scripts/           # init, lint, selftest (stdlib only)
└─ examples/          # resume review, weekly review
```

## Design notes

- **Lab1** (GSE 2026): a personal assistant needs a personal database, one composed workflow, and corrections saved as readable files.
- **Lab2**: effort is a real knob; high effort means `solve → check → revise`, not “longer answer”.
- **Lab3**: growth requires a preference benchmark; without eval cases, corrections evaporate.

The skill keeps those three ideas, but strips the course-specific parts (email, ehall, mobile) so it can run in any file-capable Agent.

## Status

`v0.1.0` — the smallest loop that works. No platform, no database server, no multi-agent ceremony.

MIT. PRs welcome, but keep the loop small.
