# 🔍 CodeLens AI

> Architecture mapper · Security auditor · Complexity profiler — powered by Llama 3.3 70B

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🗺️ Architecture Mapping | Parses code flow into interactive Mermaid.js flowcharts |
| 🔐 Security Audit | OWASP-based checks — injection risks, weak crypto, and more |
| ⚡ Complexity Profiling | Big-O runtime and space complexity analysis |

## 🛠️ Tech Stack

- **Frontend** — Streamlit
- **AI Orchestration** — Phidata Agentic Framework
- **LLM** — Llama 3.3 70B via Groq
- **Visualisation** — streamlit-mermaid

## 🚀 Quick Start

### 1 — Clone
\\\ash
git clone https://github.com/karishmaram-tech/codelens-ai.git
cd codelens-ai
\\\

### 2 — Virtual environment
\\\ash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux
\\\

### 3 — Install
\\\ash
pip install -r requirements.txt
\\\

### 4 — Configure
\\\ash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
\\\

### 5 — Run
\\\ash
streamlit run rag_reasoning_agent.py
\\\

## 🧪 Development

\\\ash
pip install -r requirements-dev.txt
pre-commit install
pytest tests/ -v
ruff check . --fix
\\\

## 📄 License

MIT © karishmaram-tech
