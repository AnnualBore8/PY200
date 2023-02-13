from typing import Union


class El_car:
    """Класс создает объект Элетро-Мобиль с атрибутами модель машины (car_model), количество
    лошадиных сил (horse power от 50 до 2000) и пробегом до зарядки (distance_to_charge от 150 до 800)"""

    def __init__(self, car_model: str, horse_power: int, distance_to_charge: Union[int, float]):
        if not isinstance(car_model, str):
            raise TypeError('Модель машины должна быть указана словами')
        self.car_model = car_model

        if horse_power not in range(50, 2001):
            raise ValueError('Количество лошадиных сил должно быть в промежутке от 50 до 2000')
        self.horse_power = horse_power

        if distance_to_charge not in range(150, 801):
            raise ValueError('Пробег до зарядки должен составлять от 150 до 800')
        self.distance_to_charge = distance_to_charge

    def distance(self) -> Union[int, float]:
        """
        Определяет расстояние, которое сможет проехать автомобиль на одной зарядке
        :return: Количество километров до зарядки
        """
        pass

    def acceleration_to_100km_h(self) -> Union[int, float]:
        """
        Рассчитывает время разгона до 100 км в час в секундах
        :return: время разгона
        """
        pass


class Dog:
    """Класс создает объект Собака с атрибутами порода (breed), кличка (name) и возраст (age)"""

    def __init__(self, breed: str, name: str, age: Union[int, float]):
        if not isinstance(breed, str):
            raise TypeError('Порода собаки должна быть указана текстом')
        self.breed = breed

        if not isinstance(name, str):
            raise TypeError('Кличка собаки должна быть указана текстом')
        self.name = name

        if age not in range(1, 21):
            raise ValueError('Возраст собаки должен быть указан в промежутке от 1 до 20')
        self.age = age

    def bark(self):
        """
        Выводит текстом лай собаки
        :return: "Woof, woof!"
        """
        pass

    def human_age(self):
        """
        Пересчитывает возраст собаки в человеческий возраст
        :return: Сколько было бы собаке лет, будь она человеком
        """
        pass


class Rectangle:
    """ Класс предназначен для работы с прямоугольниками. В качестве атрибутов выступает ширина ( width)
     и высота (height)"""

    def __init__(self, width: Union[int, float], height: Union[float, int]):
        if not isinstance(width, Union[float, int]):
            raise TypeError('Ширина должна быть указана в числовом формате')
        self.width = width

        if not isinstance(height, Union[int, float]):
            raise TypeError('Длина должна быть указана в числовом формате')
        self.height = height

    def area(self):
        """
        Считает площадь прямоугольника.
        :return: площадь
        """
        return self.width * self.height

    def perimeter(self):
        """
        Считает периметр прямоугольника.
        :return: периметр
        """
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    Ecar_1 = El_car('tesla', 600, 800)
    # Ecar_2 = El_car('tesla', 'ffff', 800)

    dog_1 = Dog('Golden Retriever', 'Freya', 1)
    # dog_2 = Dog('Golden Retriever', 111, 1)

    rect_1 = Rectangle(5, 7)
    rect_2 = Rectangle(5.5, 7.7)
    # rect_2 = Rectangle('wof', 7.7)

    # print(rect_1.area())
    # print(rect_1.perimeter())

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
