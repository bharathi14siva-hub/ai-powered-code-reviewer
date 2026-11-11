
import json

from app.mock_reviewer import generate_demo_review
from app.report_generator import save_report


def test_json_report_generation(tmp_path):
    report = generate_demo_review("sample.py", "thorough")

    json_file, _ = save_report(report, str(tmp_path))

    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)

    assert data["filename"] == "sample.py"
    assert data["overall_score"] == 65
    assert len(data["findings"]) == 2


def test_markdown_report_generation(tmp_path):
    report = generate_demo_review("sample.py", "thorough")

    _, markdown_file = save_report(report, str(tmp_path))

    content = markdown_file.read_text(encoding="utf-8")

    assert "# AI Code Review Report" in content
    assert "sample.py" in content
    assert "65/100" in content
    assert "## Findings" in content
