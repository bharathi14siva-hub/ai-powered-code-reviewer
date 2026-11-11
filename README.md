
# AI-Powered Python Code Reviewer

An AI-powered Python code review application that analyzes Python source files and Git diffs to identify bugs, code quality issues, and potential security vulnerabilities using Anthropic's Claude API.

## Features

- Analyze Python source files and Git diffs
- Three review modes: Quick, Thorough, and Security-Focused
- Claude API integration using the Anthropic SDK
- Identify bugs, code quality issues, and security vulnerabilities
- Generate structured JSON review reports
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
│   ├── __init__.py
│   ├── main.py
│   ├── reviewer.py
│   ├── prompts.py
│   ├── mock_reviewer.py
│   └── report_generator.py
├── models/
│   ├── __init__.py
│   └── schemas.py
├── tests/
│   ├── test_reviewer.py
│   ├── test_report_generator.py
│   └── test_input_validation.py
├── samples/
│   ├── sample.py
│   └── sample.diff
├── output/
├── .env
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/bharathi14siva-hub/ai-powered-code-reviewer.git
cd ai-powered-code-reviewer
```

### 2. Install dependencies

```bash
poetry install
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
CLAUDE_MODEL=claude-sonnet-4-20250514
```

Replace the placeholder with your Anthropic API key.

## Usage

### Demo Mode

Run a review without an API key using the built-in demo findings:

```bash
poetry run python -m app.main --file samples/sample.py --demo
```

### Review a Python File

```bash
poetry run python -m app.main --file samples/sample.py
```

### Review a Git Diff

```bash
poetry run python -m app.main --diff samples/sample.diff
```

### Select a Review Mode

Quick review:

```bash
poetry run python -m app.main --file samples/sample.py --mode quick
```

Thorough review:

```bash
poetry run python -m app.main --file samples/sample.py --mode thorough
```

Security-focused review:

```bash
poetry run python -m app.main --file samples/sample.py --mode security-focused
```

Add `--demo` to any supported command to run the demo reviewer without Claude API credentials.

## Review Modes

| Mode | Description |
|---|---|
| Quick | Focuses on important issues |
| Thorough | Performs a comprehensive code review |
| Security-Focused | Focuses on potential security vulnerabilities |

## Output Reports

The application generates two report formats:

- **JSON:** Structured findings suitable for programmatic use.
- **Markdown:** Human-readable review report.

Reports are saved in the `output/` directory.

Each report includes:
- Filename
- Review mode
- Overall score
- Summary
- Findings with severity and recommendations
- Positive aspects

## Running Tests

Run the complete test suite:

```bash
poetry run python -m pytest -v
```

Run code quality checks:

```bash
poetry run ruff check .
```

Format the project:

```bash
poetry run black .
```

## Current Testing Status

- 7 automated tests passing
- Black formatting completed
- Ruff checks passing

**Note:** Demo mode uses illustrative sample findings. Live Claude API functionality requires a valid Anthropic API key and API access. Live API testing should be completed separately.

## Author

**Thalla Siva Bharathi**

GitHub: [bharathi14siva-hub](https://github.com/bharathi14siva-hub)
