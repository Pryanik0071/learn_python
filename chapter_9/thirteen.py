"""Task - 9.13. Кубики"""
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(f'Sides = {self.sides}, number - {number}')


if __name__ == '__main__':
    six = Die()
    for _ in range(10):
        six.roll_die()
    twenty = Die(20)
    for _ in range(10):
        twenty.roll_die()
