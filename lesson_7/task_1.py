"""
Adventure game типа "Симулятор ходьбы"


Плоский мир на котором могут быть объекты типа трава, дерево, камень, клад, инструкция, монстр.
Присутствует туман войны размером 4, 4 от позиции юзера

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
"вы уперлись лбом в дерево"x
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
SMOG = '#'
SMOG_RADIUS = 4

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
        self.user_pos = (0, 0)

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
        field_with_smog = self.get_field_with_smog()
        for y in range(MAP_HEIGHT + 1):
            print("".join(field_with_smog[y]))
        print(''.join(['-' for i in range(MAP_WIDTH)]))

    def append(self, user):
        x, y = MAP_WIDTH // 2, MAP_HEIGHT // 2
        while self.field[y][x] in (LETTER, TREASURE):
            x, y = get_random_pos()
        else:
            self.set_user_position(user, x, y)

    def get_objects(self, x, y):
        if x < 0 or x > MAP_WIDTH:
            return STONE
        if y < 0 or y > MAP_HEIGHT:
            return STONE
        return self.field[y][x]

    def move_to(self, user, x, y):
        user_pos = user.get_position()
        self.field[user_pos[1]][user_pos[0]] = GRASS
        self.set_user_position(user, x, y)

    def set_user_position(self, user, x, y):
        self.user_pos = (x, y)
        self.field[y][x] = USER
        user.set_position(x, y)

    def get_field_with_smog(self):
        field_with_smog = []
        for y in range(MAP_HEIGHT + 1):
            field_with_smog.append(self.field[y].copy())
            for x in range(MAP_WIDTH + 1):
                if x < self.user_pos[0] - SMOG_RADIUS or x > self.user_pos[0] + SMOG_RADIUS:
                    field_with_smog[y][x] = SMOG
                elif y < self.user_pos[1] - SMOG_RADIUS or y > self.user_pos[1] + SMOG_RADIUS:
                    field_with_smog[y][x] = SMOG
        return field_with_smog


class Monster:
    pass


class User:
    def __init__(self):
        self.inventory = []
        self.pos = (0, 0)
        self.direction = 'w'
        self.message = ''

    def turn(self, field):
        c = input('Ваше действие [w, s, a, d, i, f, h, r, x]:')
        if c in ('w', 's', 'a', 'd'):
            self.direction = c
            new_pos = (0, 0)
            if c == 'w':
                new_pos = (self.pos[0], self.pos[1] - 1)
            if c == 's':
                new_pos = (self.pos[0], self.pos[1] + 1)
            if c == 'a':
                new_pos = (self.pos[0] - 1, self.pos[1])
            if c == 'd':
                new_pos = (self.pos[0] + 1, self.pos[1])
            objects = field.get_objects(new_pos[0], new_pos[1])
            if objects == STONE:
                self.message = 'Мы уперлись в камень!'
                return
            if objects == TREE:
                self.message = 'Мы уперлись в дерево!'
                return
            if objects in [TREASURE, LETTER]:
                self.message = 'Мы нашли сундук или письмо'
                return
            self.message = 'Мы пошли дальше'
            field.move_to(user, new_pos[0], new_pos[1])

    def show_inventory(self):
        print(f"В Вашем инвентаре {len(self.inventory)} сокровищ")

    def set_position(self, x, y):
        self.pos = (x, y)

    def get_position(self):
        return self.pos

    def show_message(self):
        if len(self.message) > 0:
            print(self.message)


field = Map()
field.generate()
user = User()
field.append(user)

while True:
    field.show()
    user.show_message()
    user.show_inventory()
    user.turn(field)
