import unittest
from main import Parameters  # импортируем то, что будем тестировать


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dog = Parameters('Веймаранер', 'Фрейя', 3, 50, 56, 'Grey')

    def tearDown(self) -> None:
        self.dog = None

    def test_food(self):
        self.assertEqual(self.dog.food(350), 36750.0)

        with self.assertRaises(TypeError):
            self.dog.food('puk')

        with self.assertRaises(ValueError):
            self.dog.food(-350)


if __name__ == '__main__':
    unittest.main()
