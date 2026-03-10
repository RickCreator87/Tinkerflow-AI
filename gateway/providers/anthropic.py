import aiohttp
from .base import Provider
from typing import Dict, Any

class AnthropicProvider(Provider):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config['api_key']
        self.model = config.get('model', 'claude-3-opus-20240229')
        self.timeout = config.get('timeout', 30)

    async def complete(self, request: Dict[str, Any]) -> Dict[str, Any]:
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": request.get("prompt", "")}],
            "max_tokens": request.get("options", {}).get("max_tokens", 1024)
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=payload,
                timeout=self.timeout
            ) as resp:
                resp.raise_for_status()
                return await resp.json()
