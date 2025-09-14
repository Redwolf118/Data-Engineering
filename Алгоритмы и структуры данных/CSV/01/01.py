# 1. Чтение CSV файла
# Написать программу, которая читает CSV файл со списком студентов и их оценок, 
# выводит содержимое на экран.

# Имя,Оценка
# Анна,5
# Борис,4
# Виктор,5


import csv

with open('students.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)