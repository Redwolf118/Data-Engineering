# 3. Фильтрация данных
# Написать программу, которая фильтрует CSV файл с данными о продажах, 
# оставляя только записи с суммой больше 1000 рублей.

# Дата,Товар,Сумма
# 01.01.2023,Телефон,1200
# 02.01.2023,Ручка,100
# 03.01.2023,Ноутбук,15000

import csv

input_file = "data.csv"
output_file = "filtered_data.csv"


with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    filtered = [row for row in reader if int(row["Сумма"]) > 1000]

with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Дата", "Товар", "Сумма"])
    writer.writeheader()
    writer.writerows(filtered)

print(f"Фильтрованные данные сохранены в {output_file}")