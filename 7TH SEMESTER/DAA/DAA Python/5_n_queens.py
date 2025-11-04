# N-Queens Problem using Backtracking
# Description: Program to design an n×n chessboard with the first queen placed by the user.
# Then, use backtracking to place remaining queens safely.

def n_queens(n, first_row, first_col):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
    res = []

    # Initialize the chessboard with "0"
    board = [["0"] * n for _ in range(n)]

    # Place the first queen as given by the user
    board[first_row][first_col] = "1"
    col.add(first_col)
    posDiag.add(first_row + first_col)
    negDiag.add(first_row - first_col)

    # Backtracking function
    def backtrack(r):
        if r == n:
            # Found a valid solution
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        # Skip the row if the first queen is placed there already
        if r == first_row:
            backtrack(r + 1)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # Place the queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            # Move to the next row
            backtrack(r + 1)

            # Backtrack (remove queen)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    # Start from row 0
    backtrack(0)

    # Display all valid solutions
    if res:
        print(f"\n✅ Total Solutions found: {len(res)}\n")
        for index, sol in enumerate(res, 1):
            print(f"Solution {index}:")
            for row in sol:
                print(row)
            print()
    else:
        print("\n❌ No valid solution found with that first queen position.")


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    print("♕ N-Queens Problem using Backtracking ♕\n")
    n = int(input("Enter the size of the chessboard (n x n): "))

    print("\nEnter position of the first queen (row and column, starting from 0):")
    first_row = int(input("Row: "))
    first_col = int(input("Column: "))

    # Validate input
    if first_row < 0 or first_row >= n or first_col < 0 or first_col >= n:
        print("❌ Invalid position! Row and Column must be between 0 and n-1.")
    else:
        n_queens(n, first_row, first_col)
