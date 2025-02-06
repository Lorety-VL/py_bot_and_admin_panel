# py_bot_and_admin_panel

Для развертывания проекта необходимо в корне проекта создать файл .env с переменными:

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

## Запуск админки

```sh
make build
make start
make migrate
make collectstatic
```

## Добавление пользователя для админки

```sh
make add_admin
```

## Установка сертификатов

```sh
make set_certificate
```

## Запуск бота

```sh
make start_bot
```


Для того чтобы бот и админка использовали одни и те же модели, чтобы не было дублирования, создал еще одно Django приложение - core
оно содержит модели используемые в боте и админке

## О встреченных проблемах:

Выбирая между сделать бота отдельным микросервисом в своем docker контейнере, либо встроить в django проект я мыслил так - если разнести по разным микросервисам, то при изменении в боте, прийдется отдельно вносить изменения в админку, из-за чего теряется смысл микросервисов, так как изменяя один сервис, все равно прийдется остановить второй и тоже изменить.

По этой причине я решил сделать его отдельным приложением в django проекте. Тут был соблазн определить модели лмбо в боте либо в админке. Но вынеся определение моделей в отдельное приложение, как мне кажется, повысилась переиспользуемость приложений, ведь если бы мы переносили одно приложение из проекта, нам бы пришлось менять код, если бы оно использовало модели определенные в другом, а теперь достаточно пеернести нужное приложение и приложение определяющие модели.

Но тут, по всей видимости проявилась направленность django, нет проблем написать приложение которое отдает html странички или написать бэкенд реализующий API запросы, но как быть с ботом, ведь он не отвечает на API запросы, а запустить его надо, был вариант использовать сигналы и запускать бота посли инициализации django, но тогда при попытке добавить пользователя в админку происходила повторная иницализация и скрипт добавления пользователя падал с ошибкой так как дважды подключался к телеграму для прослушки бота.

тогда пришлось запускать бота через команды management/commands, но тут тоже есть проблема, если после запуска контейнера с django слишком быстро послать в контейнер команду запуска бота, django не успеет инициализироваться и бот не запустится. Но пришлось оставить текущую реализацию, так как на ее изменене времени нехватило (не сразу увидел и начал решать тестовое).

Так же непросто было настроить выдачу сертификатов nginx, так как после выдачи сертификатов необходимо изменить конфиг nginx, а я хотел избежать изменений вручную, поэтому пришлось использовать bash скрипт.