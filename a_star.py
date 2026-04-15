"""
Pathfinding Project - A* Algorithm
A-Level Computer Science

WHAT WE GIVE YOU:
- h(n) = heuristic function (Manhattan distance)
- g(n) = cost from start (each step costs 1)
- f(n) = g(n) + h(n) (total estimated cost)
- Helper functions

YOUR TASK:
- Implement the A* algorithm using these formulas
- Make it work on all 3 levels!

A* is smarter than Dijkstra because it uses the heuristic
to guess which direction leads to the goal!
"""

import heapq
from maps import LEVEL_1, LEVEL_2, LEVEL_3, get_start_end, get_neighbors
from visualize import print_grid, print_grid_with_path, print_grid_with_explored


# ============================================
# THE FORMULAS (we give you these!)
# ============================================

def h(position, goal):
    """
    h(n) = HEURISTIC - Estimated distance to goal
    
    We use Manhattan distance: how many steps if you can only
    go up/down/left/right (no diagonals).
    
    Example: from (1, 2) to (4, 5)
    - Row difference: |1 - 4| = 3
    - Col difference: |2 - 5| = 3
    - Manhattan distance: 3 + 3 = 6
    
    Args:
        position: Current position (row, col)
        goal: Goal position (row, col)
        
    Returns:
        Estimated steps to reach goal
    """
    row1, col1 = position
    row2, col2 = goal
    return abs(row1 - row2) + abs(col1 - col2)


def g(current_g):
    """
    g(n) = ACTUAL COST from start to current node
    
    Each step costs 1, so:
    g(neighbor) = g(current) + 1
    
    Args:
        current_g: The g value of the current node
        
    Returns:
        The g value for the neighbor (current_g + 1)
    """
    return current_g + 1


def f(g_value, h_value):
    """
    f(n) = TOTAL ESTIMATED COST
    
    f(n) = g(n) + h(n)
    
    This is what A* uses to decide which node to explore next.
    Lower f = more promising path!
    
    Args:
        g_value: Actual cost from start
        h_value: Estimated cost to goal
        
    Returns:
        Total estimated cost (g + h)
    """
    return g_value + h_value


# ============================================
# PATH RECONSTRUCTION (we give you this!)
# ============================================

def reconstruct_path(came_from, start, end):
    """
    Rebuild the path from start to end by following the came_from links.
    
    Args:
        came_from: Dictionary mapping each node to the node we came from
        start: Starting position (row, col)
        end: Ending position (row, col)
        
    Returns:
        List of (row, col) positions from start to end
    """
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    
    path.reverse()
    return path


# ============================================
# YOUR TASK: IMPLEMENT A* ALGORITHM
# ============================================

def a_star(grid):
    """
    Find the shortest path using A* algorithm.
    
    A* ALGORITHM STEPS:
    1. Start at 'S', add it to priority queue with f=0+h(start,end)
    2. While the queue is not empty:
       a. Get the node with LOWEST f value from the queue
       b. If it's the end 'E', we're done! Reconstruct the path.
       c. If we've already visited it, skip it
       d. Mark it as visited
       e. For each neighbor (up, down, left, right):
          - Calculate g_new = g(current_g)
          - Calculate h_new = h(neighbor, end)
          - Calculate f_new = f(g_new, h_new)
          - If it's a better path, remember it and add to queue
    3. If queue is empty and we didn't find 'E', return empty path
    
    USEFUL FUNCTIONS:
    - get_start_end(grid) → returns (start, end) positions
    - get_neighbors(grid, row, col) → returns list of valid neighbor positions
    - g(current_g) → returns g value for neighbor
    - h(position, goal) → returns heuristic estimate
    - f(g_value, h_value) → returns total f value
    - reconstruct_path(came_from, start, end) → returns the path
    - heapq.heappush(queue, (f_value, position)) → add to priority queue
    - heapq.heappop(queue) → get (f_value, position) with lowest f
    
    Args:
        grid: 2D list representing the map
        
    Returns:
        path: List of (row, col) tuples from start to end
        explored: Set of all nodes that were visited
    """
    
    # Get start and end positions
    start, end = get_start_end(grid)
    
    # YOUR CODE HERE!
    # Hint: You'll need:
    # - A priority queue (list + heapq) - sorted by f value!
    # - A set for visited nodes
    # - A dictionary for g values (g_score)
    # - A dictionary to track where we came from (came_from)
    
    
    
    
    
    
    
    
    
    
    
    
    
    # If no path found, return empty
    return [], set()


# ============================================
# TEST YOUR CODE
# ============================================

if __name__ == "__main__":
    print("\n" + "="*50)
    print(" A* ALGORITHM")
    print("="*50)
    
    # Test Level 1
    print("\n>> Level 1 (easy - no walls)")
    print_grid(LEVEL_1, "Level 1 - Map")
    path, explored = a_star(LEVEL_1)
    
    if path and len(path) > 1:
        print_grid_with_path(LEVEL_1, path, "Level 1 - Solution")
        print(f"[OK] Success! Path length: {len(path)} steps")
    else:
        print("[X] No path found - keep working on your algorithm!")
    
    # Test Level 2
    print("\n>> Level 2 (medium - some walls)")
    print_grid(LEVEL_2, "Level 2 - Map")
    path, explored = a_star(LEVEL_2)
    
    if path and len(path) > 1:
        print_grid_with_explored(LEVEL_2, path, explored, "Level 2 - Solution")
        print(f"[OK] Success! Path length: {len(path)}, Nodes explored: {len(explored)}")
    else:
        print("[X] No path found - keep working on your algorithm!")
    
    # Test Level 3
    print("\n>> Level 3 (hard - maze)")
    print_grid(LEVEL_3, "Level 3 - Map")
    path, explored = a_star(LEVEL_3)
    
    if path and len(path) > 1:
        print_grid_with_explored(LEVEL_3, path, explored, "Level 3 - Solution")
        print(f"[OK] Success! Path length: {len(path)}, Nodes explored: {len(explored)}")
    else:
        print("[X] No path found - keep working on your algorithm!")
    
    print("\n" + "="*50)
    print(" Compare with Dijkstra - did A* explore fewer nodes?")
    print("="*50)
