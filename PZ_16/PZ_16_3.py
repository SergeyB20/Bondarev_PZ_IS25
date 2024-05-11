# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

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
        st_is_otl = average == 5
        return st_is_otl


def save_def(stud, file):
    with open(file, 'wb') as f:
        pickle.dump(stud, f)


def load_def(file):
    with open(file, 'rb') as f:
        they_bank = pickle.load(f)
    return they_bank

Bondarev = student('Сергей', 'Бондарев', [2, 1, 2, 3, 4, 5, 4])

save_def(Bondarev, 'students.pkl')
students = load_def('students.pkl')

for i in students:
    print(students.ave_marks(students.marks))
    print('Student is otlichnik -', students.respect(students.ave_marks(students.marks)))
