# Вариант 13. Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.

def pz2(number):
    try:
        number = int(number)
        #Проверка на отрицательность
        if number > 0:
            #Проверка на двузначность
            if len(str(number)) == 2:
                first = number // 10
                second = number % 10
                number = str(second)+str(first)
                print('Программа завершена, вот ваше число после перестановки цифр: ',number)
            else:
                print('Введены некорректные данные!')
                pz2(input('Введите двузначное число: '))

        else:
            num = number * -1
        #Проверка на двузначность
            if len(str(num)) == 2:
                first = num // 10
                second = num % 10
                number = str(second) + str(first)
                print('Программа завершена, вот ваше число после перестановки цифр: -',number)
            else:
                print('Введены некорректные данные!')
                pz2(input('Введите двузначное число: '))

    except ValueError:
        print('Введены некорректные данные!')
        pz2(input('Введите двузначное число: '))


pz2(input('Введите двузначное число: '))
