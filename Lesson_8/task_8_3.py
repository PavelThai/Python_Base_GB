# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# Можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from functools import wraps

def p_wrapper(func):

    @wraps(func)
    def log_type(*args):
        print(f"Аргументы функции: {', '.join(list(str(type(el)) for el in args))}")
        result = func(*args)
        print(f'Тип значения функции: {type(result)}')
        print(f'Название функции: {str(func).split()[1]}')
        return result

    return log_type

@p_wrapper
def calc_cube(*args):
   cube_list = [el ** 3 for el in args]
   return cube_list

# calc_cube = p_wrapper(calc_cube)

print(calc_cube(5, 6))
