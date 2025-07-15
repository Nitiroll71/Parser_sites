from my_parser import Parser
from my_telebot import TelegramBot

parser_pict = Parser('https://auth.fonwall.ru/auth/login',
                    'https://fonwall.ru/',
                    'https://fonwall.ru/@meow1234/')
tgbot = TelegramBot()

parser_pict.authorization()

picture_urls = parser_pict.get_pictures()

tgbot = TelegramBot(session=parser_pict.session)
tgbot.send_to_tg_urls(picture_urls)