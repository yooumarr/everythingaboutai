from crewai import Agent, LLM
import subprocess
from dotenv import load_dotenv

load_dotenv()
def check_style(file_path):
    try:
        result = subprocess.run(
            ["flake8", "--select=E,W,F", "--quiet", file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return "Style looks good (PEP8 compliant)."
        
        detailed = subprocess.run(
            ["flake8", file_path], capture_output=True, text=True
        )
        return detailed.stdout.strip()
    except Exception as e:
        return f"Style check failed: {e}"

llm = LLM(model="gemini/gemini-2.5-flash")


style_checker = Agent(
    role="Style Checker",
    goal="Enforce PEP8 and clean, readable code style",
    backstory="You flinch at missing spaces around operators.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)