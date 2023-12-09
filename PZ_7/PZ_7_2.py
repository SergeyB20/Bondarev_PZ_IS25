"""Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
расставлены правильно (то есть каждой открывающей соответствует одна
закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
в которой расположена первая ошибочная закрывающая скобка, или, если
закрывающих скобок не хватает, число —1"""

string = 'Hel(l))o world'
skob = []
counter = 0
right = 0
left = 0
for i in string:
    if i == '(':
        skob.append(i)
        right += 1
    elif i == ')':
        left += 1
        if len(skob) > 0 and skob[-1] == '(':
            skob.pop()
        else:
              counter = -1

if right > left:
    counter = -1

print(counter)


