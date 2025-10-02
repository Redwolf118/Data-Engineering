# Сортировка по сумме цифр
# Задача: отсортировать список чисел по сумме их цифр.
# Пример: [123, 45, 6, 789] → [6, 123, 45, 789] (суммы: 6, 6, 9, 24)


def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def sort_by_digit_sum(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and (sum_digits(arr[j]) > sum_digits(key) or
                        (sum_digits(arr[j]) == sum_digits(key) and arr[j] > key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


digits = [123, 45, 6, 789]
res = sort_by_digit_sum(digits)
print(res)
