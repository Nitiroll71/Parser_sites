import telebot
import os
import time
from dotenv import load_dotenv

class TelegramBot:

    chanel_id = -1002879775846

    def __init__(self):
        
        # Загружаем переменные окружения из .env (логин и пароль)
        load_dotenv()
        
        TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)


    def send_to_tg(self):

        # загрузка всех фоток из папки
        try:
            i = 0
            while True:
                with open(f'F:\\PyProjects\\Parser_sites\\pictures\\picture{i}.png', 'rb') as photo: 
                    # Задержка 4 секунды т.к. Телеграм ограничивает 20 сообщений в минуту.
                    time.sleep(4) 
                    self.bot.send_photo(self.chanel_id, photo)
                    i += 1
        except (FileNotFoundError, telebot.apihelper.ApiTelegramException) as E:
             print('Все файлы загружены на канал.')