"""

Sudoku Solver (sudokusolve.py)

Given a string in SDM format, described below, write a program to find and
return the solution for the sudoku puzzle in the string. The solution should be
returned in the same SDM format as the input.

Some puzzles will not be solvable. In that case, return the string “Unsolvable”.

The general SDM format is described here.

For our purposes, each SDM string will be a sequence of 81 digits, one for each
position on the sudoku puzzle. Known numbers will be given, and unknown position
s will have a zero value.

For example, assume you’re given this string of digits:

004006079000000602056092300078061030509000406020540890007410920105000000840600100

The string represents this starting sudoku puzzle:

    0 0 4   0 0 6   0 7 9
    0 0 0   0 0 0   6 0 2
    0 5 6   0 9 2   3 0 0

    0 7 8   0 6 1   0 3 0
    5 0 9   0 0 0   4 0 6
    0 2 0   5 4 0   8 9 0

    0 0 7   4 1 0   9 2 0
    1 0 5   0 0 0   0 0 0
    8 4 0   6 0 0   1 0 0

The provided unit tests may take a while to run, so be patient.

Note: A description of the sudoku puzzle can be found on Wikipedia.

You can see that you’ll need to deal with reading and writing to a particular
format as well as generating a solution.

"""

def sudoku_solver(sudoku):
    
