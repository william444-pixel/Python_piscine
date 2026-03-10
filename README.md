*This project has been created as part of the 42 curriculum by nsel-oua, snaomo.*

## Description
This project is a comprehensive Maze Generator and Solver developed in Python. It allows users to generate complex mazes based on custom configurations, visualize them in the terminal with an interactive menu, and find the shortest path between an entry and an exit point using professional pathfinding algorithms.

## Instructions
### Installation
1. Navigate to the project root directory.
2. Build the package:
   ```bash
   python3 -m build
Install the generated package:

Bash
pip install dist/mazegen-0.1.0.tar.gz
Execution
Run the main script using a configuration file:

Bash
python3 a_maze_ing.py config.txt
Or use the installed package command:

Bash
mazegen config.txt
Resources
External References:

Wikipedia: Maze generation algorithms (Recursive Backtracker).

Python Documentation: collections.deque for optimized BFS pathfinding.

AI Usage: AI was used as a collaborative tool for:

Structuring the pyproject.toml and ensuring PEP 517 compliance.

Optimizing bitwise operations for the wall-logic and HEX representation.

Debugging terminal-specific ANSI escape codes for the interactive UI.

Configuration File Description
The configuration file follows a KEY=VALUE format. Comments start with #.

WIDTH: Integer, number of cells horizontally.

HEIGHT: Integer, number of cells vertically.

ENTRY: Coordinates of the starting point in row,col format (e.g., 0,0).

EXIT: Coordinates of the end point (e.g., 19,19).

OUTPUT_FILE: Path where the generated maze and solution will be saved.

PERFECT: True for a maze with no loops, False for a Braid maze.

SEED: (Optional) Integer to replicate the exact same maze generation.

Maze Algorithm
Algorithm: Randomized Depth-First Search (Recursive Backtracker).

Reason for Choice: We chose DFS because it generates "Perfect" mazes with a single path between any two cells. It creates long, winding corridors and deep dead ends, which are more challenging to solve and visually more complex than other algorithms. It also guarantees 100% reachability for all non-static cells.

Maze Generator Reusable Module
The mazegen module provides a robust MazeGenerator class. It encapsulates:

my_maze(): Core generation logic including the '42' pattern integration.

resolve_bfs(): Shortest path calculation using Breadth-First Search.

display(): Dynamic terminal rendering with color and path toggling.
The module is designed to be fully reusable and can be imported into other projects as a standard Python library.

Team and Project Management
Roles:

<snaimi>: Logic Lead (DFS/BFS Algorithms, bitwise wall logic, and 42 pattern integration).

<nael-oua>: System Architect (Packaging, config parsing, error management, and interactive UI).

Planning & Evolution: Initially, we planned a basic script, but we evolved the project into a modular package. Our planning shifted to prioritize the bitwise representation to ensure the HEX output exactly matches the subject's requirements.

Self-Evaluation:

What worked well: The bitwise manipulation made the wall-logic extremely efficient.

Improvements: Implementation of a Graphical User Interface (GUI) and more generation algorithms (like Kruskal's).

Tools: flake8 for linting, mypy for static typing, and setuptools for the packaging workflow