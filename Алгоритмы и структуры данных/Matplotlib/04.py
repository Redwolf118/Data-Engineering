# Несколько графиков
# Построить на одном графике функции синуса и косинуса
# Использовать разные цвета и стили линий


import matplotlib.pyplot as plt
import math

# Создаём точки по оси X
x = [i * 0.1 for i in range(-100, 101)]  # от -10 до 10 с шагом 0.1

# Вычисляем значения синуса и косинуса
y_sin = [math.sin(val) for val in x]
y_cos = [math.cos(val) for val in x]

# Строим графики
plt.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-')   # синяя сплошная линия
plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='--')   # красная пунктирная линия

# Подписи осей и заголовок
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций sin(x) и cos(x)')

# Легенда
plt.legend()
plt.grid(True)

plt.show()