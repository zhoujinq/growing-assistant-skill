# Example 01 · Resume / JD review

A minimal example of the loop, not a full resume skill.

## Input

- `docs/resume.md` (redacted)
- `docs/jd.md`
- `PROFILE.md` (target role, constraints)

## First run

`WORKFLOW.md`:

```text
1. Extract 5 must-have requirements from the JD.
2. Map each requirement to one line in the resume; mark strong / weak / missing.
3. Rewrite only the weak/missing lines; never invent numbers.
4. Output report.md + evidence.md + handoff.md.
```

`output/2026-11-19-review-jd/report.md`:

```text
Verdict: 3 strong, 2 weak, 1 missing.
Weak 1: "海外客户" — resume says "德国/美国/日本客户" but no frequency or ownership.
Weak 2: "API 销售" — no quota or revenue number.
Missing: "开发者生态" — no evidence.
```

`evidence.md` cites `docs/resume.md#experience` and `docs/jd.md#requirements`.

## Correction

User: “不要把‘接触过’写成‘负责’。这条只能写协助。”

`RULES.md`:

```markdown
## R-002 角色动词必须可证
- 触发：写任何经历 bullet
- 动作：只有能指出“我独立做了决策”的证据，才用“负责”；否则用“参与/协助”
- 原因：面试官会追问边界
- 例子：反例：“负责海外客户全流程”；正例：“协助跟进 3 家海外客户，独立完成报价对比”
```

`evals/E-002.md`: same resume, bad output uses “负责”, expected uses “协助”.

## Second run

Re-run the same input. The “负责” line is now “协助”，and `evidence.md` cites the rule. That is the smallest proof of growth.
