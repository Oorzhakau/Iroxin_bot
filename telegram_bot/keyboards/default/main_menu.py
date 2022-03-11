from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог 📁"),
            KeyboardButton(text="Оставить заявку ✉️"),
        ],
        [
            KeyboardButton(text="О нас 👨‍⚕️"),
        ]
    ],
    resize_keyboard=True
)
