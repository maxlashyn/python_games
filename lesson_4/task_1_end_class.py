"""
текстовая игра
генерируются два объекта игрок и монстр,
здоровье и сила атаки рандомные
ходят по очереди
у каждого есть два варианта действия "атака" и "лечиться"
за монстра играет компьютер. выбор действия: рандомно, шаблонно
побеждает выживший
"""

from random import randint


ACTION_ATTACK = 1
ACTION_HEAL = 2
MAX_USER_HP = randint(700, 900)
MAX_MONSTER_HP = randint(700, 900)


class Character:
    name = ''
    hp = 0
    ap =  0
    heal = 0 
    max_hp = 0 

    def turn(self, opponent):
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

class User(Character):
    def __init__(self, name):
        self.name = name
        self.hp = MAX_USER_HP
        self.ap = randint(20, 90) 
        self.heal = randint(35, 85) 
        self.max_hp = MAX_USER_HP

    def get_action(self):
        return int(input('attack or heal: '))

        
class Monster(Character):
    def __init__(self, name):
        self.name = name
        self.hp = MAX_MONSTER_HP
        self.ap = randint(20, 90) 
        self.heal = randint(35, 85) 
        self.max_hp = MAX_MONSTER_HP

    def get_action(self):
        return randint(ACTION_ATTACK, ACTION_HEAL)


monster = Monster('Orc')
user = User('user')

while True:
    monster.show_hp()
    user.show_hp()

    user.turn(monster)
    if monster.is_dead():
        print('User win')
        break

    monster.turn(user)
    if user.is_dead():
        print('User lose')
        break
