# Pathfinding Project

**A-Level Computer Science - Group Project**

## Overview

Implement a pathfinding algorithm to find the shortest path through a maze!

**We give you:**
- The grid maps (3 levels)
- The data structures (nodes and edges built automatically from the grid)
- The visualisation (plot_path draws the result for you)

**You implement:**
- The actual algorithm logic inside `dijkstra()` or `astar()`

## Setup

### Step 1 — Check if Python is installed

```bash
python --version
```

If you see a version number, Python is installed. If not:
- Go to https://www.python.org/downloads/
- Download the latest version
- During installation **make sure to tick "Add Python to PATH"**
- Once installed, close and reopen your terminal and try `python --version` again

If `python` doesn't work, try:

```bash
python3 --version
```

On Mac and Linux, `python3` is the correct command.

---

### Step 2 — Check if pip is installed

```bash
pip --version
```

If you see a version number, pip is installed. If not:

```bash
python -m ensurepip --upgrade
```

---

### Step 3 — Install matplotlib

```bash
pip install matplotlib
```

If that doesn't work, try:

```bash
pip3 install matplotlib
```

Or:

```bash
python -m pip install matplotlib
```

---

## How to Run

```bash
python dijkstra.py
python a_star.py
```

If `python` doesn't work, try:

```bash
python3 dijkstra.py
python3 a_star.py
```

---

## Files

| File | What it does | Edit? |
|------|--------------|-------|
| `maps.py` | Grid maps + converts them to nodes and edges | No |
| `visualize.py` | Draws the path on the grid | No |
| `dijkstra.py` | Dijkstra's algorithm | Yes (Dijkstra teams) |
| `a_star.py` | A* algorithm | Yes (A* teams) |

---

## What You Have Inside the Function

When you call `build_nodes_and_edges(grid)` you get back:

```python
nodes, edges, startNode, endNode, num_nodes, num_edges = build_nodes_and_edges(grid)
```

### nodes[i] — each node has 7 fields

| Index | Constant | What it is |
|-------|----------|------------|
| 0 | NAME | node number as a string |
| 1 | DISTANCE | shortest distance found so far (starts at 9999) |
| 2 | VISITED | True/False — has this node been processed |
| 3 | PREVIOUS | index of the node we came from |
| 4 | ROW | row position in the grid |
| 5 | COL | column position in the grid |
| 6 | FSCORE | f = g + h (A* only, starts at 9999) |

### edges[k] — each edge has 4 fields

| Index | Constant | What it is |
|-------|----------|------------|
| 0 | EDGE_NAME | edge name |
| 1 | EDGE_SRC | source node index |
| 2 | EDGE_DEST | destination node index |
| 3 | EDGE_W | weight (always 1 — one step) |

### Other variables

| Variable | What it is |
|----------|------------|
| startNode | index of the S node |
| endNode | index of the E node |
| num_nodes | total number of walkable nodes |
| num_edges | total number of edges |

---

## The Maps

| Level | Size | Difficulty |
|-------|------|------------|
| 1 | 5x5 | Easy — no walls |
| 2 | 10x10 | Medium — some walls |
| 3 | 10x10 | Hard — maze |

---

## Algorithm Steps

### Dijkstra

```
1. Set start node distance to 0

2. REPEAT:
   a. Find unvisited node with lowest distance — this is current_node
   b. If current_node is endNode — stop, destination reached
   c. If current_node is -1 — stop, no path exists
   d. Mark current_node as visited
   e. For each edge leaving current_node:
      — newDistance = current distance + edge weight
      — if neighbour unvisited AND newDistance is better:
            update neighbour distance
            update neighbour previousNode

3. Traceback from endNode using previousNode
```

### A*

```
1. Set start node distance to 0
   Set start node fScore to heuristic(start, end)

2. REPEAT:
   a. Find unvisited node with lowest fScore — this is current_node
   b. If current_node is endNode — stop, destination reached
   c. If current_node is -1 — stop, no path exists
   d. Mark current_node as visited
   e. For each edge leaving current_node:
      — newG = current distance + edge weight
      — newF = newG + heuristic(neighbour, end)
      — if neighbour unvisited AND newF is better:
            update neighbour distance to newG
            update neighbour fScore to newF
            update neighbour previousNode

3. Traceback from endNode using previousNode
```

### The only difference between Dijkstra and A*

| | Dijkstra | A* |
|--|---------|-----|
| Pick next node by | lowest distance | lowest fScore |
| Update condition | newDistance < distance | newF < fScore |
| Extra calculation | none | newF = newG + heuristic |

---

## Final Challenge

After everyone finishes, we race both algorithms on Level 3.

Which explores fewer nodes — Dijkstra or A*?
```
