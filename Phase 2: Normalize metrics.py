---

Phase 2: Normalize metrics (future)

Right now Redis keys look like:
`
usage:apikey123 → { llama3:tokens: 4200, llama3:requests: 12 }
`
That’s fine, but dashboards love structure.

Standardize fields:
`
r.hincrby(f"usage:{api_key}", f"{model}.tokens", tokens)
r.hincrby(f"usage:{api_key}", f"{model}.requests", 1)
r.hincrby(f"usage:{api_key}", "total.requests", 1)
r.hincrby(f"usage:{api_key}", "total.tokens", tokens)
