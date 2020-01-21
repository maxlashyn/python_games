"""
fizzbazz

вывести в цикле список из 100 чисел (от 0 до 100)
при этом
если число делится на 3 вместо числа выводим строку fizz
если число делится на 5 вместо числа выводим строку bazz
если число делится и на 3, и на 5 вместо числа выводим строку fizzbuzz

1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz
"""

for i in range(100 + 1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
