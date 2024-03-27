from functools import lru_cache
from pathlib import Path
from typing import Final


from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, SecretStr


ROOT_DIR: DirectoryPath = Path(__file__).parent.parent.parent


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f'{ROOT_DIR}/.env',
        env_file_encoding='utf-8',
    )

    TOKEN: SecretStr

    REDIS_URL: str
    REDIS_PORT: str
    REDIS_HOST: str


class BotSettings(EnvSettings):
    TOKEN: SecretStr
    PARSE_MODE: ParseMode | str = ParseMode.HTML


class RedisSettings(EnvSettings):
    @property
    def get_url(self) -> str:
        return self.REDIS_URL.format(
            REDIS_HOST=self.REDIS_HOST,
            REDIS_PORT=self.REDIS_PORT,
        )

    TIMER: Final[int] = 600


class Settings:
    bot: BotSettings = BotSettings()
    redis: RedisSettings = RedisSettings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
