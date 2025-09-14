# 7. Обработка больших данных
# Создать программу, которая обрабатывает большой CSV файл (более 1 млн строк) и находит топ-10 самых частых значений в определенном столбце.

# Данные взять из предыдущего задания (6-е задание)

import csv
from collections import Counter

filename = "cities.csv"  
column_name = "Население" 

counter = Counter()

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        value = row[column_name]
        counter[value] += 1

top_10 = counter.most_common(10)

print(f"Топ-10 значений в столбце '{column_name}':")
for value, count in top_10:
    print(f"{value}: {count} раз(а)")