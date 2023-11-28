"""
Дан список размера N. Найти номера тех элементов списка, которые больше своего
левого соседа, и количество таких элементов. Найденные номера выводить в
порядке их убывания.
"""

numbers = [12,24,123,6,178,3,63,1234,1,23,4,2]
def task6():
    try:
        number = 0
        nums_rev = []
        for numbers[number] in numbers:
            number +=1
         #   print(numbers[counter] , numbers[counter-1])
            if numbers[number] > numbers[number-1]:
                nums_rev.append(numbers.index(numbers[number]))

    except:
        print(numbers)
        print('Номера чисел, которые больше своего левого соседа: ', nums_rev[::-1] ,'\nКоличество элементов, соответсвующее условиям: ', len(nums_rev))


task6()