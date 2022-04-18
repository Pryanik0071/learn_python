"""Task - 10.1. Изучение Python"""
with open('learning_python.txt', encoding='utf-8') as f:
    content = f.read()
print(content)

with open('learning_python.txt', encoding='utf-8') as f_1:
    for line in f_1:
        print(line.rstrip())

list_ = []
with open('learning_python.txt', encoding='utf-8') as f_1:
    for line in f_1:
        list_.append(line.rstrip())
print(list_)
