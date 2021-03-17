"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""

class Stationery():
    title = 'cool'

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой')

class Pensil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером')

st = Stationery()
st.draw()

pn = Pen()
pn.draw()

pns = Pensil()
pns.draw()

hdl = Handle()
hdl.draw()





