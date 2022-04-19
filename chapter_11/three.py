"""Task - 11.3. Работник"""
import unittest


class Employee:
    """Конструктор для работника"""
    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_=5000):
        """Прибавка, default = 5000"""
        self.salary += raise_


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.Jon = Employee('Jon', 'Snow', 10_000)

    def test_give_default_raise(self):
        self.Jon.give_raise()
        self.assertEqual(self.Jon.salary, 15_000)

    def test_give_custom_raise(self):
        self.Jon.give_raise(7_000)
        self.assertEqual(self.Jon.salary, 17_000)


if __name__ == '__main__':
    unittest.main()
