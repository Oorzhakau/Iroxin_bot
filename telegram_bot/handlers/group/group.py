import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from data.config import ADMINS

from loader import dp


@dp.message_handler(Command("chat_id"), user_id=ADMINS)
async def get_chat_id_group(message: Message):
    """Команда /chat_id для того, чтобы узнать chat id группы."""
    chat_id = message.chat.id
    await message.answer(f"Group ID - {chat_id}")
    logging.info("Сообщение о chat id группы отправлено")
