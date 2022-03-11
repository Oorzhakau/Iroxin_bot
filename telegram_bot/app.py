"""Запуск приложения телеграмм бота. Опрос сервера методом пулинга"""

from aiogram import executor


from loader import dp


def setup_django():
    import os
    import sys
    import django

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, 'django_project')
    sys.path.append(DATA_PATH)

    os.environ['DJANGO_SETTINGS_MODULE'] = "django_project.settings"
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


async def on_startup(dispatcher):
    from utils.notify_admins import on_startup_notify
    from utils.set_bot_commands import set_default_commands
    from utils.db_api import db_commands as commands

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомление о запуске бота
    await on_startup_notify(dispatcher)


if __name__ == "__main__":
    setup_django()

    import middlewares
    import filters
    import handlers
    executor.start_polling(dp, on_startup=on_startup)
