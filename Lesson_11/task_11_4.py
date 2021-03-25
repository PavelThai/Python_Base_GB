# 4. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

# 5 + 5j

class ComplexNumber:

    def __init__(self, float_real, float_imaginary):
        self.real = float_real
        self.imaginary = float_imaginary

    def __add__(self, other):                     # сложение
        return ComplexNumber(self.real + other.real,
                             f'{int(self.imaginary.strip("i")) + int(other.imaginary.strip("i"))}i')

    def __mul__(self, other):                     # умножение   (a+bi) * (c+di) = (ac-bd) + (bc+ad)i
        real_result = self.real * other.real \
                      - int(self.imaginary.strip("i")) * int(other.imaginary.strip("i"))
        imaginary_result = f'{int(self.imaginary.strip("i")) * other.real + self.real * int(other.imaginary.strip("i"))}i'
        return ComplexNumber(real_result, imaginary_result)

a = ComplexNumber(1, '6i')
b = ComplexNumber(5, '-2i')
e = ComplexNumber(9, '-15i')

c = a + b + e
print(c.real, c.imaginary)

d = a * b * e
print(d.real, d.imaginary)