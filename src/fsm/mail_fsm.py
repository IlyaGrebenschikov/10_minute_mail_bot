from aiogram.fsm.state import StatesGroup, State


class MailForm(StatesGroup):
    is_active = State()
    new_account = State()
