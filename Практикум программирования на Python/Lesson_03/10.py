# Упражнение 10.

# Магическими называются даты, в которых произведение дня и месяца составляет последние две цифры года. 
# Например, 10 июня 1960 года – магическая дата, поскольку 10 ´ 6 = 60. 
# Напишите функцию, определяющую, является ли введенная дата магической. 
# Используйте написанную функцию в главной программе для отображения всех магических дат в XX ве­ке.

def is_magic_date(day, month, year):
    return day * month == year % 100

def find_magic_dates():
    magic_dates = []
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                # Проверка корректности даты
                if (month == 2 and day > 29) or \
                   (month in [4, 6, 9, 11] and day > 30):
                    continue
                if is_magic_date(day, month, year):
                    magic_dates.append(f"{day:02d}-{month:02d}-{year}")
    return magic_dates

magic_dates = find_magic_dates()
print("Магические даты в XX веке:")
for date in magic_dates:
    print(date)
