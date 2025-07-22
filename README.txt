# 🖼️ Image Parser & Telegram Bot

Скрипт автоматизирует парсинг изображений с сайта [fonwall.ru](https://fonwall.ru) и отправку их в Telegram-канал с помощью бота. 
Проект демонстрирует работу с HTTP-запросами, парсингом HTML-страниц, авторизацией через `requests.Session`, 
использованием регулярных выражений и взаимодействием с Telegram Bot API.

---

## ⚙️ Используемые технологии

- Python 3.10+
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [pyTelegramBotAPI (telebot)](https://pypi.org/project/pyTelegramBotAPI/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [fake-useragent](https://pypi.org/project/fake-useragent/)
- `re`, `os` — стандартные библиотеки Python

---

## 🗂 Структура проекта

```

project/
├── main.py              # Точка входа
├── parser.py            # Класс для парсинга изображений
├── telegram\_bot.py      # Класс для отправки в Telegram
├── .env                 # Переменные окружения
├── requirements.txt     # Список зависимостей
└── README.md            # Документация проекта

```

---

## 🔐 Настройка переменных окружения

Создайте файл `.env` в корне проекта со следующим содержимым:

```

LOGIN=your\_fonwall\_login
PASSWORD=your\_fonwall\_password
TELEGRAM\_TOKEN=your\_telegram\_bot\_token
CHANNEL\_ID=@your\_channel\_id
BASE\_URL=[https://fonwall.ru](https://fonwall.ru)

````

---

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Nitiroll71/Parser_sites.git
````

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Запустите скрипт:

```bash
python main.py
```

---

## ✅ Возможности

* 🔐 Авторизация на сайте fonwall.ru через `requests.Session`
* 🔍 Поиск изображений по тегам `<img>` с нужным классом
* 📥 Сбор ссылок с нескольких страниц
* 🧠 Использование `fake_useragent` для имитации браузера
* 📤 Отправка изображений в Telegram-канал

---

## 🧩 Возможности для доработки

* ⏱️ Планировщик публикаций (через `schedule` или cron)
* 🌐 Поддержка других источников
* 🧾 Логирование отправленных изображений
* 🖥️ Веб-интерфейс администратора

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Свободно используйте и модифицируйте с указанием автора.

---

## 🤝 Автор

Разработано в рамках учебной практики студентом
Год: 2025

```
