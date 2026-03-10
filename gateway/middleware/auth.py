from fastapi import Request, HTTPException
import hmac
import hashlib
from ...config import load_config

async def verify_github_webhook(request: Request, call_next):
    """Middleware to verify GitHub webhook signatures."""
    config = load_config('app')
    webhook_secret = config['github']['webhook_secret']

    signature_header = request.headers.get('X-Hub-Signature-256')
    if not signature_header:
        raise HTTPException(status_code=401, detail="Missing signature")

    body = await request.body()
    expected_signature = 'sha256=' + hmac.new(
        key=webhook_secret.encode('utf-8'),
        msg=body,
        digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature_header, expected_signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

    response = await call_next(request)
    return response
