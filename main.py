import os
from my_parser import Parser
from my_telebot import TelegramBot

parser_pict = Parser('https://auth.fonwall.ru/auth/login',
                    'https://fonwall.ru/',
                    'https://fonwall.ru/@meow1234/')
tgbot = TelegramBot()

parser_pict.authorization()
parser_pict.get_pictures()

tgbot.send_to_tg()

# Удаляем фото после отправки в канал телеграм
try:
    i = 0
    while True:
        # удаление фото из системы
        os.remove(f"F:\\PyProjects\\Parser_sites\\pictures\\picture{i}.png")
        i += 1
except FileNotFoundError:
    print('все файлы удалены')