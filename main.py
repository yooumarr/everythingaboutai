import argparse
import os
from crewai import Crew
from tasks.review_tasks import create_review_tasks

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"File not found: {args.file}")
        return 1

    print(f"Reviewing: {args.file}\n")

    tasks = create_review_tasks(args.file)
    crew = Crew(
        agents=[t.agent for t in tasks],
        tasks=tasks,
        verbose=True,
    )

    result = crew.kickoff()
    print("\n" + "="*60)
    print("FINAL CODE REVIEW REPORT")
    print("="*60)
    print(result)

if __name__ == "__main__":
    exit(main())