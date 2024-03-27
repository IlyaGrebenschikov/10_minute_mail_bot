from aiogram import Router

from src.handlers.users.start_handler import start_router
from src.handlers.users.help_handler import help_router


users_router = Router()
users_router.include_router(start_router)
users_router.include_router(help_router)
