# Упражнение 6.
# Напишите функцию, которая принимает неограниченное количество числовых аргументов и возвращает кортеж из двух списков:
# ●	отрицательных значений (отсортирован по убыванию);
# ●	неотрицательных значений (отсортирован по возрастанию).

def sort_numbers(*args):
    negatives = sorted((x for x in args if x < 0), reverse=True)
    non_negatives = sorted(x for x in args if x >= 0)
    return (negatives, non_negatives)

result = sort_numbers(3, -1, 4, -5, 0, 2, -3)
print(result) 
