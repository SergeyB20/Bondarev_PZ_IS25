"""Организовать и вывести последовательность А из n чисел (n - четное). Из
последовательности А получить две последовательности В и С: в последовательности В –
первая половина элементов А,в С – вторая половина элементов А. Найти произведение
соответствующих элементов последовательностей В и С. Найти среднее арифметической
полученной последовательности."""
from functools import reduce
import random
colwo = int(input('Введите сколько будет чисел в последовательности(Четное количество): '))
if colwo % 2 == 0:
    list_ = [random.randint(0, 20) for i in range(colwo)]
    print(list_)
    listB,listC = [], []
    for i in list_:
        [listB.append(i) if list_.index(i) < ((len(list_)//2)-1) else listC.append(i)]
    print(listB,listC)
    A = [x * y for x, y in zip(listB, listC)]
    B = sum(A)/len(A)
    print('Произведение соответствующих элементов последовательностей', A)
    print('Среднее арифметическое полученной последовательности', B)


