import telebot
import os
from dotenv import load_dotenv

class TelegramBot:

    chanel_id = -1002879775846

    def __init__(self):
        
        # Загружаем переменные окружения из .env (логин и пароль)
        load_dotenv()
        
        TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)


    def send_to_tg(self):
        with open('blank_user.jpg', 'rb') as photo:  
                self.bot.send_photo(self.chanel_id, photo)  
              
