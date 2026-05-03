*This project has been created as part of the 42 curriculum by nael-oua, snaimi.*

---

# A-Maze-Ing 🏆

## Description

**A-Maze-Ing** is a procedural maze generator and solver built in Python as part of the 42 school curriculum. The program generates randomized mazes directly in the terminal, featuring a hidden "42" pattern embedded at the center of every maze as a tribute to the school.

The generator supports two maze types — **perfect** (no loops, exactly one path between any two cells) and **braid** (loops allowed, no dead ends) — and automatically computes the shortest path from entry to exit using BFS. The maze is rendered with ANSI colors and interactive controls, and the full maze data is persisted to an output file.

---

## Instructions

### Requirements

- Python 3.10 or higher (uses `int | None` union syntax)
- No external dependencies — standard library only

### Installation (as a package)

```bash
pip install .
```

This installs the `mazegen` package using the `pyproject.toml` configuration.

### Running directly

```bash
python3 a_maze_ing.py config.txt
```

### Interactive Menu

Once the maze is displayed, the following commands are available:

| Key | Action |
|-----|--------|
| `R` | Re-generate a new random maze |
| `T` | Toggle shortest path visibility |
| `C` | Change wall color (Red/Green/Yellow/Blue/Purple/Cyan) |
| `Q` | Quit the program |

---

## Configuration File

The program reads its settings from a plain-text config file (e.g. `config.txt`). Each line follows the format `KEY=VALUE`. Lines starting with `#` are treated as comments and ignored. Keys are **case-insensitive**.

| Key | Required | Type | Description |
|-----|----------|------|-------------|
| `WIDTH` | ✅ | Integer | Number of columns in the maze. Must be ≥ 7. |
| `HEIGHT` | ✅ | Integer | Number of rows in the maze. Must be ≥ 5. |
| `ENTRY` | ✅ | `row,col` | Entry cell coordinates (0-indexed). Must be within bounds and outside the "42" pattern. |
| `EXIT` | ✅ | `row,col` | Exit cell coordinates (0-indexed). Same constraints as ENTRY. |
| `OUTPUT_FILE` | ✅ | String | Path to the output file where the maze structure and solution are saved. |
| `PERFECT` | ✅ | Boolean (`True`/`False`) | If `True`, generates a perfect maze (unique path). If `False`, generates a braid maze (loops, no dead ends). |
| `SEED` | ❌ | Integer | Optional random seed for reproducible maze generation. |

**Example `config.txt`:**
```
WIDTH=20
HEIGHT=15
ENTRY=1,1
EXIT=14,19
OUTPUT_FILE=output_maze.txt
PERFECT=True
# SEED=42
```

### Output File Format

The output file contains:
1. A grid of hex digits (one character per cell), where each digit encodes the 4 walls of that cell as bits: `UP=0b0001`, `RIGHT=0b0010`, `DOWN=0b0100`, `LEFT=0b1000`
2. The entry coordinates on a new line (`row,col`)
3. The exit coordinates on the next line
4. The BFS solution path as a string of cardinal directions (`N`, `S`, `E`, `W`)

---

## Maze Algorithm

### Generation — Randomized Depth-First Search (Recursive Backtracker)

The maze is carved using a **Randomized DFS** algorithm, also known as the Recursive Backtracker:

1. Start at cell `(0, 0)`, mark it as visited.
2. Randomly shuffle the four possible directions.
3. For each direction, if the neighbor is unvisited and not a static cell, remove the wall between them and recurse into the neighbor.
4. Backtrack when no unvisited neighbors remain.

**Why this algorithm?**

Randomized DFS was chosen for several reasons:
- It guarantees a **perfect maze** (a spanning tree) by construction — every cell is reachable and there is exactly one path between any two cells, making it ideal for the `PERFECT=True` mode.
- It produces mazes with **long, winding corridors** and a strong aesthetic, which suits terminal display well.
- It is simple to implement **recursively**, keeping the code clean and readable.
- It integrates naturally with the **static cell obstacle** (the "42" pattern): the DFS simply skips static cells, leaving them as impassable blocks without any special-case logic in the carving loop.

When `PERFECT=False`, a post-processing pass (`perfect_false`) converts the maze into a **braid maze** by knocking down walls of fully-enclosed dead-end cells, eliminating dead ends and creating loops.

### Solving — Breadth-First Search (BFS)

The shortest path from entry to exit is found using standard BFS, which guarantees the minimum number of steps. The path is stored as directional arrows on each cell and appended to the output file.

---

## Module Documentation — `mazegen`

The `mazegen` package is designed as a **reusable module** that can be imported independently of the CLI entry point.

### `cell_content`

Represents a single maze cell.

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | `int` | 4-bit wall mask. Bit 0=Up, Bit 1=Right, Bit 2=Down, Bit 3=Left. A set bit means the wall is present. |
| `visited` | `bool` | Whether DFS has visited this cell. |
| `static` | `bool` | If `True`, the cell is part of the "42" pattern and is impassable. |
| `path` | `bool` | Whether this cell is on the BFS solution path. |
| `arrow` | `Optional[str]` | ANSI arrow character indicating path direction. |

### `MazeGenerator`

Main class for generating, solving, and rendering a maze.

```python
from mazegen import MazeGenerator

gen = MazeGenerator(
    height=15,
    width=20,
    entry_x=1, entry_y=1,
    exit_x=14, exit_y=19,
    output_file="output.txt",
    perfect=True,
    seed=42
)
gen.my_maze()       # Generate the maze and write to file
gen.resolve_bfs()   # Solve and append path to file
gen.display()       # Render to terminal
```

| Method | Description |
|--------|-------------|
| `my_maze()` | Runs Randomized DFS to carve the maze, embeds the "42" pattern, and writes the grid to `output_file`. |
| `resolve_bfs()` | Runs BFS from entry to exit, marks the path on cells, and appends the direction string to `output_file`. |
| `display(wall_color, show_path)` | Renders the maze to stdout using ANSI block characters. `wall_color` accepts any ANSI escape code. |

### `interactive_menu(maze_instance)`

Standalone function that wraps a `MazeGenerator` instance in an interactive terminal loop. Accepts R/T/C/Q commands. Can be used with any `MazeGenerator` object.

---

## Resources

### External References

- [Maze generation — Recursive Backtracker (Wikipedia)](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_depth-first_search)
- [Python `collections.deque` documentation](https://docs.python.org/3/library/collections.html#collections.deque)
- [ANSI escape codes reference](https://en.wikipedia.org/wiki/ANSI_escape_code)
- [Python `pyproject.toml` packaging guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

### AI Usage

AI (Claude by Anthropic) was used during this project for the following tasks:

- **README writing**: generating the structure and content of this README based on the source code.
- **Debugging assistance**: helping identify edge cases in the BFS wall-bit masking logic and the static cell boundary checks.
- **Code review**: suggesting type hints and docstring improvements for the `MazeGenerator` class methods.

AI was **not** used to write the core maze generation or solving logic; all algorithmic code was written by the team.

---

## Team & Project Management

### Roles

| Member | Role |
|--------|------|
| **snaimi** | Maze generation algorithm (Randomized DFS), BFS solver, static "42" pattern embedding, output file format |
| **nael-oua** |  terminal display rendering, config file parser, interactive menu, packaging (`pyproject.toml`) |

### Tools Used

- **Python 3.10+** — primary language
- **Git** — version control and collaboration
- **VS Code** — code editor with Python extension
- **Claude (Anthropic)** — AI assistant for debugging, documentation, and algorithm research (see AI Usage above)
