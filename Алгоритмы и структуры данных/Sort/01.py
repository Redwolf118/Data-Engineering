# Сортировка чисел по убыванию
# Задача: отсортировать список чисел в порядке убывания, 
# не используя встроенные методы сортировки.
# Пример: [5, 2, 9, 1, 5] → [9, 5, 5, 2, 1]

# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

numbers = [5, 2, 9, 1, 5]
res = selection_sort(numbers)
print(res)