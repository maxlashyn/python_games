import curses
from random import randint

HEIGHT = 20
WIDTH = 30
MIN_WIDTH = 1
MIN_HEIGHT = 1
MAX_WIDTH = WIDTH - 2
MAX_HEIGTH = HEIGHT - 2

curses.initscr()
curses.beep()
curses.beep()
window = curses.newwin(HEIGHT, WIDTH, 0, 0)
window.timeout(30)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)


x, y = MIN_WIDTH + randint(0, 10), MIN_HEIGHT + randint(0, 10)
prev_x, prev_y = x, y
dx, dy = 1, 1

window.clear()
window.border(0)

window.addstr(0, 5, "this text header")

for i in range(10):
    window.addstr(randint(MIN_HEIGHT, MAX_HEIGTH),
                  randint(MIN_WIDTH, MAX_WIDTH), '0')

while True:
    event = window.getch()

    #    if event == 27:
    #        break

    window.addstr(prev_y, prev_x, ' ')
    window.addstr(y, x, '@')

    new_x, new_y = x + dx, y + dy
    if MIN_WIDTH > new_x or new_x > MAX_WIDTH or window.inch(y, new_x) != 32:
        dx = -dx
    if MIN_HEIGHT > new_y or new_y > MAX_HEIGTH or window.inch(new_y, x) != 32:
        dy = -dy
    if window.inch(new_y, new_x) != 32:
        dx, dy = -dx, -dy

    prev_x, prev_y, x, y = x, y, new_x, new_y

curses.endwin()
