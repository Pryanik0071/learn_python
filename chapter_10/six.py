"""Task - 10.6. Изучение Python"""
try:
    a, b = int(input()), int(input())
except ValueError as err:
    print('Can\'t transform str value to int')
else:
    print(a + b)
