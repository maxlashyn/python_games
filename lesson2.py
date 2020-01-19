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


# 4. eсли число меньше 5, но больше 0, вывести таким же образом символ 'W'
elif 5 > number > 0:
    for i in range(0, number):
        print('W', end='')

# 5. если число меньше или равно 0, вывести 'Макс знает питон', но слово 'знает' заменить на слово 'изучает'
if number <= 0:
    exploded_string = 'Max знает питон'.split(' ')
    exploded_string[1] = 'изучает'
    print(exploded_string[0], exploded_string[1], exploded_string[2])
