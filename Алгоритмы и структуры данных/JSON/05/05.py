# 5. Обработка ошибок
# Напишите программу, которая пытается прочитать JSON-файл 
# и обрабатывает возможные ошибки (файл не найден, некорректный формат).

import json

# Ошибка при отсутствии файла
filename = "data.json"
try:
    with open(filename, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Ошибка: файл {filename} не найден")

# Ошибка при неверном формате файла
filename = "data.csv"
try:
    with open(filename, "r") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print(f"Ошибка: файл {filename} содержит неккоретный формат, не JSON")