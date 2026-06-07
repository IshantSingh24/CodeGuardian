from fastapi import APIRouter, Request

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
    head_sha = payload["pull_request"]["head"]["sha"]

    print("\n====== PR INFO ======")
    print("Repo:", repo)
    print("PR:", pr_number)
    print("Diff URL:", diff_url)
    print("SHA:", head_sha)
    print("=====================\n")

    return {"status": "received"}