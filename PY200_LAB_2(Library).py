from fff4 import get_random_book
from typing import Union, Optional


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """
    Класс описывает параметры книги

    Написать класс Book, конструктор которого будет инициализировать следующие атрибуты:

    id - идентификатор книги
    name - Название книги
    pages - Количество страниц в книге
    В классе объявлен метод __str__ и метод __repr__
    Метод __str__ должен возвращать строку формата, где "название_книги" берется с помощью атрибута name:
    Книга "название_книги"
    Метод __repr__ должен возвращать валидную python строку, по которой можно инициализировать точно такой же экземпляр.
    Book(id_=1, name='test_name_1', pages=200)
    """

    def __init__(self, idd: Union[int, str], name: str, pages: int):

        """Инициализация объекта книга """

        if not isinstance(idd, Union[int, str]):
            TypeError('ID книги должен быть указан в числовом виде или в виде число-буквенного кода в формате строки')
        self.id = idd

        if not isinstance(name, str):
            TypeError('Название книги должно быть написано текстом в форме str')
        self.name = name

        if not isinstance(pages, int):
            TypeError('Количество страниц должно быть указано целым числом')
        if pages <=0:
            raise ValueError('Количество страниц в книге не может быть отрицательным или равным 0')
        self.pages = pages

    def __str__(self) -> str:
        """Метод возвращает список книг"""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """ Метод возвращает список с атрибутами книг"""
        return f'{self.__class__.__name__}, id_={self.id}, name="{self.name}", pages={self.pages}'


# TODO написать класс Library
class Library:
    """ Класс-конструктор библиотеки, содержащий список книг"""
    def __init__(self, books: Optional = None):
        """
        Инициализация объекта библиотека.
        :param books: Список книг (Список объектов)
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод возвращает идентификатор для добавления новой книги. Если книги нет, то возвращает 1, а если
        книги есть, то возвращает идентификатор последней книги увеличенный на 1.
        :return: id будущей книги
        """
        if self.books is not None:
            book_id = len(self.books)
            next_book_id = book_id + 1
            return next_book_id
        else:
            return 1

    def get_index_by_book_id(self, book_id: int):
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError.

        :param book_id: id книги, которую нужно найти в библиотеке.
        :return: id книги в библиотеке или Ошибку
        """

        list_of_books_id = [book.id for book in self.books]

        for i in range(len(list_of_books_id)):
            if book_id == list_of_books_id[i]:
                return i

        if book_id not in list_of_books_id:
            raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':

    # BOOKS_DATABASE = [get_random_book() for _ in range(50)] # более интересная реализация, от преподавателя
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    #
    list_books = [
        Book(idd=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    # print([str(book) for book in list_books])
    # print([repr(book) for book in list_books])

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
