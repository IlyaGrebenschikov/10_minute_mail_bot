from pathlib import Path
from typing import Final

from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath


ROOT_DIR: DirectoryPath = Path(__file__).parent.parent.parent


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f'{ROOT_DIR}/.env',
        env_file_encoding='utf-8',
    )
    TOKEN: Final[str]
    PARSE_MODE: ParseMode = ParseMode.HTML


class Settings:
    bot: BotSettings = BotSettings()


def get_settings() -> Settings:
    return Settings()
