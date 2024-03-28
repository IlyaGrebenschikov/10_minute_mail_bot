from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.keyboards import start_kb_builder


help_router = Router()


@help_router.message(Command('help'))
async def start_message(message: Message):
    await message.answer(
        'This is 10 minute mail bot.\n'
        'This bot allows you to create an account and receive messages.\n'
        f'Bot lifespan is {hbold("10 minutes")}.',
        reply_markup=start_kb_builder().as_markup(resize_keyboard=True),
    )
