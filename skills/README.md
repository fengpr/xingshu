# 项目技能目录

本目录用于存放星枢项目的本地技能，统一管理项目内可复用的开发技能，避免与仓库根目录文档、系统技能或临时说明文件混用。

## 目录原则

- 所有技能必须放在 `skills/` 目录下，禁止在仓库根目录直接放置单独的 `skill.md` 或 `SKILL.md`。
- 每个技能必须使用独立目录，目录内至少包含一个 `SKILL.md`。
- 不同用途的技能按领域隔离，避免文档型技能、前端型技能、工程型技能混放在同一层。
- 默认采用“一次任务只启用一个主技能”的原则，确需组合时，再显式补充辅助技能。

## 当前结构

```text
skills/
├─ frontend/
│  └─ frontend-design/
│     ├─ SKILL.md
│     └─ LICENSE.txt
└─ project/
   ├─ doc-sync-development/
   │  └─ SKILL.md
   └─ karpathy-guidelines/
      ├─ SKILL.md
      └─ LICENSE.txt
```

## 使用规则

- 前端界面设计、美化、视觉优化类任务，优先使用 `skills/frontend/frontend-design/`。
- 文档同步、README 更新、接口文档维护、规范落地类任务，优先使用 `skills/project/doc-sync-development/`。
- 工程实现风格、编码取舍、重构尺度控制类任务，优先使用 `skills/project/karpathy-guidelines/`。
- 如果任务同时涉及前端实现与文档更新，先以实现任务对应的技能为主，再按需补充文档同步技能。
- 如果任务涉及实际编码实现，且需要控制复杂度、保持小步修改或减少过度设计，可将 `karpathy-guidelines` 作为辅助技能。
- 若新增技能，先确认是否属于已有领域；若不属于，再新增新的领域目录，避免多个技能堆在同一层。

## 项目规则型技能分工

- `doc-sync-development`：负责约束代码与文档同步交付。
- `karpathy-guidelines`：负责约束工程实现风格、复杂度控制与最小改动原则。
- 默认仍遵循“单任务单主技能”；只有任务同时需要交付规范与实现风格约束时，才组合使用。
