# Graph setup
nodes = {
    1: {'name': 'A', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 4},
    2: {'name': 'B', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 2},
    3: {'name': 'C', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 3},
    4: {'name': 'D', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 1},
    5: {'name': 'E', 'distance': 9999, 'visited': False, 'previous': None, 'heuristic': 0},
}

edges = [
    (1, 2, 2),  # A -> B, weight 2
    (1, 3, 3),  # A -> C, weight 3
    (2, 3, 5),  # B -> C, weight 5
    (2, 5, 4),  # B -> E, weight 4
    (3, 4, 10), # C -> D, weight 10
    (4, 5, 1),  # D -> E, weight 1
]


def reset():
    for node in nodes.values():
        node['distance'] = 9999
        node['visited']  = False
        node['previous'] = None


def traceback(start, end):
    path = []
    current = end
    while current is not None:
        path.append(nodes[current]['name'])
        current = nodes[current]['previous']
    path.reverse()
    print("Path:", " -> ".join(path))
    print("Shortest distance:", nodes[end]['distance'])


def dijkstra(start, end):
#  write your Dijkstra's algorithm here


def astar(start, end):
# write your A* algorithm here

# run both
print("=== A* ===")
astar(1, 5)

reset()

print("\n=== Dijkstra ===")
dijkstra(1, 5)