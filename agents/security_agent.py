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
    / "security.txt"
)


class SecurityIssue(BaseModel):
    type: str
    description: str
    fix: str


class SecurityReview(BaseModel):
    severity: str
    issues: list[SecurityIssue]
    summary: str


def security_agent(diff: str) -> SecurityReview:

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
        text_format=SecurityReview
    )

    return response.output_parsed