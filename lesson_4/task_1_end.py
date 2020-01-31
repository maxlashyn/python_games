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
TYPE_USER = 1
TYPE_MONSTER = 2
MAX_USER_HP = randint(700, 900)
MAX_MONSTER_HP = randint(700, 900)

def turn(character, opponent, action):
    if action == ACTION_ATTACK:
        opponent['hp'] = opponent['hp'] - character['ap']
    if action == ACTION_HEAL:
        character['hp'] = min(character['hp'] + character['heal'], character['max_hp'])

def get_user_action():
    return int(input('attack or heal:'))

def get_monster_action():
    return randint(ACTION_ATTACK, ACTION_HEAL)

def is_dead(character):
    return character['hp'] <= 0

monster = {
        'Name': 'Andrey', 
        'hp': MAX_MONSTER_HP, 
        'ap': randint(20, 90), 
        'heal': randint(35, 85), 
        'type': TYPE_MONSTER, 
        'max_hp': MAX_MONSTER_HP
        }
user = {
        'Name': 'Maxim', 
        'hp': MAX_USER_HP, 
        'ap': randint(20, 90), 
        'heal': randint(35, 85), 
        'type': TYPE_USER, 
        'max_hp': MAX_USER_HP
        }

while True:
    print(f"monsters hp = {monster['hp']}")
    print(f"users hp = {user['hp']}")

    action = get_user_action()    
    turn(user, monster, action)
    if is_dead(monster):
        print('You win')
        break

    action = get_monster_action()
    turn(monster, user, action)
    if is_dead(user):
        print('You lose')
        break
