class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i = 0  
        e = 0  
        self.graph = sorted(self.graph, key=lambda item: item[2])  
        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1:
            if i >= len(self.graph):
                break  
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        if len(result) != self.V - 1:
            print("No Minimum Spanning Tree (MST) exists (Graph might be disconnected).")
            return

        minimumCost = sum(weight for _, _, weight in result)
        print("\nEdges in the constructed Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree cost:", minimumCost)

    def displayGraph(self):
        if not self.graph:
            print("Graph is empty! Add edges first.")
        else:
            print("\nCurrent Graph Edges:")
            for u, v, w in self.graph:
                print(f"{u} -- {v} == {w}")

if __name__ == '__main__':
    print("Welcome to Kruskal’s MST Algorithm!")
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    while True:
        print("\nMenu:")
        print("1. Add Edge")
        print("2. Display Graph")
        print("3. Find Minimum Spanning Tree (MST) using Kruskal’s Algorithm")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            u = int(input("Enter starting vertex (u): "))
            v = int(input("Enter ending vertex (v): "))
            w = int(input("Enter weight of edge: "))
            if 0 <= u < vertices and 0 <= v < vertices:
                g.addEdge(u, v, w)
                print("Edge added successfully!")
            else:
                print("Invalid vertices! Please enter values between 0 and", vertices - 1)
        
        elif choice == '2':
            g.displayGraph()

        elif choice == '3':
            g.KruskalMST()

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please enter a valid option.")
