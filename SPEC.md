# 星枢 SPEC

## 1. 文档目标

本文档用于约束星枢项目的工程实现方式，统一技术栈、仓库目录结构与命名规范，作为后续架构设计、模块开发、代码评审与协作扩展的基础规范。

适用范围：

- 桌面客户端
- Python AI 与业务层
- Java 服务与调度层
- 插件与智能体扩展
- 测试、脚本、配置与文档

---

## 2. 技术栈规范

## 2.1 总体原则

- 采用 `Python + Java` 双栈，不新增第三核心后端语言。
- 采用单仓库 `monorepo` 组织方式，统一管理应用代码、服务代码、插件、脚本与文档。
- 以“本地优先、联网增强、插件扩展、智能体协同”为核心设计原则。
- 优先选择成熟、稳定、社区活跃的依赖，避免早期过度自研。
- 所有新模块必须优先考虑跨平台兼容性，首要支持 Windows，其次兼容 macOS / Linux。

## 2.2 Python 技术栈

Python 负责桌面端 UI、AI 调用、业务编排、多模态处理、知识库、插件系统与专项智能体。

推荐版本与约束：

- Python 版本：`3.11.x`
- 包管理：`uv` 或 `poetry`
- 虚拟环境：项目内 `.venv`
- 代码格式化：`ruff format`
- Lint：`ruff`
- 类型检查：`mypy`
- 测试框架：`pytest`

推荐核心依赖：

- UI：`PyQt6`
- 本地模型接入：`ollama`
- 数据校验：`pydantic`
- ORM / 数据访问：优先轻量方案，可使用 `sqlmodel` 或 `sqlalchemy`
- 文档处理：`python-docx`、`pypdf`、`openpyxl`
- OCR / 图像：`opencv-python`、按需接入 OCR 库
- 语音：`openai-whisper` 或兼容离线语音识别方案
- HTTP：`httpx`
- 任务编排：优先标准库 + 清晰服务层封装，避免过早引入重型工作流框架

Python 禁止事项：

- 禁止在 UI 层直接写复杂业务逻辑。
- 禁止将密钥加密、权限兜底、安全审计等核心安全逻辑仅放在 Python 侧。
- 禁止插件直接绕过统一接口访问数据库或系统敏感能力。

## 2.3 Java 技术栈

Java 负责本地服务、跨语言通信、安全控制、调度中枢、日志与系统支撑。

推荐版本与约束：

- Java 版本：`21 LTS`
- 构建工具：`Gradle`
- Web / 本地服务：`Spring Boot`
- 数据访问：`Spring JDBC` 或 `JPA`，优先保持简单
- 测试框架：`JUnit 5`
- 代码规范：遵循 Google Java Style 的简化子集

推荐核心依赖：

- 本地 HTTP 服务：`Spring Web`
- 校验：`jakarta validation`
- 加密：JDK 标准加密能力 + 明确封装
- 日志：`SLF4J + Logback`
- 配置管理：`Spring Boot Configuration`

Java 禁止事项：

- 禁止在 Java 侧承担桌面主 UI。
- 禁止在 Java 侧直接实现复杂模型推理工作流。
- 禁止跨模块直接访问未封装的内部实现类。

## 2.4 存储与数据规范

- 本地数据库统一使用 `SQLite`。
- 敏感数据必须加密存储，至少包括 API Key、用户凭据、敏感配置。
- 业务数据与系统日志分库或分表隔离。
- 向量索引、缓存、临时文件必须与核心业务数据目录分开。
- 云端仅允许同步非隐私配置、插件索引、模板、收藏、公共元数据。

## 2.5 通信与集成规范

- Python 与 Java 之间优先使用本地 `HTTP` 通信。
- 跨语言接口统一走内部 API，不允许通过读写临时文件进行主流程通信。
- 所有接口输入输出统一使用 JSON。
- 所有对外模型与联网服务调用需经过统一封装层，不允许业务模块直接散落调用第三方接口。

## 2.6 智能体与插件规范

