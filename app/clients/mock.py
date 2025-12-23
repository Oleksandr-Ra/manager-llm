import asyncio
from typing import Any

from .base import BaseLLMClient


class MockLLMClient(BaseLLMClient):
    async def generate(self, prompt: str, **kwargs) -> dict[str, Any]:
        await asyncio.sleep(0.5)

        return {
            "message": "This is a mock response from the Mock client.",
            "original_prompt": prompt,
            "status": "success",
        }
