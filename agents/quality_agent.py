from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "quality.txt"


def quality_agent(diff: str):

    system_prompt = PROMPT_PATH.read_text(
        encoding="utf-8"
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": diff
            }
        ]
    )

    return response.output_text