import logging

from aiogram.utils.exceptions import (CantParseEntities, MessageNotModified,
                                      TelegramAPIError)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """Error handler перехватывающий все исключения."""

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
