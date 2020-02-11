from random import randint

MAP_WIDTH = 20
MAP_HEIGHT = 10
FOOD = 'x'
SNAKE_HEAD = 'O'
SNAKE_TAIL = 'o'
"""создание поля"""
field = [
    ['.' for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)
]
head_x = randint(0, MAP_WIDTH - 1)
head_y = randint(0, MAP_HEIGHT - 1)


"""создание головы на поле"""

field[head_y][head_x] = SNAKE_HEAD
field[head_y][head_x - 1] = SNAKE_TAIL
body = [[head_x - 1, head_y]]

def place_food():
    food_x = randint(0, MAP_WIDTH - 1)
    food_y = randint(0, MAP_HEIGHT - 1)
    while field[food_y][food_x] != '.':
        food_x = randint(0, MAP_WIDTH - 1)
        food_y = randint(0, MAP_HEIGHT - 1)
    else:
        field[food_y][food_x] = FOOD
    return food_x, food_y

food_x, food_y = place_food()

"""вывод поля"""
while True:
    for y in range(MAP_HEIGHT):
        print(''.join(field[y]))
    c = input('Выберите вариант ходa: ')
    try:
        if c == 'w':
            head_x_new = head_x
            head_y_new = head_y -1
            if head_x_new < 0 or head_x_new >= MAP_WIDTH or head_y_new < 0 or head_y_new >= MAP_HEIGHT:
                raise IndexError
            field[head_y_new][head_x_new] = SNAKE_HEAD
            tail_pos = body.pop() # [1, 2] tail_pos[0] tail_pos[1]
            tail_x = tail_pos[0]
            tail_y = tail_pos[1]
            field[tail_y][tail_x] = '.'
            field[head_y][head_x] = SNAKE_TAIL
            body.insert(0, [head_x, head_y])
            head_y = head_y - 1
        if c == 's':
            head_x_new = head_x
            head_y_new = head_y + 1
            if head_x_new < 0 or head_x_new >= MAP_WIDTH or head_y_new < 0 or head_y_new >= MAP_HEIGHT:
                raise IndexError
            field[head_y + 1][head_x] = SNAKE_HEAD
            tail_pos = body.pop() # [1, 2] tail_pos[0] tail_pos[1]
            tail_x = tail_pos[0]
            tail_y = tail_pos[1]
            field[tail_y][tail_x] = '.'
            field[head_y][head_x] = SNAKE_TAIL
            body.insert(0, [head_x, head_y])
            head_y = head_y + 1
        if c == 'a':
            head_x_new = head_x - 1
            head_y_new = head_y
            if head_x_new < 0 or head_x_new >= MAP_WIDTH or head_y_new < 0 or head_y_new >= MAP_HEIGHT:
                raise IndexError
            field[head_y][head_x - 1] = SNAKE_HEAD
            tail_pos = body.pop()  # [1, 2] tail_pos[0] tail_pos[1]
            tail_x = tail_pos[0]
            tail_y = tail_pos[1]
            field[tail_y][tail_x] = '.'
            field[head_y][head_x] = SNAKE_TAIL
            body.insert(0, [head_x, head_y])
            head_x = head_x - 1
        if c == 'd':
            head_x_new = head_x + 1
            head_y_new = head_y
            if head_x_new < 0 or head_x_new >= MAP_WIDTH or head_y_new < 0 or head_y_new >= MAP_HEIGHT:
                raise IndexError
            field[head_y][head_x + 1] = SNAKE_HEAD
            tail_pos = body.pop()  # [1, 2] tail_pos[0] tail_pos[1]
            tail_x = tail_pos[0]
            tail_y = tail_pos[1]
            field[tail_y][tail_x] = '.'
            field[head_y][head_x] = SNAKE_TAIL
            body.insert(0, [head_x, head_y])
            head_x = head_x + 1
        if head_x == food_x and head_y == food_y:
            field[tail_y][tail_x] = SNAKE_TAIL
            body.append([tail_x, tail_y])
            food_x, food_y = place_food()
        if [head_x, head_y] in body:
            print('Game over')
            break
    except IndexError:
        print('Game over')
        break