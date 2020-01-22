import curses
from random import randint

HEIGHT = 20
WIDTH = 30
MIN_WIDTH = 1
MIN_HEIGHT =  1
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

window.addstr(0, 5, f"this text header")

for i in range(15):
	window.addstr(randint(MIN_HEIGHT, MAX_HEIGTH), randint(MIN_WIDTH, MAX_WIDTH), '0')

while True:
    event = window.getch()

#    if event == 27:
#        break

    window.addstr(prev_y, prev_x, ' ')
    window.addstr(y, x, '@')

    if MIN_WIDTH > x + dx or x + dx > MAX_WIDTH or window.inch(y, x + dx) != 32:
    	dx = -dx
    if MIN_HEIGHT > y + dy or y + dy > MAX_HEIGTH or window.inch(y + dy, x) != 32: 
    	dy = -dy
    if window.inch(y + dy, x + dx) != 32:
    	dx, dy = -dx, -dy

    prev_x, prev_y, x, y = x, y, x + dx, y + dy 



curses.endwin()