import requests
import fake_useragent
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

class Parser:

    url_site = None
    authorization_link = None
    page_name_user = None

    def __init__(self, authorization_link, url_site, page_name_user):

        self.set_urls(authorization_link, url_site, page_name_user)
    
    def set_urls(self, url_site, page_name_user, authorization_link):
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

        # Создаем сессию для работы с куки и авторизацией
        self.session = requests.Session()

        # Получаем случайный user-agent для маскировки
        user = fake_useragent.UserAgent().random

        # Заголовки запроса
        header = {
            'user-agent': user
        }
        self.header = header

        # Отправляем POST-запрос на авторизацию
        self.session.post(self.authorization_link, data=data, headers=header).text

        # Получаем HTML-код страницы пользователя после авторизации
        user_check_page = self.session.get(self.page_name_user, headers=header).text

        # Проверка на успешность входа
        user_soup = BeautifulSoup(user_check_page, 'lxml')
        print(user_soup.find('span', class_='ProfileHeader_profileFirstName__1G8fe').text)
    
    def get_pictures(self):

        self.session = requests.Session()