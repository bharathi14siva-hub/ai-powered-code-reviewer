import json
import os

from anthropic import Anthropic

from app.prompts import SYSTEM_PROMPT, build_review_prompt
from models.schemas import CodeReviewReport


class CodeReviewer:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model = os.getenv(
            "CLAUDE_MODEL",
            "claude-sonnet-4-20250514",
        )

        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY is missing.")

        self.client = Anthropic(api_key=self.api_key)

    def review_code(
        self,
        code: str,
        filename: str,
        mode: str = "thorough",
        is_diff: bool = False,
    ) -> CodeReviewReport:

        if not code.strip():
            raise ValueError("Input code or diff cannot be empty.")

        if mode not in ["quick", "thorough", "security-focused"]:
            raise ValueError(f"Unsupported review mode: {mode}")

        if is_diff and not filename.endswith((".diff", ".patch")):
            filename = f"{filename}.diff"

        review_prompt = build_review_prompt(
            code=code,
            mode=mode,
            filename=filename,
        )

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": review_prompt,
                }
            ],
        )

        response_text = response.content[0].text.strip()

        # Remove Markdown code fences if Claude includes them.
        if response_text.startswith("```"):
            response_text = response_text.split("\n", 1)[1]
            response_text = response_text.rsplit("```", 1)[0].strip()

        review_data = json.loads(response_text)

        report = CodeReviewReport(
            filename=filename,
            review_mode=mode,
            **review_data,
        )

        return report
