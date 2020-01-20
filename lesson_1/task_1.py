"""
1. получить с консоли некоторое число +
2. если число больше 10 вывести "число не может быть больше 10" и прекратить выполнение программы +
3. если число больше или равно 5, вывести символ "Q" в количестве равном введенному числу, одной строкой
4. eсли число меньше 5, но больше 0, вывести таким же образом символ 'W'
5. если число меньше или равно 0, вывести 'Макс знает питон', но слово 'знает' заменить на слово 'изучает'
"""

number = int(input('enter number: '))
print(number)

if number > 10:
    print('число не может быть больше 10')
    exit()


if number >= 5:
    a = ''
    for i in range(0, number, 1):
        a += 'Q'
    print(a)
# a = []
# for i in range(0, number, 1):
#     a.append('Q')
# print(''.join(a))

# a = ['Q' for i in range(0, number)]
# print(''.join(a))


# 4. eсли число меньше 5, но больше 0, вывести таким же образом символ 'W'
elif 5 > number > 0:
    for i in range(0, number):
        print('W', end='')

# 5. если число меньше или равно 0, вывести 'Макс знает питон', но слово 'знает' заменить на слово 'изучает'
if number <= 0:
    exploded_string = 'Max знает питон'.split(' ')
    exploded_string[1] = 'изучает'
    print("%s %s %s" % (exploded_string[0], exploded_string[1], exploded_string[2]))
    print(exploded_string[0], exploded_string[1], exploded_string[2])
    print(exploded_string[0], 'изучает', exploded_string[2])    
