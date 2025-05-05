def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)


def job_scheduling(jobs, t):
    jobs.sort(key=lambda x: x[2], reverse=True)
    result = [None] * t
    slot = [False] * t
    total_profit = 0

    for job in jobs:
        for j in range(min(t - 1, job[1] - 1), -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job[0]
                total_profit += job[2]
                break

    print("Scheduled Jobs:", [job for job in result if job])
    print("Total Profit:", total_profit)


def prims_algorithm_adj_list(adj_list, n):
    import heapq

    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        for v, w in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                if weight != 0:  # avoid dummy edge (first edge is 0-weight)
                    mst_edges.append((u, v, w))

    print("Edges in MST (Prim's using adjacency list):", mst_edges)
    print("Total cost of MST (Prim's):", total_weight)


def kruskals_algorithm(edges, n):
    parent = list(range(n))

    def find(u):
        while parent[u] != u:
            u = parent[u]
        return u

    def union(u, v):
        parent[find(u)] = find(v)

    edges.sort(key=lambda x: x[2])
    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v))
            mst_weight += weight

    print("Edges in MST (Kruskal's):", mst_edges)
    print("Total cost of MST (Kruskal's):", mst_weight)


# Main menu
while True:
    print("\n--- Greedy Algorithm Applications ---")
    print("1. Selection Sort")
    print("2. Job Scheduling Problem")
    print("3. Prim's MST Algorithm (Adjacency List)")
    print("4. Kruskal's MST Algorithm")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter array elements (space-separated): ").split()))
        selection_sort(arr)

    elif choice == 2:
        n = int(input("Enter number of jobs: "))
        jobs = []
        for i in range(n):
            job_id = input(f"Enter Job ID for job {i + 1}: ")
            deadline = int(input("Enter deadline: "))
            profit = int(input("Enter profit: "))
            jobs.append((job_id, deadline, profit))
        max_deadline = max(job[1] for job in jobs)
        job_scheduling(jobs, max_deadline)

    elif choice == 3:
        n = int(input("Enter number of vertices: "))
        e = int(input("Enter number of edges: "))
        adj_list = {i: [] for i in range(n)}
        for _ in range(e):
            u, v, w = map(int, input("Enter edge (u v weight): ").split())
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))  # Undirected graph
        prims_algorithm_adj_list(adj_list, n)

    elif choice == 4:
        n = int(input("Enter number of vertices: "))
        e = int(input("Enter number of edges: "))
        edges = []
        for _ in range(e):
            u, v, w = map(int, input("Enter edge (u v weight): ").split())
            edges.append((u, v, w))
        kruskals_algorithm(edges, n)

    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
