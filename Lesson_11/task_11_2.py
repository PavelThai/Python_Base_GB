# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))


class MyZeroError(ZeroDivisionError): pass

def division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        raise MyZeroError
    else:
        return c

try:
    print(division(a, b))
except MyZeroError:
    print('Ошибка в функции - деление на ноль')

