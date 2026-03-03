Wire into the request flow

Wherever  extract the API key (from Authorization: Bearer xxx), add the check.

Example:
`
from app.rate_limit import RateLimiter
import os

rate_limiter = RateLimiter(
    max_requests=int(os.getenv("RATE_LIMIT_REQUESTS", 60)),
    window_seconds=int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", 60))
)
`
Then inside endpoint or dependency:
`
def get_api_key(auth_header: str):
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing API key")

    api_key = auth_header.replace("Bearer ", "").strip()
    rate_limiter.check(api_key)
    return api_key
