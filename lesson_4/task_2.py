"""
1.загадать слово +
2.Разделить его на буквы и посчитать их количество +
2,1.устовить макс число попыток +
3.вывести подсказку с нижним подчеркиванием вместо каждой буквы +
4.попросить ввести букву +
5.определить есть ли эта буква в слове +
       6. если буква есть вывести подсказку с этой буквой в нужных местах +
7.если нет, то уменьшаем количество попыток +
8. если слово угадано пишем вы победили +
9. если количество попыток стало = 0 вы проиграли +
15. перейти к пункту 4 +
"""

made_up_word = input('Загадайте слово:')
by_chars = list(made_up_word)
count_of_chars = len(by_chars)
attempts = 10
guessed = ['_' for i in range(count_of_chars)]
while True:
    print('attempts count ', attempts)
    print(' '.join(guessed))
    char = input('Enter char:')
    if char in by_chars:
        for i, c in enumerate(by_chars):
            if c == char:
                guessed[i] = char
    else:
        attempts -= 1
    if '_' not in guessed:
        print('You win')
        break
    elif attempts == 0:
        print('You lose')
        break

print(' '.join(guessed))