import hashlib
import random
import re
from typing import Union
from product_generator import gen_product


class IdCounter:
    def __init__(self):
        self.id = 0

    def get_new_id(self):
        self.id += 1
        return self.id

    def set_id(self, value):
        self.id = value


class Password:
    """
    Класс содержит данные о значении пароля.
    Использует методы:
    get - чтобы получить первоначальный пароль и проверить его корректность.
    check - чтобы сопоставить хэш первоначального пароля и нового.
    """

    def __init__(self):
        self.password_hash = None

    def get(self, password: str):

        """
        Принимает строку пароля как input, проводит проверку пароля на
        то, что введенные данные являются строкой, имеют длину не менее 8 символов
        и то, что строка содержит как буквы, так и цифры.

        После этого создает и хранит хэш данные пароля.
        """

        if not isinstance(password, str):
            raise TypeError('Пароль должен быть строкой')

        if len(password) < 8:
            raise ValueError('Пароль должен иметь длину не менее 8 символов')

        if not re.search(r'\d', password) or not re.search(r'[a-zZ-a]', password):
            raise ValueError('Пароль должен содержать буквы и цифры')

        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        return self.password_hash

    def check(self, password):

        """
        Берет пароль, который вводит пользователь и проверяет, является ли он строкой.
        После этого программа сравнивает данные введенного пароля с хэшем, если все совпадает, программа выводит
        'True', если нет выдает 'False'
        """

        if not isinstance(password, str):
            raise TypeError('Пароль должен быть строкой')
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()


class Product:
    """Класс для хранения информации о продукте"""

    id_counter = IdCounter()

    def __init__(self, name: str, price: Union[int, float], rating: Union[int, float]):
        """
        Инициализация объекта - продукт
        :param name: Название продукта
        :param price: Цена продукта
        :param rating: Рейтинг продукта
        """
        self._id = Product.id_counter.get_new_id()

        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')
        self._name = name

        if not isinstance(price, Union[int, float]):
            raise TypeError('Цена должна быт указано в числовом формате int или float')
        if not price >= 0:
            raise ValueError('Цена должна быть положительным числом больше 0')
        self._price = price

        if not isinstance(rating, Union[int, float]):
            raise TypeError('Рейтинг должен быть указан как целое число (int) или десятичная дробь (float)')
        if not 0 < rating < 10:
            raise ValueError('Рейтинг должен быть положительным числом больше от 0 до 10')
        self._rating = rating

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, Union[int, float]):
            raise TypeError('Цена должна быт указано в числовом формате int или float')
        if not value >= 0:
            raise ValueError('Цена должна быть положительным числом больше 0')
        self._price = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def price(self, value):
        if not isinstance(value, Union[int, float]):
            raise TypeError('Рейтинг должен быть указан как целое число (int) или десятичная дробь (float)')
        if not 0 < value < 10:
            raise ValueError('Рейтинг должен быть положительным числом больше от 0 до 10')
        self._rating = value

    def __str__(self):
        return f'{self.id}_{self.name}'

    def __repr__(self):
        return f'Продукт(Название="{self.name}", Цена={self.price}, Рейтинг={self.rating})'


class Cart:
    """
    Получает список продуктов, которые нужно положить в корзину.
    Добавляет новые продукты в корзину - метод add_product.
    Убирает продукты из корзины - метод remove_product.
    Хранит информацию о том, что в корзине - метод get_product .
    """

    def __init__(self):
        """Инициализация объекта - Корзина"""
        self._product_cart = []

    @property
    def product(self):
        return self._product_cart

    def add_product(self, product):
        """Добавляет новые продукты в корзину"""
        # self._product.append(product)
        self._product_cart.append(product)

    def remove_product(self, product):  # можно добавить try except, если продукт убрать нельзя
        """Убирает продукты из корзины"""
        self._product_cart.remove(product)

    def get_product(self):
        """Хранит информацию о том, что в корзине"""
        return self._product_cart

    def __str__(self):
        return f'Содержимое корзины: {self._product_cart}'


class User(Password, Cart):
    """Класс описывает пользователя и наследует информацию из классов Password и Cart"""
    id_counter = IdCounter()

    def __init__(self, username: str, password: str):
        super().__init__()

        self._id = User.id_counter.get_new_id()

        if not isinstance(username, str):
            raise TypeError('Имя пользователя должно быть строкой (str)')
        self._username = username

        self._password = self.get(password)

        self._bucket = Cart()

    @property
    def username(self):
        return self._username

    @property
    def bucket(self):
        return self._bucket

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f'id: {self._id}, username: {self.username}, password: password1, cart: {self.bucket}'

    def __repr__(self):
        return f'User(username={self._username}, password="password1"'


class Store:
    """Класс для описания магазина"""

    def __init__(self):
        """
        Инициализирует объект Магазин
        """
        self.product_par = []
        self.user_list = []

    def add_new_user_info(self):
        """
        Метод запрашивающий имя и пароль для создания пользователя.
        :return:
        """
        user_name = input('Введите имя пользователя: ')
        user_password = input('Введите пароль пользователя: ')
        # user_id = User.id
        self.user_list.append(User(user_name, user_password))
        # print(User.id)

    # def get_id(self):
    #     user_id = User.id
    #     return user_id

    def show_user_list(self):
        return f'Shop Users {self.user_list}'

    def add_product(self, product):
        self.product_par.append(next(gen_product()))
        self.user_list[0].bucket.add_product(self.product_par)

    def view_cart(self):
        print(f"Products in cart: {self.user_list[0].bucket}")

    def __str__(self):
        return f'{self.user_list} and {self.product_par}'


if __name__ == '__main__':


    # работа с классом Магазин
    store = Store()
    store.add_new_user_info()
    store.add_product(gen_product())
    print(store)

    store.add_product(gen_product())
    print(store)
    store.view_cart()
    print(store)

