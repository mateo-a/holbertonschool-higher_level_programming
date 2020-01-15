#!/usr/bin/python3
import sys
"""

Placing N non-attacking queens on an N×N chessboard

"""


def chessboard(size):
    """Initializes the data"""
    if size < 4:
        print("N must be at least 4")
        exit(1)
    n_queens = [0] * size

    def print_result(n_queens):
        """Print result"""
        print(("[" + ", ".join(["[{}, {}]".format(y, x) for y, x in
                                enumerate(n_queens[0:], 0)]) + "]"))

    def place_queen(queens):
        """Check position"""
        for x in range(size):
            next_position = 0
            for y in range(queens):
                queen_x = n_queens[y]
                if (x == queen_x or x + queens == queen_x + y or
                        x - queens == queen_x - y):
                    next_position = 1
                    break
            if next_position == 1:
                next_position == 0
                continue
            if queens != size - 1:
                n_queens[queens + 1] = 0
                n_queens[queens] = x
                place_queen(queens + 1)
            else:
                n_queens[queens] = x
                print_result(n_queens)
    place_queen(0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    size = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
    exit(1)
chessboard(size)
