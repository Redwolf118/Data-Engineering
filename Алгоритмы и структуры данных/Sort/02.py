# Сортировка строк по длине
# Задача: отсортировать список строк по их длине в порядке возрастания.
# Пример: ["apple", "banana", "kiwi", "pear"] → ["kiwi", "pear", "apple", "banana"]

# Используя сортировку вставками
def sort_by_len(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and len(arr[j]) > len(key):
            arr[j+ 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

fruits = ["apple", "banana", "kiwi", "pear"] 
sort_fruits_by_len = sort_by_len(fruits)
print(sort_fruits_by_len)