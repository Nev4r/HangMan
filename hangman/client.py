from hangman.game import Game
from hangman.game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letter_count = len(word)

print(f'Слово состоит из {letter_count} букв.')
print('Попробуйте угадать букву за буквой.')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Выберите букву.\n')
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f'Осталось попыток = {game.remaining_tries}')
    print(f'Введенные буквы: {chars_list_to_str(game.tried_letters)}')

if game.game_status == GameStatus.LOST:
    print('Вас повесили!')
    print(f'Слово было: {game.word}')
else:
    print('Поздравляю! Вы выиграли!')

