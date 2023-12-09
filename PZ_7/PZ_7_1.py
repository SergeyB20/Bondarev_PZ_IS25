#Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N

def first():
    try:
        number = int(input('Введите число от 32 до 126: '))
        if 32 < number < 126:
            print('Символ с кодом вашего числа: ', chr(number))
        else:
            print('Неверные данные!')
            first()
    except:
        print('Неверные данные!')
        first()

first()