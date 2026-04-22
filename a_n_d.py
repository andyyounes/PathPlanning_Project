nodes = {
    1: {'name': 'A', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 4, 'fscore': 9999},
    2: {'name': 'B', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 2, 'fscore': 9999},
    3: {'name': 'C', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 3, 'fscore': 9999},
    4: {'name': 'D', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 1, 'fscore': 9999},
    5: {'name': 'E', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 0, 'fscore': 9999},
}

edges = {
    1: {'name': 'A-B', 'src': 1, 'destination': 2, 'weight': 2},
    2: {'name': 'A-C', 'src': 1, 'destination': 3, 'weight': 3},
    3: {'name': 'B-C', 'src': 2, 'destination': 3, 'weight': 5},
    4: {'name': 'B-E', 'src': 2, 'destination': 5, 'weight': 4},
    5: {'name': 'C-D', 'src': 3, 'destination': 4, 'weight': 10},
    6: {'name': 'D-E', 'src': 4, 'destination': 5, 'weight': 1},
}


def reset():
    for node in nodes.values():
        node['distance'] = 9999
        node['visited']  = False
        node['previous'] = None
        node['fscore'] = 9999

def traceback(startNode, endNode):
    path = []
    current_node = endNode
    while current_node is not None:
        path.append(nodes[current_node]['name'])
        current_node = nodes[current_node]['previous']
    path.reverse()
    print("Path:", " -> ".join(path))
    print("Shortest distance:", nodes[endNode]['distance'])


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
