from typing import Any

from config import settings
from openai import APIError, AsyncOpenAI

from .base import BaseLLMClient


class OpenAIClient(BaseLLMClient):
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    async def generate(self, prompt: str, **kwargs) -> dict[str, Any]:
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=kwargs.get("temperature", 0.7),
            )
            return {
                "status": "success",
                "content": response.choices[0].message.content,
                "usage": response.usage.model_dump() if response.usage else {},
                "model": response.model,
            }
        except APIError as e:
            return {
                "status": "error",
                "error_type": "provider_error",
                "message": f"OpenAI API returned an error: {e.message}",
            }
        except Exception as e:
            return {
                "status": "error",
                "error_type": "internal_error",
                "message": str(e),
            }
