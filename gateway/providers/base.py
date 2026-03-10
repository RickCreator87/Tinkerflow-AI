
gateway/providers/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any

class Provider(ABC):
    """Base class for all LLM providers."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    async def complete(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send a completion request to the provider."""
        pass
