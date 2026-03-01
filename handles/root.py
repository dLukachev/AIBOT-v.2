from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from utils.keyboard import start_keyboard, return_to_start

root = Router()

# тут управление рута