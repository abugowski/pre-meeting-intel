from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    anthropic_api_key: str
    tavily_api_key: str
    app_name: str = "pre-meeting-intel"
    debug: bool = False
    briefing_system_prompt: str
    briefing_user_prompt: str
    briefing_user_industry_prompt: str
    briefing_user_person_prompt: str
    briefing_user_bio_prompt: str
    briefing_user_technology_prompt: str
    agent_system_prompt: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
