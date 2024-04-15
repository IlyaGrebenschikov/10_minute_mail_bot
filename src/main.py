import asyncio
import logging
import sys

from fast_depends import dependency_provider
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties


from database.redis.redis_connect import redis_get_session
from database.markers.redis import redis_marker
from core.settings import get_settings
from handlers.users.routers import users_router


async def main():
    settings = get_settings()
    dependency_provider.override(redis_marker, redis_get_session)
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
