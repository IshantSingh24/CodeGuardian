from fastapi import APIRouter, Request
from app.github_utils import get_diff

router = APIRouter()

@router.post("/webhook/github")
async def github_webhook(request: Request):

    payload = await request.json()

    action = payload.get("action")

    print("ACTION =", action)

    if action not in ["opened", "synchronize"]:
        return {"status": "ignored"}

    repo = payload["repository"]["full_name"]
    pr_number = payload["pull_request"]["number"]
    diff_url = payload["pull_request"]["diff_url"]

    diff = get_diff(diff_url)

    print("ACTION =", action)
    print("REPO =", repo)
    print("PR =", pr_number)
    print("HEAD SHA =", head_sha)
    print("DIFF LENGTH =", len(diff))

    return {"status": "received"}