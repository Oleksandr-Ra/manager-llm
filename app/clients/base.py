from abc import ABC, abstractmethod
from typing import Any


class BaseLLMClient(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> dict[str, Any]:
        """
        The method to generate text using the LLM client.
        """
        pass
