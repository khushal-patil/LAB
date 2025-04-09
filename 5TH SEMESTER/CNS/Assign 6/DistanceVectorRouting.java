import java.util.Scanner;

class Node {
    int id;
    int[] distance;
    int[] nextHop;

    Node(int numNodes) {
        distance = new int[numNodes];
        nextHop = new int[numNodes];
    }
}

public class DistanceVectorRouting {
    static final int MAX_NODES = 10;
    static final int INFINITY = Integer.MAX_VALUE;

    static Node[] nodes = new Node[MAX_NODES];
    static int[][] costMatrix = new int[MAX_NODES][MAX_NODES];
    static int numNodes;

    public static void initializeNodes() {
        for (int i = 0; i < numNodes; i++) {
            nodes[i] = new Node(numNodes);
            for (int j = 0; j < numNodes; j++) {
                if (i == j) {
                    nodes[i].distance[j] = 0;
                    nodes[i].nextHop[j] = i;
                } else if (costMatrix[i][j] != 0) {
                    nodes[i].distance[j] = costMatrix[i][j];
                    nodes[i].nextHop[j] = j;
                } else {
                    nodes[i].distance[j] = INFINITY;
                    nodes[i].nextHop[j] = -1;
                }
            }
        }
    }

    public static void updateDistanceVector(int node) {
        for (int i = 0; i < numNodes; i++) {
            if (i != node) {
                for (int j = 0; j < numNodes; j++) {
                    if (nodes[node].distance[j] > costMatrix[node][i] + nodes[i].distance[j]) {
                        nodes[node].distance[j] = costMatrix[node][i] + nodes[i].distance[j];
                        nodes[node].nextHop[j] = i;
                    }
                }
            }
        }
    }

    public static void printRoutingTable() {
        for (int i = 0; i < numNodes; i++) {
            System.out.println("Routing table for node " + i + ":");
            System.out.println("Destination\tDistance\tNext Hop");
            for (int j = 0; j < numNodes; j++) {
                System.out.println(j + "\t\t" + nodes[i].distance[j] + "\t\t" + nodes[i].nextHop[j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of nodes: ");
        numNodes = scanner.nextInt();

        System.out.println("Enter the cost matrix:");
        for (int i = 0; i < numNodes; i++) {
            for (int j = 0; j < numNodes; j++) {
                costMatrix[i][j] = scanner.nextInt();
            }
        }

        initializeNodes();

        for (int i = 0; i < numNodes; i++) {
            updateDistanceVector(i);
        }

        printRoutingTable();

        scanner.close();
    }
}
