# 星枢 AGENTS

## 文档定位

本文档用于帮助后续工程师或代理快速接手星枢项目。内容聚焦项目定位、当前代码现状、运行事实、协作约束与下一步建议，不替代 [README.md](D:\project\xingshu\README.md)、[PRD.md](D:\project\xingshu\PRD.md) 或 [SPEC.md](D:\project\xingshu\SPEC.md)。

## 项目概览

星枢（Xingshu）是一个基于 `Python + Java` 双栈构建的混合式 AI 私人助手项目，目标形态是桌面端、本地优先、按需联网、支持多智能体协同与插件扩展的个人 AI 助手。

当前产品主线已经明确：

- 本地优先：优先保障隐私、本地知识库和本地设备控制
- 联网增强：按需接入在线模型、联网搜索与外部能力
- 多智能体协同：支持主智能体调度与专项智能体分工
- 插件扩展：支持内置插件与后续插件生态演进

## 当前状态

当前仓库处于“工程骨架已初始化、核心功能尚未落地”的阶段。

已完成的部分：

- 单仓库 `monorepo` 目录结构已搭建
- Python 桌面客户端骨架已创建
- Java 本地服务骨架已创建
- 基础配置文件、环境变量模板、测试占位与文档结构已创建
- 项目技能体系已收敛到 `skills/` 目录

尚未完成的部分：

- Python 与 Java 的实际业务通信尚未打通
- 桌面主界面仍是最小启动占位
- 知识库、设备控制、多模态、插件、智能体等核心业务尚未实现
- API 文档、架构文档、智能体文档仍是占位状态

结论：当前仓库已经适合进入第一阶段开发，但还没有进入核心业务实现阶段。

## 仓库结构

### 根目录关键子系统

- `apps/desktop-client/`：Python 桌面客户端
- `apps/java-service/`：Java 本地服务与调度层
- `configs/`：应用、模型与智能体规则配置
- `skills/`：项目本地技能目录
- `docs/`：架构、接口、路线图、插件与智能体说明
- `tests/`：仓库级测试目录
- `data/`：本地运行时数据目录
- `agents/`：主智能体与专项智能体定义占位
- `plugins/`：内置插件与社区插件目录
- `packages/`：共享 SDK、协议和插件开发基础能力

### Python 侧结构

Python 客户端位于 `apps/desktop-client/`，当前已按职责分层：

- `app/`：应用启动、依赖装配、生命周期管理
- `ui/`：界面层
- `features/`：按业务域划分的功能模块
- `integrations/`：外部能力接入
- `services/`：业务服务层
- `repositories/`：数据访问层
- `schemas/`：输入输出结构
- `models/`：内部领域模型
- `agents/`：Python 侧专项智能体
- `plugins/`：插件运行时
- `utils/`：通用工具

当前 `features/` 下已预建以下领域目录：

- `knowledge`
- `productivity`
- `device_control`
- `multimodal`
- `plugins`
- `settings`
- `security`
- `sync`

### Java 侧结构

Java 服务位于 `apps/java-service/`，当前已按典型分层组织：

- `api/`：Controller 与接口适配
- `application/`：应用服务与用例编排
- `domain/`：领域对象与规则
- `infrastructure/`：数据库、日志、外部适配与系统封装
- `security/`：安全、权限、审计相关能力
- `orchestration/`：主智能体调度与任务编排

## 技术栈与运行事实

### 当前技术栈

- Python `3.11`
- Java `21`
- `PyQt6`
- `Spring Boot`
- `SQLite`
- `Ollama`

### Python 侧事实

- Python 客户端包名为 `xingshu-desktop`
- 入口脚本为 `xingshu_desktop.main:main`
- 当前 `main -> bootstrap -> runtime` 仅完成最小启动链路
- `DesktopApplication.run()` 当前仅输出 bootstrap 提示，属于占位实现

### Java 侧事实

