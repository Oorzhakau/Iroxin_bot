import requests
import logging


def send_data_to_form(
                      email: str,
                      name: str,
                      phone: str,
                      url: str = 'https://forms.tildacdn.com/procces/'
                      ) -> None:
    """Функция отправки формы на сайте
    https://smart.iroxin.ru/.
    """
    data = {
            'email': email,
            'name': name,
            'Phone': phone
           }
    response = requests.post(url, data=data)
    logging.info(f"Форма с данными отправлена. Data - {data}. "
                 f"Ответ сервера - {response.text}.")