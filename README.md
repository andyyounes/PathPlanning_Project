# Pathfinding Project

**A-Level Computer Science - Group Project**

## Overview

Implement a pathfinding algorithm to find the shortest path through a maze!

**We give you:**
- The cost/heuristic formulas
- Helper functions
- Visualization code

**You implement:**
- The actual algorithm logic!

## Setup

```bash
pip install matplotlib numpy
```
### In case pip is not installed
visit: 
https://pip.pypa.io/en/stable/installation/

## Files

| File | What it does | Edit? |
|------|--------------|-------|
| `maps.py` | The 3 level grids | No |
| `visualize.py` | Draws the maps | No |
| `dijkstra.py` | Dijkstra's algorithm | Yes (Dijkstra teams) |
| `a_star.py` | A* algorithm | Yes (A* teams) |

## How to Run

```bash
python dijkstra.py    # Dijkstra teams
python a_star.py      # A* teams
```

## The Formulas We Give You

### Dijkstra
```
cost(neighbor) = cost(current) + 1
```
Each step costs 1. That's it!

### A* (uses 3 values)
```
g(n) = actual cost from start to n
h(n) = estimated cost from n to goal (Manhattan distance)
f(n) = g(n) + h(n)
```

A* always picks the node with lowest **f** value!

## The Maps

| Level | Size | Difficulty |
|-------|------|------------|
| 1 | 5x5 | Easy - no walls |
| 2 | 10x10 | Medium - some walls |
| 3 | 10x10 | Hard - maze |

## Algorithm Hints

### What you need:
1. **Priority queue** - use `heapq`
2. **Visited set** - don't revisit nodes!
3. **came_from dict** - remember the path
4. **cost/g_score dict** - track costs

### Basic structure:
```python
# 1. Setup
queue = []
heapq.heappush(queue, (0, start))
visited = set()
came_from = {start: None}

# 2. Main loop
while queue:
    cost, current = heapq.heappop(queue)
    
    if current == end:
        return reconstruct_path(...)
    
    if current in visited:
        continue
    visited.add(current)
    
    for neighbor in get_neighbors(grid, current[0], current[1]):
        # Calculate cost, add to queue...
```
### Heapq
visit: https://docs.python.org/3/library/heapq.html

## Final Challenge

After everyone finishes, we'll race both algorithms on a **secret map**!

Which explores fewer nodes - Dijkstra or A*?

---

Good luck!
