import random

LOWEST_NUMBER = 1

def guess(x):
    random_number = random.randint(LOWEST_NUMBER, x)

    guess = 0
    while random_number != guess:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if (guess < random_number):
            print(f'guess again! {guess} Too low.')
        elif (guess > random_number):
            print(f'guess again! {guess} Too high.')

    print(f'Congrats, you did it! You have guessed the number {random_number}!!!')

def computer_guess(x):
    low = LOWEST_NUMBER
    high = x
    feedback = ''
    print(f'Hello Human, choose a number between {low} and {high}, I\'ll guess that number.')

    while feedback != 'c':
        if (low != high):
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! I (the computer) guessed the number, {guess}')

guess(100)
# computer_guess(100)
