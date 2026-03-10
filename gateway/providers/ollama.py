providers/ollama.py

import aiohttp
from .base import Provider
from typing import Dict, Any

class OllamaProvider(Provider):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.base_url = config.get('base_url', 'http://localhost:11434')
        self.model = config.get('model', 'llama3')
        self.timeout = config.get('timeout', 30)

    async def complete(self, request: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "model": self.model,
            "prompt": request.get("prompt", ""),
            "stream": False,
            **request.get("options", {})
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=self.timeout
            ) as resp:
                resp.raise_for_status()
                return await resp.json()
