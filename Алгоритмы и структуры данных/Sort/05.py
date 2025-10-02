# Сортировка с сохранением исходных индексов
# Задача: отсортировать список чисел, но сохранить исходные индексы элементов.
# Пример: [5, 2, 9, 1] → [(3, 1), (1, 2), (0, 5), (2, 9)]

def sort_with_indices(arr):
    # Список кортежей (индекс, значение)
    indexed_arr = list(enumerate(arr))
    
    # Сортируем по значению числа (по второму элементу кортежа)
    sorted_indexed_arr = sorted(indexed_arr, key=lambda x: x[1])
    
    return sorted_indexed_arr

numbers = [5, 2, 9, 1]
sorted_numbers = sort_with_indices(numbers)
print(sorted_numbers)  # [(3, 1), (1, 2), (0, 5), (2, 9)]