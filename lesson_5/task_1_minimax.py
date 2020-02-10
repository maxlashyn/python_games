"""
крестики-нолики 3х3
  1 2 3
a _ _ 0
b х _ 0
c х 0 _

1.создать поле (_) 3 на 3, с координатами ++
2.предложить выбрать крестик или нолик(обозначить их 1,2) ++
- начало игрового цикла ++
2.1 вывести поле с координатами ++
3. Попросить координаты для хода ++
4. поставить выбранную фигуру на поле по введенным координатам ++

5. Проверить ситуацию на поле ++
6. если собраны линии по вертикали,горирзонтали или по диагонали написать победа ++

7. ход комьютера, координаты выбираются случайно из всего набора пустых ячеек++

8. Проверить ситуацию на поле++
9. если собраны линии по вертикали,горирзонтали или по диагонали написать "проиграл"++
"""
from random import randint
import sys

EMPTY_CHAR = '_'


def select(opponent_select):
    return 'x' if opponent_select == '0' else '0'


field = [[EMPTY_CHAR for i in range(3)] for j in range(3)]

user_char = input('выберите крестик или нолик:')
computer_char = select(user_char)
vertical = ['a', 'b', 'c']

scores = {
    computer_char: 10,
    user_char: -10,
    'tie': 0
}


def bestMove(field):
    board = [field[y].copy() for y in range(3)]
    bestScore = -sys.maxsize
    move = None
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY_CHAR:
                board[y][x] = computer_char
                score = minimax(board, 0, False)
                board[y][x] = EMPTY_CHAR
                if score > bestScore:
                    bestScore = score
                    move = (x, y)

    return move


def is_tie(board):
    for y in range(3):
        if EMPTY_CHAR in board[y]:
            return False
    return True


def minimax(board, depth, is_maximizing):
    if check_win(user_char, board):
        return scores[user_char]
    if check_win(computer_char, board):
        return scores[computer_char]
    if is_tie(board):
        return scores['tie']

    if is_maximizing:
        bestScore = -sys.maxsize
        for y in range(3):
            for x in range(3):
                if board[y][x] == EMPTY_CHAR:
                    board[y][x] = computer_char
                    score = minimax(board, depth + 1, False)
                    board[y][x] = EMPTY_CHAR
                    bestScore = max(score, bestScore)
    else:
        bestScore = sys.maxsize
        for y in range(3):
            for x in range(3):
                if board[y][x] == EMPTY_CHAR:
                    board[y][x] = user_char
                    score = minimax(board, depth + 1, True)
                    board[y][x] = EMPTY_CHAR
                    bestScore = min(score, bestScore)
    return bestScore


def get_user_position():
    coordinate = input('input coordinate:').strip(' ').lower()
    y, x = tuple(coordinate)
    return int(x) - 1, vertical.index(y)


def get_computer_position(field):
    x, y = randint(0, 2), randint(0, 2)
    while field[y][x] != '_':
        x, y = randint(0, 2), randint(0, 2)
    return x, y


def check_win(selected_char, field):
    opponent_char = select(selected_char)
    for y in range(3):
        row = field[y]
        if opponent_char not in row and EMPTY_CHAR not in row:
            return True

    for x in range(3):
        row = [field[0][x], field[1][x], field[2][x]]
        if opponent_char not in row and EMPTY_CHAR not in row:
            return True

    row = [field[0][0], field[1][1], field[2][2]]
    if opponent_char not in row and EMPTY_CHAR not in row:
        return True

    row = [field[0][2], field[1][1], field[2][0]]
    if opponent_char not in row and EMPTY_CHAR not in row:
        return True

    return False


def show_field(field):
    print(' ', '1', '2', '3')
    print('a', ' '.join(field[0]))
    print('b', ' '.join(field[1]))
    print('c', ' '.join(field[2]))


while True:
    show_field(field)
    x, y = get_user_position()
    if field[y][x] != '_':
        print('cell not empty')
        continue
    field[y][x] = user_char
    if check_win(user_char, field):
        print('win')
        break

    pos = bestMove(field)
    if pos != None:
        x, y = pos
        field[y][x] = computer_char
        if check_win(computer_char, field):
            print('lose')
            break
    if is_tie(field):
        print('tie')
        break
