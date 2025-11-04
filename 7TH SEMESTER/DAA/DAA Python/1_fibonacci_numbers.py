import time

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative Fibonacci
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Main Program
n = int(input("Enter the value of n: "))

# Measure recursive time
start_time = time.time()
fib_rec = fibonacci_recursive(n)
end_time = time.time()
recursive_time = end_time - start_time

# Measure iterative time
start_time = time.time()
fib_iter = fibonacci_iterative(n)
end_time = time.time()
iterative_time = end_time - start_time

# Display results
print(f"\nFibonacci({n}) using recursion = {fib_rec}")
print(f"Time taken (recursive) = {recursive_time:.6f} seconds")

print(f"\nFibonacci({n}) using iteration = {fib_iter}")
print(f"Time taken (iterative) = {iterative_time:.6f} seconds")

# Complexity analysis
print("\n--- Complexity Analysis ---")
print("Recursive Fibonacci:  Time = O(2^n),  Space = O(n)")
print("Iterative Fibonacci:  Time = O(n),    Space = O(1)")
