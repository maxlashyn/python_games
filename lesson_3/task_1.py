"""
реализовать калькулятор
пользователь вводит с консоли раздельно операнды и операцию
результат выводится в консоль
результат сохраняется и используется как первый операнд следующей операции
"""

available_operation = ('+', '-', '*', '/')
a = int(input('enter number 1: '))
while True:
    c = input('операция: ')
    if c in available_operation:
        b = int(input('enter number 2: '))
        if c == '+':
            result = a + b
        if c == '-':
            result = a - b
        if c == '*':
            result = a * b
        if c == '/':
            result = a / b
        print(result)
        a = result
    else:
        print('недопустимая операция')

