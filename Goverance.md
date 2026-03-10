# Tinkerflow-AI Governance Model

This document defines the deterministic governance rules enforced by Tinkerflow-AI on every pull request.

## Governance Steps

1. **Trigger** – On PR open, synchronize, or labeled with `governance/check`.
2. **Policy Check** – Evaluate PR against policies defined in `config/policies.config.json`.
3. **Proof Generation** – Generate cryptographic proof of compliance for each policy.
4. **Proof Verification** – Verify generated proofs; any failure blocks merge.
5. **Feedback** – Post results as a check run and optional PR comment.

## Enforcement Logic

- **Merge Block** – If any proof fails, the check run fails and merge is blocked.
- **Auto-Approval** – If all proofs pass and governance is strict, auto-approve.
- **Override** – Repository admins can override with `governance/override` label.

Traceability: All governance actions are logged and can be replayed.
