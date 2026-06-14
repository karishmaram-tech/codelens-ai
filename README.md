# 🔍 CodeLens AI: Architecture & Logic Mapper

CodeLens AI is an intelligent engineering assistant built with Streamlit and Phidata. It leverages the advanced **Llama-3.3-70b** model via Groq to perform static analysis, map out architectural data paths visually using Mermaid.js flowcharts, and run deep security audits on source code.

## ✨ Features

- 🗺️ **Architecture & Logic Mapping:** Automatically parses code flow into an interactive, visual Mermaid flowchart.
- 🔐 **Deep Security Audit:** Highlights structural software vulnerabilities based on OWASP standards, injection risks, and weak cryptography.
- ⚡ **Complexity Profiling:** Analyzes runtime and space complexity using Big-O notation O(N).

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Orchestration:** Phidata Agentic Framework
- **LLM Engine:** Llama 3.3 70B (via Groq API)
- **Visualizations:** Streamlit-Mermaid (Mermaid.js parsing)

## 🚀 Local Setup Instructions

1. Clone the repository:
```bash
   git clone https://github.com/karishmaram-tech/codelens-ai.git
```

2. Navigate into the directory:
```bash
   cd codelens-ai
```

3. Install requirements:
```bash
   pip install -r requirements.txt
```

4. Set your Groq API Key:
```bash
   $env:GROQ_API_KEY="your_api_key_here"
```

5. Run the app:
```bash
   streamlit run rag_reasoning_agent.py
```
