from typing import Annotated

from email import message
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from fast_depends import Depends, inject
from redis import Redis

from database.markers.redis import redis_marker
from keyboards.start_keyboard import start_kb_builder
from fsm.mail_fsm import MailForm
from filters.mail_filters import CanlelFilter
from mail_client.client import MailClient
from database.redis.redis_connect import redis_get_session


mail_router = Router()


@mail_router.message(Command('cancel'))
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


@mail_router.message(Command('create_user'))
@inject
async def create_user(
    message: Message,
    redis_client: Annotated[redis_get_session, Depends(redis_marker)],
    mail_client: Annotated[MailClient, Depends(MailClient)]
    ):
    account = await mail_client.create_account()
    token = await mail_client.create_token(account)
    await redis_client.set(f'{message.from_user.id}', f'{token}')
    await message.answer('User created')
