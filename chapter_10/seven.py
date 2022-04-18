"""Task - 10.7. Изучение Python"""
while True:
    try:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
    except ValueError as err:
        print('Can\'t transform str value to int')
    else:
        print(a + b)
