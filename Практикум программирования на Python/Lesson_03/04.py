# Упражнение 4.
# Для введенного предложения выведите статистику символ=количество. Регистр букв не учитывается.

s = input("Введите предложение: ").lower()

stats = dict()

for char in s:
    stats[char] = stats.get(char, 0) + 1

print("Статистика символов:")

for char, count in stats.items():
    print(f"'{char}': {count}")

