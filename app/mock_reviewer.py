from models.schemas import CodeReviewReport, ReviewFinding


def generate_demo_review(filename: str, mode: str) -> CodeReviewReport:
    findings = [
        ReviewFinding(
            severity="High",
            category="Security",
            line_number=3,
            description="Hardcoded credentials may expose sensitive information.",
            recommendation="Use environment variables to store credentials.",
        ),
        ReviewFinding(
            severity="Medium",
            category="Code Quality",
            line_number=6,
            description="Missing error handling may cause unexpected failures.",
            recommendation="Add appropriate exception handling.",
        ),
    ]

    if mode == "quick":
        findings = findings[:1]
    elif mode == "security-focused":
        findings = [f for f in findings if f.category == "Security"]

    return CodeReviewReport(
        filename=filename,
        review_mode=mode,
        overall_score=65,
        summary="Demo review generated with sample findings.",
        findings=findings,
        positive_aspects=[
            "Code is relatively simple.",
            "Function names are understandable.",
        ],
    )
