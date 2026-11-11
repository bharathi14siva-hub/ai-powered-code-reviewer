
# AI-Powered Code Reviewer

An AI-powered Python code review application designed to analyze source code, identify potential issues, and generate structured review reports.

## Features

- Analyze Python source files and Git diffs
- Three review modes: Quick, Thorough, and Security-Focused
- Claude API integration using the Anthropic SDK
- Identify bugs, code quality issues, and security vulnerabilities
- Generate structured JSON reports
- Generate readable Markdown reports
- Demo mode for testing without API credentials
- Pydantic-based data validation
- Automated tests using Pytest

## Tech Stack

- Python 3.10
- Anthropic Claude API
- Pydantic
- Poetry
- Pytest
- Black
- Ruff

## Project Structure

```text
ai-code-reviewer/
├── app/
│   ├── main.py
│   ├── reviewer.py
│   ├── prompts.py
│   ├── mock_reviewer.py
│   └── report_generator.py
├── models/
│   └── schemas.py
├── tests/
│   └── test_reviewer.py
├── samples/
│   └── sample.py
├── output/
├── .env
├── .gitignore
├── pyproject.toml
└── README.md