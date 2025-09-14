# Объединение CSV файлов
# Написать программу, которая объединяет несколько CSV файлов с одинаковыми заголовками в один файл.

# # file1.csv
# ID,Имя,Возраст
# 1,Анна,20
# 2,Борис,22

# # file2.csv
# ID,Имя,Возраст
# 3,Виктор,21
# 4,Галина,19

import csv

files = ["file1.csv", "file2.csv"]
output_file = "merged_files.csv"

all_rows = []

for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not all_rows: 
            fieldnames = reader.fieldnames
        for row in reader:
            all_rows.append(row)

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_rows)

print(f"Файлы {files} объединены в {output_file}")