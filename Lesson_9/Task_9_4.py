""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
class Car:
    color = 'red'
    name = 'zorro'
    speed = 0
    is_police = False

    def get_speed(self):
        self.speed = int(input('Введите скорость автомобиля (км/ч): '))
        return self.speed

    def show_speed(self):
        print(f'Скорость автомобиля - {self.speed} км/ч')

    def go(self):
        print('Автомобиль начал движение')

    def stop(self):
        print(f'Автомобиль остановился')

    def turn(self):
        direction = input('Введите направление поворота: ')
        print(f'Автомобиль повернул {direction}')

class TownCar(Car):
    type = 'town car'

    def show_speed(self):
       if self.speed > 60:
           print('Скорость автомобиля превышает допустимую')

class SportCar(Car):
    type = 'sport car'

class WorkCar(Car):
    type = 'work car'

    def show_speed(self):
        if self.speed > 40:
            print('Скорость автомобиля превышает допустимую')

class PoliceCar(Car):
    type = 'police car'
    is_police = True

car = Car()
print(car.name, car.color)
car.go()
car.get_speed()
car.show_speed()
car.turn()


wcar = WorkCar()
print(wcar.name, wcar.color, wcar.type)
wcar.go()
wcar.get_speed()
wcar.show_speed()



