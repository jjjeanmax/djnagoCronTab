# djnagoCronTab

Django-cron позволяет запускать код Django / Python на регулярной основе, 
доказывая базовые возможности для отслеживания и выполнения задач.
 Это ни в коем случае не замена таких очередей, как Celery.
 
## Старт

1. Создать и активировать виртуальное окружение:

    `$ python -m venv venv`

2. Установить пакеты:

    `$ pip install -r requirements.txt`

3. Выполнить команду для выполнения миграций из деректории **led_box_finder_back**:

    `$ python manage.py migrate`

4. Создать статичные файлы: 

    `$ python manage.py collectstatic`

5. Создать суперпользователя:

    `$ python manage.py createsuperuser`

6. Добавить задачу:

    `$ python manage.py crontab add`

7. Запустить сервер:

    `$ python manage.py runserver`
