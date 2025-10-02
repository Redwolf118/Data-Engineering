# Гистограмма
# Создать гистограмму распределения оценок студентов (данные: 4, 5, 3, 4, 5, 5, 4, 3, 2, 4)

import matplotlib.pyplot as plt

data = [4, 5, 3, 4, 5, 5, 4, 3, 2, 4]

plt.hist(data, bins=range(2, 7), color = 'green', edgecolor='black')  

plt.xlabel('Оценка')
plt.ylabel('Количество студентов')
plt.title('Гистограмма распределения оценок')
plt.xticks(range(2, 6)) 
plt.show()