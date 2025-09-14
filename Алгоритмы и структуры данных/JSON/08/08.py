# 8. Оптимизация хранения\
# Реализуйте сжатие JSON-данных перед сохранением в файл и их распаковку при чтении.

import json
import gzip

student_data = {
    "name": "Иван",
    "age": 20,
    "courses": ["Математика", "Физика"]
}

filename = "student_data.json.gz"

# Сохранение
with gzip.open(filename, "wt", encoding="utf-8") as f:
    json.dump(student_data, f, ensure_ascii=False)

print(f"Данные сохранены в сжатом виде: {filename}")

# Чтение и распаковка
with gzip.open(filename, "rt", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("\nЗагруженные данные:")
print(loaded_data)