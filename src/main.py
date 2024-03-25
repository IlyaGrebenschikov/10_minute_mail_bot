import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from src.core import get_settings


async def main():
    token = get_settings().bot.TOKEN
    parse_mode = get_settings().bot.PARSE_MODE

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp = Dispatcher()
    bot = Bot(token, default=DefaultBotProperties(parse_mode=parse_mode))

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
