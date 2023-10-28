"""Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить,
 имеются ли в записи числа N нечетные цифры. Если имеются, то вывести TRUE, если нет - вывести FALSE."""

def second_task():

    try:
        number = int(input('Введите любое целое число N, которое больше 0: '))
        if number > 0:
            div = 10
            first = 1
            ost = number % 10
            print(ost)
            while first != 0:
                first = number // div
                div = div * 10
                ost = first % 10
                print(first, ost)
        else:
            print('Введены некорректные данные')
            second_task()
    except:
        print('Введены некорректные данные')
        second_task()


second_task()