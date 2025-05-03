import unittest
from models import Book
from models import Library
from models import BookLib

class TestBook(unittest.TestCase):
    def test_book_init(self):
        id = 1
        title = 'Война и мир'
        author = 'Лев Толстой'
        year = 1865
        lib_id = 1

        book = Book(id, title, author, year, lib_id)

        self.assertEqual(book.id, id)
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)
        self.assertEqual(book.year, year)
        self.assertEqual(book.lib_id, lib_id)

class TestLibrary(unittest.TestCase):
    def test_library_init(self):

        id = 1
        name = 'Главная библиотека'

        library = Library(id, name)

        self.assertEqual(library.id, id)
        self.assertEqual(library.name, name)

class TestBookLib(unittest.TestCase):
    def test_book_lib_init(self):
        lib_id = 1
        book_id = 1
        count = 10

        book_lib = BookLib(lib_id, book_id, count)

        self.assertEqual(book_lib.lib_id, lib_id)
        self.assertEqual(book_lib.book_id, book_id)
        self.assertEqual(book_lib.count, count)

if __name__ == '__main__':
    unittest.main()