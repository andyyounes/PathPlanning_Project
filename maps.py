"""
Legend:
    0 = Open path (can walk)
    1 = Wall (blocked)
    'S' = Start position
    'E' = End position
"""
# column indexes for nodes
NAME     = 0
DISTANCE = 1
VISITED  = 2
PREVIOUS = 3
ROW      = 4
COL      = 5

# column indexes for edges
EDGE_NAME = 0
EDGE_SRC  = 1
EDGE_DEST = 2
EDGE_W    = 3

# LEVEL 1: Simple 5x5 Grid (No obstacles)

LEVEL_1 = [
    ['S', 0,  0,  0,  0],
    [0,   0,  0,  0,  0],
    [0,   0,  0,  0,  0],
    [0,   0,  0,  0,  0],
    [0,   0,  0,  0, 'E']
]

# LEVEL 2: 10x10 Grid with Walls

LEVEL_2 = [
    ['S', 0,  0,  0,  1,  0,  0,  0,  0,  0],
    [0,   0,  1,  0,  1,  0,  1,  1,  1,  0],
    [0,   0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,   0,  1,  1,  1,  1,  1,  0,  1,  0],
    [0,   0,  0,  0,  0,  0,  1,  0,  0,  0],
    [0,   1,  1,  1,  1,  0,  1,  1,  1,  0],
    [0,   0,  0,  0,  0,  0,  0,  0,  0,  0],
    [1,   1,  1,  1,  1,  1,  1,  1,  0,  0],
    [0,   0,  0,  0,  0,  0,  0,  0,  0,  1],
    [0,   0,  0,  0,  0,  0,  0,  0,  0, 'E']
]

# LEVEL 3: 10x10 Harder Maze
LEVEL_3 = [
    ['S', 0,  1,  0,  0,  0,  1,  0,  0,  0],
    [0,   0,  1,  0,  1,  0,  1,  0,  1,  0],
    [1,   0,  1,  0,  1,  0,  0,  0,  1,  0],
    [0,   0,  0,  0,  1,  1,  1,  0,  1,  0],
    [0,   1,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,   0,  1,  1,  1,  1,  1,  1,  1,  0],
    [1,   0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,   0,  1,  1,  1,  1,  1,  1,  1,  1],
    [0,   1,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,   0,  0,  1,  1,  1,  1,  1,  0, 'E']
]


LEVEL_4 = [
    ['S', 0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  0],
    [1,   0,  1,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1,  1,  0],
    [0,   0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0],
    [0,   1,  1,  1,  1,  1,  1,  0,  1,  1,  1,  1,  1,  0,  1],
    [0,   0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0],
    [1,   1,  1,  0,  1,  0,  1,  1,  1,  0,  1,  0,  1,  1,  0],
    [0,   0,  1,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0],
    [0,   1,  1,  0,  1,  1,  1,  1,  1,  0,  1,  1,  1,  0,  1],
    [0,   0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0],
    [1,   0,  1,  1,  1,  1,  1,  0,  1,  1,  1,  0,  1,  1,  0],
    [0,   0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0],
    [0,   1,  1,  0,  1,  1,  1,  1,  1,  0,  1,  1,  1,  0,  1],
    [0,   0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0],
    [1,   1,  0,  1,  1,  0,  1,  1,  0,  1,  1,  0,  1,  1,  0],
    [0,   0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0, 'E']
]

# CONVERTER
def build_nodes_and_edges(grid):
    """
    Converts a 2D grid into a nodes array and edges array
    exactly like the named graph students already know.

    nodes[i] = [name, distance, visited, previous, row, col]
    edges[k] = [name, src, destination, weight]

    Walls (1) are skipped.
    Index 0 of both arrays is unused so numbering starts at 1.
    """
    rows = len(grid)
    cols = len(grid[0])

    nodes      = [[]]
    edges      = [[]]
    start_node = None
    end_node   = None

    # node_id[r][c] = node number for that cell (0 = wall)
    node_id = [[0] * cols for _ in range(rows)]

    # pass 1: assign a node number to every walkable cell
    counter = 1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                node_id[r][c] = counter
                nodes.append([str(counter), 9999, False, None, r, c])
                if grid[r][c] == 'S':
                    start_node = counter
                elif grid[r][c] == 'E':
                    end_node = counter
                counter += 1

    # pass 2: connect neighbours with edges (both directions)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                continue
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < rows and nc < cols and grid[nr][nc] != 1:
                    src  = node_id[r][c]
                    dest = node_id[nr][nc]
                    edges.append(['', src,  dest, 1])
                    edges.append(['', dest, src,  1])

    num_nodes = len(nodes) - 1
    num_edges = len(edges) - 1

    return nodes, edges, start_node, end_node, num_nodes, num_edges


# RESET
def reset(nodes, num_nodes):
    """Reset all nodes back to starting values for a second run."""
    for i in range(1, num_nodes + 1):
        nodes[i][DISTANCE] = 9999
        nodes[i][VISITED]  = False
        nodes[i][PREVIOUS] = None
        if len(nodes[i]) > 6:
            nodes[i][6] = 9999
