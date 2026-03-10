import hashlib
import json
from typing import List
from ..models.schemas import PolicyResult

def generate_proofs(results: List[PolicyResult]) -> List[str]:
    """Generate deterministic proofs for policy results."""
    proofs = []
    for r in results:
        # Simple hash of result details as proof (for demo)
        data = json.dumps({
            "policy": r.policy_name,
            "passed": r.passed,
            "timestamp": "2025-01-01T00:00:00Z"  # would be actual timestamp
        }, sort_keys=True)
        proof = hashlib.sha256(data.encode()).hexdigest()
        r.proof = proof
        proofs.append(proof)
    return proofs
