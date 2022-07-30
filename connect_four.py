from textwrap import dedent
from typing import List

EMPTY = "_"  # underscore
EX = "X"  # capital x
OH = "O"  # capital o

NUM_ROWS = 6
NUM_COLS = 7

def lowest_empty_row(board: List[List[str]], col: int) -> int:
    row = 5
    while 0 <= row <=5:
        if board[row][col] == EMPTY:
            break
        else:
            row -= 1
    return row


def has_connect_four(board: List[List[str]]) -> bool:

    # NUM_ROWS = 6
    # NUM_COLS = 7

    OH = 'O'
    EX = 'X'
    EMPTY = '_'


# horizontal
    for row in range(NUM_ROWS): # checks every row
        for col in range(4): # only certain col can have 4 in a row
            if EMPTY != board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                return True
            else:
                continue

# vertical
    for col in range(NUM_COLS):
        for row in range(3):
            if EMPTY != board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return True
            else:
                continue

# diagonal \
    for row in range(3):
        for col in range(4):
            if EMPTY != board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return True
            else:
                continue

# diagonal /
    for row in range(3):
        for col in range(4):
            if EMPTY != board[row][col + 3] == board[row + 1][col + 2] == board[row + 2][col + 1] == board[row + 3][col]:
                return True
            else:
                continue

    return False


def get_input(board: List[List[str]]) -> int:

    i = 0
    while (i >= 0):
        column_num = int(input("Choose a column to drop your disc: "))
        if 0 <= column_num <= 6:
            if lowest_empty_row(board, column_num) >= 0:
                return column_num
            else:
                print("Column full.")
                i += 1
        else:
            print("Not an integer between 0 and 6 inclusive.")
            i += 1


### DO NOT CHANGE ANYTHING BELOW THIS LINE ###

# UTILITY


def str_to_board(string: str) -> List[List[str]]:
    """Convert a readable board (as a string) to a nested list representation.

    This function takes a string and returns a nested list that corresponds to
    the depicted board.  The string should look like
    the following:

    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  X  _  _  _ |
    3  | _  _  _  O  _  _  _ |
    4  | _  _  _  X  X  _  _ |
    5  | O  O  O  O  X  _  _ |
       +---------------------+
         0  1  2  3  4  5  6

    Where X (capital X) and O (capital O) are the players, and empty spaces are
    represented by the underscore.

    Arguments:
        string (str): The readable version of the board.

    Returns:
        list: The list representation of the board.
    """
    import re
    string = dedent(string).strip()
    board = []
    for line in string.splitlines():
        line = re.sub('[^_OX]', '', line)
        if not line:
            continue
        if len(line) != NUM_COLS:
            raise ValueError('Each row must have {} columns'.format(NUM_COLS))
        board.append(list(char for char in line))
    if len(board) != NUM_ROWS:
        raise ValueError('There must be {} rows'.format(NUM_ROWS))
    return board


# INITIATION


def create_empty_board() -> List[List[str]]:
    """Create an empty board.

    This function returns a new nested list, filled with EMPTY, that represents
    a new Connect 4 board.

    Returns:
        list: A board willed with EMPTY spaces.
    """
    board = []
    for row in range(NUM_ROWS):
        board.append(NUM_COLS * [EMPTY])
    return board


# PRINTING


def print_salutation() -> None:
    """Greet the player to the game.
    """
    print(dedent('''
    ##########################
    #        COMP 131        #
    #      CONNECT FOUR      #
    ##########################
    ''').strip())


def print_board(board: List[List[str]]) -> None:
    """Print the board.

    Arguments:
        board (list): A list representation of the board.
    """
    for i, row in enumerate(board):
        print(str(i) + '  | ' + '  '.join(col for col in row) + ' |')
    print('   +---------------------+')
    print('     0  1  2  3  4  5  6')


def print_valediction(num_empties: int, player: str) -> None:
    """Congratulate the winning player if appropriate.

    Arguments:
        num_empties (int): The number of empty spaces on the board.
        player (EX or OH): The player whose turn just ended.
    """
    if num_empties == 0:
        text = 'A DRAW'
    elif player == EX:
        text = 'X WINS'
    else:
        text = 'O WINS'
    print(dedent('''
    ##########################
    #  !!!!   {}   !!!!  #
    ##########################
    '''.format(text)).strip())


# MAIN


def main() -> None:
    """Play a two-player game of Connect 4.
    """
    print_salutation()
    # initialize the game with an empty board
    board = create_empty_board()
    player = EX
    has_win = False
    # keep track of how many empty spaces remain
    num_empties = NUM_ROWS * NUM_COLS
    # while no one has won and there are still empty spaces on the board
    while not has_win and num_empties:
        # print the board
        print()
        print_board(board)
        print()
        # switch players
        if player == EX:
            player = OH
        else:
            player = EX
        # get the player's input
        col = get_input(board)
        row = lowest_empty_row(board, col)
        board[row][col] = player
        # check for fours-in-a-row
        has_win = has_connect_four(board)
        num_empties -= 1
    # end the game
    print()
    print_board(board)
    print()
    print_valediction(num_empties, player)


if __name__ == '__main__':
    main()
