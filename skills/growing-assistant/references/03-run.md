# 03 · Run：第一次工作流

## 先写 WORKFLOW.md

```markdown
# WORKFLOW: <name>

## Trigger
用户说什么/给什么时启动。

## Inputs
- 必需：
- 可选：
- 不给怎么办：

## Steps
1.
2.
3.

## Output
- `output/<date>-<task>/report.md`
- `evidence.md`（引用 + 检查结果）
- `handoff.md`（下一步）

## Acceptance
- [ ] 产物存在且能打开
- [ ] 每条事实有引用
- [ ] 没有编造的数字/人名/结论
- [ ] 反例检查通过

## Stop
- 缺关键输入 → 停下来问，不猜。
- 涉及不可逆动作 → 先确认。
- 预算/时间超限 → 报卡点。
```

## 运行顺序

1. 读 `PROFILE.md`、`RULES.md`、`WORKFLOW.md`。
2. 复述目标 + 验收，不超过 5 行。
3. 列 3 步计划；超过 7 步就拆。
4. 执行；每一步留一个可检查的痕迹。
5. 写 `report.md` + `evidence.md` + `handoff.md`。
6. 跑验收；不过就修，不交半成品。

## 输出契约

`report.md` 只写结论与依据，不写过程流水账。`evidence.md` 写“哪条结论来自哪个文件/行”。`handoff.md` 写“下一步谁做什么”。

## Effort

- `low`：一次成型；只适合简单、可逆任务。
- `medium`：draft → self-check → revise once。
- `high`：solve → check → revise；至少多一次回源/反例检查；保留当前最好版本。

## 反例

至少跑一个“它不在时会失败”的检查：

- 删掉一个引用，检查 `evidence.md` 是否报错。
- 给一个文档里没有的问题，检查是否回 `not in docs`。
- 改一个数字，检查验收是否红。
