# Составить функцию, которая напечатает 40 любых символов
from random import randint

symbols_list = ['a', 'b','c','d','e', 'f','j']
def any40s():
    try:
        word = len(symbols_list) - 1
        print('Ваши 40 любых символов: ')
        for i in range(40):
            a = randint(0, word)
            res = symbols_list[a]
            print(res)
    except:
        print("Произошла ошибка!")
        any40s()


any40s()