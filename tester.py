from textwrap import dedent
from typing import List

EMPTY = "_"  # underscore
EX = "X"  # capital x
OH = "O"  # capital o

NUM_ROWS = 6
NUM_COLS = 7


def lowest_empty_row(board: List[List[str]], col: int) -> int:
    """Return the lowest row that has space in the column.

    This function takes a board (nested list) and a column (0 <= col <= 6). It
    returns index of the lowest row (the row with the highest index) in that
    column that is EMPTY, or returns -1 if the column is full.

    Arguments:
        board (list): The Connect 4 board.
        col (int): The column to check.

    Returns:
        int: The lowest row in the column that is EMPTY, -1 if the column is
            full.
    """
    row = 5
    while 0 <= col <= 6 and row >= 0:  #loop through row number
        if board[row[str]] == "_":
            return row # return row number
        else:
            row -= 1

    #find column loop through column
    #check from bottom
    #find lowest empty row