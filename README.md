# 🚀 Dynamic-RAG: 基于 FastAPI + LangChain 的动态网页问答系统

这是一个端到端的 RAG（检索增强生成）应用程序。用户可以输入任意网页 URL，系统将自动抓取、切分并向量化网页内容，随后允许用户针对该网页内容进行深度问答。



## ✨ 项目特性

* **动态内容解析**：支持实时抓取用户输入的网页 URL，而非固定在本地文档。
* **向量化检索**：基于 ChromaDB 实现高效的本地文档检索，支持语义级匹配。
* **自定义风格**：支持用户选择或定制不同的 Prompt 回答风格，满足多样化的回复需求。
* **现代前端界面**：简洁的聊天式 UI，提供实时状态反馈与解析进度提示。
* **环境安全**：通过环境变量管理 API 密钥，避免敏感信息硬编码。

## 🛠️ 技术栈

* **后端**: FastAPI (Web 框架), LangChain (AI 工作流), Pydantic (数据校验)
* **AI 模型**: Google Gemini API (提供大模型推理能力)
* **向量库**: ChromaDB (本地向量化存储)
* **前端**: 原生 HTML5, CSS3, JavaScript (Fetch API 异步交互)

## 📥 安装与运行

### 1. 克隆仓库
```bash
git clone https://github.com/CatNapperr/rag-starter-kit.git
cd rag-starter-kit

```

### 2. 创建并激活虚拟环境 (推荐)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```

### 3. 安装依赖

```bash
pip install -r requirements.txt

```

### 4. 环境配置 (重要) ⚠️

在项目根目录下创建一个名为 `.env` 的文件。

请在 `.env` 中填写以下内容：

```env
# 你的 Google Gemini API 密钥 (必填)
GOOGLE_API_KEY=你的密钥

# 如果你身处中国大陆或其他无法直接访问国外 API 的地区，请务必指定代理 (可选)
HTTP_PROXY=[http://127.0.0.1](http://127.0.0.1):你的代理端口
HTTPS_PROXY=[http://127.0.0.1](http://127.0.0.1):你的代理端口

```

### 5. 启动服务

```bash
uvicorn main:app --reload

```

启动后访问：`http://127.0.0.1:8000`

## 📂 项目结构

```text
my_rag_project/
├── main.py              # FastAPI 应用程序入口，挂载路由和静态文件
├── api/
│   └── chat_router.py   # 定义 API 端点 (Endpoint)
├── services/
│   └── rag_engine.py    # 封装 LangChain 逻辑的核心服务层
├── schemas/
│   └── models.py        # Pydantic 数据模型，定义输入输出格式
├── core/
│   └── config.py        # 环境变量加载与全局配置管理
├── static/              # 存放前端 HTML/CSS/JS 资源
└── .env                 # 存放敏感信息 (已忽略)

```

## 📝 许可证

MIT License

---

**提示**：在使用过程中，如果遇到回答风格不符合预期的情况，可以在前端界面尝试自定义 Prompt 模板。

