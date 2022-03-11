"""
Инициализация бота bot, машины состояния storage и диспетчера dp
"""

import os
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

DATA_DIR = os.path.join(Path(__file__).parents[1])
sys.path.append(DATA_DIR)

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
