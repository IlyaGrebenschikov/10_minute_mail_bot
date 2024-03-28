from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards import start_kb_builder
from src.fsm import MailForm
from src.filters import CanlelFilter


mail_router = Router()


@mail_router.message(Command("cancel"))
@mail_router.message(CanlelFilter())
async def cancel_handler(message: Message, state: FSMContext) -> None | str:
    current_state = await state.get_state()

    if current_state is None:
        await message.answer(
            'You are not logged into the state machine.',
            reply_markup=start_kb_builder().as_markup(resize_keyboard=True),
        )
        return

    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=start_kb_builder().as_markup(resize_keyboard=True),
    )
