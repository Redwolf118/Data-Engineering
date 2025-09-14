# 2. Чтение JSON-файла
# Дан файл data.json со следующей структурой:
# {
#     "name": "Иван",
#     "age": 20,
#     "courses": ["Математика", "Физика"]
# }

# Напишите программу, которая прочитает файл и выведет имя студента.

import json

with open('data.json', 'r') as json_file:
    student_data = json.load(json_file)

print("Имя студента: ", student_data["name"])
