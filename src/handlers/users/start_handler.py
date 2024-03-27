from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.keyboards import start_kb_builder


start_router = Router()


@start_router.message(CommandStart())
async def start_message(message: Message):
    builder = start_kb_builder()
    await message.answer(
        f'Добрый день, {hbold(message.from_user.full_name)}!',
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
