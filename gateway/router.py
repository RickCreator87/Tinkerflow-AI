"""
Main routing layer for the gateway. Routes requests to appropriate providers.
"""
import asyncio
from typing import Dict, Any, Optional
from .providers.base import Provider
from .providers.ollama import OllamaProvider
from .providers.openai import OpenAIProvider
from .providers.anthropic import AnthropicProvider
from ..config import load_config

class Router:
    def __init__(self):
        self.config = load_config('gateway')
        self.providers = self._init_providers()
        self.strategy = self.config.get('routing', {}).get('strategy', 'round_robin')
        self._round_robin_index = 0

    def _init_providers(self) -> Dict[str, Provider]:
        providers = {}
        provider_configs = self.config.get('providers', {})
        if 'ollama' in provider_configs:
            providers['ollama'] = OllamaProvider(provider_configs['ollama'])
        if 'openai' in provider_configs:
            providers['openai'] = OpenAIProvider(provider_configs['openai'])
        if 'anthropic' in provider_configs:
            providers['anthropic'] = AnthropicProvider(provider_configs['anthropic'])
        return providers

    async def route(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Route a request to the appropriate provider."""
        provider_name = self._select_provider(request)
        provider = self.providers.get(provider_name)
        if not provider:
            raise ValueError(f"Provider {provider_name} not configured")
        return await provider.complete(request)

    def _select_provider(self, request: Dict[str, Any]) -> str:
        """Select provider based on routing strategy."""
        if self.strategy == 'round_robin':
            provider_names = list(self.providers.keys())
            if not provider_names:
                raise RuntimeError("No providers available")
            selected = provider_names[self._round_robin_index % len(provider_names)]
            self._round_robin_index += 1
            return selected
        elif self.strategy == 'first_available':
            # try each provider in order until one works (simplified)
            return list(self.providers.keys())[0]
        else:
            return self.config.get('default_provider', 'ollama')