- 主智能体调度能力由 Java 服务层承担。
- 专项智能体实现默认在 Python 侧。
- 插件默认以 Python 形态实现，遵循统一插件清单和生命周期接口。
- 插件与智能体共享一套能力注册与权限声明机制。
- 智能体名称、插件名称、模块名称必须稳定，不允许同义词并存。

---

## 3. 目录结构规范

## 3.1 仓库根目录

建议采用如下结构：

```text
xingshu/
├─ apps/
│  ├─ desktop-client/
│  └─ java-service/
├─ skills/
│  ├─ frontend/
│  └─ project/
├─ packages/
│  ├─ py-sdk/
│  ├─ shared-schemas/
│  └─ plugin-sdk/
├─ plugins/
│  ├─ builtin/
│  └─ community/
├─ agents/
│  ├─ orchestrator/
│  └─ specialists/
├─ data/
│  ├─ local/
│  ├─ cache/
│  ├─ vector/
│  ├─ logs/
│  └─ backups/
├─ scripts/
├─ tests/
│  ├─ python/
│  ├─ java/
│  └─ integration/
├─ docs/
├─ configs/
├─ .gitignore
├─ README.md
├─ PRD.md
└─ SPEC.md
```

## 3.2 目录职责说明

### `apps/`

存放主应用代码。

- `apps/desktop-client/`：Python 桌面客户端
- `apps/java-service/`：Java 本地服务与主调度中枢

### `packages/`

存放可复用能力包。

- `packages/py-sdk/`：Python 公共 SDK、统一客户端、业务基础组件
- `packages/shared-schemas/`：跨端共享的数据结构说明、接口协议文档或 schema
- `packages/plugin-sdk/`：插件开发基础接口与模板

### `skills/`

存放项目本地技能，统一管理项目专属工作流与开发约束。

- `skills/frontend/`：前端设计、界面美化、视觉优化类技能
- `skills/project/`：项目规则、文档同步、工程流程类技能

当前 `skills/project/` 典型技能示例：

- `doc-sync-development`：文档同步与交付约束
- `karpathy-guidelines`：工程实现风格与最小改动原则

技能目录约束：

- 所有项目本地技能必须存放在 `skills/` 下
- 禁止在仓库根目录直接放置独立的 `skill.md` 或 `SKILL.md`
- 每个技能必须使用独立文件夹，不同领域的技能不得平铺混放
- 默认遵循“单任务单主技能”原则，确需组合时再显式增加辅助技能

### `plugins/`

存放插件实现。

- `plugins/builtin/`：内置插件
- `plugins/community/`：外部插件或示例插件

### `agents/`

存放智能体定义与协同规则。

- `agents/orchestrator/`：主智能体调度相关定义
- `agents/specialists/`：专项智能体实现或注册信息

### `data/`

存放本地运行时数据。

- `data/local/`：SQLite、本地配置、用户状态
- `data/cache/`：联网缓存、临时处理结果
- `data/vector/`：知识库索引、向量存储
- `data/logs/`：系统日志、联网日志、智能体协同日志
- `data/backups/`：本地备份

说明：

- `data/` 为运行时目录，不应提交用户真实数据。
- 仅保留 `.gitkeep`、示例结构或脱敏样例。

### `scripts/`

存放开发、构建、初始化、迁移、打包、检查脚本。

### `tests/`

存放测试代码。

- `tests/python/`：Python 单元测试
- `tests/java/`：Java 单元测试
- `tests/integration/`：跨语言、跨模块集成测试

### `docs/`

存放设计文档、架构说明、接口文档、开发指南。

### `configs/`

存放环境模板、应用配置、默认策略配置。

---

## 4. 应用内目录建议

## 4.1 Python 客户端目录建议

`apps/desktop-client/` 推荐结构：

