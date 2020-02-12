from random import randint

ATTACK = 1
HEAL = 2
MAX_USER_HP = randint(1300, 1800)
MAX_MONSTER_HP = randint(1300, 1800)
user = {'Name': 'Maxim', 'hp': MAX_USER_HP, 'ap': randint(150, 210), 'heal': randint(120, 200)}
monster = {'Name': 'Andrey', 'hp': MAX_MONSTER_HP, 'ap': randint(100, 170), 'heal': randint(150, 200)}

while True:
    print(f"user hp = {user['hp']}")
    print(f"monster hp = {monster['hp']}")
    action = int(input('attack or heal:'))
    if action == ATTACK:
        monster['hp'] = monster['hp'] - user['ap']
    if action == HEAL:
        user['hp'] = min(user['hp'] + user['heal'], MAX_USER_HP)
    if monster['hp'] <= 0:
        print('You win')
        break

    action = randint(ATTACK, HEAL)
    if action == ATTACK:
        user['hp'] = user['hp'] - monster['ap']
    if action == HEAL:
        monster['hp'] = min(monster['hp'] + monster['heal'], MAX_MONSTER_HP)
    if user['hp'] <= 0:
        print('You lose')
        break