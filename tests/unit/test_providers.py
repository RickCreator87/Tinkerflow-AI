tests/unit/test_providers.py

```python
import pytest
from gateway.providers.ollama import OllamaProvider
from gateway.providers.openai import OpenAIProvider

@pytest.mark.asyncio
async def test_ollama_provider():
    config = {"base_url": "http://localhost:11434", "model": "llama3"}
    provider = OllamaProvider(config)
    # Mock aiohttp session
    # ...
```
