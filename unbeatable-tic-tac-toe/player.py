import random
import math

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

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        return super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves()) #initialy random choose
        else:
            return self.minimax(game, self.letter)['position']

    def minimax(self, state, player):
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' # the other player
        # returns for recursion
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else
                -1 * (state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}


        # Initialize the dictionary
        best = {
            'position': None,
            'score': -math.inf if player == max_player else math.inf
            }

        for possible_move in state.available_moves():
            # 1 - try that spot
            state.make_move(possible_move, player)
            # 2 - using recursive to simulate the game
            sim_score = self.minimax(state, other_player)
            # 3 - undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # otherwise this will messup with the recursion
            # 4 - update the dictionary with the best values
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
