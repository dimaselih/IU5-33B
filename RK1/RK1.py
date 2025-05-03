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


# Библиотеки
libs = [
    Library(1, 'Главная библиотека'),
    Library(2, 'Университетская библиотека'),
    Library(3, 'Городская библиотека'),
    Library(4, 'Детская библиотека'),
    Library(5, 'Научная библиотека'),
    Library(6, 'Историческая библиотека'),
]

# Книги
books = [
    Book(1, 'Война и мир', 'Лев Толстой', 1865, 1),
    Book(2, 'Анна Каренина', 'Лев Толстой', 1877, 1),
    Book(3, 'Преступление и наказание', 'Федор Достоевский', 1866, 2),
    Book(4, 'Братья Карамазовы', 'Федор Достоевский', 1880, 2),
    Book(5, '1984', 'Джордж Оруэлл', 1949, 3),
    Book(6, 'Скотный двор', 'Джордж Оруэлл', 1945, 3),
    Book(7, 'Мастер и Маргарита', 'Михаил Булгаков', 1939, 4),
    Book(8, 'Собачье сердце', 'Михаил Булгаков', 1925, 5),
    Book(9, 'Доктор Живаго', 'Борис Пастернак', 1957, 6),
    Book(10, 'Лолита', 'Владимир Набоков', 1955, 6),
]

# Связь книг и библиотек
books_libs = [
    BookLib(1, 1, 5),
    BookLib(1, 2, 3),
    BookLib(2, 3, 2),
    BookLib(2, 4, 1),
    BookLib(3, 5, 1),
    BookLib(3, 6, 2),
    BookLib(4, 7, 1),
    BookLib(5, 8, 3),
    BookLib(6, 9, 2),
    BookLib(6, 10, 1),
    BookLib(2, 1, 9),
    BookLib(3, 2, 8),
    BookLib(4, 3, 7),
    BookLib(5, 4, 6),
    BookLib(6, 5, 5),
    BookLib(6, 6, 4),
    BookLib(1, 7, 9),
    BookLib(3, 8, 3),
    BookLib(2, 9, 3),
    BookLib(1, 10, 10),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(b.title, b.author, b.year, l.name) 
    for l in libs 
    for b in books 
    if b.lib_id == l.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(lib.name, bl.lib_id, bl.book_id) 
        for lib in libs 
        for bl in books_libs 
        if lib.id == bl.lib_id]

    many_to_many = [(book.title, book.author, book.year, lib_name) 
        for lib_name, lib_id, book_id in many_to_many_temp
        for book in books if book.id == book_id]


    #B1
    #«Библиотека» и «Книга» связаны соотношением один-ко-многим. 
    #Выведите список всех книг, у которых название начинается с буквы «А», и названия их библиотек.

    print('Задание В1')
    result = [item for item in one_to_many if item[0].startswith('С')]
    for i in result:
        print(i[0],i[2])


    #B2
    #«Библиотека» и «Книга» связаны соотношением один-ко-многим. 
    #Выведите список отделов с минимальной годом создания книги в каждой библиотеке, 
    #отсортированный по минимальному году.

    print('\nЗадание В2')
    min_years = {}
    for title, author, year, lib in one_to_many:
        if lib not in min_years or year < min_years[lib]:
            min_years[lib] = year
    sorted_libs = sorted(min_years.items(), key=lambda x: x[1])
    for lib, year in sorted_libs:
        print(f"Библиотека: {lib}, Год самой старой книги: {year}")


    #B3
    #«Библиотека» и «Книга» связаны соотношением многие-ко-многим. 
    #Выведите список всех связанных книг и библиотек, отсортированный по книгам, 
    #сортировка по библиотекам произвольная. 
        
    print('\nЗадание В3')
    sorted_books = sorted(many_to_many, key=lambda x: (x[0], x[1]))
    for book in sorted_books:
        print(book[0],book[3])

if __name__ == '__main__':
    main()