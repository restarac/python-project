import random

def play():
    user = input("'r' for rock, 'p' paper and 's' for scissors: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You WON!'

    return 'You LOOSE'
# too complex to do this -> https://www.tutorialspoint.com/How-to-overload-Python-comparison-operators
def is_win(player, computer):
    if  (player == 'r' and computer == 's') or\
        (player == 's' and computer == 'p') or\
        (player == 'p' and computer == 'r'):
            return True


print(play())
