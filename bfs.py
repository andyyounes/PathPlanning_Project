from maps import LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4,build_nodes_and_edges, reset, NAME, DISTANCE, VISITED, PREVIOUS, ROW, COL, EDGE_SRC, EDGE_DEST, EDGE_W
from visualize import plot_path
import queue

def findNeighbour(edges, node):
    l = []
    for i in range(1,len(edges)):
        print(edges[i][EDGE_SRC] == node)
        if edges[i][EDGE_SRC] == node:
            l.append(edges[i][EDGE_DEST])
    return l

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
    path = []
    # Step 2 — Initialise: set start distance to 0 and enqueue it
    
    toExplore = queue.Queue()
    toExplore.put(nodes[start_node])
    nodes[start_node][DISTANCE] = 0
    nodes[start_node][VISITED] = True
    currentNode = nodes[start_node]

    # Step 3 — BFS main loop
    print(end_node)

    while not toExplore.empty():
        currentNode = toExplore.get()
        if int(currentNode[NAME]) == end_node:
            found = True
            break
        else:
            neighbours = findNeighbour(edges,int(currentNode[NAME]))
            print(neighbours)
            for i in neighbours:
                if nodes[i][VISITED] == False:
                    nodes[i][DISTANCE] = currentNode[DISTANCE] + 1
                    nodes[i][PREVIOUS] = int(currentNode[NAME])
                    nodes[i][VISITED] = True
                    toExplore.put(nodes[i])
        print(currentNode, toExplore.empty())


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
