from aiogram import Router

from .start_handler import start_router
from .help_handler import help_router
from .mail_handlers import mail_router


users_router = Router()
users_router.include_router(start_router)
users_router.include_router(help_router)
users_router.include_router(mail_router)
