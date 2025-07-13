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

        try:
            i = 0
            while True:
                with open(f'F:\\PyProjects\\Parser_sites\\pictures\\picture{i}.png', 'rb') as photo: 
                    time.sleep(2) 
                    self.bot.send_photo(self.chanel_id, photo)
                    os.remove("F:\\PyProjects\\Parser_sites\\pictures\\picture{i}.png")
                    i += 1  
        except FileNotFoundError:
             pass