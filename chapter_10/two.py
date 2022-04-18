"""Task - 10.2. Изучение C"""
with open('learning_python.txt', encoding='utf-8') as f:
    for line in f:
        print(line.replace('Python', 'Java').rstrip())
