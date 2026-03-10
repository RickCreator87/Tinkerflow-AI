import logging
import time
from fastapi import Request

logger = logging.getLogger(__name__)

async def log_requests(request: Request, call_next):
    """Middleware to log request/response details."""
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    logger.info(
        f"{request.method} {request.url.path} - {response.status_code} - {process_time:.2f}ms"
    )
    return response
