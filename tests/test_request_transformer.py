# tests/test_request_transformer.py
import pytest
from gateway.main import transform_openai_to_ollama, transform_ollama_to_openai

def test_transform_openai_to_ollama_basic():
    """Test basic OpenAI to Ollama transformation."""
    openai_request = {
        "model": "llama2",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    ollama_request = transform_openai_to_ollama(openai_request)
    
    assert ollama_request["model"] == "llama2"
    assert ollama_request["options"]["temperature"] == 0.7
    assert "prompt" in ollama_request or "messages" in ollama_request
    assert "stream" in ollama_request

def test_transform_openai_to_ollama_with_stream():
    """Test transformation with streaming enabled."""
    openai_request = {
        "model": "llama2",
        "messages": [{"role": "user", "content": "Hello"}],
        "stream": True
    }
    
    ollama_request = transform_openai_to_ollama(openai_request)
    assert ollama_request["stream"] is True

def test_transform_ollama_to_openai_basic():
    """Test basic Ollama to OpenAI transformation."""
    ollama_response = {
        "model": "llama2",
        "message": {"role": "assistant", "content": "Hello there!"},
        "done": True,
        "total_duration": 1500000000
    }
    
    openai_response = transform_ollama_to_openai(ollama_response)
    
    assert openai_response["object"] == "chat.completion"
    assert openai_response["model"] == "llama2"
    assert len(openai_response["choices"]) == 1
    assert openai_response["choices"][0]["message"]["content"] == "Hello there!"
    assert openai_response["choices"][0]["finish_reason"] == "stop"

def test_transform_ollama_to_openai_streaming():
    """Test streaming response transformation."""
    ollama_chunk = {
        "model": "llama2",
        "message": {"role": "assistant", "content": "Hello"},
        "done": False
    }
    
    openai_chunk = transform_ollama_to_openai(ollama_chunk, stream=True)
    
    assert openai_chunk["object"] == "chat.completion.chunk"
    assert len(openai_chunk["choices"]) == 1
    assert openai_chunk["choices"][0]["delta"]["content"] == "Hello"

def test_transform_with_system_message():
    """Test handling of system messages."""
    openai_request = {
        "model": "llama2",
        "messages": [
            {"role": "system", "content": "You are a pirate. Talk like one."},
            {"role": "user", "content": "Hello there!"}
        ]
    }
    
    ollama_request = transform_openai_to_ollama(openai_request)
    # Verify system message is properly incorporated
    assert "system" in str(ollama_request.get("prompt", "")) or \
           any(msg.get("role") == "system" for msg in ollama_request.get("messages", []))

@pytest.mark.parametrize("temperature", [0.0, 0.5, 1.0, 2.0])
def test_temperature_transformation(temperature):
    """Test temperature parameter transformation."""
    openai_request = {
        "model": "llama2",
        "messages": [{"role": "user", "content": "Hello"}],
        "temperature": temperature
    }
    
    ollama_request = transform_openai_to_ollama(openai_request)
    assert ollama_request.get("options", {}).get("temperature") == temperature
