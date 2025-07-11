import requests
import fake_useragent
import os
import re
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Ссылка для авторизации (с токеном)
authorization_link = 'https://auth.fonwall.ru/auth/login?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkF1dGggRm9ud2FsbCIsImlhdCI6MTUxNjIzOTAyMn0.BU2Itfl1n3r2urmXTZv2TrjWRlp3C_p7xgSUJFh87CE&requestMade=site'

# Главная страница сайта с картинками
page_link = 'https://fonwall.ru/'

# Прямая ссылка на картинку (пример)
picture_link = 'https://image.fonwall.ru/o/el/caucasian-forest-fog.jpeg?auto=compress&fit=resize&h=286&w=500&display=thumb&domain=img3.fonwall.ru'

# URL страницы пользователя (личного кабинета)
page_name_user = 'https://fonwall.ru/@meow1234/'

# Загружаем переменные окружения из .env (логин и пароль)
load_dotenv()

# Получаем логин и пароль из переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Данные для авторизации
data = {
    'mail': LOGIN,
    'password': PASSWORD
}

# Создаем сессию для работы с куки и авторизацией
session = requests.Session()

# Получаем случайный user-agent для маскировки
user = fake_useragent.UserAgent().random

# Заголовки запроса
header = {
    'user-agent': user
}

# Отправляем POST-запрос на авторизацию
responce = session.post(authorization_link, data=data, headers=header).text

# Получаем HTML-код страницы пользователя после авторизации
user_check_page = session.get(page_name_user, headers=header).text

# Парсим страницу с помощью BeautifulSoup
user_soup = BeautifulSoup(user_check_page, 'lxml')

# Ищем имя пользователя в блоке профиля
chek_user = user_soup.find('span', class_='ProfileHeader_profileFirstName__1G8fe').text

# Выводим имя пользователя в консоль
print(chek_user)

# Ищем все картинки на странице
page_block = session.get(page_link, headers=header).text
all_pic_block = BeautifulSoup(page_block, 'lxml')
all_pic_soup = all_pic_block.find_all('img', class_ = re.compile(r'^Article_image__I_3mF'))

# Получение ссылок на картинки
urls_pict = []
for i, img in enumerate(all_pic_soup, start=1):
    src = img.get('src')
    urls_pict.append(src)

# Загружаем картинку по прямой ссылке (авторизованной сессией). Сохраняем картинку в файл
# for i, src in enumerate(urls_pict):
#     picture = session.get(src, headers=header).content
#     with open(f'F:\\PyProjects\\Parser_sites\\pictures\\picture{i}.png', 'wb') as f:
#         f.write(picture)