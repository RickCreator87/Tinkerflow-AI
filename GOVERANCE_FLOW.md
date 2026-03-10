GOVERNANCE_FLOW.md

```markdown
# Governance Flow – Step by Step

This document details the exact sequence Tinkerflow-AI follows for every pull request.

## 1. Webhook Reception

- **Trigger**: `pull_request` event (opened, synchronize, labeled)
- **Verification**: Signature validated using shared secret.
- **Parsing**: Extract repo, PR number, installation ID, sender.

## 2. Fetch PR Context

- **Diff**: GitHub API call to get unified diff of the PR.
- **Commits**: List of commit messages and SHAs.
- **Files**: List of changed files with status (added, modified, deleted).

## 3. Load Policies

- **Priority**:
  1. `.github/tinkerflow/policies.yml` in the repository.
  2. Global policies from app config.
  3. Default built-in policies.
- **Merge**: Local policies override global.

## 4. Evaluate Policies

For each enabled policy:

- **Input**: diff, commit messages, file list.
- **Method**: 
  - Regex-based (secrets, license headers)
  - LLM-based (commit message convention, code review)
- **Output**: Pass/Fail + optional message.

## 5. Generate Proofs

- Each result is serialized and hashed using SHA-256.
- The hash is stored as the proof (or recorded on a blockchain for Pro tier).

## 6. Post Feedback

- **Check Run**: Created with conclusion (success/failure) and detailed output.
- **Comment**: Optional comment if warnings exist (configurable).
- **Labels**: Optionally add `governance/pass` or `governance/fail` label.

## 7. Audit Log

- All actions are logged with timestamps and request IDs for traceability.

## Diagram

```

[PR Opened] → [Webhook] → [Fetch Diff] → [Load Policies] → [Evaluate] → [Generate Proofs] → [Post Check Run] → [Block/Allow Merge]
