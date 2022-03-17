"""Task - 9.14. Лотерея"""
import string
from random import choice


def lottery():
    numbers = list(range(10))
    letters = [choice(string.ascii_lowercase.upper()) for _ in range(4)]
    list_ = numbers + letters
    return [choice(list_) for _ in range(4)]


if __name__ == '__main__':
    print(*lottery(), sep='')
