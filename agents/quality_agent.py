from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseModel
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

PROMPT_PATH = (
    Path(__file__).parent.parent
    / "prompts"
    / "quality.txt"
)


class QualityReview(BaseModel):
    score: int
    findings: list[str]
    recommendations: list[str]
    summary: str


def quality_agent(diff: str) -> QualityReview:

    prompt = PROMPT_PATH.read_text(
        encoding="utf-8"
    )

    response = client.responses.parse(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": diff
            }
        ],
        text_format=QualityReview
    )

    return response.output_parsed