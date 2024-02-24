# В матрице найти сумму отрицательных элементов в первой трети матрицы

import random
matrix = [[random.randint(-2,2) for i in range(6)] for i in range(6)]
a = 0
def cogl(towns):
    for town in towns:
        for i in town:
            if i < 0:
                yield i
print(matrix)
print(matrix[:(len(matrix)//3)])

print('Сумма отрицательных чисел: ',sum(list(cogl(matrix[:(len(matrix)//3)]))))
