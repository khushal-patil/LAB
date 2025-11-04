# 0/1 Knapsack Problem using Dynamic Programming
# Description: Solves knapsack problem by selecting items such that total value is maximized
# without exceeding the given weight capacity.

def solve_knapsack():
    print("🔹 0/1 Knapsack Problem using Dynamic Programming 🔹\n")

    # Step 1: Take dynamic user input
    n = int(input("Enter the number of items: "))
    values = []
    weights = []

    print("\nEnter the value and weight for each item:")
    for i in range(n):
        val = int(input(f"Value of item {i+1}: "))
        wt = int(input(f"Weight of item {i+1}: "))
        values.append(val)
        weights.append(wt)

    W = int(input("\nEnter the maximum capacity of the knapsack: "))

    # Step 2: Initialize DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 3: Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                # Include or exclude the current item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Step 4: Display maximum profit
    max_value = dp[n][W]
    print(f"\n✅ Maximum value that can be obtained: {max_value}")

    # Step 5: Trace back the selected items
    print("\nItems included in the knapsack:")
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            print(f"  → Item {i} (Value: {values[i - 1]}, Weight: {weights[i - 1]})")
            w -= weights[i - 1]

if __name__ == "__main__":
    solve_knapsack()
