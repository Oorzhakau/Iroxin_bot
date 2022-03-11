"""Главное меню бота."""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог 📁"),
            KeyboardButton(text="Оставить заявку ✉️"),
        ],
        [
            KeyboardButton(text="О нас 👨‍⚕️"),
        ],
    ],
    resize_keyboard=True,
)
