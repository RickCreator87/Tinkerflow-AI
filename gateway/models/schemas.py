from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

class GovernanceRequest(BaseModel):
    repo: str
    pull_number: int
    installation_id: int
    trigger: str  # 'opened', 'synchronize', 'labeled'
    options: Optional[Dict[str, Any]] = {}

class PolicyResult(BaseModel):
    policy_name: str
    passed: bool
    severity: str  # 'error', 'warning'
    message: Optional[str] = None
    proof: Optional[str] = None  # cryptographic proof

class GovernanceResponse(BaseModel):
    request_id: str
    results: List[PolicyResult]
    overall_pass: bool
    summary: str
