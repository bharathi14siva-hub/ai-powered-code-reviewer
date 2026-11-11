from app.mock_reviewer import generate_demo_review


def test_thorough_review():
    report = generate_demo_review("sample.py", "thorough")
    assert report.overall_score == 65
    assert len(report.findings) == 2


def test_quick_review():
    report = generate_demo_review("sample.py", "quick")
    assert len(report.findings) == 1


def test_security_review():
    report = generate_demo_review("sample.py", "security-focused")
    assert all(finding.category == "Security" for finding in report.findings)
