import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

<<<<<<< HEAD
from loader import dp
from utils.db_api import db_commands as commands
=======
from utils.db_api import db_commands as commands
from loader import dp
>>>>>>> 726a0b617a65e04458ebf848925a9db0276da33d


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
<<<<<<< HEAD
    """handler для запуска бота"""
=======
    '''handler для запуска бота'''
>>>>>>> 726a0b617a65e04458ebf848925a9db0276da33d
    chat_id = message.from_user.id
    logging.info(f"Бот активирован пользователем telegram id - {chat_id}")
    subscriber = await commands.get_subscriber(message.from_user.id)
    if not subscriber:
<<<<<<< HEAD
        subscriber = await commands.add_subscriber(
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
        )
        await message.answer(
            "\n".join(
                [
                    f"Здравствуйте, <b>{message.from_user.username}</b>!",
                    f'Вы были занесен в базу компании <b>"КоРус"</b>.',
                    f"Telegram id: <b>{subscriber.user_id}</b>",
                    f"Username: <b>{subscriber.username}</b>",
                    f"ФИО: <b>{subscriber.first_name} {subscriber.last_name}</b>",
                ]
            )
        )
        return
    await message.answer(f"Здравствуйте, <b>{message.from_user.username}</b>!")
=======
        subscriber = await commands.add_subscriber(user_id=message.from_user.id,
                                                   first_name=message.from_user.first_name,
                                                   last_name=message.from_user.last_name,
                                                   username=message.from_user.username)
        await message.answer(
            "\n".join(
                [
                    f'Здравствуйте, <b>{message.from_user.username}</b>!',
                    f'Вы были занесен в базу компании <b>"КоРус"</b>.',
                    f'Telegram id: <b>{subscriber.user_id}</b>',
                    f'Username: <b>{subscriber.username}</b>',
                    f'ФИО: <b>{subscriber.first_name} {subscriber.last_name}</b>',
                ]))
        return
    await message.answer(f'Здравствуйте, <b>{message.from_user.username}</b>!')
>>>>>>> 726a0b617a65e04458ebf848925a9db0276da33d
