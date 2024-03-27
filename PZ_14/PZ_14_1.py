"""Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
произведения ими написанные. Посчитать общее количество произведений в данном
файле."""

import re


with open('writer.txt', 'r', encoding='utf-8') as file:
    data = file.read()

author = re.findall(r'(.+[)])|([«][^»]+)', data)

ag = re.findall(r'(?<=[«])[^»]+', data)

author = [[x for x in y if x!=""] for y in author]

for i in author:
    print(i)

print('Общее количество произведений -',len(ag))
