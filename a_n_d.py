#index name dist visited previous heuristic fscore
nodes = [
    [],#index 0 unused, so nodes[1] = A
    ['A', 9999, False, None, 4, 9999],# node 1 = A
    ['B', 9999, False, None, 2, 9999],# node 2 = B
    ['C', 9999, False, None, 3, 9999],# node 3 = C
    ['D', 9999, False, None, 1, 9999],# node 4 = D
    ['E', 9999, False, None, 0, 9999],# node 5 = E
]

#index name src neighbor weight
edges = [
    [],# index 0 unused
    ['A-B', 1, 2, 2],#edge 1
    ['A-C', 1, 3, 3],# edge 2
    ['B-C', 2, 3, 5],#edge 3
    ['B-E', 2, 5, 4],# edge 4
    ['C-D', 3, 4, 10],# edge 5
    ['D-E', 4, 5, 1],# edge 6
]

#column indexes for readability, use those instead of hardcoding numbers in the code below
NAME     = 0
DISTANCE = 1
VISITED  = 2
PREVIOUS = 3
H        = 4
FSCORE   = 5

EDGE_SRC  = 1
EDGE_DEST = 2
EDGE_W    = 3

def reset():
    for node in range(1, len(nodes)):
        nodes[node][DISTANCE] = 9999
        nodes[node][VISITED]  = False
        nodes[node][PREVIOUS] = None
        nodes[node][FSCORE] = 9999

def traceback(startNode, endNode):
    path = []
    current_node = endNode
    while current_node is not None:
        path.append(nodes[current_node][NAME])
        current_node = nodes[current_node][PREVIOUS]
    path.reverse()
    print("Path:", " -> ".join(path))
    print("Shortest distance:", nodes[endNode][DISTANCE])

def dijkstra(startNode, endNode):
#  write your Dijkstra's algorithm here


def astar(start, end):
# write your A* algorithm here

# run both
print("=== A* ===")
astar(1, 5)

reset()

print("\n=== Dijkstra ===")
dijkstra(1, 5)
