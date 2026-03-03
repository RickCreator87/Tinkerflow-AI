import time
from collections import defaultdict, deque
from fastapi import HTTPException, status

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(deque)

    def check(self, api_key: str):
        now = time.time()
        window_start = now - self.window
        q = self.requests[api_key]

        # Remove expired timestamps
        while q and q[0] < window_start:
            q.popleft()

        if len(q) >= self.max_requests:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded"
            )

        q.append(now)
