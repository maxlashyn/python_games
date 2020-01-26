user_name = 'Maxim'
user_hp = 1


def print_user(user_name, user_hp, user_ap, user_heal):
    pass


def deal_damage():
    pass


def deal_damage2(user):
    pass


user = {
    'name': 'Maxim',
    'hp': 1,
    'ap': 2,
    'heal': 3,
    'deal_damage': deal_damage2
}
print(user['name'])
print(user['deal_damage'](user))

# имитация словаря без возможности использовать как итеррируемый объект
class Max:
    pass

max = Max()
max.test = 'kaj;dkfj'
print(max.test)


# общие для всех экземпляров класса параметры
class User:
    name = 'Maxim'
    pass


user = User()  # эксземпляр класса User или объект
print(user.name)

from random import randint


class User2:
    name = 'Maxim User2'
    equip = ['chest', 'legs', 'bow']
    public = ''
    _protected = ''
    __private = ''

    def __init__(self, fio):
        self.ap = randint(1, 10)
        self.fio = fio

    def show_name(self):
        print(self.name)

    def show_equip(self):
        print(' '.join(self.equip))

    def add_equip(self, name):
        self.equip.append(name)


user = User2('Lashyn')
user.show_name()

user2 = User2('Kvashyn')
user2.name = 'user2 name'
user2.show_name()

user.show_name()

user.show_equip()

user2.add_equip('empty')  # побочный эффект от использования общих переменных
user2.show_equip()
user.show_equip()

print(user.fio)
print(user.ap)
print(user2.fio)
print(user2.ap)


# что делать если мы хотим реализовать ряд геометрических фигур квадрат, круг, треугольник

class Squere:
    angles = 4

    def perimetr(self):
        return 1 + 1

    def get_angles(self):
        return self.angles


class Circle:
    angles = 0

    def perimetr(self):
        return 1 + 2

    def get_angles(self):
        return self.angles


class Triangle:
    angles = 3

    def perimetr(self):
        return 4 + 4

    def get_angles(self):
        return self.angles

class Figure:
    angles = 0

    def get_angles(self):
        return self.angles


class Square2(Figure):
    angles = 4

    def perimetr(self):
        return 1 + 1

square = Square2()
print(square.get_angles())


# множественное наследование
class Ship:
    def can_swim(self):
        return True

class Plain:
    def can_fly(self):
        return True


class Ecranopla (Ship, Plain):
    name = ''

eqr = Ecranopla()

print(eqr.can_fly())
print(eqr.can_swim())

# iterators

for i in [1, 2, 3]:
    pass

class Iterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > 10:
            raise StopIteration
        return self.start


iter = Iterator(0)
for i in iter:
    print(i)

# генераторы

class Generator:
    def __init__(self, figures):
        self.data = figures

    def next(self):
        for i in range(len(self.data)):
            yield self.data[i]


gen = Generator([Squere(), Circle(), Triangle()])
for i in gen.next():
    print(i.get_angles())

