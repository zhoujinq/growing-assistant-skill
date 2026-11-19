# Example 02 · Weekly review

Same loop, different workflow. This is here to show the skill is not resume-specific.

## Input

- `docs/notes/` — daily notes for the week
- `docs/calendar.md` — optional
- `PROFILE.md` — goals and tone

## First run

`WORKFLOW.md`:

```text
1. Read the week's notes; extract decisions, open loops, and blockers.
2. Compare with last week's open loops.
3. Output: 3 wins, 3 open loops, 1 next action, 1 question for the user.
4. Every item cites a note file.
```

Output: `output/2026-11-19-weekly/report.md` + `evidence.md` + `handoff.md`.

## Correction

User: “不要列 10 条。只留会影响下周决策的 3 条。”

`RULES.md`:

```markdown
## R-003 周报只留决策项
- 触发：weekly review
- 动作：最多 3 条 open loop；每条必须写“下周做什么/不做什么”
- 原因：列表不是决策
- 例子：反例：10 条流水账；正例：3 条，每条带 next action
```

`evals/E-003.md`: same notes, bad output is a 10-item list; expected is 3 decision items.

## Second run

The report shrinks, but the next action is clearer. That is the trade: less output, more decisions.
