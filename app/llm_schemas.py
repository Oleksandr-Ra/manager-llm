from typing import Any

from pydantic import BaseModel, Field


class GenerationRequest(BaseModel):
    client_name: str = Field(example="Choose model: 'mock', 'openai', 'groq'")
    prompt: str = Field(min_length=1, example="Text prompt for LLM")
    temperature: float = 0.7


class GenerationResponse(BaseModel):
    result: dict[str, Any]
