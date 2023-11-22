"""
Описать функцию Mean(параметры), вычисляющую среднее арифметическое
AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух положительных 
чисел X и Y. С помощью этой функции найти среднее арифметическое и среднее
геометрическое для пар (A, B), (A, C), (A, D), если даны A, B, C, D.
"""
from math import sqrt

numbers = [5,3,4,2]
def AB():
    print('Результаты для A,B')
    Mean(numbers[0],numbers[2])

def AC():
    print('\nРезультаты для A,C')
    Mean(numbers[0], numbers[1])

def AD():
    print('\nРезультаты для A,D')
    Mean(numbers[0], numbers[3])

def Mean(X,Y):
    print('Среднее арифметическое: ', ((X + Y) / 2))
    print('Среднее геометрическое: ', (sqrt(X * Y)))

AB()
AC()
AD()