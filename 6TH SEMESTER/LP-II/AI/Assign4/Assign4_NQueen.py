def is_safe(board, row, col, n):
    # Check the same column and both diagonals
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def backtracking(board, row, n, count):
    if row == n:
        print_board(board, n)
        count[0] += 1
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            backtracking(board, row + 1, n, count)
            board[row] = -1  # Backtrack

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
    count = [0]

    def backtrack(row):
        if row == n:
            print_board(board, n)
            count[0] += 1
            return

        for col in range(n):
            if col in columns or (row - col) in diag1 or (row + col) in diag2:
                continue

            board[row] = col
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # Backtrack
            board[row] = -1
            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    print(f"Total solutions found using Branch and Bound: {count[0]}")

def n_queens_solution(n):
    print("Solution using Backtracking:")
    board_backtracking = [-1] * n
    count_backtrack = [0]
    backtracking(board_backtracking, 0, n, count_backtrack)
    print(f"Total solutions found using Backtracking: {count_backtrack[0]}")

    print("\nSolution using Branch and Bound:")
    branch_bound(n)

# Main
n = int(input("Enter the number of queens: "))
n_queens_solution(n)
