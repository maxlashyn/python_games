from random import randint

HULK = 'D'

field = [
    list('xxxxxxxxxxx'),
    list('x.........x'),
    list('x.........x'),
    list('x.........x'),
    list('x....o....x'),
    list('x.........x'),
    list('x......D..x'),
    list('x.........x'),
    list('x.........x'),
    list('xxxxxxxxxxx')
]

position = []

for y in range(0, len(field)):
    for x in range(0, len(field[y])):
        if field[y][x] == 'o':
            position = [x, y]
while True:
    for row in field:
        print(' '.join(row))
    new_position = position
    inquiry = input('Выберите направление: ')
    if inquiry == 'a':
        new_position = [max(0, position[0] - 1), position[1]]
    if inquiry == 'd':
        new_position = [min(position[0] + 1, len(field[0]) - 1), position[1]]
    if inquiry == 'w':
        new_position = [position[0], max(0, position[1] - 1)]
    if inquiry == 's':
        new_position = [position[0], min(position[1] + 1, len(field) - 1)]

    #проверить что находится в этом месте карты
    #если пусто - ходим
    #если стенка - стоим
    #eсли ящик - двигаем ящик, и если он подвинулся, перейти на его место
    x = new_position[0]
    y = new_position[1]
    char = field[y][x]
    if char == 'x':
        continue
    if char == '.':
        field[position[1]][position[0]] = '.'
        field[new_position[1]][new_position[0]] = 'o'
        position = new_position