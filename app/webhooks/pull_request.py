from fastapi import APIRouter, Request, HTTPException
from ..services.governance_engine import run_governance
from ..services.feedback_poster import post_feedback
from ...config import load_config
import logging

router = APIRouter(prefix="/webhooks/github", tags=["webhooks"])
logger = logging.getLogger(__name__)

@router.post("/pull_request")
async def handle_pull_request(request: Request):
    """Handle pull_request webhook events."""
    payload = await request.json()
    action = payload.get("action")
    if action not in ["opened", "synchronize", "labeled"]:
        logger.debug(f"Ignoring action: {action}")
        return {"status": "ignored"}

    # Extract relevant data
    repo = payload["repository"]["full_name"]
    pull_number = payload["number"]
    installation_id = payload["installation"]["id"]
    sender = payload["sender"]["login"]

    logger.info(f"Processing PR #{pull_number} in {repo} by {sender}")

    # Run governance checks
    result = await run_governance(repo, pull_number, installation_id, action)

    # Post feedback (check runs, comments)
    await post_feedback(result, repo, pull_number, installation_id)

    return {"status": "processed", "result": result.dict()}
