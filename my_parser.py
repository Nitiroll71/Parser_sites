import requests
import fake_useragent
import os
import re
from dotenv import load_dotenv
from bs4 import BeautifulSoup

class Parser:

    url_site = None
    authorization_link = None
    page_name_user = None

    def __init__(self, authorization_link, url_site, page_name_user):

        self.set_urls(authorization_link, url_site, page_name_user)

        # Создаем сессию для работы с куки и авторизацией
        self.session = requests.Session()
    
    def set_urls(self, url_site, authorization_link, page_name_user):
        self.url_site = url_site
        self.page_name_user = page_name_user
        self.authorization_link = authorization_link

    def get_urls(self):
        
        return self.url_site, self.authorization_link, self.page_name_user

    def authorization(self):

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

        # Получаем случайный user-agent для маскировки
        user = fake_useragent.UserAgent().random

        # Заголовки запроса
        header = {
            'user-agent': user
        }
        self.header = header

        # 🔧 ВАЖНО: отправляем POST-запрос для авторизации
        auth_response = self.session.post(self.authorization_link, data=data, headers=header)

        # Проверка, вдруг авторизация не удалась
        print(f"[DEBUG] Auth status: {auth_response.status_code}")
        if auth_response.status_code != 200:
            print("❌ Авторизация не удалась.")
            return

        # Получаем HTML-код страницы пользователя после авторизации
        user_check_page = self.session.get(self.page_name_user, headers=header).text

        # Парсим страницу с помощью BeautifulSoup
        user_soup = BeautifulSoup(user_check_page, 'lxml')

        # Ищем имя пользователя в блоке профиля
        chek_user = user_soup.find('span', class_='ProfileHeader_profileFirstName__1G8fe').text

        # Выводим имя пользователя в консоль
        print(chek_user)
    
    def get_pictures(self):

        self.session = requests.Session()