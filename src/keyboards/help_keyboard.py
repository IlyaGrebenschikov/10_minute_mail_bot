from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def help_keyboard() -> ReplyKeyboardMarkup:
    kb = [
            [KeyboardButton(text='/help')]
        ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        is_persistent=True,
    )

    return keyboard
