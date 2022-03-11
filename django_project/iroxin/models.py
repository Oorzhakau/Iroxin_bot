from django.contrib.auth import get_user_model
from django.db import models


class Subscriber(models.Model):
    user_id = models.BigIntegerField(
        verbose_name="ID Пользователя Телеграм",
        unique=True,
    )
    username = models.CharField(
        verbose_name="username",
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name="фамилия",
        max_length=150,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='email',
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=12,
        verbose_name='Телефон',
        blank=True,
        null=True,
    )
    company = models.CharField(
        max_length=100,
        verbose_name='Компания',
        blank=True,
        null=True
    )
    notes = models.TextField(
        verbose_name='Заметки',
        blank=True,
        null=True,
    )
    status = models.BooleanField(
        verbose_name='Статус обработки заявки',
        default=False,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
    
    def __str__(self):
        return f"(tel id {self.user_id}) {self.username}"


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    description = models.TextField(verbose_name='Описание типа продукции')
    about = models.TextField(verbose_name='Описание применения')
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='products/models/',
        blank=True,
        null=True,
        help_text='Загрузите картинку'
    )
    image_size = models.ImageField(
        verbose_name='Картинка с размерами',
        upload_to='products/sizes/',
        blank=True,
        null=True,
        help_text='Загрузите картинку'
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукция"
    
    def get_absolute_url(self):
        return f'/products/models/{self.id}/'

    def __str__(self):
        return self.title[:15]