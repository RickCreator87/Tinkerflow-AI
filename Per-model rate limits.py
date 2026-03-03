---

2️⃣ Per-model rate limits (GPU sanity)

You never want llama3:70b treated the same as phi.

Config (example)
`
MODEL_LIMIT_llama3=60
MODEL_LIMIT_llama3_70b=10
`

---

Enforce per-model
`
def enforce_model_limit(api_key: str, model: str):
    limit = int(os.getenv(f"MODEL_LIMIT_{model}", 60))
    limiter = RedisRateLimiter(limit, 60)
    limiter.check(f"{api_key}:{model}")
```
