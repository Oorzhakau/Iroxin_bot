import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto, Message

from loader import dp
from utils.db_api import db_commands as commands
from utils.misc.pagination import get_pages_keyboard, pagination_call


@dp.message_handler(Text(startswith="Каталог"))
async def get_catalog(message: Message):
    """Функция отправки каталога пользователю."""
    root_path = "/src"
    products = list(await commands.get_all_products())
    if products is not None:
        await message.answer_photo(
            photo=InputFile(root_path + products[0].image.url),
            caption="\n".join(
                [
                    f"<b>{products[0].title}</b>",
                    f"{products[0].description}",
                    f"\n{products[0].about}",
                ]
            ),
            reply_markup=get_pages_keyboard(products),
        )


@dp.callback_query_handler(pagination_call.filter(key="items"))
async def show_chosen_page(call: CallbackQuery, callback_data: dict):
    await call.answer()
    products = list(await commands.get_all_products())
    root_path = "/src"
    current_page = int(callback_data.get("page"))
    current_ind = current_page - 1
    photo = InputMediaPhoto(
        InputFile(root_path + products[current_ind].image.url)
    )
    text = "\n".join(
        [
            f"<b>{products[current_ind].title}</b>",
            f"{products[current_ind].description}",
            f"\n{products[current_ind].about}",
        ]
    )
    markup = get_pages_keyboard(products, page=current_page)
    await call.message.edit_media(
        media=photo,
        reply_markup=markup,
    )
    await call.message.edit_caption(
        caption=text,
        reply_markup=markup,
    )
