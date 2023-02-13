class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для описания бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация объекта бумажная книга (Paper Book)
        :param name: Название книги
        :param author: Имя автора
        :param pages: Количество страниц
        """

        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError('Неверный тип данных, страницы (pages) должны быть указаны целым числом (int)')
        if pages <= 0:
            raise ValueError('Количество страниц (pages) в книге должно быть указано числом больше 0')
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}."

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.name}, {self.author}, {self.pages})'


class AudioBook(Book):
    """Класс для описания аудиокнига"""
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация объекта аудиокнига
        :param name: название аудиокниги
        :param author: автор аудиокниги
        :param duration: продолжительность аудиокниги
        """

        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError('Продолжительность книги (duration) должна быть указана как десятичная дробь')
        if duration <= 0:
            raise ValueError('Продолжительность книги (duration) должна быть больше 0')
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}."

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.author}, {self.duration})'


if __name__ == "__main__":
    # book = Book('ghbdtn', 'ghjghjg')
    # print(book)

    paper_book = PaperBook('Привет', 'poka', 45)
    print(paper_book)

    audio_book = AudioBook('Цветы для Элджернона', 'Дэниел Киз', 312.32)
    print(audio_book)

    audio_book1 = audio_book.__repr__()
    print(audio_book1)
