from fastapi import APIRouter, Request
from ..services.governance_engine import run_governance
from ...config import load_config
import logging

router = APIRouter(prefix="/webhooks/github", tags=["webhooks"])
logger = logging.getLogger(__name__)

@router.post("/check_run")
async def handle_check_run(request: Request):
    """Handle check_run events (e.g., re-requested)."""
    payload = await request.json()
    action = payload.get("action")
    if action != "rerequested":
        return {"status": "ignored"}

    # Re-run governance for the associated PR
    check_run = payload["check_run"]
    # In a real implementation, you'd map check_run to PR via annotations or external store
    # For simplicity, we'll assume check_run name includes PR number
    name_parts = check_run["name"].split("#")
    if len(name_parts) != 2:
        logger.warning("Could not parse PR number from check_run name")
        return {"status": "error", "message": "Invalid check_run name"}

    repo = payload["repository"]["full_name"]
    pull_number = int(name_parts[1])
    installation_id = payload["installation"]["id"]

    result = await run_governance(repo, pull_number, installation_id, "rerequested")
    # post_feedback will be called by the governance engine or separately
    return {"status": "processed"}
