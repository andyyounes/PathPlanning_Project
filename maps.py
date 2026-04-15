"""
Pathfinding Project - Grid Maps
A-Level Computer Science

Legend:
    0 = Open path (can walk)
    1 = Wall (blocked)
    'S' = Start position
    'E' = End position
"""

# ============================================
# LEVEL 1: Simple 5x5 Grid (No obstacles)
# ============================================

LEVEL_1 = [
    ['S', 0,  0,  0,  0],
    [0,   0,  0,  0,  0],
    [0,   0,  0,  0,  0],
    [0,   0,  0,  0,  0],
    [0,   0,  0,  0, 'E']
]

# ============================================
# LEVEL 2: 10x10 Grid with Walls
# ============================================

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

# ============================================
# LEVEL 3: 10x10 Harder Maze
# ============================================

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


def get_start_end(grid):
    """Find the start (S) and end (E) positions in the grid."""
    start = None
    end = None
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start = (row, col)
            elif grid[row][col] == 'E':
                end = (row, col)
    
    return start, end


def is_valid(grid, row, col):
    """Check if a position is valid (within bounds and not a wall)."""
    rows = len(grid)
    cols = len(grid[0])
    
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False
    
    if grid[row][col] == 1:
        return False
    
    return True


def get_neighbors(grid, row, col):
    """Get all valid neighboring positions (up, down, left, right)."""
    neighbors = []
    
    # Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid(grid, new_row, new_col):
            neighbors.append((new_row, new_col))
    
    return neighbors
