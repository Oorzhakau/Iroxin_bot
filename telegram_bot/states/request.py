from aiogram.dispatcher.filters.state import State, StatesGroup


class RequestState(StatesGroup):
    """Класс машины состояния для оформления заявки."""
    email = State()
    name = State()
    phone = State()
