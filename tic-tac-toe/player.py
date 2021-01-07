import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        """
        we want all player get their next move given a game
        """
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        return super().__init__(letter)

    def get_move(self, game):
        # get a valid spot
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        return super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we are going to check the values
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')

        return val
