import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from core.settings import get_settings
from handlers.users.routers import users_router


async def main():
    settings = get_settings()
    bot = Bot(
        settings.bot.TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=settings.bot.PARSE_MODE)
    )
    dp = Dispatcher()
    dp.include_router(users_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