```text
desktop-client/
├─ pyproject.toml
├─ README.md
├─ src/
│  └─ xingshu_desktop/
│     ├─ app/
│     ├─ ui/
│     ├─ features/
│     ├─ agents/
│     ├─ plugins/
│     ├─ integrations/
│     ├─ repositories/
│     ├─ services/
│     ├─ models/
│     ├─ schemas/
│     ├─ utils/
│     └─ main.py
└─ tests/
```

各目录含义：

- `app/`：应用启动、依赖装配、生命周期管理
- `ui/`：窗口、组件、视图模型、界面资源管理
- `features/`：按业务域划分的功能模块，如 knowledge、automation、device_control
- `agents/`：Python 侧专项智能体实现
- `plugins/`：插件加载、插件运行时、插件桥接层
- `integrations/`：Ollama、在线模型、搜索、OCR、语音等外部集成
- `repositories/`：数据访问层
- `services/`：业务服务层
- `models/`：内部领域模型
- `schemas/`：输入输出结构、DTO、消息体
- `utils/`：无业务语义的纯工具函数

## 4.2 Java 服务目录建议

`apps/java-service/` 推荐结构：

```text
java-service/
├─ build.gradle.kts
├─ settings.gradle.kts
├─ src/
│  ├─ main/
│  │  ├─ java/
│  │  │  └─ com/xingshu/service/
│  │  │     ├─ api/
│  │  │     ├─ application/
│  │  │     ├─ domain/
│  │  │     ├─ infrastructure/
│  │  │     ├─ security/
│  │  │     ├─ orchestration/
│  │  │     └─ XingshuServiceApplication.java
│  │  └─ resources/
│  └─ test/
```

各目录含义：

- `api/`：Controller、请求响应对象、接口适配
- `application/`：应用服务、用例编排
- `domain/`：领域对象、规则、核心抽象
- `infrastructure/`：数据库、日志、外部适配、系统能力封装
- `security/`：加密、权限、敏感词过滤、审计
- `orchestration/`：主智能体调度、任务编排、路由策略

---

## 5. 命名规范

## 5.1 通用命名原则

- 命名必须语义明确，避免使用 `misc`、`common2`、`temp_final` 等无意义名称。
- 一类概念只使用一种固定命名，不允许同一语义多种写法混用。
- 名称优先英文，小范围展示文案可使用中文。
- 缩写仅在行业通用时允许使用，如 `api`、`ocr`、`tts`、`rag`。

## 5.2 仓库与目录命名

- 仓库根目录：`xingshu`
- 目录名统一使用 `kebab-case`
- Python 包目录名使用 `snake_case`
- Java 包名使用全小写反向域名风格，如 `com.xingshu.service`
- 技能领域目录使用语义化英文名，如 `frontend`、`project`
- 技能目录名使用 `kebab-case`，如 `frontend-design`

示例：

- 正确：`device-control`、`plugin-sdk`、`knowledge_base`
- 错误：`DeviceControl`、`pluginSDK`、`knowledgeBase`

## 5.3 Python 命名

- 文件名：`snake_case.py`
- 包名：`snake_case`
- 类名：`PascalCase`
- 函数名：`snake_case`
- 变量名：`snake_case`
- 常量名：`UPPER_SNAKE_CASE`
- 私有方法 / 属性：前缀单下划线，如 `_load_index`

示例：

```python
class KnowledgeSearchService:
    DEFAULT_TIMEOUT = 30

    def search_documents(self, query_text: str) -> list[str]:
        ...
```

## 5.4 Java 命名

- 类名：`PascalCase`
- 接口名：`PascalCase`
- 方法名：`camelCase`
- 变量名：`camelCase`
- 常量名：`UPPER_SNAKE_CASE`
- 包名：全小写

后缀约定：

- Controller：`*Controller`
- Service：`*Service`
- Repository：`*Repository`
- Request DTO：`*Request`
- Response DTO：`*Response`
- Entity：`*Entity`
- Config：`*Config`

## 5.5 接口与协议命名

- 内部 API 路径统一使用 `/api/v1/...`
- 资源路径使用 `kebab-case`
- JSON 字段统一使用 `snake_case`
- 事件名称统一使用 `dot.case`

