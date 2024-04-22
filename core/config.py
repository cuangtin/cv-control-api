import secrets

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = "CV Collection"
    API_V1_STR: str = "/api/v1"
    MONGODB_HOST: str ="localhost"
    MONGODB_PORT: int = 27017
    DOMAIN: str ="localhost"

    @computed_field  # type: ignore[misc]
    @property
    def server_host(self) -> str:
        # Use HTTPS for anything other than local development
        return f"https://{self.DOMAIN}"


settings = Settings()  # type: ignore
