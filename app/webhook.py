from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook/github")
async def github_webhook(request: Request):

    payload = await request.json()

    print("\n========== WEBHOOK RECEIVED ==========")
    print(payload)
    print("======================================\n")

    return {"status": "received"}