def is_safe(node, graph, color, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, m, color, node=0):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring(graph, m, color, node + 1):
                return True
            color[node] = 0
    return False

def draw_text_graph(graph, color):
    color_names = ['None', 'Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']

    print("\n--- Graph Representation (ASCII Art) ---")
    for i in range(len(graph)):
        print(f"[{i}:{color_names[color[i]]}]", end="")
        for j in range(len(graph)):
            if graph[i][j] == 1:
                print(f" --[{j}]--> ", end="")
        print()


print("Graph Coloring with ASCII Art Output")

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
m = int(input("Enter number of colors: "))

graph = [[0 for _ in range(n)] for _ in range(n)]

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

color = [0] * n

if graph_coloring(graph, m, color):
    print("\nColor assignment:")
    for i in range(n):
        print(f"Vertex {i} --> Color {color[i]}")
    draw_text_graph(graph, color)
else:
    print("No solution with given number of colors.")


