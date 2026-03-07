### UPGRADING.md
```markdown
# Upgrading Tinkerflow-AI

## From v0.x to v1.0

### Breaking Changes

- The configuration format has changed from YAML to JSON. Use the migration tool:
  ```bash
  ./scripts/migrate-config.sh old-config.yml > config/app.config.json
```

· Environment variables prefix changed from TINKERFLOW_ to TF_.
· The /api/v1/governance endpoint now requires installation_id in the request body.

New Features

· Support for multiple LLM providers.
· Cryptographic proofs for each policy result.
· Check run annotations linking to specific lines.

See the CHANGELOG for a full list of changes.

```
