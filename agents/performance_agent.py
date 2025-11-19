from crewai import Agent, LLM
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def check_performance(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    issues = []
    for i, line in enumerate(lines, 1):
        if ".readlines()" in line and "with open" in "\n".join(lines[max(0, i-3):i]):
            issues.append(f"Line {i}: Avoid readlines() on large files – use iterative reading.")
        if "for" in line and "range(len(" in line:
            issues.append(f"Line {i}: Consider using enumerate() instead of range(len(...)).")

    return "\n".join(issues) if issues else "No obvious performance red flags."

llm = LLM(model="gemini/gemini-2.5-flash")

performance_optimizer = Agent(
    role="Performance Optimizer",
    goal="Spot inefficient patterns (e.g., O(n²) loops, bad I/O)",
    backstory="You optimize code that runs at 3 AM when no one’s watching.",
    verbose=True,
    allow_delegation=False,
    llm=llm 

)