import pytest

from app.reviewer import CodeReviewer


def test_empty_code_rejected():
    reviewer = CodeReviewer.__new__(CodeReviewer)

    with pytest.raises(ValueError, match="cannot be empty"):
        reviewer.review_code("", "sample.py", "thorough")


def test_invalid_mode_rejected():
    reviewer = CodeReviewer.__new__(CodeReviewer)

    with pytest.raises(ValueError, match="Unsupported review mode"):
        reviewer.review_code("print('hello')", "sample.py", "invalid")
