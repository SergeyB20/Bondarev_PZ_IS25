"""
 Сформировать и вывести целочисленный список размера 10, содержащий степени
двойки от первой до 10-й: 2, 4, 8,16, ... .
"""

def spet():
    two = []
    degree = 1
    for i in range(11):
        two.append(2**degree)
        degree += 1
    print(two)

spet()


