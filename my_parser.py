import requests
import fake_useragent
import os
import re
from dotenv import load_dotenv
from bs4 import BeautifulSoup

class Parser:

    def __init__(self, authorization_link, url_site, page_name_user):

        self.set_urls(authorization_link, url_site, page_name_user)
        
        # Получаем случайный user-agent для маскировки
        user = fake_useragent.UserAgent().random

        # Заголовки запроса
        self.header = {
            'user-agent': user
        }
        
        # Загружаем переменные окружения из .env (логин и пароль)
        load_dotenv()
        LOGIN = os.getenv('LOGIN')
        PASSWORD = os.getenv('PASSWORD')

        # Данные для авторизации
        self.data = {
            'mail': LOGIN,
            'password': PASSWORD
        }

        # Создаем сессию для работы с куки и авторизацией
        self.session = requests.Session()
    
    def set_urls(self, authorization_link, url_site, page_name_user):
        self.url_site = url_site
        self.page_name_user = page_name_user
        self.authorization_link = authorization_link

    def authorization(self):

        # отправляем POST-запрос для авторизации
        auth_response = self.session.post(self.authorization_link, json=self.data, headers=self.header)

        # Проверка авторизации
        if auth_response.status_code != 200:
            print(f"Авторизация не удалась. Код ошибки: {auth_response.status_code}\nОтвет от сервера: {auth_response.text}")
            return
        else:
            print(f"Авторизация удалась. Код: {auth_response.status_code}")
        
        # Выводим имя пользователя в консоль
        user_check_page = self.session.get(self.page_name_user, headers=self.header).text
        user_soup = BeautifulSoup(user_check_page, 'lxml')
        chek_user = user_soup.find('span', class_='ProfileHeader_profileFirstName__1G8fe').text
        print(f'Имя пользователя: {chek_user}')
    
    def find_pict_url(self):
        
        # Ищем все картинки на странице
        page_block = self.session.get(self.url_site, headers=self.header).text
        all_pic_block = BeautifulSoup(page_block, 'lxml')
        all_pic_soup = all_pic_block.find_all('img', class_ = re.compile(r'^Article_image__I_3mF'))
        
        return all_pic_soup
    
    def get_pictures_url(self, block):
        
        # Получение ссылок на картинки
        urls_pict = []
        for i, img in enumerate(block, start=1):
            src = img.get('src')
            urls_pict.append(src)
        
        # возвращаем ссылки на картинки
        return urls_pict