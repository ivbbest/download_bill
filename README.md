# Задача:

Реализовать REST API для загрузки файлов, записи в Postgres и обработки информации

## Функциональные требования:
### Создать следующие модули:

**Детектор мошенничества**

На вход принимает str, на выходе float рандомно в диапазоне от 0 до 1. При загрузке файла bills.xlsx колонку service пропускать через “Детектор мошенничества” и сохранять это значение в бд под названием fraud_score.

**Классификатор услуг**

На вход принимает str, на выходе dict вида {service_class: int, ‘service_name’: str}
Возвращаемый dict формировать путём рандомного выбора пары ключ-значение из этого словаря {1: ‘консультация’, 2: ‘лечение’, 3: ‘стационар’, 4: ‘диагностика’, 5: ‘лаборатория’}, где ключ это service_class, а значение это ‘service_name’.
При загрузке файла bills.xlsx колонку service пропускать через “Классификатор услуг” и сохранять service_class, service_name в бд.

### API
1. эндпоинт загрузки файлов bills.xlsx и client_org.xlsx  (может быть по одному на файл, как посчитаете правильным)

2. эндпоинт со списком клиентов
Данные, которые нужно отдавать для каждого элемента списка:
 - Название клиента
 - Кол-во организаций
 - Приход (сумма по счетам всех организаций клиента)

3. эндпоинт со списком счетов с возможностью фильтровать по организации, клиенту.

## Нефункциональные требования:
- Использование Django ORM
- Следование принципам REST
- Django REST framework
- База данных на PostgreSQL
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv
- Использование свежих версий python и Django

## Установка:
Клонируем репозиторий на локальную машину:

    git clone https://github.com/ivbbest/download_bill.git

или 

    git clone git@github.com:ivbbest/download_bill.git

Переходим в папку с проектом.

    cd download_bill

Установка всех зависимостей из requirements.txt.

    python3 -m pip install -r requirements.txt

Сделать миграции.

    python3 manage.py migrate

Если локально запустить требуется проект, то:

    python3 manage.py runserver 127.0.0.1:8000

Если требуется проект глобально запустить, например при помощи VPS или виртуальной машины, то:

    python3 manage.py runserver 0.0.0.0:8000

А после этого с любого компьютера вводим: 

    виртуальный_адрес:8000

Пример:

    194.67.86.252:8000

 
## Доступны основные следующие страницы:

| Страница                           | Описание                                                           |
|------------------------------------|--------------------------------------------------------------------|
| `http://127.0.0.1:8000/client_org/`     | POST запрос для загрузки файла client_org.xlsx                     |
| `http://127.0.0.1:8000/bills/` | POST запрос для загрузки файла bills.xlsx                          |
| `http://127.0.0.1:8000/clients/` | Список клиентов из БД с количеством организаций и суммой по счетам |
| `http://127.0.0.1:8000/invoices/`    | эндпоинт со списком счетов с возможностью фильтровать по организации, клиенту.                                                   |

## Использовано:
- Python 3.9
- Django 4.0.5
- Django Rest Framework 3.13.1
- Django-filter 22.1
- Psycopg2-binary 2.9.3