from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since the graph is undirected

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs_recursive_helper(self, queue, visited):
        if not queue:
            return
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        self.bfs_recursive_helper(queue, visited)

    def bfs_recursive(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        self.bfs_recursive_helper(queue, visited)

def menu():
    g = Graph()
    while True:
        print("\nMenu")
        print("1. Add edge")
        print("2. Depth First Search (DFS)")
        print("3. Breadth First Search (BFS)")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            u = int(input("Enter vertex u: "))
            v = int(input("Enter vertex v: "))
            g.add_edge(u, v)
        elif choice == '2':
            start = int(input("Enter starting vertex for DFS: "))
            print("Depth First Search (DFS):")
            g.dfs(start)
            print()
        elif choice == '3':
            start = int(input("Enter starting vertex for BFS: "))
            print("Breadth First Search (BFS):")
            g.bfs_recursive(start)
            print()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


menu()


