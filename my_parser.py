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

        set_urls(authorization_link, url_site, page_name_user)
    
    def set_urls(self, url_site, page_name_user, authorization_link):
        self.url_site = url_site
        self.page_name_user = page_name_user
        self.authorization_link = authorization_link

    def get_urls(self):
        
        return self.url_site
        return self.page_name_user
        return self.authorization_link

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
        session = requests.Session()