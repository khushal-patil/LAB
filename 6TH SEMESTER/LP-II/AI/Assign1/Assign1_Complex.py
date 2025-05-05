from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't exist"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v):
        """Add an edge between vertices u and v"""
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)  # Since the graph is undirected
    
    def remove_edge(self, u, v):
        """Remove edge between vertices u and v"""
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
    
    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges from the graph"""
        if vertex in self.graph:
            # Remove all edges connected to this vertex
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            # Remove the vertex itself
            del self.graph[vertex]
    
    def dfs(self, start, visited=None):
        """Depth First Search traversal"""
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def bfs_iterative(self, start):
        """Breadth First Search traversal (iterative implementation)"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def bfs_recursive_helper(self, queue, visited):
        """Helper function for recursive BFS"""
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
        """Breadth First Search traversal (recursive implementation)"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        self.bfs_recursive_helper(queue, visited)
    
    def print_graph(self):
        """Print the graph's adjacency list representation"""
        print("\nGraph Representation (Adjacency List):")
        for vertex in sorted(self.graph.keys()):
            neighbors = sorted(self.graph[vertex])
            print(f"{vertex}: {', '.join(map(str, neighbors))}")
    
    def has_path(self, u, v, visited=None):
        """Check if there's a path between vertices u and v"""
        if visited is None:
            visited = set()
        
        if u == v:
            return True
        
        visited.add(u)
        
        for neighbor in self.graph.get(u, []):
            if neighbor not in visited:
                if self.has_path(neighbor, v, visited):
                    return True
        return False
    
    def count_vertices(self):
        """Return the number of vertices in the graph"""
        return len(self.graph)
    
    def count_edges(self):
        """Return the number of edges in the graph"""
        edge_count = 0
        for vertex in self.graph:
            edge_count += len(self.graph[vertex])
        return edge_count // 2  # Each edge counted twice in undirected graph

def menu():
    g = Graph()
    while True:
        print("\nMenu")
        print("1. Add vertex")
        print("2. Add edge")
        print("3. Remove vertex")
        print("4. Remove edge")
        print("5. Depth First Search (DFS)")
        print("6. Breadth First Search (BFS) - Iterative")
        print("7. Breadth First Search (BFS) - Recursive")
        print("8. Print graph")
        print("9. Check path between vertices")
        print("10. Count vertices and edges")
        print("11. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            vertex = int(input("Enter vertex to add: "))
            g.add_vertex(vertex)
            print(f"Vertex {vertex} added.")
        elif choice == '2':
            u = int(input("Enter vertex u: "))
            v = int(input("Enter vertex v: "))
            g.add_edge(u, v)
            print(f"Edge between {u} and {v} added.")
        elif choice == '3':
            vertex = int(input("Enter vertex to remove: "))
            g.remove_vertex(vertex)
            print(f"Vertex {vertex} removed.")
        elif choice == '4':
            u = int(input("Enter vertex u: "))
            v = int(input("Enter vertex v: "))
            g.remove_edge(u, v)
            print(f"Edge between {u} and {v} removed.")
        elif choice == '5':
            start = int(input("Enter starting vertex for DFS: "))
            print("Depth First Search (DFS):")
            g.dfs(start)
            print()
        elif choice == '6':
            start = int(input("Enter starting vertex for BFS: "))
            print("Breadth First Search (BFS - Iterative):")
            g.bfs_iterative(start)
            print()
        elif choice == '7':
            start = int(input("Enter starting vertex for BFS: "))
            print("Breadth First Search (BFS - Recursive):")
            g.bfs_recursive(start)
            print()
        elif choice == '8':
            g.print_graph()
        elif choice == '9':
            u = int(input("Enter first vertex: "))
            v = int(input("Enter second vertex: "))
            if g.has_path(u, v):
                print(f"There is a path between {u} and {v}")
            else:
                print(f"There is NO path between {u} and {v}")
        elif choice == '10':
            print(f"Number of vertices: {g.count_vertices()}")
            print(f"Number of edges: {g.count_edges()}")
        elif choice == '11':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()