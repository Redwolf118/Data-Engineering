# Генерация данных
# Сгенерируйте файл csv более 1 млн строк с похожей структурой данных, запишите полученные данные CSV файл.

# Город,Население
# Москва,12000000
# Санкт-Петербург,5000000
# Новосибирск,1600000


import csv
import random

# Количество строк
num_rows = 1_000_000 

filename = "cities.csv"

with open(filename, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Город", "Население"]) 

    for i in range(1, num_rows + 1):
        city = f"Город_{i}"  
        population = random.randint(1, 25) * 1_000_000
        writer.writerow([city, population])

print(f"CSV файл '{filename}' с {num_rows} городами создан!")