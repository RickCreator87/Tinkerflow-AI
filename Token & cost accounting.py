
---

3️⃣ Token & cost accounting (the SaaS core)

Even if you’re not billing yet, tracking is non-optional.

Simple token estimator (good enough)
`
def estimate_tokens(messages):
    return sum(len(m["content"].split()) for m in messages)
`

---

Track usage in Redis
`
def record_usage(api_key, model, tokens):
    r.hincrby(f"usage:{api_key}", f"{model}:tokens", tokens)
    r.hincrby(f"usage:{api_key}", f"{model}:requests", 1)
`
Call this after every successful completion.


Cost mapping (future-proof)
`
MODEL_COSTS = {
    "llama3": 0.000002,
    "llama3_70b": 0.00002
}

def estimate_cost(model, tokens):
    return tokens * MODEL_COSTS.get(model, 0)
