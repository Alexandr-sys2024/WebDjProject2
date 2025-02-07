# WebDjProject2

## 📌 О проекте
**WebDjProject2** — это веб-приложение, созданное с использованием Django. В проекте есть базовая маршрутизация, несколько представлений и подключение к базе данных SQLite.

## 🚀 Функционал
- Простая маршрутизация Django
- Несколько страниц с `HttpResponse`
- Подключение к базе данных SQLite
- Возможность расширения функционала

## 📥 Установка и запуск
```bash
# Клонируем репозиторий
git clone https://github.com/Alexandr-sys2024/WebDjProject2.git
cd WebDjProject2

# Создаем виртуальное окружение
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем миграции и сервер
python manage.py migrate
python manage.py runserver
```

## 📂 Структура проекта
```
WebDjProject2/
│── SashaandDjango/          # Основной Django-проект
│   │── settings.py          # Настройки Django
│   │── urls.py              # Маршрутизация
│   │── wsgi.py              # WSGI-конфигурация
│   │── asgi.py              # ASGI-конфигурация
│
│── first/                   # Django-приложение
│   │── views.py             # Контроллеры
│   │── urls.py              # URL-маршрутизация
│   │── models.py            # Модели базы данных
│
│── manage.py                # Файл управления Django
│── requirements.txt         # Зависимости проекта
│── README.md                # Описание проекта
```

## 🔧 Будущие улучшения
- Добавление HTML-шаблонов (Django Templates)
- Подключение базы данных PostgreSQL
- Расширение функционала (авторизация, API)

## 📜 Лицензия
Этот проект распространяется по лицензии MIT. См. файл `LICENSE` для подробностей.