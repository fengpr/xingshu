# 星枢

星枢（Xingshu）是一个基于 `Python + Java` 双栈构建的混合式 AI 私人助手项目，面向个人用户提供本地优先、按需联网、多智能体协同的桌面端能力。

项目当前采用单仓库 `monorepo` 结构，覆盖桌面客户端、本地服务、插件扩展、智能体定义、共享协议与工程文档，作为后续产品研发与持续迭代的统一代码仓库。

## 功能特性

- 本地优先：支持本地模型、本地知识库、本地设备控制与本地数据存储。
- 联网增强：支持接入在线大模型、联网搜索与在线能力扩展。
- 多智能体协同：支持主智能体调度与专项智能体扩展，便于复杂任务拆解与执行。
- 桌面客户端：采用 `PyQt6` 构建跨平台桌面应用，首期优先支持 Windows。
- 本地服务中枢：采用 `Spring Boot` 提供本地 HTTP 服务、调度、安全与存储支撑。
- 插件扩展：支持内置插件、社区插件与后续插件市场能力演进。
- 项目内技能体系：支持将项目专属技能收敛到 `skills/` 目录，并按领域隔离管理，避免多个技能文件混用。
- 工程规范清晰：已建立 `PRD.md`、`SPEC.md` 与文档同步约束，便于后续规范化开发。

## 仓库结构

- `apps/desktop-client/`：Python 桌面客户端
- `apps/java-service/`：Java 本地服务与主调度层
- `packages/`：共享 SDK、协议结构与插件开发基础能力
- `plugins/`：内置插件与社区插件
- `agents/`：主智能体与专项智能体相关定义
- `skills/`：项目本地技能目录，按领域隔离管理技能
- `configs/`：应用配置、模型配置与智能体规则配置
- `data/`：本地运行时数据目录
- `docs/`：架构、接口、路线图与开发说明文档
- `tests/`：仓库级测试与集成测试

## 环境配置

项目根目录提供了环境变量模板文件 [`.env.example`](D:\project\xingshu\.env.example)。首次开发前，建议复制为 `.env` 并按本机环境调整。

当前已定义的核心环境变量如下：

| 变量名 | 用途 | 是否必填 | 示例值 |
| --- | --- | --- | --- |
| `XINGSHU_ENV` | 运行环境标识 | 否 | `local` |
| `XINGSHU_APP_NAME` | 应用名称 | 否 | `xingshu` |
| `XINGSHU_LOG_LEVEL` | 日志级别 | 否 | `INFO` |
| `XINGSHU_JAVA_SERVICE_HOST` | Java 本地服务地址 | 否 | `127.0.0.1` |
| `XINGSHU_JAVA_SERVICE_PORT` | Java 本地服务端口 | 否 | `18080` |
| `XINGSHU_OLLAMA_BASE_URL` | Ollama 服务地址 | 否 | `http://127.0.0.1:11434` |
| `XINGSHU_DEFAULT_LOCAL_MODEL` | 默认本地模型 | 否 | `qwen2.5:7b` |
| `XINGSHU_DEFAULT_ONLINE_PROVIDER` | 默认在线模型提供方 | 否 | `openai` |
| `XINGSHU_OPENAI_API_KEY` | OpenAI API Key | 按需 | 留空 |
| `XINGSHU_DEEPSEEK_API_KEY` | DeepSeek API Key | 按需 | 留空 |

补充说明：

- 如仅运行本地模式，可暂不填写在线模型相关密钥。
- 实际业务配置以 `configs/` 目录下的 `*.toml` 文件为准。
- 禁止将真实密钥提交到仓库。

## 快速开始

### 1. 准备环境

建议安装以下基础环境：

- Python `3.11`
- Java `21`
- Gradle（可使用本地安装版本，后续可再补充 Wrapper）
- Ollama（如需本地模型能力）

### 2. 初始化环境变量

在项目根目录创建 `.env` 文件，可参考 `.env.example`：

```bash
cp .env.example .env
```

在 Windows PowerShell 中也可以手动复制：

```powershell
Copy-Item .env.example .env
```

### 3. 启动 Python 客户端

进入 [apps/desktop-client](D:\project\xingshu\apps\desktop-client) 后安装依赖并运行：

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
python -m xingshu_desktop.main
```

Windows PowerShell 示例：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
python -m xingshu_desktop.main
```

### 4. 启动 Java 本地服务

进入 [apps/java-service](D:\project\xingshu\apps\java-service) 后启动 Spring Boot 服务：

```bash
gradle bootRun
```

默认健康检查地址：

```text
http://127.0.0.1:18080/api/v1/system/health
```

## 开发规范

- 产品需求基线见 [PRD.md](D:\project\xingshu\PRD.md)
- 工程规范见 [SPEC.md](D:\project\xingshu\SPEC.md)
- 技能目录说明见 [skills/README.md](D:\project\xingshu\skills\README.md)
- 文档同步技能见 [skills/project/doc-sync-development/SKILL.md](D:\project\xingshu\skills\project\doc-sync-development\SKILL.md)
- Karpathy 工程实现技能见 [skills/project/karpathy-guidelines/SKILL.md](D:\project\xingshu\skills\project\karpathy-guidelines\SKILL.md)
- 前端界面美化技能见 [skills/frontend/frontend-design/SKILL.md](D:\project\xingshu\skills\frontend\frontend-design\SKILL.md)

所有核心功能开发、接口调整、配置扩展和架构变更，必须同步更新对应文档，禁止只改代码不补文档。
