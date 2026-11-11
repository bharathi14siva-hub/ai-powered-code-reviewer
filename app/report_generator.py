import json
from pathlib import Path

from models.schemas import CodeReviewReport


def save_report(report: CodeReviewReport, output_dir: str = "output"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    filename = Path(report.filename).stem

    json_file = output_path / f"{filename}_review.json"
    markdown_file = output_path / f"{filename}_review.md"

    # Save JSON report
    json_file.write_text(json.dumps(report.model_dump(), indent=4), encoding="utf-8")

    # Build Markdown report
    lines = [
        "# AI Code Review Report",
        "",
        f"**File:** {report.filename}",
        f"**Review Mode:** {report.review_mode}",
        f"**Overall Score:** {report.overall_score}/100",
        "",
        "## Summary",
        "",
        report.summary,
        "",
        "## Findings",
        "",
    ]

    if report.findings:
        for index, finding in enumerate(report.findings, start=1):
            lines.extend(
                [
                    f"### {index}. {finding.severity} - {finding.category}",
                    "",
                    f"**Line:** {finding.line_number or 'Not specified'}",
                    "",
                    f"**Issue:** {finding.description}",
                    "",
                    f"**Recommendation:** {finding.recommendation}",
                    "",
                ]
            )
    else:
        lines.extend(["No issues found.", ""])

    lines.extend(["## Positive Aspects", ""])

    if report.positive_aspects:
        for aspect in report.positive_aspects:
            lines.append(f"- {aspect}")
    else:
        lines.append("No positive aspects reported.")

    markdown_file.write_text("\n".join(lines), encoding="utf-8")

    return json_file, markdown_file
