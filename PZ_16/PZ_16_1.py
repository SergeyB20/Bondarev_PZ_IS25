<<<<<<< HEAD
# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником.

=======
>>>>>>> origin/main
class student:

    def __init__(self, name, sec_n, marks):
        self.name = name
        self.sec_n = sec_n
        self.marks = marks

    @staticmethod
    def ave_marks(marks):
        average = sum(marks) / len(marks)
        return average

    @staticmethod
    def respect(average):
<<<<<<< HEAD
        st_is_otl = average == 5
=======
        st_is_otl = 'TRUE' if average == 5 else 'FALSE'
>>>>>>> origin/main
        return st_is_otl


Bondarev = student('Сергей', 'Бондарев', [2, 1, 2, 3, 4, 5, 3])

print(Bondarev.ave_marks(Bondarev.marks))
print('Student is otlichnik -', Bondarev.respect(Bondarev.ave_marks(Bondarev.marks)))
