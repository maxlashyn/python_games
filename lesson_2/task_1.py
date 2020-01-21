"""
Факториал это произведение всех простых чисел из ряда
5! = 1 * 2 * 3 * 4 * 5
1! = 1
2! = 1 * 2
0! = 1

Написать функцию расчета факториала
"""


def factorial(x):
    if x < 0:
        return 0
    y = 1
    while x > 0:
        y = y * x
        x = x - 1
    return y


def factorial2(x):
    if x < 0:
        return 0
    y = 1
    for i in range(1, x + 1, 1):
        y = y * i
    return y


print(factorial(5))
