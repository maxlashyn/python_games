from random import randint

HULK = 'D'


def get_new_position(current_position, inquiry):
    _new_position = current_position
    if inquiry == 'a':
        _new_position = [max(0, current_position[0] - 1), current_position[1]]
    if inquiry == 'd':
        _new_position = [min(current_position[0] + 1, len(field[0]) - 1), current_position[1]]
    if inquiry == 'w':
        _new_position = [current_position[0], max(0, current_position[1] - 1)]
    if inquiry == 's':
        _new_position = [current_position[0], min(current_position[1] + 1, len(field) - 1)]
    return _new_position


def move_char(position, new_position, char):
    if position in target_pos:
        field[position[1]][position[0]] = '0'
    else:
        field[position[1]][position[0]] = '.'
    field[new_position[1]][new_position[0]] = char

def free_target_position():
    buffer = target_pos.copy()
    for pos in position_box:
        if pos in buffer:
            buffer.remove(pos)
    return buffer

field = [
    list('xxxxxxxxxxx'),
    list('x.........x'),
    list('x.........x'),
    list('x.........x'),
    list('x....o....x'),
    list('x.........x'),
    list('x......D..x'),
    list('x..0......x'),
    list('x.........x'),
    list('xxxxxxxxxxx')
]

position = []

for y in range(0, len(field)):
    for x in range(0, len(field[y])):
        if field[y][x] == 'o':
            position = [x, y]

position_box = []

for y in range(0, len(field)):
    for x in range(0, len(field[y])):
        if field[y][x] == 'D':
            position_box.append([x, y])

target_pos = []
for y in range(0, len(field)):
    for x in range(0, len(field[y])):
        if field[y][x] == '0':
            target_pos.append([x, y])




while True:
    for row in field:
        print(' '.join(row))

    inquiry = input('Выберите направление: ')
    new_position = get_new_position(position, inquiry)

    char = field[new_position[1]][new_position[0]]
    if char == 'x':
        continue
    if char in ['.', '0']:
        move_char(position, new_position, 'o')
        position = new_position
    if char == 'D':
        box_pos = new_position
        new_box_position = get_new_position(box_pos, inquiry)

        char = field[new_box_position[1]][new_box_position[0]]
        print(char)
        if char == 'x':
            continue
        if char in ['.', '0']:
            move_char(box_pos, new_box_position, 'D')
            position_box.remove(box_pos)
            position_box.append(new_box_position)

            move_char(position, new_position, 'o')
            position = new_position

            # выполнить проверку, что все ящики на своих позициях
            buffer = free_target_position()
            if len(buffer) == 0:
                print('game over')
                break
for row in field:
    print(' '.join(row))