from aiogram.dispatcher.filters.state import StatesGroup, State


class RequestState(StatesGroup):
    email = State()
    name = State()
    phone = State()
