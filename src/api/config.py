from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    anthropic_api_key: str
    app_name: str = "FDE Portfolio"
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env")
