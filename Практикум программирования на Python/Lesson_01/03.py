# Задача 3.
# Вычислите значение следующего выражения (аргументы - целые числа и вводятся с клавиатуры):
# f =  ∛((x^5  + 7)/(|-6| ⋅ y))/(7 - z mody)
# Округлите результат до 3-х знаков после запятой, используя функцию round().

import math

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

x_res = x ** 5 + 7
y_res = abs(-6) * y
z_res = 7 - (z%y)

cube_root = (x_res / y_res) ** (1/3)

result = round(cube_root / z_res, 3)

print("Результат:", result)