from crewai import Task
from agents.security_agent import security_analyst, scan_with_bandit
from agents.performance_agent import performance_optimizer, check_performance
from agents.style_agent import style_checker, check_style
from agents.docs_agent import documentation_agent, check_docs


def create_review_tasks(file_path):
    security_result = scan_with_bandit(file_path)
    performance_result = check_performance(file_path)
    style_result = check_style(file_path)
    docs_result = check_docs(file_path)

    return [
        Task(
            description=(
                f"Analyze the following Bandit security scan output for '{file_path}':\n\n"
                f"{security_result}\n\n"
                "Your job: Summarize the findings in plain English. "
                "Highlight real risks (ignore 'no issues found' messages). "
                "Mention severity, location (line number), and a short fix suggestion."
            ),
            expected_output=(
                "A concise paragraph or bullet list of actual security issues. "
                "If no issues, say: 'No security issues detected.'"
            ),
            agent=security_analyst,
        ),
        Task(
            description=(
                f"Review this performance analysis for '{file_path}':\n\n"
                f"{performance_result}\n\n"
                "Explain what's inefficient and how a developer can fix it. "
                "Be specific: mention line numbers and alternatives (e.g., 'use enumerate()')."
            ),
            expected_output=(
                "2–4 actionable performance tips. If none: 'Code appears efficient.'"
            ),
            agent=performance_optimizer,
        ),
        Task(
            description=(
                f"Here is the flake8 output for '{file_path}':\n\n"
                f"{style_result}\n\n"
                "Convert these PEP8 errors into clear, developer-friendly advice. "
                "Group by issue type if possible, and show corrected examples."
            ),
            expected_output=(
                "A readable list of style fixes (e.g., 'Line 23: Add whitespace around operator → total += item'). "
                "If clean: 'Code follows PEP8 style.'"
            ),
            agent=style_checker,
        ),
        Task(
            description=(
                f"Documentation check result for '{file_path}':\n\n"
                f"{docs_result}\n\n"
                "Summarize docstring status. If issues exist, list functions missing docstrings."
            ),
            expected_output=(
                "Brief summary like: 'Missing docstrings in: get_user_data(), process_logs()' "
                "or 'All functions have proper docstrings.'"
            ),
            agent=documentation_agent,
        ),
    ]