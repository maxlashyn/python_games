"""
Adventure game типа "Симулятор ходьбы"


Плоский мир на котором могут быть объекты типа трава, дерево, камень, клад, инструкция, монстр.

Игрок респается в средине карты.
Игрок может идти по траве, может рубить дерево (на месте срубленного дерева остается трава), не может пройти камень,
может читать инструкцию (после прочтения заменяется на траву), может подобрать в инвентарь клад и может драться
с монстром (интегрируем реализацию монстер хантер из предыдущих уроков) или убежать (монстры неподвижны)

Как выглядит процесс со стороны игрока:

"Вы попали в чудесный мир. Найдите все сокровища используя подсказки. Убивайте монстров."
"В Вашем инвентаре 0 сокровищ"

>>> Ваше действие [w, s, a, d, i, f, h, r, x]:?
где w, s, a, d - движение
i - собрать в инвентарь
r - читать инструкцию
x - рубить дерево
f - атаковать соседнего монстра
h - лечиться

если ходим и ход возможен:
"вы идете по зеленой траве"
если в клетке по ходу дерево:
"вы уперлись лбом в дерево"
>>> Ваше действие [w, s, a, d, i, f, h, r, x]:?

если в клетке сокровище:
    "Вы видите сокровище"
>>> Ваше действие [w, s, a, d, i, f, h, r, x]:?

и т.п.

в иснтрукции содержится направление и количество шагов до следующего сокровища
"Следующее сокровище находится выше-ниже-левее-правее на х шагов"

"""
from random import randint

MAP_WIDTH = 50
MAP_HEIGHT = 20
GRASS = ' '
TREE = '1'
STONE = 'D'
TREASURE = 'X'
LETTER = '@'
MONSTER = '&'
USER = 'H'

MAX_TREES = 500
MAX_STONES = 20
MAX_TREASURES = 7
MAX_LETTERS = MAX_TREASURES
MAX_MONSTERS = 2


def get_random_pos():
    return randint(0, MAP_WIDTH), randint(0, MAP_HEIGHT)


class Map:
    def __init__(self):
        self.field = []

    def generate(self):
        self.field = [
            [GRASS for i in range(MAP_WIDTH + 1)] for j in range(MAP_HEIGHT + 1)
        ]
        for i in range(MAX_TREES):
            x, y = get_random_pos()
            self.field[y][x] = TREE
        for i in range(MAX_STONES):
            x, y = get_random_pos()
            self.field[y][x] = STONE
        for i in range(MAX_TREASURES):
            x, y = get_random_pos()
            while self.field[y][x] == TREASURE:
                x, y = get_random_pos()
            else:
                self.field[y][x] = TREASURE
        for i in range(MAX_LETTERS):
            x, y = get_random_pos()
            while self.field[y][x] in (LETTER, TREASURE):
                x, y = get_random_pos()
            else:
                self.field[y][x] = LETTER

    def show(self):
        print(''.join(['-' for i in range(MAP_WIDTH)]))
        for y in range(MAP_HEIGHT + 1):
            print("".join(self.field[y]))
        print(''.join(['-' for i in range(MAP_WIDTH)]))

    def append(self, user):
        x, y = MAP_WIDTH // 2, MAP_HEIGHT // 2
        while self.field[y][x] in (LETTER, TREASURE):
            x, y = get_random_pos()
        else:
            self.field[y][x] = USER
            user.set_position(x, y)


class Monster:
    pass


class User:
    def __init__(self):
        self.inventory = []
        self.pos = (0, 0)

    def turn(self):
        c = input('Ваше действие [w, s, a, d, i, f, h, r, x]:')

    def show_inventory(self):
        print(f"В Вашем инвентаре {len(self.inventory)} сокровищ")

    def set_position(self, x, y):
        self.pos = (x, y)


field = Map()
field.generate()
user = User()
field.append(user)

while True:
    field.show()
    user.show_inventory()
    user.turn()
