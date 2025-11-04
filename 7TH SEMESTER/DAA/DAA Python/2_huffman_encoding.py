import heapq

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq        # Frequency of symbol
        self.symbol = symbol    # Symbol name (character)
        self.left = left        # Left child node
        self.right = right      # Right child node
        self.huff = ''          # Tree direction (0/1)

    # Define less-than for heapq comparison
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Recursive function to print Huffman codes
def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    # Traverse the left and right children
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)

    # Leaf node — print symbol and code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

# Main program
if __name__ == "__main__":
    print("🔹 Huffman Encoding using Greedy Strategy 🔹\n")

    # Take dynamic user input
    chars = input("Enter characters (without spaces): ")
    print("Enter their corresponding frequencies:")

    freq = []
    for ch in chars:
        f = int(input(f"Frequency of '{ch}': "))
        freq.append(f)

    # Convert to list of nodes
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    # Build Huffman Tree
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        # Combine two smallest nodes
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    # Print Huffman Codes
    print("\nHuffman Codes for the given characters:")
    print_nodes(nodes[0])
