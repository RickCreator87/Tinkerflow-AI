# tests/test_gateway.py
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi.testclient import TestClient
import json
from datetime import datetime
from gateway.main import app  # Assuming this is your main FastAPI app

client = TestClient(app)

def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "service" in data

def test_v1_chat_completions_missing_auth():
    """Test chat completions endpoint without authorization."""
    response = client.post("/v1/chat/completions", json={
        "model": "llama2",
        "messages": [{"role": "user", "content": "Hello"}]
    })
    assert response.status_code == 401
    assert "detail" in response.json()

@patch('gateway.main.httpx.AsyncClient.post')
def test_v1_chat_completions_success(mock_post):
    """Test successful chat completions request."""
    # Mock Ollama response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "model": "llama2",
        "message": {"role": "assistant", "content": "Hello there!"},
        "done": True
    }
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response
    
    response = client.post(
        "/v1/chat/completions",
        headers={"Authorization": "Bearer test-key"},
        json={
            "model": "llama2",
            "messages": [{"role": "user", "content": "Hello"}],
            "temperature": 0.7
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["object"] == "chat.completion"
    assert len(data["choices"]) == 1
    assert data["choices"][0]["message"]["content"] == "Hello there!"
    assert data["model"] == "llama2"

@patch('gateway.main.httpx.AsyncClient.post')
def test_v1_chat_completions_streaming(mock_post):
    """Test streaming chat completions."""
    # Mock streaming response from Ollama
    mock_response = MagicMock()
    mock_response.iter_lines.return_value = [
        '{"model":"llama2","message":{"role":"assistant","content":"Hello"},"done":false}',
        '{"model":"llama2","message":{"role":"assistant","content":" there"},"done":false}',
        '{"model":"llama2","done":true}'
    ]
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response
    
    response = client.post(
        "/v1/chat/completions",
        headers={"Authorization": "Bearer test-key"},
        json={
            "model": "llama2",
            "messages": [{"role": "user", "content": "Hello"}],
            "stream": True
        }
    )
    
    assert response.status_code == 200
    assert "text/event-stream" in response.headers.get("content-type", "")
    
    # Parse streaming response
    lines = response.text.strip().split('\n')
    assert len(lines) > 0
    for line in lines:
        if line.startswith("data: "):
            data = json.loads(line[6:])
            assert "choices" in data

def test_v1_models_endpoint():
    """Test the models endpoint."""
    response = client.get("/v1/models")
    assert response.status_code == 200
    data = response.json()
    assert data["object"] == "list"
    assert "data" in data

@patch('gateway.main.httpx.AsyncClient.post')
def test_request_validation_errors(mock_post):
    """Test various request validation scenarios."""
    # Test with missing messages
    response = client.post(
        "/v1/chat/completions",
        headers={"Authorization": "Bearer test-key"},
        json={"model": "llama2"}
    )
    assert response.status_code == 422  # Validation error
    
    # Test with empty messages
    response = client.post(
        "/v1/chat/completions",
        headers={"Authorization": "Bearer test-key"},
        json={"model": "llama2", "messages": []}
    )
    assert response.status_code == 422

@patch('gateway.main.httpx.AsyncClient.post')
def test_ollama_error_handling(mock_post):
    """Test handling of Ollama errors."""
    # Simulate Ollama 404 error
    mock_post.side_effect = Exception("Ollama service not available")
    
    response = client.post(
        "/v1/chat/completions",
        headers={"Authorization": "Bearer test-key"},
        json={
            "model": "llama2",
            "messages": [{"role": "user", "content": "Hello"}]
        }
    )
    
    assert response.status_code == 502  # Bad Gateway
    error_data = response.json()
    assert "error" in error_data

def test_api_key_validation():
    """Test different API key scenarios."""
    # Test invalid API key format
    response = client.post(
        "/v1/chat/completions",
        headers={"Authorization": "InvalidFormat"},
        json={"model": "llama2", "messages": [{"role": "user", "content": "Hello"}]}
    )
    assert response.status_code == 401
    
    # Test missing authorization header
    response = client.post(
        "/v1/chat/completions",
        json={"model": "llama2", "messages": [{"role": "user", "content": "Hello"}]}
    )
    assert response.status_code == 401
