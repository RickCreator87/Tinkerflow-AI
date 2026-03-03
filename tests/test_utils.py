# tests/test_utils.py
import pytest
import time
from gateway.main import rate_limit_check, format_error_response

def test_rate_limit_check():
    """Test rate limiting functionality."""
    # Test within limit
    for i in range(5):
        allowed, remaining = rate_limit_check("test-key", "llama2")
        assert allowed is True
        assert remaining > 0
    
    # This would depend on your actual rate limit implementation
    # You might need to mock time or use a test rate limiter

def test_format_error_response():
    """Test error response formatting."""
    error_msg = "Model not found"
    status_code = 404
    
    response = format_error_response(error_msg, status_code)
    
    assert response["error"]["message"] == error_msg
    assert response["error"]["type"] == "invalid_request_error"
    assert response["error"]["code"] == "model_not_found"
    assert response["error"]["param"] is None

@pytest.mark.parametrize("error_type,expected_code", [
    ("not_found", "not_found"),
    ("rate_limit", "rate_limit_exceeded"),
    ("invalid_request", "invalid_request_error"),
    ("server_error", "server_error"),
])
def test_format_error_parametrized(error_type, expected_code):
    """Parametrized test for error formatting."""
    response = format_error_response(f"Test {error_type} error", 400, error_type)
    assert response["error"]["code"] == expected_code

def test_request_timing():
    """Test request timing measurement."""
    # This would test any timing/logging decorators you have
    pass
