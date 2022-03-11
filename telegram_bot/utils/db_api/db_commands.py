"""Реализация базовых команд для асинхронного запроса к базе
данных Postgres через Django ORM.
"""

import os
import sys
from pathlib import Path
from typing import List, Optional, Union

from asgiref.sync import sync_to_async

ROOT_DIR = Path(__file__).parents[3]
MODEL_PATH = os.path.join(ROOT_DIR, "django_project")
sys.path.append(MODEL_PATH)

from iroxin.models import Product, Subscriber


@sync_to_async
def add_subscriber(
    user_id: Union[str, int],
    username: str,
    first_name: Optional[str],
    last_name: Optional[str],
) -> Subscriber:
    """Добавить подписчика."""
    sub = Subscriber.objects.create(
        user_id=int(user_id),
        first_name=first_name,
        last_name=last_name,
        username=username,
    )
    sub.save()
    return sub


@sync_to_async
def get_all_subscribers() -> List[Subscriber]:
    """Получить всех подписчиков."""
    users = Subscriber.objects.all()
    return users


@sync_to_async
def get_subscriber(user_id: int) -> Optional[Subscriber]:
    """Получить подписчика по user_id."""
    if Subscriber.objects.filter(user_id=user_id).exists():
        subscriber = Subscriber.objects.get(user_id=user_id)
        return subscriber
    return None


async def get_then_update(
    user_id: int, name: str, email: str, phone: str
) -> Subscriber:
    """Получение и обновление подписчика."""
    subscriber = await get_subscriber(user_id)
    if not subscriber.first_name:
        subscriber.first_name = name
    if not subscriber.email:
        subscriber.email = email
    if not subscriber.phone:
        subscriber.phone = phone
    subscriber.save()
    return subscriber


@sync_to_async
def get_count_subscribers() -> int:
    """Получить число зарегистрированных подписчиков."""
    total = Subscriber.objects.all().count()
    return total


@sync_to_async
def get_product(title: str) -> Optional[Product]:
    """Получить товары title."""
    prod = Product.objects.get(title=title)
    return prod


@sync_to_async
def get_all_products() -> List[Product]:
    """Получить все товары."""
    prods = Product.objects.all()
    return prods


@sync_to_async
def get_count_products() -> int:
    """Получить количество товаров."""
    count = Product.objects.all().count()
    return count


async def get_page(page: int = 1) -> int:
    """Получить страницу."""
    max_val = await get_count_products()
    if page >= max_val:
        page = max_val
    arr = await get_all_products()
    return arr[page]
