#В матрице найти минимальный и максимальные элементы.

import random

matrix = [[random.randint(0,20) for i in range(3)] for i in range(3)]

print('Матрица: ',matrix)
print('Минимальный элемент: ',min(min(matrix)))
print('Максимальный элемент: ',max(max(matrix)))
