# Простой линейный график
# Построить график функции  𝑦=𝑥2  на отрезке [-10, 10]
# Добавить заголовок графика
# Подписать оси координат


import matplotlib.pyplot as plt

x =  list()
y = list()

step = 0.1 
current = -10
while current <= 10:
    x.append(current)
    y.append(current ** 2)
    current += step

# Строим график
plt.plot(x, y, label='y = x^2', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = x^2')
plt.grid(True)
plt.legend()
plt.show()