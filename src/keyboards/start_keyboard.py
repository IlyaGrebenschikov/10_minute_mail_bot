from aiogram.utils.keyboard import ReplyKeyboardBuilder

from .buttons.help_button import help_button


def start_kb_builder() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    help_kb = help_button()
    builder.attach(ReplyKeyboardBuilder.from_markup(help_kb))
    return builder
