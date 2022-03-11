from aiogram.dispatcher.filters import Text
from aiogram.types import Message
import logging

from loader import dp


@dp.message_handler(Text(startswith="О нас"))
async def about_us(message: Message):
    text = '\n'.join([
        "💉Компания <b>«КоРус»</b> работает с 2013 года и за это время "+
        "зарекомендовала себя как надежный партнер.\n",
        "👨‍⚕️ 📞 В компании работают опытные и грамотные менеджеры, "+
        "которые владеют, информацией о продукции на уровне врача и "+
        "всегда помогут с выбором продукции.\n",
        "📖Мы регулярно проводим выездные региональные мастер-классы "+
        "и семинары для наших клиентов.\n",
        "В портфеле компании, на сегодняшний день, ряд производителей "+
        "и продуктов, которые могут заинтересовать любого потребителя.\n",
        "Вебсайт: https://smart.iroxin.ru/",
    ])
    logging.info(text)
    await message.answer(text=text)
