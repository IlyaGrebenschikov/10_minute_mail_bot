from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.keyboards.buttons import help_button


def start_kb_builder() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    help_kb = help_button()
    builder.attach(ReplyKeyboardBuilder.from_markup(help_kb))
    return builder
