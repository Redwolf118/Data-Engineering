# Сортировка с удалением дубликатов
# Задача: отсортировать список чисел, удалив дубликаты.
# Пример: [5, 2, 9, 1, 5, 2] → [1, 2, 5, 9]

def sort_unique(arr):
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    
    # Сортировка вставками
    n = len(unique)
    for i in range(1, n):
        key = unique[i]
        j = i - 1
        while j >= 0 and unique[j] > key:
            unique[j + 1] = unique[j]
            j -= 1
        unique[j + 1] = key
    return unique

numbers = [5, 2, 9, 1, 5, 2]
print(sort_unique(numbers))  # [1, 2, 5, 9]