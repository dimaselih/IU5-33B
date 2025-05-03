# Рефакторинг и модульное тестирование библиотечной системы

## Рефакторинг кода

### Структура проекта после рефакторинга
```
library_system/
├── models.py         # Классы данных
├── data.py        # Тестовые данные
└── RK2.py           # Точка входа
```

### 1. Файл models.py (отдельные классы)
```python
class Book:
    """Класс книги с основной информацией"""
    def __init__(self, id, title, author, year, lib_id):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.lib_id = lib_id

class Library:
    """Класс библиотеки"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BookLib:
    """Класс для связи многие-ко-многим"""
    def __init__(self, lib_id, book_id, count):
        self.lib_id = lib_id
        self.book_id = book_id
        self.count = count
```

### 2. Файл queries.py (бизнес-логика)
```python
from models import Book, Library, BookLib

def create_one_to_many(libs, books):
    """Создание связи один-ко-многим"""
    return [
        (b.title, b.author, b.year, l.name) 
        for l in libs 
        for b in books 
        if b.lib_id == l.id
    ]

def create_many_to_many(libs, books, books_libs):
    """Создание связи многие-ко-многим"""
    temp = [
        (l.name, bl.lib_id, bl.book_id) 
        for l in libs 
        for bl in books_libs 
        if l.id == bl.lib_id
    ]
    return [
        (b.title, b.author, b.year, lib_name)
        for lib_name, lib_id, book_id in temp
        for b in books if b.id == book_id
    ]

def get_books_starting_with(one_to_many, letter):
    """Запрос B1: книги, начинающиеся с буквы"""
    return [item for item in one_to_many if item[0].startswith(letter)]

def get_libraries_min_year(one_to_many):
    """Запрос B2: библиотеки с минимальным годом книг"""
    min_years = {}
    for _, _, year, lib in one_to_many:
        if lib not in min_years or year < min_years[lib]:
            min_years[lib] = year
    return sorted(min_years.items(), key=lambda x: x[1])

def get_sorted_book_library_relations(many_to_many):
    """Запрос B3: отсортированные связи книг и библиотек"""
    return sorted(many_to_many, key=lambda x: (x[0], x[1]))
```

### 3. Файл test_data.py (тестовые данные)
```python
from models import Library, Book, BookLib

# Тестовые данные
libs = [
    Library(1, 'Главная библиотека'),
    # ... остальные библиотеки
]

books = [
    Book(1, 'Война и мир', 'Лев Толстой', 1865, 1),
    # ... остальные книги
]

books_libs = [
    BookLib(1, 1, 5),
    # ... остальные связи
]
```

## Модульные тесты (TDD подход)

### 1. Тесты моделей (test_models.py)
```python
import unittest
from models import Book, Library, BookLib

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book(1, 'Test', 'Author', 2000, 1)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, 'Test')
        # ... другие проверки

class TestLibrary(unittest.TestCase):
    def test_library_creation(self):
        lib = Library(1, 'Test Library')
        self.assertEqual(lib.id, 1)
        self.assertEqual(lib.name, 'Test Library')

class TestBookLib(unittest.TestCase):
    def test_book_lib_creation(self):
        book_lib = BookLib(1, 1, 5)
        self.assertEqual(book_lib.lib_id, 1)
        self.assertEqual(book_lib.book_id, 1)
        self.assertEqual(book_lib.count, 5)
```

### 2. Тесты запросов (test_queries.py)
```python
import unittest
from queries import *
from test_data import libs, books, books_libs

class TestQueries(unittest.TestCase):
    def setUp(self):
        self.one_to_many = create_one_to_many(libs, books)
        self.many_to_many = create_many_to_many(libs, books, books_libs)

    def test_books_starting_with_letter(self):
        result = get_books_starting_with(self.one_to_many, 'С')
        self.assertEqual(len(result), 2)  # Ожидаем 2 книги на 'С'
        titles = [item[0] for item in result]
        self.assertIn('Скотный двор', titles)

    def test_libraries_min_year(self):
        result = get_libraries_min_year(self.one_to_many)
        self.assertEqual(len(result), len(libs))
        # Проверяем что сортировка по году работает
        years = [year for _, year in result]
        self.assertEqual(years, sorted(years))

    def test_sorted_book_library_relations(self):
        result = get_sorted_book_library_relations(self.many_to_many)
        # Проверяем сортировку по названию книги
        titles = [item[0] for item in result]
        self.assertEqual(titles, sorted(titles))
```

## Основные изменения после рефакторинга

1. **Разделение ответственности**:
   - Модели данных вынесены в отдельный файл
   - Бизнес-логика выделена в отдельный модуль
   - Тестовые данные вынесены в отдельный файл

2. **Улучшение тестируемости**:
   - Каждая функция выполняет одну четкую задачу
   - Функции не зависят от глобальных переменных
   - Данные передаются явно через параметры

3. **Полноценное модульное тестирование**:
   - Тесты для всех основных компонентов
   - Тесты проверяют как корректность данных, так и бизнес-логику
   - Использован TDD подход с четкими проверками

4. **Гибкость и расширяемость**:
   - Легко добавлять новые запросы
   - Просто модифицировать существующую логику
   - Удобно добавлять новые тесты

Такой подход соответствует принципам чистой архитектуры и облегчает дальнейшую разработку и поддержку кода.
