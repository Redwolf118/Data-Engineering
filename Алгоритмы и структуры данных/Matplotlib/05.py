# Комбинированный график
# Построить график с несколькими типами визуализации: линия, столбцы, точки
# Настроить прозрачность элементов

import matplotlib.pyplot as plt

# Данные
x = [1, 2, 3, 4, 5]
y_line = [2, 3, 5, 7, 6]       # для линии
y_bar = [1, 4, 2, 6, 5]        # для столбцов
y_scatter = [3, 2, 4, 5, 7]    # для точек

# Строим столбцы
plt.bar(x, y_bar, color='skyblue', alpha=0.5, label='Столбцы')  # alpha=0.5 → прозрачность

# Строим линию
plt.plot(x, y_line, color='green', linestyle='-', linewidth=2, alpha=0.8, label='Линия')

# Строим точки
plt.scatter(x, y_scatter, color='red', s=100, alpha=0.7, label='Точки')  # s — размер точек

# Подписи и заголовок
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Комбинированный график: линия, столбцы, точки')
plt.legend()
plt.grid(True)

plt.show()