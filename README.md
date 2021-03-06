# Iroxin_bot
## Описание
Телеграм-бот компании **Iroxin**.

Бот регистрирует пользователя, заносит его в базу данных, позволяет просматривать каталог товаров и отправлять заявку на сайт компании для консультации, при этом дублируя ее в телеграм группу для менеджеров.
Взаимодействие с базой данных PostgreSQL реализовано через ORM и Админ-панель Django.
<img src="media/Django.JPG" alt="django" border="1">
Асинхронная логика телеграм-бота реализована с помощью фреймворка aiogram.

Для ознакомление с проектом можно перейти на бота по ссылке https://t.me/iroxin_bot
## Технологии
* Python 3.8
* Django 4.0
* PostgreSQL 4.0
* Aiogram 2.19
* Docker 3.1

## Запуск проекта в dev-режиме
- Устанавливаете docker и docker-compose;
```
sudo apt update
sudo apt install docker docker-compose -y
```
- Переименовываете файл .env_example на .env и заполняете его нужными значениями переменных окружения.<br>
Help по токенам
    <ul>
       <li><a href="https://core.telegram.org/bots#6-botfather">Токен телеграмм-бота</a></li>
       <li>Ваш telegram id можно узнать у бота @userinfobot</li>
    </ul>
- В папке проекта запускаете docker-compose: 
```
docker-compose up --build
```
- По адресу localhost:8002/admin/ переходим в панель и входим под ранее созданным superuser-ом;
<img src="media/Django_admin.JPG" alt="django-admin" border="1">

- Проект запущен и готов к работе.

### Список исполнителей
[Александр Ооржак](https://github.com/Oorzhakau)

