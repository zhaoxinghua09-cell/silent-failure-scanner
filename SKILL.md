---
name: silent-failure-scanner
description: "Scan AI outputs for silent failures: placeholders, empty stubs, hedging, no-progress repeats, hallucination markers. 扫描 AI 输出的静默失败：占位、空壳、含糊、原地重复、幻觉标记。"
version: 1.0.0
license: MIT
category: 质量
author: SynomosAI (LGD initiative)
platforms: [windows, macos, linux]
tags: [silent,failure,scanner]
slug: silent-failure-scanner
risk_tier: medium
---

# Silent Failure Scanner (静默失败扫描器)

> **Catch silent AI failures before they ship.**
> **在静默失败上线前抓住它们。**
> 理论根基：LGD 三律（有籍·有证·有门禁）

## 功能 / Capabilities
- 6-class silent-failure taxonomy (catalog-based)
- Quality score with fail-closed verdict
- Snippet-level evidence for every hit
- 六类静默失败分类法（基于目录）
- 质量评分 + fail-closed 判定
- 每个命中附片段级证据

## 用法 / Usage
```bash
python scripts/silent_scanner.py <file|text> [--json]
```

## 三律对齐 / LGD alignment
| 律 | 本技能如何满足 |
|---|---|
| 有籍 Registered | frontmatter 完整（name/description/license/version），作者与命名空间明确 |
| 有证 Evidenced | 输出可复现（SHA-256 锚点/结构化 JSON），含验证方式 |
| 有门禁 Gated | 最小权限、fail-closed 退出码、危险操作默认拒绝 |

## 安全边界 / Safety boundary
- 只做静态分析，不自动执行任何外部命令
- 检出风险即 FAIL（fail-closed），由人决策
- 不代用户删除/修改/发布任何内容

## Standard alignment / 标准对齐
- **Agent Skills open standard**: compatible with [agentskills.io](https://agentskills.io) format (SKILL.md + scripts/, frontmatter name/description). Adopted by Claude/Codex and the broader agent ecosystem.
- **AEO**: llms.txt / AGENTS.md friendly (AI-agent discoverable).

## Skill card / 技能卡（对标 NVIDIA Verified Agent Skills）
- **Ownership / 所有权**: SynomosAI initiative — Steven Zhao (ORCID 0009-0001-0512-1237)
- **Dependencies / 依赖**: none (Python 3 stdlib only)
- **Limitations / 限制**: static analysis only; not a substitute for runtime verification
- **Verification status / 验证状态**: self-reported PASS via skill-quality-gate; not a certification or endorsement
- **Security posture / 安全姿态**: no network calls, no destructive operations, fail-closed exit codes

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `scripts/*.py` | **MIT** |
| 文档与理论文本 | 本 `SKILL.md`、`README.md` 及理论表述 | **All rights reserved** |

```
© 2026 赵兴华 / Steven Zhao·China (ORCID 0009-0001-0512-1237). All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" / "MedXpert" — 未申请实体注册、未申请商标注册
生产参考部署 (production reference, self-reported) : MedXpert（非认证、非背书、非监管认可）
引用格式 (cite as)      : 本资产无 DOI
```
（上列为《LGD 对外表述规范》§3.2 统一块，整体复制、未删改；发布/重提前须照最新版本复核。）
