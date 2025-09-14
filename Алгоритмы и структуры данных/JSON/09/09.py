# Валидация данных
# Напишите функцию для проверки корректности JSON-структуры по заданному шаблону 
# (например, проверка наличия обязательных полей).

import json

template = {
    "Имя": str,
    "Возраст": int,
    "Оценки": dict  # словарь с предметами и оценками
}


def validate_json(data, template):
    errors = []

    for key, expected_type in template.items():
        if key not in data:
            errors.append(f"Отсутствует поле: '{key}'")
        elif not isinstance(data[key], expected_type):
            errors.append(f"Неверный тип поля '{key}': ожидался {expected_type.__name__}, получен {type(data[key]).__name__}")

    return errors

# Корректный JSON
student = {
    "Имя": "Анна",
    "Возраст": 20,
    "Оценки": {"Математика": 5, "Физика": 4}
}

# Неправильный тип
# student = {
#     "Имя": "Александр",
#     "Возраст": "20",
#     "Оценки": {"Информатика": 5}
# }

# Отсутствие поля
# student = {
#     "Имя": "Мария",
#     "Возраст": 24,
# }

# Проверка
errors = validate_json(student, template)

if errors:
    print("Ошибки валидации:")
    for e in errors:
        print("-", e)
else:
    print("JSON корректен!")