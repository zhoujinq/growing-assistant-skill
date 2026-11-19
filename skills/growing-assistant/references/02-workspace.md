# 02 · Workspace：文件契约

## 目录

```text
assistant/
├─ PROFILE.md
├─ RULES.md
├─ WORKFLOW.md
├─ memory/
│  ├─ YYYY-MM-DD.md
│  └─ open-loops.md
├─ docs/
│  └─ README.md
├─ workflows/
│  └─ <workflow>.md
├─ evals/
│  └─ <case>.md
├─ output/
│  └─ YYYY-MM-DD-<task>/
│     ├─ report.md
│     ├─ evidence.md
│     └─ handoff.md
├─ skills/
│  └─ <name>/SKILL.md
└─ private/          # gitignored
```

## 每个文件只做一件事

| 文件 | 写什么 | 不写什么 |
|---|---|---|
| `PROFILE.md` | 角色、目标、偏好、数据边界 | 任务过程 |
| `RULES.md` | 可复用的硬规则，一条一个 | 一次性背景 |
| `WORKFLOW.md` | 第一个工作流的输入/步骤/验收 | 某次任务的结果 |
| `memory/` | 日期、决定、未决事项 | 大段原文 |
| `docs/` | 只读源材料 | 生成物 |
| `evals/` | 可重复跑的好/坏案例 | 主观感受 |
| `output/` | 某次任务的产物与证据 | 规则 |
| `skills/` | 从稳定工作流蒸馏出的独立技能 | 草稿 |

## 命名

- 日期：`YYYY-MM-DD`。
- 任务：`YYYY-MM-DD-<动词>-<对象>`，例如 `2026-11-19-review-jd`。
- 规则：`R-001`、`R-002`，不复用编号。
- 评测：`E-001`、`E-002`。

## 引用

- 文件内：`docs/pricing.md#discount`。
- 行号：`docs/pricing.md:42`。
- 不能引用时：写 `not in docs`，不要补。

## 隐私

- `private/` 不进 Git；`.gitignore` 已处理。
- 公开产物不得出现：密钥、客户实名、公司内部路径、未公开报价。
- 需要展示真实案例时，先脱敏，再写 `evidence.md`。
