from crewai import Agent, LLM
import subprocess
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def scan_with_bandit(file_path):
    if not os.path.exists(file_path):
        return "File not found."
    try:
        result = subprocess.run(
            ["bandit", "-f", "txt", "-ll", file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return "No security issues found."
        return result.stdout.strip() or "Bandit found issues (see output)."
    except Exception as e:
        return f"Bandit scan failed: {str(e)}"

llm = LLM(model="gemini/gemini-2.5-flash")


security_analyst = Agent(
    role="Security Analyst",
    goal="Find security flaws like injection, hardcoded secrets, or unsafe functions",
    backstory=(
        "You’ve worked as an appsec engineer for 10 years. "
        "You’re paranoid about code that talks to the outside world."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)