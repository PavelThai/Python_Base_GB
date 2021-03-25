# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
#   Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#   Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import  re

class Date:
    def __init__(self, date):
        self.data = date

    @classmethod
    def get_int(cls, date):
        date_dict = {'число': int(date.split('/')[0]),
                     'месяц': int(date.split('/')[1]),
                     'год': int(date.split('/')[2])}
        return date_dict

    @staticmethod
    def check_date(date):
        cheking = "Дата введена верно"
        date_dict = {'число': int(date.split('/')[0]),
                     'месяц': int(date.split('/')[1]),
                     'год': int(date.split('/')[2])}
        if date_dict['число'] > 31 or date_dict['число'] <= 0:
            cheking = 'Неверно введено число'
        if date_dict['месяц'] > 12 or date_dict['месяц'] <=0:
            cheking = 'Неверно введен месяц'
        if date_dict['год'] <= 0:
            cheking = 'Неверно введен год'
        return cheking

    # Решение через регулярку
    @staticmethod
    def check_date_reg(date):
        template = re.compile(r"(?P<day>(0?[1-9]|[12][0-9])|3[01])[\/\-]((?P<month>0?[1-9]|1[012]))[\/\-](?P<year>\d{4})")
        if template.search(date) is not None:
            user_dict = dict(*map(lambda x: x.groupdict(), template.finditer(date)))
            return "Дата введена верно"
        else:
            raise ValueError('Дата введена с ошибками')


a = Date('01/01/2021')

print(Date.get_int('19/01/2021'))
#print(Date.date_dict)               # не могу понять, почему не могу достучаться до аттрибута

print(Date.check_date('31/01/2001'))
print(Date.check_date_reg('31/01/2001'))
#print(Date.user_dict)               # не могу понять, почему не могу достучаться до аттрибута