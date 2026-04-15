"""
Pathfinding Project - Dijkstra's Algorithm
A-Level Computer Science

WHAT WE GIVE YOU:
- The cost calculation (each step costs 1)
- Helper functions
- The structure

YOUR TASK:
- Implement the algorithm using the cost formula
- Make it work on all 3 levels!
"""

import heapq
from maps import LEVEL_1, LEVEL_2, LEVEL_3, get_start_end, get_neighbors
from visualize import print_grid, print_grid_with_path, print_grid_with_explored


# ============================================
# COST FORMULA (we give you this!)
# ============================================

def calculate_cost(current_cost):
    """
    Calculate the cost to move to a neighbor.
    
    In Dijkstra, every step costs 1.
    So if we're at a node with cost 5, moving to a neighbor costs 5 + 1 = 6
    
    Args:
        current_cost: The cost to reach the current node
        
    Returns:
        The cost to reach the neighbor (current_cost + 1)
    """
    return current_cost + 1


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
# YOUR TASK: IMPLEMENT DIJKSTRA'S ALGORITHM
# ============================================

def dijkstra(grid):
    """
    Find the shortest path using Dijkstra's algorithm.
    
    ALGORITHM STEPS:
    1. Start at 'S', add it to a priority queue with cost 0
    2. While the queue is not empty:
       a. Get the node with LOWEST cost from the queue
       b. If it's the end 'E', we're done! Reconstruct the path.
       c. If we've already visited it, skip it
       d. Mark it as visited
       e. For each neighbor (up, down, left, right):
          - Calculate the cost using calculate_cost()
          - If it's a better path, remember it and add to queue
    3. If queue is empty and we didn't find 'E', return empty path
    
    USEFUL FUNCTIONS:
    - get_start_end(grid) → returns (start, end) positions
    - get_neighbors(grid, row, col) → returns list of valid neighbor positions
    - calculate_cost(current_cost) → returns cost to reach neighbor
    - reconstruct_path(came_from, start, end) → returns the path
    - heapq.heappush(queue, (cost, position)) → add to priority queue
    - heapq.heappop(queue) → get (cost, position) with lowest cost
    
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
    # - A priority queue (list + heapq)
    # - A set for visited nodes
    # - A dictionary for costs (cost_so_far)
    # - A dictionary to track where we came from (came_from)
    
    
    
    
    
    
    
    
    
    
    
    
    
    # If no path found, return empty
    return [], set()


# ============================================
# TEST YOUR CODE
# ============================================

if __name__ == "__main__":
    print("\n" + "="*50)
    print(" DIJKSTRA'S ALGORITHM")
    print("="*50)
    
    # Test Level 1
    print("\n>> Level 1 (easy - no walls)")
    print_grid(LEVEL_1, "Level 1 - Map")
    path, explored = dijkstra(LEVEL_1)
    
    if path and len(path) > 1:
        print_grid_with_path(LEVEL_1, path, "Level 1 - Solution")
        print(f"[OK] Success! Path length: {len(path)} steps")
    else:
        print("[X] No path found - keep working on your algorithm!")
    
    # Test Level 2
    print("\n>> Level 2 (medium - some walls)")
    print_grid(LEVEL_2, "Level 2 - Map")
    path, explored = dijkstra(LEVEL_2)
    
    if path and len(path) > 1:
        print_grid_with_explored(LEVEL_2, path, explored, "Level 2 - Solution")
        print(f"[OK] Success! Path length: {len(path)}, Nodes explored: {len(explored)}")
    else:
        print("[X] No path found - keep working on your algorithm!")
    
    # Test Level 3
    print("\n>> Level 3 (hard - maze)")
    print_grid(LEVEL_3, "Level 3 - Map")
    path, explored = dijkstra(LEVEL_3)
    
    if path and len(path) > 1:
        print_grid_with_explored(LEVEL_3, path, explored, "Level 3 - Solution")
        print(f"[OK] Success! Path length: {len(path)}, Nodes explored: {len(explored)}")
    else:
        print("[X] No path found - keep working on your algorithm!")
    
    print("\n" + "="*50)
