# py_bot_and_admin_panel

## Запуск бота и админки

```sh
make build
make start
make migrate
```

## Добавление пользователя для админки

```sh
make add_admin
```

## Установка сертификатов

```sh
make set_certificate
```

Для запуска необходимо в корне проекта создать файл .env с переменными:

```sh
TELEGRAM_BOT_TOKEN
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_PORT
DJANGO_SECRET
DOMAIN_URL
DOMAIN_EMAIL
```


Для того чтобы бот и админка использовали одни и те же модели, чтобы не было дублирования, создал еще одно Django приложение - core
оно содержит модели используемые в боте и админке
