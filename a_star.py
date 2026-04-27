from maps import LEVEL_1, LEVEL_2, LEVEL_3, build_nodes_and_edges, reset, NAME, DISTANCE, VISITED, PREVIOUS, ROW, COL, EDGE_SRC, EDGE_DEST, EDGE_W
from visualize import plot_path, print_grid, print_grid_with_path, print_grid_with_explored


def heuristic(nodes, node, end_node):
    row1 = nodes[node][ROW]
    col1 = nodes[node][COL]
    row2 = nodes[end_node][ROW]
    col2 = nodes[end_node][COL]
    return abs(row1 - row2) + abs(col1 - col2)

def a_star(grid):
    """
    A* ALGORITHM STEPS:
    1. Set start node distance to 0
    set start node fScore to heuristic(start, end)
    2. REPEAT:
        a. Find the unvisited node with the lowest fScore
            — this is your current_node
            — if none found, no path exists, stop
        b. If current_node is the end node, stop — destination reached
        c. Mark current_node as visited
        d. For each edge leaving current_node:
            — calculate newG = current distance + edge weight
            — calculate newF = newG + heuristic(neighbour, end)
            — if neighbour is unvisited AND newF is better than what it already has:
                    update neighbour distance to newG
                    update neighbour fScore to newF
                    update neighbour previousNode to current_node
    3. Traceback from end node using previousNode until you reach None
    WHAT YOU HAVE:
    nodes : array of all nodes, each has:
        [NAME, DISTANCE, VISITED, PREVIOUS, ROW, COL, FSCORE]
    edges :array of all edges, each has:
        [NAME, SRC, DEST, WEIGHT]
    startNode : index of the start node
    endNode : index of the end node
    num_nodes : total number of nodes
    num_edges : total number of edges
    heuristic(nodes, node, endNode) : gives you the Manhattan distance
                                        from any node to the end
    """
    nodes,edges,startNode,endNode,num_nodes,num_edges = build_nodes_and_edges(grid)
    FSCORE = 6
    for i in range(1, num_nodes+1):
        nodes[i].append(9999)

    #my code
    nodes[startNode][DISTANCE] = 0
    nodes[startNode][FSCORE] = heuristic(nodes, startNode, endNode)


    while True:
        currentNode = None
        minFScore = 99999
        for i in range(1,num_nodes+1):
            if not nodes[i][VISITED] and nodes[i][FSCORE]<minFScore:
                minFScore = nodes[i][FSCORE]
                currentNode = i
        
        if currentNode == None or minFScore == 99999:
            print("No way")
            break
        if currentNode == endNode:
            break

        nodes[currentNode][VISITED] = True
        for i in range(1, num_edges + 1):
            if edges[i][EDGE_SRC] == currentNode:
                neighbour = edges[i][EDGE_DEST]
                weight = edges[i][EDGE_W]
                
                new_distance = nodes[currentNode][DISTANCE] + weight
                new_Fscore = new_distance + heuristic(nodes, neighbour, endNode)

                if not nodes[neighbour][VISITED]:
                    if new_Fscore < nodes[neighbour][FSCORE]:
                        nodes[neighbour][DISTANCE] = new_distance
                        nodes[neighbour][FSCORE] = new_Fscore
                        nodes[neighbour][PREVIOUS] = currentNode

    path = []
    visited = set()
    
    trace=endNode
    while trace is not None:
        path.append(trace)
        trace=nodes[trace][PREVIOUS]
    path.reverse()
    for i in range(1,num_nodes+1):
        if nodes[i][VISITED]:
            visited.add(i)
    return nodes,path,visited

# TEST YOUR CODE
if __name__ == "__main__":
    print("\n" + "="*50)
    print(" A* ALGORITHM")
    print("="*50)

    print("\n>> Level 1 (easy - no walls)")
    nodes,path,visited = a_star(LEVEL_1)
    plot_path(LEVEL_1, nodes, path, visited, title="A* — Level 1")

    print("\n>> Level 2 (medium - some walls)")
    nodes,path,visited = a_star(LEVEL_2)
    plot_path(LEVEL_2, nodes, path, visited, title="A* — Level 2")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")

    print("\n>> Level 3 (hard - maze)")
    nodes,path,visited = a_star(LEVEL_3)
    plot_path(LEVEL_3, nodes, path, visited, title="A* — Level 3")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")
