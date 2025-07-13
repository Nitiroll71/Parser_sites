from my_parser import Parser

parser_pict = Parser('https://auth.fonwall.ru/auth/login',
                    'https://fonwall.ru/',
                    'https://fonwall.ru/@meow1234/')

parser_pict.authorization()
parser_pict.get_pictures()