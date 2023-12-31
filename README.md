![Sprint 9](https://github.com/ikorepanov/api_final_yatube/assets/108400524/ab4635c6-e555-4034-8dc4-b65051904d19)
# Проект «API для Yatube»
## Описание проекта
Учебный проект в рамках 9 спринта курса Python-разработчик Яндекс Практикума.  
Вторая часть проекта ([Первая часть](https://github.com/ikorepanov/api_yatube)) по разработке REST API для подготовленного ранее проекта социальной сети.  

## Содержание
1. [Структура проекта](#структура-проекта)
2. [Как запустить проект](#как-запустить-проект)
3. [Стек технологий](#стек-технологий)
4. [Авторы, контакты](#авторы-контакты)

## Структура проекта
Согласно заданию - необходимо дописать предоставленный код и привести его в соответствие с документацией: 
- добавить недостающие модели в приложении **posts**; 
- создать адреса и представления для обработки запросов в приложении **api**.  

В качестве технического задания необходимо использовать документацию, предоставленную в формате **Redoc**.  

Помимо прочего - в проекте должна быть описана модель **Follow**, в ней должно быть два поля — `user` (кто подписан) и `following` (на кого подписан). Для этой модели в документации описан эндпоинт `/follow/` и два метода: 
- GET — возвращает все подписки пользователя, сделавшего запрос. Возможен поиск по подпискам по параметру `search`;
- POST — подписать пользователя, сделавшего запрос на пользователя, переданного в теле запроса. При попытке подписаться на самого себя, пользователь должен получить информативное сообщение об ошибке. Проверка должна осуществляться на уровне API.  

Анонимный пользователь на запросы к этому эндпоинту должен получать ответ с кодом **401 Unauthorized**.  

### Примеры запросов
#### GET: /api/v1/posts/ ####
*200:* 
```JSON
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
*400:* 
```JSON
{
  "text": [
    "Обязательное поле."
  ]
}
```
#### POST: /api/v1/follow/ ####
```JSON
{
  "following": "string"
}
```
*200:*
```JSON
{
  "user": "string",
  "following": "string"
}
```
*401:*
```JSON
{
  "detail": "Учетные данные не были предоставлены."
}
```

## Как запустить проект
В дальнейших командах используйте `python3` вместо `python` - **для Linux и macOS**.   
- клонируйте репозиторий:
  ```
  git clone git@github.com:ikorepanov/api_final_yatube.git
  ```
- перейдите в папку с проектом:
  ```
  cd api_final_yatube
  ```
- разверните виртуальное окружение:
  ```
  python -m venv venv
  ```
- активируйте виртуальное окружение:
  * команда для Windows
    ```
    source venv/Scripts/activate
    ```
  * команда для Linux и macOS
    ```
    source venv/bin/activate
    ```
- обновите `pip`:
  ```
  python -m pip install --upgrade pip
  ```
- установите зависимости:
  ```
  pip install -r requirements.txt
  ```
- перейдите в папку `yatube_api`:
  ```
  cd yatube_api
  ```
- выполните миграции:
  ```
  python manage.py migrate
  ```
- создайте суперпользователя:
  ```
  python manage.py createsuperuser
  ```
- запустите сервер разработчика:
  ```
  python manage.py runserver
  ```
Проект будет доступен по адресу [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).  

Документация: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/).    

Админка проекта: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).  
Для доступа - использовать данные суперпользователя, созданные ранее.  

Отправку запросов на эндпоинты удобно осуществлять через [Postman](https://www.postman.com/).  

## Стек технологий
- Python 3.9
- Django 2.2.9
- Django Rest Framework

## Авторы, контакты
- Илья Корепанов  
[![Telegram Badge](https://img.shields.io/badge/Telegram-blue?style=social&logo=Telegram)](https://t.me/number_one_lobster) [![Gmail Badge](https://img.shields.io/badge/Gmail-red?style=social&logo=Gmail)](mailto:ikorepanov.study@gmail.com)   
- Yandex Practicum