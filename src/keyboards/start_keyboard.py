from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.keyboards import help_keyboard


def start_kb_builder() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    help_kb = help_keyboard()
    builder.attach(ReplyKeyboardBuilder.from_markup(help_kb))
    return builder
