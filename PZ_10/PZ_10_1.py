"""
Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
Италия . РейнаТур – Англия,Япония,Канада,ЮАР. Определить:
1. какие туры из Вояж, отсутствуют в РейнаТур.
2. какие туры из РейнаТур, отсутствуют в Вояж
3. перечень одинаковых туров.
4. равны ли перечни туров.
"""

Voyazh = {'Мексика','Канада','Израиль','Италия'}
ReinaTour = {'Англия','Япония','Канада','ЮАР'}

print('Туры из Вояж, отсутствующие в РейнаТур', Voyazh - ReinaTour)
print('Туры из РейнаТур, отсутствующие в Вояж', ReinaTour - Voyazh)
print('Перечень одинаковых туров:', Voyazh&ReinaTour)
print('Равны ли перечни туров -', Voyazh == ReinaTour)