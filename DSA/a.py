def optimal_bst(keys, weights, q):
    n = len(keys)
    
    # Initialize cost and weight arrays
    C = [[0] * (n + 1) for _ in range(n + 1)]
    W = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize weight array with dummy keys
    for i in range(n + 1):
        W[i][i] = q[i]
        for j in range(i + 1, n + 1):
            W[i][j] = W[i][j - 1] + weights[j - 1] + q[j]
    
    # Dynamic programming to compute optimal cost
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            C[i][j] = float('inf')
            W[i][j] = W[i][j] + W[i][j - 1]
            for k in range(i, j):
                c = C[i][k] + C[k + 1][j] + W[i][j]
                if c < C[i][j]:
                    C[i][j] = c
    
    return C, W

def construct_optimal_bst(keys, weights, q):
    n = len(keys)
    C, _ = optimal_bst(keys, weights, q)
    R = [[0] * n for _ in range(n)]
    return construct_tree(C, R, 0, n - 1)

def construct_tree(C, R, i, j):
    if i == j:
        return f"K{i+1}"
    else:
        root = R[i][j]
        if root == 0:
            return "None"
        else:
            return f"R{root} ( {construct_tree(C, R, i, root - 1)}, {construct_tree(C, R, root, j)} )"

# Example usage
keys = ["k1", "k2", "k3", "k4", "k5", "k6"]
weights = [10, 3, 9, 2, 0, 10]
q = [5, 6, 4, 4, 3, 8, 0]
def optimal_bst(keys, weights, q):
    n = len(keys)
    
    # Initialize cost and weight arrays
    C = [[0] * (n + 1) for _ in range(n + 1)]
    W = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize weight array with dummy keys
    for i in range(n + 1):
        W[i][i] = q[i]
        for j in range(i + 1, n + 1):
            W[i][j] = W[i][j - 1] + weights[j - 1] + q[j]
    
    # Dynamic programming to compute optimal cost
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            C[i][j] = float('inf')
            W[i][j] = W[i][j] + W[i][j - 1]
            for k in range(i, j):
                c = C[i][k] + C[k + 1][j] + W[i][j]
                if c < C[i][j]:
                    C[i][j] = c
    
    return C, W

def construct_optimal_bst(keys, weights, q):
    n = len(keys)
    C, _ = optimal_bst(keys, weights, q)
    R = [[0] * n for _ in range(n)]
    return construct_tree(C, R, 0, n - 1)

def construct_tree(C, R, i, j):
    if i == j:
        return f"K{i+1}"
    else:
        root = R[i][j]
        if root == 0:
            return "None"
        else:
            return f"R{root} ( {construct_tree(C, R, i, root - 1)}, {construct_tree(C, R, root, j)} )"

# Example usage
keys = ["k1", "k2", "k3", "k4", "k5", "k6"]
weights = [10, 3, 9, 2, 0, 10]
q = [5, 6, 4, 4, 3, 8, 0]

C, R = optimal_bst(keys, weights, q)
print("Cost array:")
for row in C:
    print(row)

print("\nRoot array:")
for row in R:
    print(row)

print("\nOptimal Binary Search Tree:")
print(construct_optimal_bst(keys, weights, q))
def optimal_bst(keys, weights, q):
    n = len(keys)
    
    # Initialize cost and weight arrays
    C = [[0] * (n + 1) for _ in range(n + 1)]
    W = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize weight array with dummy keys
    for i in range(n + 1):
        W[i][i] = q[i]
        for j in range(i + 1, n + 1):
            W[i][j] = W[i][j - 1] + weights[j - 1] + q[j]
    
    # Dynamic programming to compute optimal cost
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            C[i][j] = float('inf')
            W[i][j] = W[i][j] + W[i][j - 1]
            for k in range(i, j):
                c = C[i][k] + C[k + 1][j] + W[i][j]
                if c < C[i][j]:
                    C[i][j] = c
    
    return C, W

def construct_optimal_bst(keys, weights, q):
    n = len(keys)
    C, _ = optimal_bst(keys, weights, q)
    R = [[0] * n for _ in range(n)]
    return construct_tree(C, R, 0, n - 1)

def construct_tree(C, R, i, j):
    if i == j:
        return f"K{i+1}"
    else:
        root = R[i][j]
        if root == 0:
            return "None"
        else:
            return f"R{root} ( {construct_tree(C, R, i, root - 1)}, {construct_tree(C, R, root, j)} )"

# Example usage
keys = ["k1", "k2", "k3", "k4", "k5", "k6"]
weights = [10, 3, 9, 2, 0, 10]
q = [5, 6, 4, 4, 3, 8, 0]

C, R = optimal_bst(keys, weights, q)
print("Cost array:")
for row in C:
    print(row)

print("\nRoot array:")
for row in R:
    print(row)

print("\nOptimal Binary Search Tree:")
print(construct_optimal_bst(keys, weights, q))

C, R = optimal_bst(keys, weights, q)
print("Cost array:")
for row in C:
    print(row)

print("\nRoot array:")
for row in R:
    print(row)

print("\nOptimal Binary Search Tree:")
print(construct_optimal_bst(keys, weights, q))
