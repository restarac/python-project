import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function
        self.board = self.make_new_board() #plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of wich locations we've uncovered
        # we'll save (row, col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board
        # we should construct the list of list here (or wharever you prefer, but since we have a 2d board
        # list of list is most natural)

        # generate the board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this will create a board like:
        # [[None, None,..., None],
        #  [None, None,..., None],
        #  [...                       ],
        #  [None, None,..., None]]
        # This is the board we created.

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) # return a random integer N between 0 and Last space on board
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now we have bombs plated, lets assign a number 0-8 for all empty spaces,
        # which representshow many neighboring bombs there are. We can precompute these and itl save
        # us some effort checking whats around the board later on :)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this already a bomb, we dont want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure we not go out of bounds!
        num_neighboring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original localtion, dont check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        # dig the location!
        # return True if successful dig, false if bomb dug

        # hit a bom -> game over
        # dig a location with neighboring bombs -> finish dig
        # dig a location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0,row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    # dont dig where you dug
                    continue
                self.dig(r,c)
        # if our initial dig dont hit a bomb we shouldnt hit a bomb here
        return True

    def __str__(self):
        # magic function, it will be called when you print the object
        # return a string that shows the board to the player
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '

        # put this together in a string
        return self.print_formated_board(visible_board)

    def print_formated_board(self, visible_board):

        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


# Play the game
def play(dim_size=10, num_bombs=10):
    # step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # step 2: show the board and ask the user where to dig
    # step 3a: if location is a bomb, show game over
    # step 3b: if location is not a bom, dig recursively until each square is at least next to a bomb
    # step 4: repeat steps 2 and 3a/b until there is no more places to dig
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*',input("where would you like to dig? input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1]) # get the first and last values

        if row < 0 or row>=board.dim_size or col<0 or col>=board.dim_size:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row, col)
        if not safe:
            # we dug a bomb
            break

    if safe:
        print("CONGRATULATIONS!!! YOU WON!!")
    else:
        print("SORRY GAME OVER!")
        # lets reveal all bombs
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == '__main__': # good practice :)
    play()
