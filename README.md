## Задание
Разработка системы управления библиотекой

## Описание
#### Необходимо разработать консольное приложение для управления библиотекой книг. 
#### Приложение должно позволять добавлять, удалять, искать и отображать книги. 
#### Каждая книга должна содержать следующие поля:
- id (уникальный идентификатор, генерируется автоматически)
- title (название книги)
- author (автор книги)
- year (год издания)
- status (статус книги: “в наличии”, “выдана”)

#### Требования
1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
2. Удаление книги: Пользователь вводит id книги, которую нужно удалить.
3. Поиск книги: Пользователь может искать книги по title, author или year.
4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

#### Дополнительные требования
- Реализовать хранение данных в текстовом или json формате.
- Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу).
- Написать функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
- Не использовать сторонние библиотеки.

## Использование

### Основные классы и методы

#### Класс Book

Представляет книгу с атрибутами, такими как ID книги, название, автор, год издания и статус.

##### Атрибуты

- `book_id` (int): Уникальный идентификатор книги.
- `title` (str): Название книги.
- `author` (str): Автор книги.
- `year` (int): Год издания книги.
- `status` (bool): Статус книги (True - "в наличии", False - "выдана"). По умолчанию True.

#### Класс Library

Управляет коллекцией экземпляров класса Book, включая загрузку и сохранение данных в JSON файл.

##### Методы

- `__init__(self, library_file='library.json')`: Инициализирует новый экземпляр библиотеки с указанием файла JSON для хранения данных.
- `load_books(self)`: Загружает книги из файла JSON.
- `save_books(self)`: Сохраняет текущий список книг в файл JSON.
- `generate_book_id(self)`: Генерирует новый уникальный ID книги.
- `add_book(self, title, author, year)`: Добавляет новую книгу в библиотеку.
- `delete_book(self, book_id)`: Удаляет книгу из библиотеки по ее ID.
- `find_books(self, **kwargs)`: Находит книги, соответствующие заданным критериям.
- `get_all_books(self)`: Возвращает все книги в библиотеке.
- `change_book_status(self, book_id, new_status)`: Изменяет статус книги.


## Установка и запуск проекта

Склонировать проект:

```
git clone https://github.com/ezemskov24/library_application_task.git
```

Для запуска основной программы выполните:

```
python main.py
```

Программа предложит вам выбрать команду для управления библиотекой:

- Добавить книгу
- Удалить книгу
- Найти книгу
- Получить все книги
- Изменить статус книги
- Выйти