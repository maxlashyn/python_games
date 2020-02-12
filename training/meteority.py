"""

прямоугольное поле
сверху падают символы случайным образом
по нижней границе поля перемещается корзина у которой 3 жизни
если символ падает в корзину - + 1 жизнь
если пролетает мимо - -1 жизнь
если у корзины 0 жизней - игра закончилась

"""
from random import randint

MAP_WIDTH = 10
MAP_HEIGHT = 10
BASKET = 'U'
BALL = 'o'
MAX_LIFE = 3
field = [
    ['.' for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)
]
basket_x = MAP_WIDTH // 2
basket_y = MAP_HEIGHT - 1

field[basket_y][basket_x] = BASKET
has_ball = False
ball_count_in_basket = 0
life = MAX_LIFE
while True:
    print(f'life = {life}, ball = {ball_count_in_basket}')
    if not has_ball:
        ball_x = randint(0, MAP_WIDTH - 1)
        ball_y = 0
        field[ball_y][ball_x] = BALL
        has_ball = True
    for y in range(MAP_HEIGHT):
        print(''.join(field[y]))
    c = input('Выберите вариант ходa: ')
    if c == 'a':
        basket_x_new = basket_x - 1
        if 0 <= basket_x_new < MAP_WIDTH:
            field[basket_y][basket_x] = '.'
            field[basket_y][basket_x_new] = BASKET
            basket_x = basket_x_new
    if c == 'd':
        basket_x_new = basket_x + 1
        if 0 <= basket_x_new < MAP_WIDTH:
            field[basket_y][basket_x] = '.'
            field[basket_y][basket_x_new] = BASKET
            basket_x = basket_x_new

    ball_new_y = ball_y + 1
    field[ball_y][ball_x] = '.'
    if ball_new_y == basket_y and ball_x == basket_x:
        has_ball = False
        ball_count_in_basket = ball_count_in_basket + 1
    elif ball_new_y == MAP_HEIGHT:
        has_ball = False
        life = life - 1
    else:
        field[ball_new_y][ball_x] = BALL
        ball_y = ball_new_y
    if life == 0:
        print('Game over')
        break