from typing import Any

from config import settings
from openai import APIError, AsyncOpenAI

from .base import BaseLLMClient


class GroqClient(BaseLLMClient):
    def __init__(self):
        # Groq uses OpenAI format, but a different URL
        self.client = AsyncOpenAI(
            api_key=settings.groq_api_key, base_url="https://api.groq.com/openai/v1"
        )
        self.model = settings.groq_model

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
                "model": response.model,
                "provider": "groq",
            }
        except APIError as e:
            return {
                "status": "error",
                "error_type": "provider_error",
                "message": f"Groq error: {e.message}",
            }
        except Exception as e:
            return {
                "status": "error",
                "error_type": "internal_error",
                "message": str(e),
            }
