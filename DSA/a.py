N = 6
p = [0, 10, 3, 9, 2, 0, 10]
q = [5, 6, 4, 4, 3, 8, 0]

W = [[0 for _ in range(N+2)] for _ in range(N+2)]
C = [[0 for _ in range(N+2)] for _ in range(N+2)]
R = [[0 for _ in range(N+1)] for _ in range(N+1)]

# Calculate W array
for i in range(N+1):
    W[i][i] = q[i]
    for j in range(i+1, N+1):
        W[i][j] = W[i][j-1] + p[j] + q[j]

# Calculate C and R arrays
for d in range(1, N+1):
    for i in range(0, N-d+1):
        j = i + d
        min_val = float('inf')
        min_k = i
        for k in range(i, j):
            if C[i][k] + C[k+1][j] < min_val:
                min_val = C[i][k] + C[k+1][j]
                min_k = k
        C[i][j] = W[i][j-1] + min_val
        R[i][j] = min_k
