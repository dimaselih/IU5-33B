class Book:
    """Книга"""
    def __init__(self, id, title, author, year, lib_id):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.lib_id = lib_id

class Library:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BookLib:
    """
    'Книги в библиотеке' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lib_id, book_id, count):
        self.lib_id = lib_id
        self.book_id = book_id
        self.count = count
