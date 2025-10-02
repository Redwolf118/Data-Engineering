import numpy as np


# 1. Создать вектор (одномерный массив) размера 10, заполненый нулями
print("Задание 1.")
vec_zeros = np.zeros(10)
print("\nВектор из нулей:", vec_zeros)

# 2. Создать вектор размер 10, заполненный единицами
print("\nЗадание 2.")
vec_ones = np.ones(10)
print("Вектор из единиц:", vec_ones)

# 3. Создать вектор размера 10, заполненный числом 2.5
print("\nЗадание 3.")
vec_value = np.full(10, 2.5)
print("Вектор из 2.5:", vec_value)

# 4. Создать вектор заполненный нулями, но пятый элемент равен 1
print("\nЗадание 4.")
vec_fifth_one = np.zeros(10)
vec_fifth_one[4] = 1
print("Вектор с пятым элементом 1:", vec_fifth_one)

# 5. Создать вектор со значениями от 10 до 49
print("\nЗадание 5.")
vec_10_to_49 = np.arange(10, 50)
print("Вектор от 10 до 49:", vec_10_to_49)

# 6. Развернуть вектор (первый становится последним)
print("\nЗадание 6.")
vec_reversed = vec_10_to_49[::-1]
print("Развернутый вектор:", vec_reversed)

# 7. Создать матрицу (двумерный массив) 3x3 со значениями от 0 до 8
print("\nЗадание 7.")
matrix_3x3 = np.arange(9).reshape(3, 3)
print("Матрица 3x3:\n", matrix_3x3)

# 8. Найти индексы ненулевых элементов в [1,2,0,0,4,0]
print("\nЗадание 8.")
array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array)[0]
print("Индексы ненулевых элементов:", non_zero_indices)

# 9. Создать массив 3x3x3 со случайными значениями
print("\nЗадание 9.")
random_3d_array = np.random.rand(3, 3, 3)
print("Случайный массив 3x3x3:\n", random_3d_array)

# 10. Создать массив 10x10 со случайными значениями, найти минимум и максимум
print("\nЗадание 10.")
random_10x10 = np.random.rand(10, 10)
min_value = random_10x10.min()
max_value = random_10x10.max()
print("Минимум в массиве 10x10:", min_value)
print("Максимум в массиве 10x10:", max_value)

# 11. Создать матрицу с 0 внутри и 1 на границах
print("\nЗадание 11.")
matrix_border = np.ones((10, 10))
matrix_border[1:-1, 1:-1] = 0
print("\nМатрица с 0 внутри и 1 на границах:\n", matrix_border)

# Создать матрицу 8x8 и заполнить ее в шахматном порядке
print("\nЗадание 12.")
chessboard = np.zeros((8, 8), dtype=int)
chessboard[1::2, ::2] = 1
chessboard[::2, 1::2] = 1
print("Шахматная матрица 8x8:\n", chessboard)

# Перемножить матрицы 5x3 и 3x2
print("\nЗадание 13.")
matrix_a = np.random.rand(5, 3)
matrix_b = np.random.rand(3, 2)
matrix_product = np.dot(matrix_a, matrix_b)
print("Произведение матриц 5x3 и 3x2:\n", matrix_product)

# Создать случайную матрицу 5x7 целых чисел от 1 до 100 и удалить [3,5] колонки
print("\nЗадание 14.")
random_matrix_5x7 = np.random.randint(1, 101, size=(5, 7))
matrix_deleted_cols = np.delete(random_matrix_5x7, [3, 5], axis=1)
print("Матрица 5x7 с удалёнными 3 и 5 колонками:\n", matrix_deleted_cols)

# Есть генератор, сделать с его помощью массив
# def generate():
#     for x in range(10):
#         yield x
print("\nЗадание 15.")
def generate():
    for x in range(10):
        yield x
array_from_generator = np.fromiter(generate(), dtype=int, count=10)
print("Массив из генератора:", array_from_generator)