'''
Functions to display grids and paths using matplotlib.
'''
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def print_grid(grid, title="Grid"):
    """Display the grid using matplotlib."""
    rows = len(grid)
    cols = len(grid[0])
    
    fig, ax = plt.subplots(figsize=(cols, rows))
    
    # Create color grid
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            
            if cell == 'S':
                color = '#4CAF50'  # Green - Start
            elif cell == 'E':
                color = '#F44336'  # Red - End
            elif cell == 1:
                color = '#424242'  # Dark grey - Wall
            else:
                color = '#FFFFFF'  # White - Open
            
            rect = plt.Rectangle((c, rows - 1 - r), 1, 1, 
                                   facecolor=color, edgecolor='black', linewidth=1)
            ax.add_patch(rect)
            
            # Add S and E labels
            if cell == 'S' or cell == 'E':
                ax.text(c + 0.5, rows - 1 - r + 0.5, cell, 
                       ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    # Add grid coordinates
    ax.set_xticks(np.arange(0.5, cols, 1))
    ax.set_yticks(np.arange(0.5, rows, 1))
    ax.set_xticklabels(range(cols))
    ax.set_yticklabels(range(rows - 1, -1, -1))
    
    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#4CAF50', edgecolor='black', label='Start (S)'),
        mpatches.Patch(facecolor='#F44336', edgecolor='black', label='End (E)'),
        mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='Open'),
        mpatches.Patch(facecolor='#424242', edgecolor='black', label='Wall'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.show()


def print_grid_with_path(grid, path, title="Solution"):
    """Display the grid with the path marked."""
    rows = len(grid)
    cols = len(grid[0])
    
    fig, ax = plt.subplots(figsize=(cols, rows))
    
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            
            if cell == 'S':
                color = '#4CAF50'  # Green - Start
            elif cell == 'E':
                color = '#F44336'  # Red - End
            elif (r, c) in path:
                color = '#2196F3'  # Blue - Path
            elif cell == 1:
                color = '#424242'  # Dark grey - Wall
            else:
                color = '#FFFFFF'  # White - Open
            
            rect = plt.Rectangle((c, rows - 1 - r), 1, 1,
                                   facecolor=color, edgecolor='black', linewidth=1)
            ax.add_patch(rect)
            
            if cell == 'S' or cell == 'E':
                ax.text(c + 0.5, rows - 1 - r + 0.5, cell,
                       ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.set_title(f"{title}\nPath length: {len(path)} steps", fontsize=14, fontweight='bold')
    
    ax.set_xticks(np.arange(0.5, cols, 1))
    ax.set_yticks(np.arange(0.5, rows, 1))
    ax.set_xticklabels(range(cols))
    ax.set_yticklabels(range(rows - 1, -1, -1))
    
    legend_elements = [
        mpatches.Patch(facecolor='#4CAF50', edgecolor='black', label='Start (S)'),
        mpatches.Patch(facecolor='#F44336', edgecolor='black', label='End (E)'),
        mpatches.Patch(facecolor='#2196F3', edgecolor='black', label='Path'),
        mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='Open'),
        mpatches.Patch(facecolor='#424242', edgecolor='black', label='Wall'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.show()


def print_grid_with_explored(grid, path, explored, title="Algorithm Visualization"):
    """Display the grid showing both the path and explored nodes."""
    rows = len(grid)
    cols = len(grid[0])
    
    fig, ax = plt.subplots(figsize=(cols, rows))
    
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            
            if cell == 'S':
                color = '#4CAF50'  # Green - Start
            elif cell == 'E':
                color = '#F44336'  # Red - End
            elif (r, c) in path:
                color = '#2196F3'  # Blue - Path
            elif (r, c) in explored:
                color = '#FFEB3B'  # Yellow - Explored
            elif cell == 1:
                color = '#424242'  # Dark grey - Wall
            else:
                color = '#FFFFFF'  # White - Open
            
            rect = plt.Rectangle((c, rows - 1 - r), 1, 1,
                                   facecolor=color, edgecolor='black', linewidth=1)
            ax.add_patch(rect)
            
            if cell == 'S' or cell == 'E':
                ax.text(c + 0.5, rows - 1 - r + 0.5, cell,
                       ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.set_title(f"{title}\nPath: {len(path)} steps | Explored: {len(explored)} nodes", 
                 fontsize=14, fontweight='bold')
    
    ax.set_xticks(np.arange(0.5, cols, 1))
    ax.set_yticks(np.arange(0.5, rows, 1))
    ax.set_xticklabels(range(cols))
    ax.set_yticklabels(range(rows - 1, -1, -1))
    
    legend_elements = [
        mpatches.Patch(facecolor='#4CAF50', edgecolor='black', label='Start (S)'),
        mpatches.Patch(facecolor='#F44336', edgecolor='black', label='End (E)'),
        mpatches.Patch(facecolor='#2196F3', edgecolor='black', label='Path'),
        mpatches.Patch(facecolor='#FFEB3B', edgecolor='black', label='Explored'),
        mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='Open'),
        mpatches.Patch(facecolor='#424242', edgecolor='black', label='Wall'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.show()


def plot_path(grid, nodes, path, visited=None, title="Result"):
    rows = len(grid)
    cols = len(grid[0])

    # build lookup: node_number -> (row, col)
    node_pos = {}
    counter = 1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                node_pos[counter] = (r, c)
                counter += 1

    # convert path and visited from node numbers to (row, col)
    path_cells    = set(node_pos[n] for n in path    if n in node_pos)
    visited_cells = set(node_pos[n] for n in visited if n in node_pos) if visited else set()

    fig, ax = plt.subplots(figsize=(cols * 0.8, rows * 0.8))

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]

            if cell == 'S':
                color = '#4CAF50'
            elif cell == 'E':
                color = '#F44336'
            elif cell == 1:
                color = '#424242'
            elif (r, c) in path_cells:
                color = '#2196F3'
            elif (r, c) in visited_cells:
                color = '#FFEB3B'
            else:
                color = '#FFFFFF'

            rect = plt.Rectangle(
                (c, rows - 1 - r), 1, 1,
                facecolor=color, edgecolor='black', linewidth=0.5
            )
            ax.add_patch(rect)

            if cell == 'S' or cell == 'E':
                ax.text(
                    c + 0.5, rows - 1 - r + 0.5, cell,
                    ha='center', va='center',
                    fontsize=12, fontweight='bold', color='white'
                )

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.set_title(
        f"{title}  |  Path: {len(path)} steps  |  Explored: {len(visited_cells)} nodes",
        fontsize=12, fontweight='bold'
    )

    ax.set_xticks([c + 0.5 for c in range(cols)])
    ax.set_yticks([r + 0.5 for r in range(rows)])
    ax.set_xticklabels(range(cols))
    ax.set_yticklabels(range(rows - 1, -1, -1))

    legend = [
        mpatches.Patch(facecolor='#4CAF50', edgecolor='black', label='Start'),
        mpatches.Patch(facecolor='#F44336', edgecolor='black', label='End'),
        mpatches.Patch(facecolor='#2196F3', edgecolor='black', label='Path'),
        mpatches.Patch(facecolor='#FFEB3B', edgecolor='black', label='Explored'),
        mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='Open'),
        mpatches.Patch(facecolor='#424242', edgecolor='black', label='Wall'),
    ]
    ax.legend(handles=legend, loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()
