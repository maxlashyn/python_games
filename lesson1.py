""" строка """
hello = 'Hello world'
print(hello)

print(hello.split('l'))

""" целое число """
one = 1
print(one)

"""кортеж"""
a = [1, 2, 3]
a[0] = 10
print(a[0], a[2], a[1])

""" словарь """
b = {'are': 1, 0: 1}
print(b['are'], b[0])

""" список, не изменяется """
c = (1, 'word')
print("hello %s %s" % c)
print(c[1])

""" ввод строки с консоли """
age = int(input('enter age in years: '))
print(age)

""" условный оператор """
if age > 18:
    print('age > 18')
elif age > 10:
    print('age > 10')
elif age > 5:
    print('age > 5')
else:
    print('age <= 5')

""" циклы """
""" while """
while age <= 5:
    print('age == 5')
    print('another operations')
    age = age + 1
    break
else:
    print('loop end')

print('next step')

""" for """
for i in range(1, 10, 2):
    if i == 3:
        continue
    print(i)

a = (1, 2, 3, 4)
for i in a:
    print(i)

i = 0
while i < 4:
    print(a[i])
    i = i + 1

""" функция """


def add(x: 'int, >0', y: int) -> int:
    return x + y


if add(1, 2) is None:
    print('result none')

print(add(4, 2))
print(add('hello', 'world'))

""" принудительная остановка программы """

# exit()


"""
1. получить с консоли некоторое число +
2. если число больше 10 вывести "число не может быть больше 10" и прекратить выполнение программы +
3. если число больше или равно 5, вывести символ "Q" в количестве равном введенному числу, одной строкой
4. eсли число меньше 5, но больше 0, вывести таким же образом символ 'W'
5. если число меньше или равно 0, вывести 'Макс знает питон', но слово 'знает' заменить на слово 'изучает'
"""


