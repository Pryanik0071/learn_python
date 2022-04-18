"""Task - 10.3. Гость"""

name = input('Enter your name, user: ')
with open('guest.txt', 'w') as f:
    f.write(name)

with open('guest.txt') as f:
    file = f.read()
print(file)
