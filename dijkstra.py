from maps import LEVEL_1,LEVEL_2,LEVEL_3,build_nodes_and_edges,NAME,DISTANCE,VISITED,PREVIOUS,ROW,COL,EDGE_SRC,EDGE_DEST,EDGE_W
from visualize import plot_path


def dijkstra(grid):
    """
    DIJKSTRA ALGORITHM STEPS:
    1. Set start node distance to 0
    2. REPEAT:
       a. Find the unvisited node with the lowest distance
          — this is your current_node
          — if none found, no path exists, stop
       b. If current_node is the end node, stop — destination reached
       c. Mark current_node as visited
       d. For each edge leaving current_node:
          — calculate newDistance = current distance + edge weight
          — if neighbour is unvisited AND newDistance is better than what it already has:
                update neighbour distance to newDistance
                update neighbour previousNode to current_node
    3. Traceback from end node using previousNode until you reach None
    WHAT YOU HAVE:
       nodes:  array of all nodes, each has:
            [NAME, DISTANCE, VISITED, PREVIOUS, ROW, COL]
       edges: array of all edges, each has:
           [NAME, SRC, DEST, WEIGHT]
       startNode : index of the start node
       endNode : index of the end node
       num_nodes : total number of nodes
       num_edges : total number of edges
    """
    nodes,edges,startNode,endNode,num_nodes,num_edges = build_nodes_and_edges(grid)

    #my code
    nodes[startNode][DISTANCE] = 0

    while True:
        currentNode = None
        minDistance = 99999
        for i in range(1,num_nodes+1):
            if not nodes[i][VISITED] and nodes[i][DISTANCE]<minDistance:
                minDistance = nodes[i][DISTANCE]
                currentNode = i
        if currentNode == None or minDistance == 99999:
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

                if not nodes[neighbour][VISITED]:
                    if new_distance < nodes[neighbour][DISTANCE]:
                        nodes[neighbour][DISTANCE] = new_distance
                        nodes[neighbour][PREVIOUS] = currentNode


    path=[]
    visited=set()
    trace=endNode
    while trace is not None:
        path.append(trace)
        trace=nodes[trace][PREVIOUS]
    path.reverse()
    for i in range(1,num_nodes+1):
        if nodes[i][VISITED]:
            visited.add(i)
    return nodes,path,visited


if __name__ == "__main__":
    print("\n"+"="*50)
    print(" DIJKSTRA'S ALGORITHM")
    print("="*50)
    print("\n>> Level 1 (easy - no walls)")
    nodes,path,visited=dijkstra(LEVEL_1)
    plot_path(LEVEL_1,nodes,path,visited,title="Dijkstra — Level 1")
    print("\n>> Level 2 (medium - some walls)")
    nodes,path,visited=dijkstra(LEVEL_2)
    plot_path(LEVEL_2,nodes,path,visited,title="Dijkstra — Level 2")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")
    print("\n>> Level 3 (hard - maze)")
    nodes,path,visited=dijkstra(LEVEL_3)
    plot_path(LEVEL_3,nodes,path,visited,title="Dijkstra — Level 3")
    print(f"Path: {len(path)} steps | Explored: {len(visited)} nodes")
