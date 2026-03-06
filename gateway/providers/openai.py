import aiohttp
from .base import Provider
from typing import Dict, Any

class OpenAIProvider(Provider):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config['api_key']
        self.model = config.get('model', 'gpt-4')
        self.timeout = config.get('timeout', 30)

    async def complete(self, request: Dict[str, Any]) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": request.get("prompt", "")}],
            **request.get("options", {})
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=self.timeout
            ) as resp:
                resp.raise_for_status()
                return await resp.json()
