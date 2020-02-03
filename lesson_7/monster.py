from random import randint
from lesson_7.character import Character
from lesson_7.options import *


class Monster(Character):
    def __init__(self, name):
        self.name = name
        self.hp = MAX_MONSTER_HP
        self.ap = randint(20, 90)
        self.heal = randint(35, 85)
        self.max_hp = MAX_MONSTER_HP
        self.pos = (0, 0)

    def set_position(self, x, y):
        self.pos = (x, y)

    def get_position(self):
        return self.pos
