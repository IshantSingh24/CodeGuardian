from fastapi import APIRouter, Request

from app.github_utils import get_diff
from app.github_comment import post_comment

from graph.workflow import graph

router = APIRouter()


@router.post("/webhook/github")
async def github_webhook(request: Request):

    payload = await request.json()

    action = payload.get("action")

    print(f"\nACTION = {action}")

    VALID_ACTIONS = [
        "opened",
        "synchronize",
        "reopened"
    ]

    if action not in VALID_ACTIONS:

        print("Ignoring event")

        return {
            "status": "ignored"
        }

    repo = payload["repository"]["full_name"]

    pr_number = payload["pull_request"]["number"]

    pr_api_url = payload["pull_request"]["url"]

    head_sha = payload["pull_request"]["head"]["sha"]

    print("\n====== PR INFO ======")

    print("Repo:", repo)
    print("PR:", pr_number)
    print("SHA:", head_sha)
    print("PR API URL:", pr_api_url)

    print("=====================\n")

    try:

        # Fetch Diff
        diff = get_diff(pr_api_url)

        print(
            f"DIFF LENGTH = {len(diff)}"
        )

        # Run LangGraph
        result = graph.invoke(
            {
                "diff": diff,
                "security_result": None,
                "quality_result": None,
                "final_review": ""
            }
        )

        review = result["final_review"]

        print(
            "\n========== FINAL REVIEW ==========\n"
        )

        print(review)

        print(
            "\n==================================\n"
        )

        # Post comment on GitHub PR
        post_comment(
            repo=repo,
            pr_number=pr_number,
            review=review
        )

        print(
            "\n====== COMMENT POSTED ======\n"
        )

        return {
            "status": "review_generated",
            "pr": pr_number
        }

    except Exception as e:

        print(
            "\n========== ERROR ==========\n"
        )

        print(str(e))

        print(
            "\n===========================\n"
        )

        return {
            "status": "failed",
            "error": str(e)
        }