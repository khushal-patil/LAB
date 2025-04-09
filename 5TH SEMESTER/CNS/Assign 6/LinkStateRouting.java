import java.util.*;

class LinkStateRouting {
    private static final int INF = Integer.MAX_VALUE;

    // Dijkstra's algorithm to find the shortest path
    public void dijkstra(int[][] graph, int source) {
        int nodes = graph.length;
        int[] dist = new int[nodes]; // The output array. dist[i] holds the shortest distance from source to i.
        boolean[] visited = new boolean[nodes]; // visited[i] is true if the vertex i is processed

        // Initialize distances with INF and set the distance to the source to 0
        Arrays.fill(dist, INF);
        dist[source] = 0;

        // Find shortest path for all nodes
        for (int i = 0; i < nodes - 1; i++) {
            // Pick the minimum distance node from the set of vertices not yet processed
            int u = minDistance(dist, visited);

            // Mark the picked node as processed
            visited[u] = true;

            // Update dist value of the adjacent vertices of the picked node
            for (int v = 0; v < nodes; v++) {
                // Update dist[v] only if it is not visited, there's an edge from u to v,
                // and the total weight of path from source to v through u is smaller than the
                // current value of dist[v]
                if (!visited[v] && graph[u][v] != 0 && dist[u] != INF && dist[u] + graph[u][v] < dist[v]) {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }

        // Print the shortest distances from the source node
        printSolution(dist, source);
    }

    // Utility function to find the vertex with minimum distance value, from the set
    // of vertices not yet processed
    private int minDistance(int[] dist, boolean[] visited) {
        int min = INF, minIndex = -1;

        for (int v = 0; v < dist.length; v++) {
            if (!visited[v] && dist[v] < min) {
                min = dist[v];
                minIndex = v;
            }
        }
        return minIndex;
    }

    // Utility function to print the constructed distance array
    private void printSolution(int[] dist, int source) {
        System.out.println("Vertex\t\tDistance from Source " + source);
        for (int i = 0; i < dist.length; i++) {
            System.out.println(i + "\t\t" + (dist[i] == INF ? "INF" : dist[i]));
        }
    }

    public static void main(String[] args) {
        // Example graph represented as an adjacency matrix
        // 0 means no direct link
        int[][] graph = {
                { 0, 2, 0, 1, 0 },
                { 2, 0, 3, 2, 0 },
                { 0, 3, 0, 0, 7 },
                { 1, 2, 0, 0, 4 },
                { 0, 0, 7, 4, 0 }
        };

        LinkStateRouting lsp = new LinkStateRouting();
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter source node (0-" + (graph.length - 1) + "): ");
        int source = sc.nextInt();

        // Run Dijkstra's algorithm to find the shortest path
        lsp.dijkstra(graph, source);
    }
}
