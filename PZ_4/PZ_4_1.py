"""Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
 расположенные между A и B (не включая числа A и B), а также количество N этих чисел."""


def first_task():
    try:
        first = int(input('Введите любое целое число A: '))
        second = int(input('Введите любое целое число, которое больше A: '))
        #Ввод счётчика
        if first < second:
            counter = 0
            #Вывод чисел и подсчёт их количества
            while first < second-1:
                second -= 1
                counter += 1
                print(second)
            print('Количество целых цифр между введенными значениями: ', counter)

        else:
            print('Введены некорректные данные!')
            first_task()
    except:
        print('Введены некорректные данные!')
        first_task()


first_task()