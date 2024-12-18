# Function to create a graph using an adjacency list
def create_graph(num_nodes, num_edges):

    graph = {i: [] for i in range(0, num_nodes)}

    # Add edges
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph[u].append(v)  # Add v to the list of neighbors for node u
        graph[v].append(u)  # Add u to the list of neighbors for node v (because it's an undirected graph)

    return graph

def colored_graph(graph):

    colors = {node: None for node in graph}

    # Function to check if it's safe to color a node with a given color
    def is_safe(node, color):
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
        return True

    # Function to color a node
    def color_node(node):
        for color in range(1, 2):
            if is_safe(node, color):
                colors[node] = color
                break

    # Color each node
    for node in graph:
        color_node(node)

    return colors

def is_bicolourable(graph):
    BICOLOURABLE = True
    for node, neighbors in graph.items():


        for num_neighbor in neighbors:
            if color_graph[node] == color_graph[neighbors[len(neighbors)-1]]:
                BICOLOURABLE = False
                break
        
    if BICOLOURABLE == False:
        print("NOT BICOLOURABLE")
    else:
        print("BICOLOURABLE")

# Main code
while True:

    # Read number of nodes and edges
    num_nodes = int(input())
    if num_nodes == 0:
        break

    num_edges = int(input())

    # Using the function
    graph = create_graph(num_nodes, num_edges)
    color_graph = colored_graph(graph)
    is_bicolourable(graph)