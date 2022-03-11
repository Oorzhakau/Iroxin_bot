import logging

from aiogram.utils.exceptions import (CantParseEntities, MessageNotModified,
                                      TelegramAPIError)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, MessageNotModified):
        logging.exception("Message is not modified")
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f"CantParseEntities: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f"TelegramAPIError: {exception} \nUpdate: {update}")
        return True

    logging.exception(f"Update: {update} \n{exception}")
