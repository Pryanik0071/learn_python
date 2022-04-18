"""Task - 10.4. Гостевая книга"""
while True:
    name = input('Enter your name, user: ')
    if not name:
        break
    with open('guest_book.txt', encoding='utf-8', mode='a') as f:
        f.write(f'Welcome, {name.capitalize()}!\n')
