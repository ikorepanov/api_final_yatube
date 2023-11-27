![Sprint 9](https://github.com/ikorepanov/api_final_yatube/assets/108400524/ab4635c6-e555-4034-8dc4-b65051904d19)

# API_FINAL_YATUBE
## Учебный проект на курсе Python-разработчик Яндекс-Практикума (9 српинт)

### Концепция проекта ###
Настоящий проект призван помочь студендам отточить навыки проектирования, создания и отладки API на базе архитектуры REST с использованием Django Rest Framework.

За основу был взят ранее выполненный Django-проект социальной сети YaTube.

В ходе проекта 
* были изучены теоретические основы разработки проектов API на базе REST;
* отработаны навыки составления разных типов запросов (GET, POST, PUT и т.д.) к различным таблицам (Follow, Group, Comment) базы данных;
* изучены практические приёмы решения различных прикладных задач (организация фильтрации и поиска, пагинация и т.д.)

### Примеры запросов и ответов: ###
### GET: /api/v1/posts/ ###
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
### POST /api/v1/follow/ ###
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

### Как запустить проект ###
* Клонировать репозиторий и перейти в него в командной строке: 
```bash
git clone https://github.com/ikorepanov/api_final_yatube
```
```bash
cd api_final_yatube
```
* Cоздать и активировать виртуальное окружение: 
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
* Установить зависимости из файла requirements.txt:

```bash
python -m pip install --upgrade pip 
```
```bash
pip install -r requirements.txt 
```
* Выполнить миграции:
```bash
python manage.py migrate 
```
* Запустить проект:
```bash
python manage.py runserver
```

### Автор: Илья Корепанов, ikorepanov.study@gmail.com, https://t.me/number_one_lobster
