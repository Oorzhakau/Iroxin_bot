from typing import List, Coroutine, Optional, Union
from asgiref.sync import sync_to_async

from pathlib import Path
import os
import sys

from data.config import ADMINS

ROOT_DIR = Path(__file__).parents[3]
MODEL_PATH = os.path.join(ROOT_DIR, 'django_project')
sys.path.append(MODEL_PATH)

from iroxin.models import Subscriber, Product


@sync_to_async
def add_subscriber(user_id: Union[str, int],
                   username: str,
                   first_name: Optional[str],
                   last_name: Optional[str]) -> Subscriber:
    '''Добавить подписчика.'''
    sub = Subscriber.objects.create(
        user_id=int(user_id),
        first_name=first_name,
        last_name=last_name,
        username=username
    )
    sub.save()
    return sub


@sync_to_async
def get_all_subscribers() -> List[Subscriber]:
    '''Получить всех подписчиков.'''
    users = Subscriber.objects.all()
    return users


@sync_to_async
def get_subscriber(user_id: int) -> Optional[Subscriber]:
    '''Получить подписчика по user_id.'''
    if Subscriber.objects.filter(user_id=user_id).exists():
        subscriber = Subscriber.objects.get(user_id=user_id)
        return subscriber
    return None


@sync_to_async
def get_count_subscribers() -> int:
    '''Получить число зарегистрированных подписчиков.'''
    total = Subscriber.objects.all().count()
    return total


@sync_to_async
def get_product(title: str) -> Optional[Product]:
    '''Получить товары title.'''
    prod = Product.objects.get(title=title)
    return prod


@sync_to_async
def get_all_products() -> List[Product]:
    '''Получить все товары.'''
    prods = Product.objects.all()
    return prods