示例：

- API：`/api/v1/agents/run-task`
- JSON：`task_id`、`agent_name`、`execution_mode`
- Event：`agent.task.started`

## 5.6 数据库命名

- 表名：`snake_case` 复数优先或集合语义统一
- 字段名：`snake_case`
- 主键统一：`id`
- 时间字段统一：`created_at`、`updated_at`
- 逻辑删除字段统一：`deleted_at`
- 外键字段统一：`{resource}_id`

示例：

- `documents`
- `agent_runs`
- `plugin_installations`

## 5.7 插件与智能体命名

- 插件标识：`plugin.{domain}.{name}`
- 智能体标识：`agent.{domain}.{name}`
- 内置插件目录：`plugins/builtin/{plugin_name}`
- 专项智能体目录：`agents/specialists/{agent_name}`

示例：

- `plugin.office.excel_tools`
- `plugin.dev.code_review`
- `agent.knowledge.retriever`
- `agent.system.device_controller`

---

## 6. 模块划分规范

业务功能按领域拆分，禁止按“页面 + 页面 + 页面”的方式堆叠所有逻辑。

推荐一级领域：

- `knowledge`
- `productivity`
- `device_control`
- `multimodal`
- `plugins`
- `agents`
- `settings`
- `security`
- `sync`

每个领域模块优先包含：

- `schemas`
- `service`
- `repository`
- `handlers` 或 `use_cases`

避免：

- 超大 `utils.py`
- 超大 `helper.py`
- 超大 `common.py`

---

## 7. 配置规范

- 所有环境配置统一放在 `configs/`
- 环境变量样例使用 `.env.example`
- 禁止提交真实密钥、令牌、账号信息
- 配置分层建议：
  - `base`
  - `local`
  - `dev`
  - `prod`

推荐配置文件命名：

- `configs/app.base.toml`
- `configs/app.local.toml`
- `configs/model.providers.toml`
- `configs/agent.rules.toml`

---

## 8. 测试规范

- 单元测试必须与业务模块同步建设。
- Python 测试文件命名：`test_*.py`
- Java 测试类命名：`*Test.java`
- 集成测试命名：`test_*_integration.py` 或 `*IntegrationTest.java`
- 核心模块必须覆盖：
  - 知识库导入与检索
  - 本地 / 联网模型切换
  - 插件加载
  - 智能体调度
  - 权限与隐私过滤

---

## 9. 文档规范

- 产品文档：`PRD.md`
- 技术规范：`SPEC.md`
- 架构设计：`ARCHITECTURE.md`
- 开发计划：`ROADMAP.md`
- 接口文档：`API.md`
- 插件开发说明：`PLUGIN_DEV.md`
- 智能体开发说明：`AGENT_DEV.md`

文档命名原则：

- 根目录核心文档统一大写英文文件名
- 主题性说明优先放入 `docs/`
- 同类文档使用统一前缀或统一主题目录
- 技能文档统一放入 `skills/<domain>/<skill-name>/SKILL.md`

---

## 10. Git 与分支规范

- 主分支：`main`
- 开发分支：`develop`
- 功能分支：`feature/<domain>-<short-name>`
- 修复分支：`fix/<domain>-<short-name>`
- 文档分支：`docs/<short-name>`
- 重构分支：`refactor/<domain>-<short-name>`

提交信息建议：

- `feat: add local knowledge indexing`
- `fix: handle empty plugin manifest`
- `docs: add architecture overview`
- `refactor: split agent routing service`

---

## 11. 落地约束

- 第一阶段开发必须先搭建目录骨架，再进入功能编码。
- 所有新功能必须先落到明确模块目录，不允许直接散落在根目录。
- 所有跨语言协议必须先定义 schema，再实现调用。
- 插件、智能体、联网能力必须经过统一注册与权限控制。
- 项目技能必须统一收敛到 `skills/` 目录，避免与普通文档混用。
- 若后续实际工程需要偏离本文档，必须先更新 `SPEC.md` 再执行调整。
