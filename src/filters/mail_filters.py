from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


class CanlelFilter(Filter):
    def __init__(self):
        self.text = 'cancel'

    async def __call__(self, message: Message, state: FSMContext) -> bool:
        return message.text == self.text
