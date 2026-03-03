# tests/conftest.py
import pytest
import asyncio
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
import os
from gateway.main import app

@pytest.fixture
def client():
    """Fixture to provide a test client."""
    return TestClient(app)

@pytest.fixture
def sample_openai_request():
    """Fixture providing a sample OpenAI format request."""
    return {
        "model": "llama2",
        "messages": [
            {"role": "user", "content": "Hello, how are you?"}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

@pytest.fixture
def sample_ollama_response():
    """Fixture providing a sample Ollama format response."""
    return {
        "model": "llama2",
        "message": {
            "role": "assistant",
            "content": "I'm doing well, thank you for asking!"
        },
        "done": True,
        "total_duration": 1234567890
    }

@pytest.fixture
def mock_ollama_response():
    """Fixture to mock Ollama responses."""
    with patch('gateway.main.httpx.AsyncClient.post') as mock_post:
        mock_response = AsyncMock()
        mock_response.json.return_value = {
            "model": "llama2",
            "message": {"role": "assistant", "content": "Mocked response"},
            "done": True
        }
        mock_response.raise_for_status.return_value = None
        mock_response.iter_lines.return_value = []
        mock_post.return_value = mock_response
        yield mock_post

@pytest.fixture
def valid_api_key():
    """Fixture providing a valid API key."""
    return "sk-test-valid-key-123"

@pytest.fixture
def auth_headers(valid_api_key):
    """Fixture providing authentication headers."""
    return {"Authorization": f"Bearer {valid_api_key}"}

# Async test support
@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for session scope."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

# Environment setup
@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment variables."""
    old_env = os.environ.copy()
    os.environ["OLLAMA_HOST"] = "http://localhost:11434"
    os.environ["API_KEYS"] = "sk-test-valid-key-123,sk-llama2-key,sk-mistral-key"
    yield
    os.environ.clear()
    os.environ.update(old_env)
