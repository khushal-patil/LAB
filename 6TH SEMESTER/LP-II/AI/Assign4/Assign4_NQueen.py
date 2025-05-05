import math

def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i] == col or  board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def backtracking(board, row, n):
    if row == n:
        print_board(board, n)
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if backtracking(board, row + 1, n):
                return True
            board[row] = -1  
    return False


def print_board(board, n):
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))
    print("\n")


def branch_bound(n):
    board = [-1] * n  
    columns = set()   
    diag1 = set()     
    diag2 = set()     

    def backtrack(row):
        if row == n:
            print_board(board, n)
            return True
        
        for col in range(n):
            if col in columns or (row - col) in diag1 or (row + col) in diag2:
                continue  

            board[row] = col
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True

            board[row] = -1
            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

    if not backtrack(0):
        print("No solution exists.")
    else:
        print("\nSolution found using Branch and Bound:\n")

def n_queens_solution(n):
    print("Solution using Backtracking:")
    board_backtracking = [-1] * n
    backtracking(board_backtracking, 0, n)

    print("\nSolution using Branch and Bound:")
    branch_bound(n)

n = int(input("Enter the number of queens: "))
n_queens_solution(n)

