import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv

from app.mock_reviewer import generate_demo_review
from app.report_generator import save_report
from app.reviewer import CodeReviewer

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="AI-powered Python Code Reviewer")

    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", help="Path to a Python file")
    source.add_argument("--diff", help="Path to a Git diff file")

    parser.add_argument(
        "--mode",
        choices=["quick", "thorough", "security-focused"],
        default="thorough",
        help="Select the review mode",
    )

    parser.add_argument(
        "--demo",
        action="store_true",
        help="Generate a sample review without calling Claude",
    )

    args = parser.parse_args()

    input_path = Path(args.file or args.diff)

    if not input_path.is_file():
        parser.error(f"Input file not found: {input_path}")

    try:
        code = input_path.read_text(encoding="utf-8")
        filename = input_path.name
        is_diff = args.diff is not None

        if not code.strip():
            raise ValueError("Input file is empty.")

        if args.demo:
            print("\nGenerating DEMO review...")
            report = generate_demo_review(filename, args.mode)

        else:
            if not os.getenv("ANTHROPIC_API_KEY"):
                raise ValueError(
                    "Claude API key missing. Use --demo for a sample review."
                )

            print("\nSending input to Claude for review...")

            reviewer = CodeReviewer()

            report = reviewer.review_code(
                code=code,
                filename=filename,
                mode=args.mode,
                is_diff=is_diff,
            )

        json_file, markdown_file = save_report(report)

        print("\nReview completed!")
        print(f"Score: {report.overall_score}/100")
        print(f"Findings: {len(report.findings)}")
        print(f"JSON report: {json_file}")
        print(f"Markdown report: {markdown_file}")

    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(f"\nReview failed: {error}")


if __name__ == "__main__":
    main()
