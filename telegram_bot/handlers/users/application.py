import logging
import re

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from data.config import GROUP

from keyboards.default.cancel_menu import cancel_menu
from loader import dp
from states.request import RequestState
from utils.db_api import db_commands as commands
from utils.misc.send_request import send_data_to_form


@dp.message_handler(Text(startswith="❌Отменить"), state="*")
async def cancel_application(message: Message, state: FSMContext):
    """Реализация функции кнопки отмены."""
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(
        f"Подача заявки отменена.",
        reply_markup=ReplyKeyboardRemove(),
    )
    logging.info("Отмена на этапе %r", current_state)


@dp.message_handler(Text(startswith="Оставить заявку"))
async def start_application(message: Message):
    """Начало формирования заявки. Инициализация состояния email."""
    await message.answer(f"Введите адрес электронной почты")
    await RequestState.email.set()


@dp.message_handler(state=RequestState.email)
async def get_email(message: Message, state: FSMContext):
    """Получение электронной почты для заявки."""
    email = message.text
    pattern = re.compile(
        "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    if not re.fullmatch(pattern, email):
        await message.answer(
            "Введен некорректный email. Повторите попытку "
            + "или отмените заявку.",
            reply_markup=cancel_menu,
        )
        return
    await state.update_data(email=email)
    await message.answer(
        "Введите ваше имя",
        reply_markup=cancel_menu,
    )
    await RequestState.next()


@dp.message_handler(state=RequestState.name)
async def get_name(message: Message, state: FSMContext):
    """Получение имени для заявки."""
    name = message.text
    pattern = re.compile("[А-Яа-яЁёA-Za-z ]+")
    if not re.fullmatch(pattern, name):
        await message.reply(
            "Повторите попытку ввода имени " + "или отмените подачу заявки.",
            reply_markup=cancel_menu,
        )
        return
    await state.update_data(name=name)
    await message.answer(
        "Введите номер телефона (+7XXXXXXXXXX)",
        reply_markup=cancel_menu,
    )
    await RequestState.next()


@dp.message_handler(state=RequestState.phone)
async def get_phone(message: Message, state: FSMContext):
    """Получение номера телефона для заявки."""
    data = await state.get_data()
    email = data.get("email")
    name = data.get("name")
    phone = message.text
    pattern = re.compile("\+7([0-9]){10}")
    if not re.fullmatch(pattern, phone):
        await message.reply(
            "Некорректно указан номер. Введите согласно шаблону +7XXXXXXXXXX\n"
            + "или отмените подачу заявки.",
            reply_markup=cancel_menu,
        )
        return
    await message.answer(
        text=f"Спасибо за ваши ответы! Заявка отправлена!\n"
        + f"Наш менеджер свяжется с вами в ближайшее время.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await commands.get_then_update(
        user_id=message.from_user.id, name=name, email=email, phone=phone
    )
    await dp.bot.send_message(
        chat_id=int(GROUP),
        text="\n".join(
            [
                f"✉️ Заявка от:",
                f"Имя: {name}",
                f"Email: {email}",
                f"Phone: {phone}",
            ]
        ),
    )
    # send_data_to_form(email=email, name=name, phone=phone)
    await state.finish()
    logging.info(f"Заявка оформлена и отправлена.")
