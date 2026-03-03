Phase 1: Expose metrics (no UI yet, just truth)

Before dashboards, We need a metrics endpoint. Think of it as your gateway confessing its sins.
`
Add /admin/metrics

from fastapi import APIRouter, Header, HTTPException
import redis

router = APIRouter()
r = redis.Redis(host="redis", port=6379, decode_responses=True)

ADMIN_KEY = "super-secret-admin-key"  # move to env later

@router.get("/admin/metrics")
def metrics(x_admin_key: str = Header(None)):
    if x_admin_key != ADMIN_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

    keys = r.keys("usage:*")
    data = {}

    for key in keys:
        api_key = key.replace("usage:", "")
        data[api_key] = r.hgetall(key)

    return data
