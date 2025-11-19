#  CrewAI-Powered Code Reviewer

A lightweight, multi-agent code review system built with **CrewAI** that analyzes Python files for common issues — no fluff, just actionable feedback.

##  What It Checks

- ** Security**: Finds SQL injection, unsafe patterns (via `bandit`)
- ** Performance**: Flags inefficient loops, bad I/O habits
- ** Style**: Enforces PEP8 (via `flake8`)
- ** Documentation**: Validates Google-style docstrings (via `pydocstyle`)

Each check is handled by a dedicated AI agent that explains issues in plain English — powered by **Gemini** (free tier works great!).

##  Quick Start

1. **Get a Gemini API key**  
   → [Create one here (free)](https://aistudio.google.com/app/apikey)

2. **Set up the project**
   ```bash
   git clone https://github.com/your-username/crewai-code-reviewer.git
   cd crewai-code-reviewer
   pip install -r requirements.txt

3. **Add your API key**
    ```bash
    echo "GEMINI_API_KEY=your_key_here" > .env

4. **Run a review**
    ```bash
    python main.py --file test_file.py