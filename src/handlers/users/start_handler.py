from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold


start_router = Router()


@start_router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(
        f'Добрый день, {hbold(message.from_user.full_name)}!'
    )
