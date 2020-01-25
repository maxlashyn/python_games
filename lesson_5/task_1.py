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
field = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]
user_char = input('выберите крестик или нолик:')
if user_char == '0':
    computer_char = 'x'
else:
    computer_char = '0'
vertical = ['a', 'b', 'c']


def get_user_position():
    coordinate = input('input coordinate:')
    y, x = tuple(coordinate)
    return int(x) - 1, vertical.index(y)


def get_computer_position(field):
    x = randint(0, 2)
    y = randint(0, 2)
    while field[y][x] != '_':
        x = randint(0, 2)
        y = randint(0, 2)
    return x, y


def three_in_row(user_char, field):
    for y in range(3):
        count = 0
        for x in range(3):
            if field[y][x] == user_char:
                count +=1
        if count == 3:
            return True

    for x in range(3):
        count = 0
        for y in range(3):
            if field[y][x] == user_char:
                count +=1
        if count == 3:
            return True
    count = 0
    for n in [0, 1, 2]:
        if field[n][n] == user_char:
            count +=1
    if count == 3:
        return True
    count = 0
    for n in [2, 1, 0]:
        if field[n][n] == user_char:
            count +=1
    if count == 3:
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
    if three_in_row(user_char, field):
        print('win')
        break

    x, y = get_computer_position(field)
    field[y][x] = computer_char
    if three_in_row(computer_char, field):
        print('lose')
        break




