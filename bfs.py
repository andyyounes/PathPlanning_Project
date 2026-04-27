from maps import LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4,build_nodes_and_edges, reset, NAME, DISTANCE, VISITED, PREVIOUS, ROW, COL, EDGE_SRC, EDGE_DEST, EDGE_W
from visualize import plot_path


def bfs(grid):
    """
    Parameters:
        grid : 2D list — the maze ('S' = start, 'E' = end, 1 = wall, 0 = open)

    Returns:
        nodes   : the nodes array (updated distances + previous pointers)
        path    : list of node numbers from start to end (shortest path)
        visited : set of node numbers that were fully explored
    """

    # Step 1 — Build nodes and edges from the grid
    nodes, edges, start_node, end_node, num_nodes, num_edges = build_nodes_and_edges(grid)
    found = False
    path =[]
    # Step 2 — Initialise: set start distance to 0 and enqueue it
    nodes[start_node][DISTANCE] = 0
    found = False

    # Step 3 — BFS main loop
    while True:
        current_node = None
        min_distance = 99999
        for i in range(1, 1+num_nodes):
            if nodes[i][DISTANCE]<min_distance and not nodes[i][VISITED]:
                min_distance = nodes[i][DISTANCE]
                current_node = i
        
        if current_node == None or min_distance == 99999:
            print("No way")
            break
        if current_node == end_node:
            break

        nodes[current_node][VISITED] = True
        for i in range(1, num_edges + 1):
            if edges[i][EDGE_SRC] == current_node:
                neighbour = edges[i][EDGE_DEST]
                weight = edges[i][EDGE_W]
                
                new_distance = nodes[current_node][DISTANCE] + weight

                if not nodes[neighbour][VISITED]:
                    if new_distance < nodes[neighbour][DISTANCE]:
                        nodes[neighbour][DISTANCE] = new_distance
                        nodes[neighbour][PREVIOUS] = current_node
                        found = True


    # Step 5 — Reconstruct path 
    if found:
        trace = end_node
        while trace is not None:
            path.append(trace)
            trace = nodes[trace][PREVIOUS]
        path.reverse()

    # Step 6 — Collect all visited nodes into a set for visualisation
    visited = set()
    for i in range(1, num_nodes + 1):
        if nodes[i][VISITED]:
            visited.add(i)

    return nodes, path, visited

if __name__ == "__main__":
    print("\n>> Level 1 (BFS - simple)")
    nodes, path, visited = bfs(LEVEL_1) 
    plot_path(LEVEL_1, nodes, path, visited, title="BFS — Level 1")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")

    print("\n>> Level 2 (BFS - medium)")
    nodes, path, visited = bfs(LEVEL_2)
    plot_path(LEVEL_2, nodes, path, visited, title="BFS — Level 2")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")
    print("\n>> Level 3 (BFS - hard)")
    nodes, path, visited = bfs(LEVEL_3)
    plot_path(LEVEL_3, nodes, path, visited, title="BFS — Level 3")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")


    print("\n>> Level 4 (BFS - maze)")
    nodes, path, visited = bfs(LEVEL_4)
    plot_path(LEVEL_4, nodes, path, visited, title="BFS — Level 4")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")
