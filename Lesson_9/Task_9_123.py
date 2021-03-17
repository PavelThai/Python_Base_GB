#1. Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.

import time

class TrafficLight:
    __trafficlight_color = 'None'

    def running(self):
        self.__trafficlight_color = 'red'
        print(self.__trafficlight_color)
        time.sleep(7)
        self.__trafficlight_color = 'yellow'
        print(self.__trafficlight_color)
        time.sleep(2)
        self.__trafficlight_color = 'green'
        print(self.__trafficlight_color)
        time.sleep(5)

a = TrafficLight()
a.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.

class Road:
    _asphalt_weight_m2 = 0.025
    _asphalt_height_sm = 5

    def __init__(self, road_length, width):
        self._road_length = road_length
        self._width = width

    def weight(self):
        return self._road_length * self._width * self._asphalt_weight_m2 * self._asphalt_height_sm

r_1 = Road(5000, 20)
print(int(r_1.weight()))


#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_in

class Worker:

    def worker_name(self):
        self.worker_name = input(f'Введите имя сотрудника: ')
        return self.worker_name

    def worker_surname(self):
        self.worker_surname = input(f'Введите фамилию сотрудника: ')
        return self.worker_surname

    def worker_position(self):
        self.worker_position = input(f'Введите должность сотрудника: ')
        return self.worker_position

    def worker_income(self):
        self.salary = input(f'Введите зарплату сотрудника: ')
        self.bonus = input(f'Введите премию сотрудника: ')
        self.__worker_income = dict()
        self.__worker_income['Зарплата'] = [int(self.salary)]
        self.__worker_income['Премия'] = [int(self.bonus)]
        return self.__worker_income

class Position(Worker):

    def get_full_name(self):
        self.worker_name()
        self.worker_surname()
        self.full_name = str(f'{self.worker_name} {self.worker_surname}')
        return self.full_name

    def get_total_income(self):
        self.worker_income()
        self.total_income = int(self.salary) + int(self.bonus)
        return self.total_income

a = Position()
b = a.get_full_name()
print(b)
c = a.get_total_income()
print(c)