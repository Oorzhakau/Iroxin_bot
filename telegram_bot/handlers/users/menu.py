<<<<<<< HEAD
import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.main_menu import main_menu
=======
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, MediaGroup
from aiogram.dispatcher import FSMContext
import re
import logging

from keyboards.default.main_menu import main_menu
from utils.db_api import db_commands as commands
from utils.misc.send_request import send_data_to_form
from states.request import RequestState
from data.config import ADMINS, GROUP
>>>>>>> 726a0b617a65e04458ebf848925a9db0276da33d
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    """Функция отображения кнопок меню."""
    await message.answer("Главное меню", reply_markup=main_menu)
<<<<<<< HEAD
    logging.info(f"Выполнение команды menu. User id {message.from_user.id}")
=======


@dp.message_handler(Text(startswith="Каталог"))
async def get_catalog(message: Message):
    """Функция отправки каталога пользователю."""
    products = await commands.get_all_products()
    MEDIA_ROOT = 'media/'
    for product in products:
        print(MEDIA_ROOT+product.get_absolute_url)
        print(MEDIA_ROOT+product.get_absolute_url)
        album = MediaGroup()
        album.attach_photo(photo=MEDIA_ROOT+product.get_absolute_url)
        album.attach_photo(photo=MEDIA_ROOT+product.get_absolute_url,
                           caption=f"<b>{product.title}<b>."+
                                   f"<code>\n{product.description}</code>")
        await message.answer_media_group(media=album)


@dp.message_handler(Text(startswith="Оставить заявку"))
async def start_application(message: Message):
    await message.answer(f"Введите адрес электронной почты")
    await RequestState.email.set()


@dp.message_handler(state=RequestState.email)
async def get_email(message: Message, state: FSMContext):
    """Получение электронной почты для заявки."""
    email = message.text
    pattern = re.compile('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(pattern, email):
        await message.reply("Введен некорректный email. Повторите попытку")
        state.previous()
    await state.update_data(email=email)
    await message.answer("Введите ваше имя")
    await RequestState.next()


@dp.message_handler(state=RequestState.name)
async def get_name(message: Message, state: FSMContext):
    """Получение имени для заявки."""
    name = message.text
    pattern = re.compile('[А-Яа-яЁёA-Za-z ]+')
    if not re.fullmatch(pattern, name):
        await message.reply("Повторите попытку ввода имени")
        state.previous()
    await state.update_data(name=name)
    await message.answer("Введите номер телефона (+7XXXXXXXXXX)")
    await RequestState.next()


@dp.message_handler(state=RequestState.phone)
async def get_phone(message: Message, state: FSMContext):
    """Получение номера телефона для заявки."""
    chat_id = message.from_user.id
    data = await state.get_data()
    email = data.get("email")
    name = data.get("name")
    phone = message.text
    pattern = re.compile('\+7([0-9]){10}')
    if not re.fullmatch(pattern, phone):
        await message.reply("Введите номер согласно шаблону (+7XXXXXXXXXX)")
        state.previous()
    await message.answer(f"Спасибо за ваши ответы! Заявка отправлена!\n"
                         f"Наш менеджер свяжется с вами в ближайшее время.")
    subscriber = await commands.get_subscriber(message.from_user.id)
    if not subscriber:
        subscriber = await commands.add_subscriber(user_id=message.from_user.id,
                                                   username=message.from_user.username,
                                                   first_name=name,
                                                   email=email,
                                                   phone=phone,
                                                   )
    else:
        if not subscriber.first_name:
            subscriber.first_name=name
        if not subscriber.email:
            subscriber.email=email
        if not subscriber.phone:
            subscriber.phone=phone
        subscriber.save()
    await dp.bot.send_message(
        chat_id=int(GROUP),
        text='\n'.join([
                        f"✉️ Заявка от:",
                        f"Имя: {name}",
                        f"Email: {email}",
                        f"Phone: {phone}",
                        ])
    )
    # send_data_to_form(email=email, name=name, phone=phone)
    await state.finish()
    logging.info(f"Заявка оформлена и отправлена.")

>>>>>>> 726a0b617a65e04458ebf848925a9db0276da33d
