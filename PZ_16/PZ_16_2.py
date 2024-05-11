# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.

class human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class man(human):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.sex = sex

class woman(human):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)



Bondarev = man('Сергей', '18', 'Мужчина')

print(Bondarev.sex)

