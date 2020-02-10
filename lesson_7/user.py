from options import *
from character import Character
from random import randint


class User(Character):
    def __init__(self, name):
        self.inventory = []
        self.pos = (0, 0)
        self.direction = 'w'
        self.message = ''
        self.name = name
        self.hp = MAX_USER_HP
        self.ap = randint(20, 90)
        self.heal = randint(35, 85)
        self.max_hp = MAX_USER_HP

    def turn(self, field):
        print(f'Текущая позиция ({self.pos[0]}, {self.pos[1]})')
        c = input('Ваше действие [w, s, a, d, i, f, h, r, x]:')
        if c in ('w', 's', 'a', 'd'):
            self.move_to(c, field)
        if c == 'x':
            self.axe_tree(field)
        if c == 'i':
            self.put_treasure(field)
        if c == 'r':
            self.read_letter(field)
        if c == 'f':
            self.fight(field)
        if c == 'h':
            self.escape_from_monster(field)

    def read_letter(self, field):
        new_pos = self.get_new_pos(self.direction)
        objects = field.get_objects(new_pos[0], new_pos[1])
        if objects == LETTER:
            field.remove(new_pos[0], new_pos[1])
            treasure_pos = field.get_pos_nearest_treasure(new_pos[0], new_pos[1])
            if treasure_pos is None:
                self.message = 'Сокровищ больше нет'
            else:
                self.message = f'Ближайшее сокровище находится в ({treasure_pos[0]},{treasure_pos[1]})!'

    def put_treasure(self, field):
        new_pos = self.get_new_pos(self.direction)
        objects = field.get_objects(new_pos[0], new_pos[1])
        if objects == TREASURE:
            field.remove(new_pos[0], new_pos[1])
            self.inventory.append(TREASURE)
            self.message = 'Мы открыли клад !'

    def axe_tree(self, field):
        new_pos = self.get_new_pos(self.direction)
        objects = field.get_objects(new_pos[0], new_pos[1])
        if objects == TREE:
            field.remove(new_pos[0], new_pos[1])
            self.message = 'Мы срубили дерево!'

    def fight(self, field):
        new_pos = self.get_new_pos(self.direction)
        objects = field.get_objects(new_pos[0], new_pos[1])
        if objects == MONSTER:
            monster = field.monster
            while True:
                monster.show_hp()
                self.show_hp()

                self.turn_in_fight(monster)
                if monster.is_dead():
                    field.monster_dead()
                    for i in range(10):
                        self.inventory.append(TREASURE)
                    break

                monster.turn_in_fight(self)
                if self.is_dead():
                    break

    def escape_from_monster(self, field):
        if self.direction == 'w':
            self.direction = 's'
        if self.direction == 's':
            self.direction = 'w'
        if self.direction == 'a':
            self.direction = 'd'
        if self.direction == 'd':
            self.direction = 'a'

    def move_to(self, c, field):
        self.direction = c
        new_pos = self.get_new_pos(c)
        objects = field.get_objects(new_pos[0], new_pos[1])
        if objects == STONE:
            self.message = 'Мы уперлись в камень!'
        elif objects == TREE:
            self.message = 'Мы уперлись в дерево!'
        elif objects in [TREASURE, LETTER]:
            self.message = 'Мы нашли сундук или письмо'
        elif objects == MONSTER:
            self.message = 'АААА!! Мы встретили злого монстра'
        else:
            self.message = 'Мы пошли дальше'
            field.move_to(self, new_pos[0], new_pos[1])

    def get_new_pos(self, c):
        new_pos = (0, 0)
        if c == 'w':
            new_pos = (self.pos[0], self.pos[1] - 1)
        if c == 's':
            new_pos = (self.pos[0], self.pos[1] + 1)
        if c == 'a':
            new_pos = (self.pos[0] - 1, self.pos[1])
        if c == 'd':
            new_pos = (self.pos[0] + 1, self.pos[1])
        return new_pos

    def show_inventory(self):
        print(f"В Вашем инвентаре {len(self.inventory)} сокровищ")

    def set_position(self, x, y):
        self.pos = (x, y)

    def get_position(self):
        return self.pos

    def show_message(self):
        if len(self.message) > 0:
            print(self.message)

    def get_action(self):
        return int(input('attack or heal: '))
