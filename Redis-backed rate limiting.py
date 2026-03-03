1️⃣ Redis-backed rate limiting (real scaling starts here)

In-memory limits die the moment you add a second container. Redis fixes that.

Add Redis (Docker)

In docker-compose.yml:
`
services:
  redis:
    image: redis:7
    ports:
      - "6379:6379"
`

---

Install dependency
`
pip install redis
`

---

Redis rate limiter (app/rate_limit.py)
`
import time
import redis
from fastapi import HTTPException

r = redis.Redis(host="redis", port=6379, decode_responses=True)

class RedisRateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max = max_requests
        self.window = window_seconds

    def check(self, api_key: str):
        key = f"rl:{api_key}"
        now = int(time.time())

        pipe = r.pipeline()
        pipe.zremrangebyscore(key, 0, now - self.window)
        pipe.zcard(key)
        pipe.zadd(key, {now: now})
        pipe.expire(key, self.window)
        _, count, _, _ = pipe.execute()

        if count >= self.max:
            raise HTTPException(
                status_code=429,
                detail={
                    "error": {
                        "message": "Rate limit exceeded",
                        "type": "rate_limit_error",
                        "code": "rate_limit_exceeded"
                    }
                )
