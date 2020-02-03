""" modules """
from lesson_4.test import *

print(append(1, 2))
print(div(9,3))

""" make modules """
""" __all__ """
"""
что б создать модуль, нужно просто создать файл с функциями
и желательно перечислить их в переменной __all__
"""

""" aliases """
from lesson_4.test import mul as умножить

print(умножить(2, 3))

""" dir() """
""" import """
import lesson_4.test
print(dir(lesson_4.test)) # покажет, что можно из этого модуля использовать

""" run modules as script """

if __name__ == '__main__':
    print('Запущен как скрипт')


""" packages """
""" __init__.py """

from lesson_4.testpack.test import *

print(append1(1, 2))

from lesson_4.testpack.level2.test import *

print(append2(5, 2))

""" python libraries """

from random import randint as r

print(r(1, 100))

