import telebot
import os
import time
from dotenv import load_dotenv

class TelegramBot:    

    def __init__(self):
        
        # Загружаем переменные окружения из .env (токен и id канала)
        load_dotenv()
        
        self.CHANEL_ID=os.getenv('CHANEL_ID')
        TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)


    def send_to_tg(self):

        # загрузка всех фоток из папки
        try:
            i = 0
            while True:
                with open(f'F:\\MyProjects\\Parser_sites\\pictures\\picture{i}.png', 'rb') as photo: 
                    # Задержка 4 секунды т.к. Телеграм ограничивает 20 сообщений в минуту.
                    time.sleep(4) 
                    self.bot.send_photo(self.CHANEL_ID, photo)
                    i += 1
        except (FileNotFoundError, telebot.apihelper.ApiTelegramException) as E:
             print('Все файлы загружены на канал.')