from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌Отменить"),
        ],
    ],
    resize_keyboard=True
)
