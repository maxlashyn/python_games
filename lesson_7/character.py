from random import randint
from lesson_7.options import *


class Character:
    name = ''
    hp = 0
    ap = 0
    heal = 0
    max_hp = 0

    def turn_in_fight(self, opponent):
        action = self.get_action()
        if action == ACTION_ATTACK:
            opponent.damage_done(self.ap)
        if action == ACTION_HEAL:
            self.hp = min(self.hp + self.heal, self.max_hp)

    def is_dead(self):
        return self.hp <= 0

    def damage_done(self, damage):
        self.hp -= damage

    def show_hp(self):
        print(f"{self.name}'s hp = {self.hp}")

    @staticmethod
    def get_action():
        return randint(ACTION_ATTACK, ACTION_HEAL)
