"""
Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
информацию из строки в словарь, найти среднее арифметическое
оценок, результаты вывести на экран.
"""
res = {}
text = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
text = text.split()

res['Оценки'] = []
for i in text[3:]:
    res['Оценки'].append(int(i))

average = 0
for i in res['Оценки']:
    average += i

print('Средняя оценка ученика:',average/len(res['Оценки']))