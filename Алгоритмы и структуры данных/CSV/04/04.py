# 4. Подсчет статистики
# Создать программу, которая подсчитывает среднюю оценку по предмету из CSV файла с оценками студентов.

# Студент,Математика,Физика,Химия
# Анна,5,4,5
# Борис,4,3,4
# Виктор,5,5,5

import csv

input_file = "data.csv"

subjects = {}

with open(input_file, "r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        for subject, grade in row.items():
            if subject == "Студент":  # пропускаем колонку с именами
                continue
            grade = int(grade)
            if subject not in subjects:
                subjects[subject] = {"sum": 0, "count": 0}
            subjects[subject]["sum"] += grade
            subjects[subject]["count"] += 1


# вычисляем средние
print("Средние оценки по предметам:")
for subject, values in subjects.items():
    avg = values["sum"] / values["count"]
    print(f"{subject}: {avg:.2f}")