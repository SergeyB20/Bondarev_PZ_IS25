# Вариант 2
# Дано целое число А. Проверить истинность высказывания: "Число А является положительным".
def first():
    try:
        number = int(input('Введите целое число: '))
        if (number % 2) != 1:
            print('Введено четное число!')
        else:
            print('Введено нечетное число!')

    except:
        print('Введены некорректные данные!')
        first()

first()

'''
При открытии вклада в банке установлены следующие годовые проценты:
    при вкладе до 50000р. процент составит 4%;
    при вкладе от 50000р. до 100000р. процент составит 5%;
    при вкладе от 100000р. до 150000р. скидка составит 6%;
    при вкладе от 150000 р. до 200000 р. процент составит 7%. 
Составить программу, определяющую процентной ставки в зависимости от вносимой суммы.
'''
def second():
    try:
        money = int(input('Введите кол-во денег, которые вы бы хотели внести на вклад: '))
        if money > 0:
            if 200000 >= money > 150000:
                print("Ваш процент вклада составит 7%")
            if 150000 >= money > 100000:
                print("Ваш процент вклада составит 6%")
            if 100000 >= money > 50000:
                print("Ваш процент вклада составит 5%")
            if money <= 50000:
                print("Ваш процент вклада составит 4%")
            if money > 200000:
                print('Ваша сумма денег слишком велика для нашего банка')
        else:
            print('Введены некорректные данные!')

    except:
        print('Введены некорректные данные')

second()
