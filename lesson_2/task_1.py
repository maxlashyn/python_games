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


"""
3 9 + 4 + 0
s = x**2 + (x-1)**2 + (x-2)**2 + 0
"""


def sum_square(max_x):
    s = 0
    for x in range(2, max_x + 1, 1):
        s += (x - 2) ** 2
    return s


def sum_reqursion(max_x):
    if max_x <= 2:
        return 0
    return (max_x -2) ** 2 + sum_reqursion(max_x - 1)



print(sum_square(6))
print(sum_reqursion(6))
