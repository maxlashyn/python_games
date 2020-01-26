"""
Место действия этой игры — «вселенная» — это размеченная на клетки поверхность или плоскость — безграничная,
ограниченная, или замкнутая (в пределе — бесконечная плоскость).
Каждая клетка на этой поверхности может находиться в двух состояниях: быть «живой» (заполненной)
или быть «мёртвой» (пустой). Клетка имеет восемь соседей   , окружающих её.
Распределение живых клеток в начале игры называется первым поколением.
Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:
    в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
    если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить;
    в противном случае, если соседей меньше двух или больше трёх, клетка умирает («от одиночества»
    или «от перенаселённости»)
Игра прекращается, если
    на поле не останется ни одной «живой» клетки
    конфигурация на очередном шаге в точности (без сдвигов и поворотов) повторит себя же на
    одном из более ранних шагов (складывается периодическая конфигурация)
    при очередном шаге ни одна из клеток не меняет своего состояния (складывается стабильная конфигурация;
    предыдущее правило, вырожденное до одного шага назад)
Игрок не принимает прямого участия в игре, а лишь расставляет или генерирует начальную конфигурацию «живых» клеток,
которые затем взаимодействуют согласно правилам уже без его участия (он является наблюдателем).
"""
from random import randint


def next_yx(y, x):
    yield y - 1, x - 1
    yield y - 1, x
    yield y - 1, x + 1
    yield y, x + 1
    yield y + 1, x + 1
    yield y + 1, x
    yield y + 1, x - 1
    yield y, x - 1


def is_live(field, ny, nx):
    return MIN_RANGE <= ny <= MAX_RANGE \
           and MIN_RANGE <= nx <= MAX_RANGE \
           and field[ny][nx] == LIFE


def get_empty_map():
    return [
        [DEAD for i in range(MAX_RANGE + 1)] for j in range(MAX_RANGE + 1)
    ]


LIFE = 'x'
DEAD = ' '
MIN_RANGE = 0
MAX_RANGE = 10
variants = [DEAD, LIFE]
field = [
    [variants[randint(0, 1)] for i in range(MAX_RANGE + 1)] for j in range(MAX_RANGE + 1)
]

while True:
    print('next step')
    for y in range(MAX_RANGE + 1):
        print(''.join(field[y]))
    buffer = get_empty_map()
    for y in range(MAX_RANGE + 1):
        for x in range(MAX_RANGE + 1):
            c = field[y][x]
            neighbors = 0
            if c == DEAD:
                for ny, nx in next_yx(y, x):
                    neighbors += 1 if is_live(field, ny, nx) else 0
                    if neighbors == 3:
                        buffer[y][x] = LIFE
                        break
            else:
                for ny, nx in next_yx(y, x):
                    neighbors += 1 if is_live(field, ny, nx) else 0
                buffer[y][x] = LIFE if neighbors in [2, 3] else DEAD
    if field == buffer:
        print('stasis')
        break
    field = buffer
