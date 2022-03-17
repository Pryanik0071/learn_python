"""9.15 Анализ лотереи"""
from chapter_9.fourteen import lottery

if __name__ == '__main__':
    my_ticket = [1, 2, 3, 'T']
    count = 0
    while True:
        if lottery() != my_ticket:
            count += 1
        else:
            print(count)
            break
