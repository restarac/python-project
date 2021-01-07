from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep a 3x3 board
        self.current_winner = None # keep track of the winner

    def print_board(self):
        # this is getting the board rows
        # to do that slice the list into 1 list with 3 pieces with 3 elements
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number correspond to what box)
        for row in [[str(j) for j in range(i*3, (i+1)*3)] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # short version
        return [i for (i, spot) in enumerate(self.board) if (spot == ' ')]
        # Long version
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if (spot == ' '):
        #         moves.append(i)
        # return moves
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere
        # first checking the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True

        # check collumn
        col_ind = square % 3
        collum = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in collum):
            return True

        # Check diagonals
        # The square is a even number (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    # return the winner of the game, or none if its a tie.
    if print_game:
        game.print_board_nums()

    letter = 'X' # Starting letter or player

    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let move the game
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # empty line

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X' #switches players
        # time.sleep(0.5)

    if print_game:
        print('it\'s a tie')

if __name__ == '__main__':
    x_player = GeniusComputerPlayer('X')
    o_player = HumanPlayer('O')
    g = TicTacToe()
    play(g, x_player, o_player)

# if __name__ == '__main__':
#     x_wins = 0
#     o_wins = 0
#     ties = 0
#     interations = 100
#     for _ in range(interations):
#         x_player = RandomComputerPlayer('X')
#         o_player = GeniusComputerPlayer('O')
#         g = TicTacToe()
#         result = play(g, x_player, o_player, print_game=False)
#         if result == 'X':
#             x_wins += 1
#         elif result == 'O':
#             o_wins += 1
#         else:
#             ties += 1
#     print(f'After {interations} interations, we see {x_wins} x_wins, {o_wins} o_wins and {ties} ties.')
