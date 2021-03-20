#   Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
#   К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#   Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
#   Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod

class ClovesAll(ABC):
    total_cons = 0

    @abstractmethod
    def __init__(self):
        pass

    @property
    def show_cons(self):
        print(f'Расход ткани на данное изделие - {self.consumption} \n'
              f'Общий расход ткани - {ClovesAll.total_cons} \n')

class Coat(ClovesAll):

    def __init__(self, size):
        self.consumption = round(size / 6.5 + 0.5, 2)
        ClovesAll.total_cons += self.consumption

class Suit(ClovesAll):

    def __init__(self, growth):
        self.consumption = round(2 * growth + 0.3, 2)
        ClovesAll.total_cons += self.consumption

a = Coat(44)
print(a.consumption, ClovesAll.total_cons)
a.show_cons

b = Coat(44)
print(b.consumption, ClovesAll.total_cons)
b.show_cons

c = Suit(1.75)
print(c.consumption, ClovesAll.total_cons)
c.show_cons

