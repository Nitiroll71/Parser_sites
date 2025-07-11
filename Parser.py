
import requests
import fake_useragent
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Создаем сессию для сохранения cookies между запросами
session = requests.Session()

# URL для авторизации
authorization_link = 'https://auth.fonwall.ru/auth/login?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkF1dGggRm9ud2FsbCIsImlhdCI6MTUxNjIzOTAyMn0.BU2Itfl1n3r2urmXTZv2TrjWRlp3C_p7xgSUJFh87CE&requestMade=site'

# Генерируем случайный User-Agent
user = fake_useragent.UserAgent().random

# Заголовки для HTTP-запросов
header = {
        'user-agent' : user
}

# Данные для авторизации
load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

data = {
        'mail' : LOGIN,
        'password' : PASSWORD
}

# Отправляем POST-запрос для авторизации
responce = session.post(authorization_link, data=data, headers=header).text

# URL страницы комикса
page_name_user = 'https://fonwall.ru/@meow1234/'

user_check_page = session.get(page_name_user, headers=header).text
user_soup = BeautifulSoup(user_check_page, 'lxml')
chek_user = user_soup.find('span', class_='ProfileHeader_profileFirstName__1G8fe')
print(chek_user)

picture_link = 'https://image.fonwall.ru/o/el/caucasian-forest-fog.jpeg?auto=compress&fit=resize&h=286&w=500&display=thumb&domain=img3.fonwall.ru'
# Получаем содержимое страницы комикса
comix_page_responce = session.get(picture_link, headers=header).content

# Сохраняем изображение комикса в файл
with open('comix2.png', 'wb') as f:
    f.write(comix_page_responce)