# tests/test_auth.py
import pytest
from gateway.main import validate_api_key, extract_api_key

def test_extract_api_key_valid():
    """Test extraction of valid API key from header."""
    # Test Bearer token
    header = "Bearer sk-1234567890abcdef"
    key = extract_api_key(header)
    assert key == "sk-1234567890abcdef"
    
    # Test API key without Bearer
    header = "sk-1234567890abcdef"
    key = extract_api_key(header)
    assert key == "sk-1234567890abcdef"

def test_extract_api_key_invalid():
    """Test extraction with invalid headers."""
    assert extract_api_key("") is None
    assert extract_api_key(None) is None
    assert extract_api_key("Invalid Format") is None

def test_validate_api_key():
    """Test API key validation logic."""
    # Test valid key
    assert validate_api_key("sk-1234567890abcdef") is True
    
    # Test invalid keys
    assert validate_api_key("") is False
    assert validate_api_key(None) is False
    assert validate_api_key("invalid-key") is False
    
    # Test key with model mapping (if implemented)
    assert validate_api_key("sk-llama2-model") is True

@pytest.mark.parametrize("api_key,expected", [
    ("sk-llama2-prod", True),
    ("sk-mistral-dev", True),
    ("", False),
    (None, False),
    ("invalid", False),
])
def test_api_key_parametrized(api_key, expected):
    """Parametrized test for API key validation."""
    result = validate_api_key(api_key)
    assert result == expected

def test_api_key_model_mapping():
    """Test that API keys map to correct models."""
    # Assuming API keys contain model names
    test_cases = [
        ("sk-llama2-key", "llama2"),
        ("sk-mistral-key", "mistral"),
        ("sk-codellama-key", "codellama"),
    ]
    
    for api_key, expected_model in test_cases:
        # This would depend on your actual implementation
        model = extract_model_from_key(api_key)  # You need to implement this
        assert model == expected_model
