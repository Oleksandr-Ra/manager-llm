from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )
    openai_api_key: str
    openai_model: str = "gpt-4.1-mini"

    groq_api_key: str
    groq_model: str = "llama-3.3-70b-versatile"


settings = Settings()
