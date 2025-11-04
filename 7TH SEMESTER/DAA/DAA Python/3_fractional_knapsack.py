import time

def fractional_knapsack():
    # Take dynamic input from the user
    n = int(input("Enter the number of items: "))
    weights = []
    values = []

    print("\nEnter the weight and value for each item:")
    for i in range(n):
        w = float(input(f"Weight of item {i+1}: "))
        v = float(input(f"Value of item {i+1}: "))
        weights.append(w)
        values.append(v)

    capacity = float(input("\nEnter knapsack capacity: "))

    # Start time measurement
    start_time = time.time()

    res = 0.0  # Total value in knapsack

    # Sort items based on value/weight ratio in descending order
    for w, v in sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True):
        if capacity <= 0:
            break

        if w <= capacity:  # Take the full item
            res += v
            capacity -= w
        else:  # Take a fraction of the item
            res += v * (capacity / w)
            capacity = 0

    # End time measurement
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display results
    print(f"\nMaximum value in Knapsack = {res:.2f}")
    print(f"Time taken = {elapsed_time:.6f} seconds")

# Run the program
if __name__ == "__main__":
    print("🔹 Fractional Knapsack using Greedy Method 🔹\n")
    fractional_knapsack()
