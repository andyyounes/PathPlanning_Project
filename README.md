# Pathfinding Project

## Overview
Implement a pathfinding algorithm to find the shortest path through a maze!

**We give you:**
- The grid maps (3 levels)
- The data structures (nodes and edges built automatically from the grid)
- The visualisation (plot_path draws the result for you)

**You implement:**
- The actual algorithm logic inside `dijkstra()` or `astar()`

## Setup

### Step 1: Check if Python is installed

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

### Step 2: Check if pip is installed

```bash
pip --version
```

If you see a version number, pip is installed. If not:

```bash
python -m ensurepip --upgrade
```

---

### Step 3: Install matplotlib

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
## Getting the Latest Updates

If your teacher pushes an update to the project, here is how to get it on your laptop.

### If you are using Git

Check if Git is installed:

```bash
git --version
```

If not installed:
- Go to https://git-scm.com/downloads
- Download and install for your operating system
- Close and reopen your terminal and try `git --version` again

Pull the latest updates:

```bash
git pull
```

If that doesn't work, make sure you are in the right folder first:

```bash
cd path/to/your/project/folder
git pull
```
### If you are using Git

Each student works on their own branch. Do this **once** at the start of the project to create your branch:
```
     git checkout -b your-branch-name
```
To get the latest updates from your teacher:
```
    git checkout main
    git pull
    git checkout your-branch-name
    git merge main
```
### If you are NOT using Git

Your teacher will share the updated files. You have two options:

**Option 1 — Download the zip**
- Download the zip file your teacher shares
- Extract it
- Copy the updated files into your project folder
- Do NOT overwrite `dijkstra.py` or `a_star.py` if you have already written code in them

**Option 2 — Copy the file manually**
- Your teacher will tell you which file changed
- Open the new file and copy its contents
- Paste it into your version of that file

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
| `a_n_d.py` | Practice file - simple path (A to E) | Yes (everyone) |
---
## Start Here : a_n_d.py
Before touching the grid levels, open `a_n_d.py` first.
It has a simple graph with 5 named nodes (A, B, C, D, E) and 6 edges — the same one you studied in class:

```
    2       4
A ----- B ----- E
 \      |       |
  3     5       1
   \    |       |
    C -----10-- D
```

The nodes and edges are already set up for you as 2D arrays — exactly like you learned. Your job is to implement Dijkstra or A* inside the procedure at the bottom.

This is your warm up. Once it works on the named graph, the grid version in `dijkstra.py` or `a_star.py` uses the exact same algorithm the only difference is the map is bigger and built automatically.

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
| 1 | 5x5 | Easy: no walls |
| 2 | 10x10 | Medium: some walls |
| 3 | 10x10 | Hard: maze |

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
Which explores fewer nodes — Dijkstra or A*?
```
