"""Кнопка отмены в меню при заполнении заявки."""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌Отменить"),
        ],
    ],
    resize_keyboard=True,
)
