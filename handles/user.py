from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from database.repo import UserRepository
from database.db import session

user = Router()

# обработчики для юзера

@user.message(CommandStart())
async def hello(message: Message):
    r = UserRepository(session())
    user = await r.select(message.from_user.id) # type: ignore
    if not user:
        await r.create(message.from_user.id, message.from_user.username) # type: ignore
    await r.close()
    await message.answer('Приветствую в нашем боте ИИ!')
