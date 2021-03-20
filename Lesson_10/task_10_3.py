# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и округление до целого числа деления клеток, соответственно.

class Cell():

    def __init__(self, partition):
        self.partition = partition

    def __add__(self, other):  # сложение
        return Cell(self.partition + other.partition)

    def __sub__(self, other):  # вычитание
        if self.partition >= other.partition:
            return Cell(self.partition - other.partition)
        else:
            return Cell(0)

    def __mul__(self, other):  # умножение
        return Cell(self.partition * other.partition)

    def __floordiv__(self, other):  # деление
        return Cell(self.partition // other.partition)

    def make_order(self, num):  # организовать ячейки по рядам.
        self.num = num
        user_str = '*' * self.partition
        result = '\n'.join([user_str[x:x+num] for x in range(0, len(user_str), num)])
        print(f'Результат упорядочивания {self.partition} ячеек в ряды по {self.num}: \n{result}')


a = Cell(18)
b = Cell(10)

c = a + b
print(f'Результат сложения клеток - {c.partition}')

d = a - b
print(f'Результат вычитания клеток - {d.partition}')

e = a * b
print(f'Результат умножения клеток - {e.partition}')

f = a // b
print(f'Результат целочисленного деления клеток - {f.partition}')

a.make_order(5)