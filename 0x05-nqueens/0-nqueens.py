#!/usr/bin/python3
import sys

def print_solution(solution):
    """Print a solution in the required format."""
    print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row, board, solutions):
    """Recursive backtracking function to find all solutions."""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(n, row + 1, board, solutions)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_nqueens(n, 0, board, solutions)
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()

