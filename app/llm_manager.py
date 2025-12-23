from clients.base import BaseLLMClient
from clients.groq import GroqClient
from clients.mock import MockLLMClient
from clients.openai import OpenAIClient


class LLMFactory:
    def __init__(self):
        self._creators: dict[str, type[BaseLLMClient]] = {}

    def register_client(self, name: str, client_class: type[BaseLLMClient]):
        """New client class registration"""
        self._creators[name.lower()] = client_class

    def get_client(self, name: str) -> BaseLLMClient:
        """Receiving an instance of the client by name"""
        client_class = self._creators.get(name.lower())
        if not client_class:
            raise ValueError(
                f"Client '{name}' not found. Available: {list(self._creators.keys())}"
            )
        return client_class()


llm_factory = LLMFactory()

llm_factory.register_client(name="mock", client_class=MockLLMClient)
llm_factory.register_client(name="openai", client_class=OpenAIClient)
llm_factory.register_client(name="groq", client_class=GroqClient)
