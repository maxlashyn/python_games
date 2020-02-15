"""
крестики нолики

"""
from random import randint

VERTICAL_COORDINATS = ['a', 'b', 'c', 'd']



def get_user_char():
    user_char = input('Select char (x,0): ').strip(' ').lower()
    while user_char not in ('x', '0'):
        print('Not available char')
        user_char = input('Select char (x,0): ').strip(' ').lower()
    return user_char


def show_field(field):
    print(' ', '1', '2', '3', '4')
    for y, v in enumerate(VERTICAL_COORDINATS):
        print(v, ' '.join(field[y]))


def is_draw(field):
    count = 0
    for y in range(4):
        count += 1 if '_' in field[y] else 0
    return count == 0

def get_user_position(field):
    while True:
        coordinats = input('Input coordinats: ').lower().strip(' ')
        y, x = tuple(coordinats)

        if int(x) not in (1, 2, 3, 4) or y not in VERTICAL_COORDINATS:
            print('Not valid coordinats')
            continue

        real_x, real_y = int(x) - 1, VERTICAL_COORDINATS.index(y)
        if field[real_y][real_x] == '_':
            break
        else:
            print('Position not empty')
    return real_x, real_y


def get_opponent_char(char):
    return '0' if char == 'x' else 'x'


def is_win(char, field):
    opponent_char = get_opponent_char(char)
    win_sequence = [
        [char, char, char, '_'],
        [char, char, char, opponent_char],
        ['_', char, char, char],
        [opponent_char, char, char, char],
    ]

    for y in range(4):
        if field[y] in win_sequence:
            return True

    for x in range(4):
        col = [field[0][x], field[1][x], field[2][x], field[3][x]]
        if col in win_sequence:
            return True

    diagonal = [field[0][0], field[1][1], field[2][2], field[3][3]]
    if diagonal in win_sequence:
        return True

    diagonal = [field[0][3], field[1][2], field[2][1], field[3][0]]
    if diagonal in win_sequence:
        return True
    return False

def get_computer_position(field):
    x, y = randint(0, 3), randint(0, 3)
    while field[y][x] != '_':
        x, y = randint(0, 3), randint(0, 3)
    return x, y

field = [
    ['_' for x in range(4)] for y in range(4)
]

user_char = get_user_char()
computer_char = get_opponent_char(user_char)


while True:
    show_field(field)
    if is_draw(field):
        print('is draw')
        break
    x, y = get_user_position(field)
    field[y][x] = user_char
    if is_win(user_char, field):
        print('You win')
        break

    x, y = get_computer_position(field)
    field[y][x] = computer_char
    if is_win(computer_char, field):
        print('You lose')
        break
