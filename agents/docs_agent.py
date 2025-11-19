from crewai import Agent, LLM
import subprocess

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
def check_docs(file_path):
    import subprocess, os
    if not os.path.exists(file_path):
        return "File not found."
    try:
        result = subprocess.run(
            ["pydocstyle", "--convention=google", file_path],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return "Documentation meets Google style guide."
        return result.stdout.strip() or "Docstring issues found."
    except Exception as e:
        return f"Doc check failed: {e}"

# Still use Ollama (in case you want future flexibility)
# Use Gemini instead of Ollama
llm = LLM(model="gemini/gemini-2.5-flash")

documentation_agent = Agent(
    role="Documentation Agent",
    goal="Report docstring status",
    backstory="I return exactly what pydocstyle says.",
    verbose=False,
    allow_delegation=False,
    llm=llm
)