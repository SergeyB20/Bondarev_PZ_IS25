"""Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
произведения ими написанные. Посчитать общее количество произведений в данном
файле."""

import re
from collections import OrderedDict

with open('writer.txt', 'r', encoding='utf-8') as file:
    data = file.read()

author = re.findall(r'(.+[)])|(«(.* ?)»)', data)

result = [[x for x in y if x!=""] for y in author]
print(result)

# author = OrderedDict.fromkeys(author)
#
# for item1 in author:
#     print('\n',item1)
