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

monster = {'Name': 'Andrey', 'hp': MAX_MONSTER_HP, 'ap': randint(20, 90), 'heal': randint(35, 85)}
user = {'Name': 'Maxim', 'hp': MAX_USER_HP, 'ap': randint(20, 90), 'heal': randint(35, 85)}

while True:
    print(f"monsters hp = {monster['hp']}")
    print(f"users hp = {user['hp']}")
    action = int(input('attack or heal:'))
    if action == ACTION_ATTACK:
        monster['hp'] = monster['hp'] - user['ap']
    if action == ACTION_HEAL:
        user['hp'] = min(user['hp'] + user['heal'], MAX_USER_HP)
    if monster['hp'] <= 0:
        print('You win')
        break

    action = randint(ACTION_ATTACK, ACTION_HEAL)
    if action == ACTION_ATTACK:
        user['hp'] = user['hp'] - monster['ap']
    if action == ACTION_HEAL:
        monster['hp'] = min(monster['hp'] + monster['heal'], MAX_MONSTER_HP)
    if user['hp'] <= 0:
        print('You lose')
        break
