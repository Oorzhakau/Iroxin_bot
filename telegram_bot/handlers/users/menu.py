import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.main_menu import main_menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    """Функция отображения кнопок меню."""
    await message.answer("Главное меню", reply_markup=main_menu)
    logging.info(f"Выполнение команды menu. User id {message.from_user.id}")
