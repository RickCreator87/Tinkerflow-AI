import uuid
from typing import List
from ...config import load_config
from ...gateway.router import Router
from .policy_checker import check_policies
from .proof_generator import generate_proofs
from .proof_verifier import verify_proofs
from ..models.schemas import GovernanceResponse, PolicyResult
import logging

logger = logging.getLogger(__name__)

async def run_governance(repo: str, pull_number: int, installation_id: int, trigger: str) -> GovernanceResponse:
    """Orchestrate the entire governance flow."""
    request_id = str(uuid.uuid4())
    logger.info(f"Starting governance {request_id} for {repo}#{pull_number}")

    # Load policies
    policies_config = load_config('policies')
    policies = policies_config.get('policies', [])

    # 1. Check policies against PR diff (simplified: fetch diff via GitHub API)
    diff = await fetch_pr_diff(repo, pull_number, installation_id)  # not shown for brevity
    policy_results = await check_policies(policies, diff)

    # 2. Generate cryptographic proofs for each result
    proofs = await generate_proofs(policy_results)

    # 3. Verify proofs (could be done immediately or stored for later)
    verified = await verify_proofs(proofs)

    # 4. Determine overall pass/fail
    overall_pass = all(r.passed for r in policy_results) and verified

    summary = f"Governance check {request_id}: {'PASS' if overall_pass else 'FAIL'}"

    return GovernanceResponse(
        request_id=request_id,
        results=policy_results,
        overall_pass=overall_pass,
        summary=summary
    )
