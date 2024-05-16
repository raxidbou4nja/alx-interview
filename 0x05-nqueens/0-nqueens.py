#!/usr/bin/python3
"""N queens problem solver."""
import sys


def validate_args():
    """Validate command-line arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    N = int(sys.argv[1])

    if N < 4:
        print("N must be at least 4")
        exit(1)

    return N


def queens(N, row=0, columns=[], diag1=[], diag2=[]):
    """Recursive generator function to find all solutions."""
    if row == N:
        yield columns
    else:
        for col in range(N):
            if col not in columns and (row + col) not in diag1 and \
               (row - col) not in diag2:
                yield from queens(N, row + 1, columns + [col],
                                  diag1 + [row + col], diag2 + [row - col])


def print_solutions(N):
    """Generate and print all solutions for the N queens problem."""
    for solution in queens(N):
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)


if __name__ == "__main__":
    N = validate_args()
    print_solutions(N)
