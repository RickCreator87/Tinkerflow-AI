# app/main.py
"""
Main application entry point for AI Gateway for Ollama.
This is a FastAPI server that acts as an OpenAI-compatible gateway to Ollama.
"""

import os
import logging
from typing import Optional, Dict, Any

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Import project modules
from app.rate_limit import check_rate_limit, RateLimitConfig
from app.ollama_client import OllamaClient
from app.auth import validate_api_key, get_api_key_info

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Gateway for Ollama",
    description="OpenAI API-compatible gateway that proxies requests to a local Ollama instance",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize clients and configuration
ollama_client = OllamaClient()
rate_limit_config = RateLimitConfig()

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    """Log all incoming requests."""
    logger.info(f"Incoming request: {request.method} {request.url}")
    logger.info(f"Headers: {dict(request.headers)}")
    
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    
    return response

@app.on_event("startup")
async def startup_event():
    """Initialize resources on application startup."""
    logger.info("Starting AI Gateway for Ollama...")
    
    # Check if Ollama is available
    try:
        ollama_available = await ollama_client.check_health()
        if ollama_available:
            logger.info("✅ Ollama is available and ready")
        else:
            logger.warning("⚠️ Ollama may not be available")
    except Exception as e:
        logger.error(f"Failed to connect to Ollama: {e}")

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "service": "AI Gateway for Ollama",
        "version": "1.0.0",
        "endpoints": {
            "openai_compatible": "/v1/chat/completions",
            "health": "/health",
            "models": "/v1/models"
        },
        "documentation": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for the gateway and Ollama."""
    try:
        ollama_health = await ollama_client.check_health()
        return {
            "gateway": "healthy",
            "ollama": "healthy" if ollama_health else "unavailable",
            "status": "ok" if ollama_health else "degraded"
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JSONResponse(
            status_code=503,
            content={"gateway": "healthy", "ollama": "unavailable", "status": "degraded"}
        )

@app.get("/v1/models")
async def list_models(authorization: Optional[str] = Header(None)):
    """
    List available models (OpenAI-compatible endpoint).
    
    Note: This returns the model configured in the gateway or available Ollama models.
    """
    # Validate API key if provided
    if authorization:
        api_key_info = validate_api_key(authorization)
        if not api_key_info:
            raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        models = await ollama_client.list_models()
        return {
            "object": "list",
            "data": models
        }
    except Exception as e:
        logger.error(f"Failed to list models: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve models")

@app.post("/v1/chat/completions")
async def chat_completions(
    request: Request,
    authorization: Optional[str] = Header(None)
):
    """
    Main endpoint for chat completions (OpenAI-compatible).
    
    This endpoint accepts requests in OpenAI format and proxies them to Ollama.
    """
    # Validate API key
    api_key_info = None
    if authorization:
        api_key_info = validate_api_key(authorization)
        if not api_key_info:
            raise HTTPException(status_code=401, detail="Invalid API key")
    
    # Check rate limits
    if api_key_info:
        rate_ok, limit_info = check_rate_limit(
            api_key_info["key_id"], 
            rate_limit_config
        )
        if not rate_ok:
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded. Limits: {limit_info}"
            )
    
    # Parse request body
    try:
        request_data = await request.json()
        logger.info(f"Chat completion request: {request_data}")
    except Exception as e:
        logger.error(f"Failed to parse request JSON: {e}")
        raise HTTPException(status_code=400, detail="Invalid JSON payload")
    
    # Validate required fields
    if "model" not in request_data:
        raise HTTPException(status_code=400, detail="Missing required field: model")
    
    if "messages" not in request_data:
        raise HTTPException(status_code=400, detail="Missing required field: messages")
    
    # Process the chat completion request
    try:
        response = await ollama_client.chat_completion(
            model=request_data["model"],
            messages=request_data["messages"],
            temperature=request_data.get("temperature", 0.7),
            max_tokens=request_data.get("max_tokens"),
            stream=request_data.get("stream", False)
        )
        
        # Return in OpenAI-compatible format
        return response
        
    except Exception as e:
        logger.error(f"Chat completion failed: {e}")
        
        # Return OpenAI-style error
        error_response = {
            "error": {
                "message": str(e),
                "type": "api_error",
                "code": 500
            }
        }
        
        return JSONResponse(
            status_code=500,
            content=error_response
        )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Custom handler for HTTP exceptions to return OpenAI-style errors."""
    error_response = {
        "error": {
            "message": exc.detail,
            "type": "invalid_request_error" if exc.status_code < 500 else "api_error",
            "code": exc.status_code
        }
    }
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response
    )

if __name__ == "__main__":
    # Get configuration from environment variables
    host = os.getenv("GATEWAY_HOST", "0.0.0.0")
    port = int(os.getenv("GATEWAY_PORT", "8000"))
    
    logger.info(f"Starting server on {host}:{port}")
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info"
    )