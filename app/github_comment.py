import os
import requests

from dotenv import load_dotenv

load_dotenv()


def post_comment(
    repo: str,
    pr_number: int,
    review: str
):

    token = os.getenv(
        "GITHUB_TOKEN"
    )

    url = (
        f"https://api.github.com/repos/"
        f"{repo}/issues/{pr_number}/comments"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "body": review
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print(
        "COMMENT STATUS:",
        response.status_code
    )

    print(response.text)

    response.raise_for_status()

    return response.json()