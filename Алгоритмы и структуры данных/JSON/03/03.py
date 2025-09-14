# 3. Модификация данных
# Добавьте в JSON-объект новое поле email и обновите файл на диске.

import json

student_data = {
    "name": "Иван",
    "age": 20,
    "courses": ["Математика", "Физика"]
}

student_data["email"] = "ivan@misis.edu.ru"

with open('data.json', 'w') as json_write:
    json.dump(student_data, json_write, ensure_ascii=False, indent=4)