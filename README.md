## YaMDb API (База отзывов о фильмах, книгах и музыке)

### Описание
Проект YaMDb API собирает отзывы (Review) пользователей на произведения (Titles). 
Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Список категорий быть расширен администратором.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/antonvm26/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:
Команда для установки виртуального окружения на Mac или Linux:
```
python3 -m venv env
source env/bin/activate
```
Команда для Windows должна быть такая:
```
python -m venv venv
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Заполнение таблиц тестовыми данными 
* Таблица reviews_user
  ```
  python manage.py users_csv
  ```

* Таблица reviews_category
  ```
  python manage.py category_csv
  ```

* Таблица reviews_genre
  ```
  python manage.py genre_csv
  ```

* Таблица reviews_title
  ```
  python manage.py title_csv
  ```

* Таблица reviews_title_genre
  ```
  python manage.py genre_title_csv
  ```

  Полная документация доступна по адресу http://127.0.0.1:8000/redoc/
## Участники:

[Анатолий Бессмертный](https://github.com/AnatoliiBessmertnyi). 
Управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

[Денис Дриц](https://github.com/Den2605). 
Категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты.

[Антон Майдаровский](https://github.com/antonvm26). 
Отзывы (Review) и комментарии (Comments): модели и view, эндпойнты. Рейтинги произведений.
