from fastapi import Request, status
from fastapi.responses import JSONResponse
import logging
from ...config.errors import get_error_message

logger = logging.getLogger(__name__)

async def unified_error_handler(request: Request, call_next):
    """Catch exceptions and return standardized error responses."""
    try:
        return await call_next(request)
    except Exception as exc:
        logger.exception("Unhandled exception")
        error_code = getattr(exc, 'error_code', 'E010')
        message = get_error_message(error_code) or "An internal error has occurred."
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": error_code, "message": message}
        )
