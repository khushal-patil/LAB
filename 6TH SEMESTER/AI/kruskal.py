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
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            minimumCost += weight
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree cost:", minimumCost)


if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
    g = Graph(vertices)

    print("Enter the edges (u, v, weight) for each edge:")
    for _ in range(edges):
        u, v, w = map(int, input().split())
        g.addEdge(u, v, w)

    g.KruskalMST()

