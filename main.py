from my_parser import Parser
from my_telebot import TelegramBot
from threading import Thread

parser_pict = Parser('https://fonwall.ru/')
tgbot = TelegramBot()

parser_pict.authorization('https://auth.fonwall.ru/auth/login',
                    'https://fonwall.ru/@meow1234/')

pict_block = parser_pict.find_pict_block(10)

# picture_urls = parser_pict.get_pictures_url(pict_block)
# picture_text = parser_pict.get_pict_text(pict_block)

picture_urls = []
picture_text = []

# Запуск через потоки
def get_urls():
    result = parser_pict.get_pictures_url(pict_block)
    picture_urls.extend(result)

def get_texts():
    result = parser_pict.get_pict_text(pict_block)
    picture_text.extend(result)

t1 = Thread(target=get_urls)
t2 = Thread(target=get_texts)

t1.start()
t2.start()

t1.join()
t2.join()

tgbot = TelegramBot(session=parser_pict.session)
tgbot.send_to_tg_urls(picture_urls, picture_text)