# В матрице найти сумму отрицательных элементов в первой трети матрицы

import random

matrix = [[random.randint(-20,20) for i in range(3)] for i in range(3)]

print('Матрица: ',matrix)

sum_of_neg =lambda nums: sum(num for num in matrix[0] if num < 0)

print((sum_of_neg(matrix[0])))