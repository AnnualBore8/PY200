from typing import Union


class Dog:
    """Класс создает объект Собака с атрибутами порода (breed), кличка (name) и возраст (age)"""

    def __init__(self, breed: str, name: str, age: Union[int, float]):
        """
        Инициализация объекта собака

        :param breed: Порода собаки
        :param name: Кличка собаки
        :param age: Возраст собаки
        """

        if not isinstance(breed, str):
            raise TypeError('Порода собаки должна быть указана текстом')
        self._breed = breed

        if not isinstance(name, str):
            raise TypeError('Кличка собаки должна быть указана текстом')
        self._name = name

        if age not in range(1, 21):
            raise ValueError('Возраст собаки должен быть указан в промежутке от 1 до 20')
        self._age = age

    @property
    def breed(self):
        return self._breed

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def bark(self):
        """
        Выводит текстом лай собаки
        :return: "Woof, woof!!!"
        """
        return f'{self.breed} - {self.name} говорит Woof, woof!!!'

    def human_age(self):
        """
         Пересчитывает возраст собаки в человеческий возраст

        :param human_age: возраст собаки переведенный в человеческие года
        :return: Сколько было бы собаке лет, будь она человеком
        """
        if 0 <= self.age <= 2:
            human_age = self.age * 12
        else:
            human_age = 24 + (self.age - 2) * 4

        return f'Возраст собаки породы {self.breed} по кличке {self.name} при переводе в человеческие года ' \
               f'составляет {human_age}.'


class Parameters(Dog):
    """Класс описывающий параметры собаки"""

    def __init__(self, breed, name, age, weight: Union[int, float], height: Union[int, float], color: str):
        """
        Инициализация объекта собака с расширенными параметрами
        :param weight: Вес собаки
        :param height: Рост собаки
        :param color: Цвет собаки
        """
        super().__init__(breed, name, age)

        if not isinstance(weight, Union[int, float]):
            raise TypeError('Вес собаки должен быть указан целым числом или десятичной дробью')
        if not 0 < weight <= 100:
            raise ValueError('Вес собаки должен быть больше 0, но меньше 100 кг.')
        self._weight = weight

        if not isinstance(height, Union[int, float]):
            raise TypeError('Рост собаки должен быть указан целым числом или десятичной дробью')
        if not 0 < height <= 120:
            raise ValueError('Рост собаки должен быть больше 0, но меньше 100 см.')
        self._height = height

        if not isinstance(color, str):
            raise TypeError('Цвет собаки должен быть указан текстом')
        self._color = color

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._weight

    @property
    def color(self):
        return self._color

    @height.setter
    def height(self, height: Union[int, float]):
        if not isinstance(height, Union[int, float]):
            raise TypeError('Рост собаки должен быть указан целым числом или десятичной дробью')
        if 0 < height <= 120:
            raise ValueError('Рост собаки должен быть больше 0, но меньше 100 см.')
        self._height = height

    @color.setter
    def color(self, color: str):
        if not isinstance(color, str):
            raise TypeError('Цвет собаки должен быть указан текстом')
        self._color = color

    @staticmethod
    def competitions(self):
        """
        Метод описывает параметры собаки для участия в соревнованиях.
        :return: текст описывающий все необходимы параметры собаки
        """
        return f'\nПараметры собаки для участия в соревнованиях: \nПорода: {self.breed} \nКличка: {self.name}\n' \
               f'Возраст: {self.age} \nВес: {self.weight} \nРост: {self.height} \nЦвет: {self.color}'

    def food(self, price: Union[int, float]):
        """
        Рассчитывает количество еды необходимой собаке в день в кг. И затраты на корм в месяц.
        :param price: стоимость килограмма еды.
        :return: Массу еды в кг.
        """
        if not isinstance(price, Union[int, float]):
            raise TypeError('Стоимость корма должна быть указана целым числом или десятичной дробью')
        if price <= 0:
            raise ValueError('Стоимость корма должна быть больше 0 рублей')

        day_food = round(self.weight * 0.07, 2)
        monthly_expenses = round(30 * day_food * price, 2)
        # return f'Собака {self.name} должна кушать {day_food} кг. собачьего корма в день! Затраты на еду в месяц: {monthly_expenses} рублей.'
        return monthly_expenses


if __name__ == "__main__":
    dog = Dog('Веймаранер', 'Фрейя', 3)
    print(dog.bark())

    print(dog.human_age())

    dog_par = Parameters('Веймаранер', 'Фрейя', 3, 50, 56, 'Grey')
    print(Parameters.competitions(dog_par))
    print(Parameters.food(dog_par, 350))
