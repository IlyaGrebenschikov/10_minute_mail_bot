import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from src.core import get_settings
from src.handlers.users import start_router


async def main():
    bot = Bot(
        get_settings().bot.TOKEN,
        default=DefaultBotProperties(parse_mode=get_settings().bot.PARSE_MODE)
    )
    dp = Dispatcher()
    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
