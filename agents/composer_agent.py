from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

PROMPT_PATH = (
    Path(__file__).parent.parent
    / "prompts"
    / "composer.txt"
)


def composer_agent(
    security_result,
    quality_result
):

    prompt = PROMPT_PATH.read_text(
        encoding="utf-8"
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content":
                f"""
Security Agent Output:

{security_result.model_dump_json(indent=2)}

Quality Agent Output:

{quality_result.model_dump_json(indent=2)}
"""
            }
        ]
    )

    return response.output_text