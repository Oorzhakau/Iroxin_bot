from aiogram.dispatcher.filters.state import State, StatesGroup


class RequestState(StatesGroup):
    email = State()
    name = State()
    phone = State()