- Java 服务使用 `Gradle` 构建
- 已接入 `spring-boot-starter-web`、`validation`、`jdbc`
- 使用 `sqlite-jdbc`
- 当前服务入口为 `XingshuServiceApplication`
- 当前仅提供一个最小健康检查接口

### 配置与运行事实

- Java 服务默认地址：`127.0.0.1:18080`
- 当前最小接口：`/api/v1/system/health`
- SQLite 数据库默认路径：`data/local/xingshu.db`
- 默认运行模式：`hybrid`
- 本地模型提供方：`ollama`
- 默认本地模型：`qwen2.5:7b`
- 已预留在线模型配置：`OpenAI`、`DeepSeek`
- 已预留智能体规则配置：知识检索、本地设备控制、在线搜索

### 当前启动现状

- Python 客户端可以按最小入口启动，但没有实际桌面功能
- Java 服务可以按 Spring Boot 方式启动，但业务接口仍为空壳
- 当前项目属于“可启动骨架”，不是“可用产品”

## 当前文档与技能体系

### 核心文档

- [README.md](D:\project\xingshu\README.md)：项目首页、环境配置、快速开始
- [PRD.md](D:\project\xingshu\PRD.md)：产品目标、核心功能与范围
- [SPEC.md](D:\project\xingshu\SPEC.md)：工程规范、目录结构、命名规则

### 技能目录

项目本地技能统一放在 `skills/` 下，禁止在仓库根目录放置单独技能文件。

当前已有两个项目技能：

- [skills/frontend/frontend-design/SKILL.md](D:\project\xingshu\skills\frontend\frontend-design\SKILL.md)
  - 用于前端界面设计、美化与视觉优化
- [skills/project/doc-sync-development/SKILL.md](D:\project\xingshu\skills\project\doc-sync-development\SKILL.md)
  - 用于约束“代码与文档同步交付”

默认规则：

- 尽量遵循“单任务单主技能”
- 若任务同时涉及实现与文档更新，可在主技能基础上补充文档同步技能

## 开发约束

以下规则是接手开发时必须优先遵守的高优先级约束：

- 功能开发完成后，必须同步更新相关文档
- API 变动后，必须同步更新 `docs/API.md`
- 架构、目录或规范变动后，必须同步更新 `SPEC.md`
- 用户可见文档、说明、操作手册优先使用中文
- 项目技能必须统一放在 `skills/` 目录下
- 不要在 UI 层直接堆复杂业务逻辑
- 不要让 Python 单独承担安全兜底逻辑
- 不要绕过统一接口直接访问敏感系统能力或数据库

## 快速接手建议

### 建议阅读顺序

1. 先读 [README.md](D:\project\xingshu\README.md)
2. 再读 [PRD.md](D:\project\xingshu\PRD.md)
3. 再读 [SPEC.md](D:\project\xingshu\SPEC.md)
4. 若任务涉及前端，补读前端技能
5. 若任务涉及交付规范，补读文档同步技能

### 当前最适合优先推进的方向

- 打通 Python 与 Java 的本地 HTTP 通信
- 建立桌面主界面雏形
- 落地知识库最小闭环：导入、索引、检索
- 落地设备控制或智能体最小实现链路

### 建议的第一批实现顺序

1. 建立 Python 调用 Java 服务的基础客户端
2. 补齐 Java 侧最小业务 API 与统一响应结构
3. 将桌面主界面从启动占位升级为可交互壳层
4. 选择一个高频模块做最小闭环，优先推荐知识库或设备控制

## 对后续代理的提醒

- 当前仓库的优势是规范和骨架已经清楚，适合稳步推进
- 当前仓库的风险是容易因为目录很多而误判“功能已存在”
- 接手时请以“骨架已好、业务未实装”的心态工作，不要默认已有实现
- 做任何核心改动前，优先确认是否会影响 `README.md`、`PRD.md`、`SPEC.md` 或 `docs/API.md`
