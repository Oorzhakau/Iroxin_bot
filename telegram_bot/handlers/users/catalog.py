from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, MediaGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
import re
import logging

from keyboards.default.main_menu import main_menu
from keyboards.default.cancel_menu import cancel_menu
from utils.db_api import db_commands as commands
from utils.misc.send_request import send_data_to_form
from states.request import RequestState
from data.config import ADMINS, GROUP
from loader import dp


@dp.message_handler(Text(startswith="Каталог"))
async def get_catalog(message: Message):
    """Функция отправки каталога пользователю."""
    
    await message.answer_media_group(media=album)


products = await commands.get_all_products()
root_path = '/src'
for product in products:
    album = MediaGroup()
    logging.info(product.image.url)
    logging.info(product.image_size.url)
    album.attach_photo(photo=InputFile(root_path+product.image.url))
    album.attach_photo(
        photo=InputFile(root_path+product.image_size.url),
        caption='\n'.join([
            f"<b>{product.title}</b>",
            f"{product.description}",
            f"\n{product.about}",
            ])
    )