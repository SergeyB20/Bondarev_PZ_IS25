"""
Дан список размера N. Обнулить элементы списка, расположенные между его
минимальным и максимальным элементами (не включая минимальный и
максимальный элементы).
"""

numbers = [12,1234,123,6,178,3,63,1,23,4,2]
def zero():
    print(numbers)
    max_num, min_num = numbers.index(max(numbers)), numbers.index(min(numbers))

    if max_num>min_num :
        for i in range(min_num+1,max_num):
            numbers[i]=0
    if max_num<min_num :
        for i in range(max_num+1,min_num):
            numbers[i]=0
    print('Список с обнулением чисел между максимальным и минимальным значением: ',numbers)

zero()