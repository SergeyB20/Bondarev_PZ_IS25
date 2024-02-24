# В матрице найти сумму отрицательных элементов в первой трети матрицы

import random
matrix = [[random.randint(-20,20) for i in range(3)] for i in range(3)]
a = 0
def cogl(towns):
    for town in towns:
            if town < 0:
                yield town

print('Отрицательные числа: ',(list(cogl(matrix[0]))))
print('Сумма отрицательных чисел: ',sum(list(cogl(matrix[0]))))
