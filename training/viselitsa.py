attempts = 5
word = input('Enter word:').lower()
parsing_a_word_into_pieces = list(word)
replacement = ['_' for i in parsing_a_word_into_pieces]
while True:
    print(' '.join(replacement))
    print('Attempts: ', attempts)
    char = input('Enter_char:').strip(' ').lower()
    if char in parsing_a_word_into_pieces:
        for i,c in enumerate(parsing_a_word_into_pieces):
            if c == char:
                replacement[i] = char
        if '_' not in replacement:
            print('You win')
            break
    else:
        attempts -= 1
    if attempts == 0:
        print('You lose')
        break
print(' '.join(replacement))