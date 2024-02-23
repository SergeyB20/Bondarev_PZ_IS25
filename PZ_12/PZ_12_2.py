'''Составить список, в который будут включены только согласные буквы и 
привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 
'Дели', 'Каир']'''

def cogl(towns):
    for town in towns:
        for bykva in town:
            if bykva.upper() not in ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']:
                yield bykva.upper()

towns = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
print(list(cogl(towns)))
