# ARCHITECTURE.md
```markdown
# Architecture Overview

Tinkerflow-AI is built as a modular system with three main components:

```

┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   GitHub App    │────▶│  Governance     │────▶│   LLM Gateway   │
│   (webhooks)    │     │   Engine        │     │   (router)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
│                        │
▼                        ▼
┌─────────────────┐     ┌─────────────────┐
│   Policy        │     │   Providers     │
│   Checker       │     │   (OpenAI, etc.)│
└─────────────────┘     └─────────────────┘

```

### Components

1. **GitHub App** – Listens for pull_request events, authenticates with GitHub, and triggers governance.
2. **Governance Engine** – Orchestrates policy evaluation, proof generation, and feedback posting.
3. **LLM Gateway** – Routes prompts to appropriate LLM providers with fallback logic.
4. **Policy Checker** – Evaluates policies against PR diffs using regex, AST, or LLM calls.
5. **Providers** – Adapters for Ollama, OpenAI, Anthropic, etc.

### Data Flow

1. Webhook received → authentication middleware verifies signature.
2. Payload parsed, PR diff fetched via GitHub API.
3. Governance engine loads policies from repo config or global config.
4. Each policy evaluated; results are hashed to create cryptographic proofs.
5. Proofs optionally verified (external service or local).
6. Check run created; if any policy fails, PR merge blocked.
7. Results logged and audit trail stored.

### Deterministic Governance

All decisions are based solely on the PR content and fixed policies. No external factors alter the outcome, ensuring reproducibility.
```
