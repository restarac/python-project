import random
import string

from words import words
from ascii_art import show_hagman

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 5
    # get user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left')
        show_hagman(lives)
        print('You used this letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('\nCurrent word:', ' '.join(word_list))

        user_letter = input('Guess the letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('\nCorrect letter!')
            else:
                lives -= 1
                print('\nThe letter is not in the word. You lose 1 live')

        elif user_letter in used_letters:
            print('You already use that word!')

        else:
            print('Invalid character! Try again!')
    if lives == 0:
        show_hagman(lives)
        print('\nYou died!\nThe word you are trying to guess is:', word)
    else:
        print('Congrats! you guessed the word:', word)

hangman()
