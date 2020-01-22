"""
реализовать калькулятор с польской нотацией
1 5 6 + - = 10
\6 5 a b - -> 6 - 5= a -b
пользователь вводит с консоли раздельно операнды и операцию, оператды сохраняются в стек
результат сохраняется в стек и используется как первый операнд следующей операции
при вводе с консоли "=" выпводится (но не удаляется) верхний элемент стека
"""


available_operation = ('+', '-', '*', '/', '=')
stack = []

while True:
    print('=', stack)
    c = input('цифра или операция: ')
    if c in available_operation:
        if c == '=':
            if len(stack) > 0:
                result = stack.pop()
                stack.append(result)
                print(result)
                continue
            else:
                print('Стек пуст')
                continue
        if len(stack) > 1:
            b, a = stack.pop(), stack.pop()
            if c == '+':
                stack.append(a + b)
            if c == '-':
                stack.append(a - b)
            if c == '*':
                stack.append(a * b)
            if c == '/':
                stack.append(a / b)
        else:
            print('Стек пуст')
    else:
        stack.append(int(c))
