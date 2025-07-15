import telebot
import os
import time
import requests
from dotenv import load_dotenv
from io import BytesIO

class TelegramBot:    

    def __init__(self, session=None):
        
        # Загружаем переменные окружения из .env (токен и id канала)
        load_dotenv()
        
        self.CHANEL_ID=os.getenv('CHANEL_ID')
        print(self.CHANEL_ID)
        TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)
        self.session = session or requests.Session()


    def send_to_tg_urls(self, urls):

        # загрузка всех фоток ссылок
        for i, url in enumerate(urls):
            try:
                time.sleep(4)
                response = self.session.get(url)
                if response.status_code == 200:
                    photo = BytesIO(response.content)
                    photo.name = f"picture{i+1}.png"
                    self.bot.send_photo(self.CHANEL_ID, photo)
                    print(f"Фото {i+1} отправлено")
                else:
                    print(f"Не удалось скачать фото {i+1}, статус: {response.status_code}")
            except Exception as e:
                print(f"Ошибка при отправке фото {i+1}: {e}")