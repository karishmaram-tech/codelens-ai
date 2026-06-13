import streamlit as st
import streamlit_mermaid as st_mermaid
import re
from phi.agent import Agent
from phi.model.groq import Groq

st.set_page_config(
    page_title="AI Code Analyzer",
    page_icon="💻",
    layout="wide"
)

st.sidebar.markdown("### 🔑 System Status")
st.sidebar.success("🟢 Static Analysis Engine Active!")
st.sidebar.info("Model Backend: llama-3.3-70b-versatile (via Groq)")

st.title("💻 AI Code Analyzer & Architecture Mapper")
st.markdown("Upload your source code to map logic paths, perform security audits, or optimize runtime complexity.")

if "code_context" not in st.session_state:
    st.session_state.code_context = ""
if "code_file_name" not in st.session_state:
    st.session_state.code_file_name = ""

st.subheader("📂 Upload Source Code")
uploaded_file = st.file_uploader(
    "Upload a code file to analyze (Supports .py, .java, .cpp, .c, .sql, .js, .html, .txt)",
    type=["py", "java", "cpp", "c", "sql", "js", "html", "txt"]
)

if uploaded_file is not None:
    try:
        content = uploaded_file.read().decode("utf-8")
        st.session_state.code_context = content
        st.session_state.code_file_name = uploaded_file.name
        st.success(f"Successfully loaded {uploaded_file.name}!")
    except Exception as e:
        st.error(f"Error reading file: {e}")

if st.session_state.code_context:
    with st.expander("📝 View Loaded Source Code Preview", expanded=False):
        st.code(st.session_state.code_context, line_numbers=True)

st.subheader("⚙️ Select Analysis Strategy")
strategy = st.selectbox(
    "What dimension would you like to analyze?",
    options=[
        "🏗️ Architecture & Logic Mapping: Explain Data Flow and System Design",
        "🛡️ Deep Security Audit: Identify vulnerabilities (OWASP, SQLi, Buffer Overflows)",
        "⚡ Performance & Complexity Profiling: Analyze Time/Space Complexity O(N)"
    ]
)

custom_prompt = st.text_input(
    "Add specific review instructions (Optional):",
    placeholder="e.g., 'Check for SQL injection vulnerabilities' or 'Optimize memory allocation'"
)

if st.button("Run AI Engine Analysis"):
    if not st.session_state.code_context:
        st.warning("Please upload a source code file first.")
    else:
        with st.spinner("Llama agent parsing AST and mapping architecture paths..."):
            try:
                agent = Agent(
                    model=Groq(id="llama-3.3-70b-versatile"),
                    markdown=True
                )
                
                # We use clean string chaining so indentation never breaks
                code_prompt = (
                    f"You are an expert principal software engineer, security auditor, and systems architect.\n"
                    f"Analyze the source code provided below carefully based on the selected audit strategy: {strategy}\n\n"
                    f"[FILENAME]: {st.session_state.code_file_name}\n\n"
                    f"[SOURCE CODE]:\n"
                    f"```python\n{st.session_state.code_context}\n```\n\n"
                    f"[ADDITIONAL USER INSTRUCTIONS]:\n"
                    f"{(custom_prompt if custom_prompt.strip() else 'Perform standard deep code review.')}\n\n"
                    f"CRITICAL FORMATTING REQUIREMENT:\n"
                    f"If the strategy is 'Architecture & Logic Mapping', you MUST provide a valid Mermaid flowchart syntax block.\n"
                    f"You MUST write the flowchart inside standard markdown code fences starting with ```mermaid.\n"
                    f"Example layout format:\n"
                    f"```mermaid\n"
                    f"graph TD\n"
                    f"    A[User Input] --> B[Database Connection]\n"
                    f"```\n"
                    f"Ensure there are no extraneous text symbols or illegal structural arrows inside the diagram block."
                )
                
                response = agent.run(code_prompt)
                st.subheader("💡 AI Engineering Analysis Output")
                st.markdown(response.content)
                
                if "graph " in response.content or "mermaid" in response.content:
                    match = re.search(r"```mermaid\s*([\s\S]*?)\s*```", response.content)
                    if match:
                        clean_mermaid = match.group(1).strip()
                        st.subheader("📊 Interactive Logic Flowchart")
                        st_mermaid.st_mermaid(clean_mermaid)
                    else:
                        fallback_match = re.search(r"(graph (?:TD|LR|BU|RL)[\s\S]*?)(?=\n\n|$)", response.content)
                        if fallback_match:
                            st.subheader("📊 Interactive Logic Flowchart")
                            st_mermaid.st_mermaid(fallback_match.group(1).strip())
            except Exception as err:
                st.error(f"Processing error: {err}")