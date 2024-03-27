from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.keyboards import help_keyboard


start_router = Router()


@start_router.message(CommandStart())
async def start_message(message: Message):
    help_kb = help_keyboard()
    await message.answer(
        f'Добрый день, {hbold(message.from_user.full_name)}!',
        reply_markup=help_kb,   # todo Создать keyboard bilder, чтобы регать все кнопки
    )
