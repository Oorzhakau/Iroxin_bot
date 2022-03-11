"""Задание базовых конфигурация для логгирования."""

import logging

logging.basicConfig(
    level=logging.INFO,
    format=" %(asctime)s, %(levelname)s, %(message)s, %(name)s, %(filename)s",
)
