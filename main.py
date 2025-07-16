from my_parser import Parser
from my_telebot import TelegramBot

parser_pict = Parser('https://fonwall.ru/')
tgbot = TelegramBot()

parser_pict.authorization('https://auth.fonwall.ru/auth/login',
                    'https://fonwall.ru/@meow1234/')

picture_urls = parser_pict.get_pictures_url(parser_pict.find_pict_block(10))

tgbot = TelegramBot(session=parser_pict.session)
tgbot.send_to_tg_urls(picture_urls)