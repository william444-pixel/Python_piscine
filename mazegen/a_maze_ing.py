import os
import random
import sys
from collections import deque
from typing import List, Tuple, Optional, Dict, Set

class cell_content:
    def __init__(self, value: int, visited: bool, static: bool) -> None:
        """Initializes a maze cell with its properties."""
        self.value: int = value
        self.visited: bool = visited
        self.static: bool = static
        self.path: bool = False
        self.arrow: Optional[str] = None


class MazeGenerator:
    def __init__(self, height: int, width: int, entry_x: int, entry_y: int, 
                 exit_x: int, exit_y: int, output_file: str, perfect: bool, seed: Optional[int]) -> None:
        """Initializes the MazeGenerator with dimensions, constraints and output settings."""
        self.height: int = height
        self.width: int = width
        self.entry: Tuple[int, int] = (entry_x, entry_y)
        self.exit: Tuple[int, int] = (exit_x, exit_y)
        self.arr: Optional[List[List[cell_content]]] = None
        self.outputfile: str = output_file
        self.perfect: bool = perfect
        self.seed: Optional[int] = seed

    # ================= DFS =================

    def my_maze(self) -> None:
        """Generates the maze using Randomized DFS and saves the initial structure to a file."""
        top: int = (self.height - 5) // 2
        right: int = (self.width - 7) // 2

        arr: List[List[cell_content]] = [[cell_content(0b1111, False, False)
                                          for _ in range(self.width)]
                                         for _ in range(self.height)]

        if self.height < 5 or self.width < 7:
            print("\033[33mWarning: Maze size too small to display '42' pattern.\033[0m")
            sys.exit(1)
            
        # ===== STATIC BLOCK =====
        static_coords: List[Tuple[int, int]] = [
                (top, right), (top, right+4), (top, right+5), (top, right+6),
                (top+1, right), (top+1, right+6),
                (top+2, right), (top+2, right+1), (top+2, right+2), (top+2, right+4), (top+2, right+5), (top+2, right+6),
                (top+3, right+2), (top+3, right+4),
                (top+4, right+2), (top+4, right+4), (top+4, right+5), (top+4, right+6)
            ]
        for r, c in static_coords:
            if (r, c) != self.entry and (r, c) != self.exit:
                arr[r][c].static = True
            else:
                print("Error: ENTRY or exit is inside 42 bounds")
                sys.exit(1)

        if self.seed is not None:
            random.seed(self.seed)

        def dfs(i: int, j: int) -> None:
            """Recursive Depth-First Search to carve the maze paths."""
            if arr[i][j].static or arr[i][j].visited:
                return

            arr[i][j].visited = True
            directions: List[int] = [0b1110, 0b1101, 0b1011, 0b0111]
            random.shuffle(directions)

            for direx in directions:
                ni, nj = i, j
                if direx == 0b1110:   # up
                    ni -= 1
                elif direx == 0b1101:  # right
                    nj += 1
                elif direx == 0b1011:  # down
                    ni += 1
                elif direx == 0b0111:  # left
                    nj -= 1

                if (0 <= ni < self.height and
                    0 <= nj < self.width and
                    not arr[ni][nj].visited and
                    not arr[ni][nj].static):

                    arr[i][j].value &= direx
                    if direx == 0b1110:
                        arr[ni][nj].value &= 0b1011
                    elif direx == 0b1101:
                        arr[ni][nj].value &= 0b0111
                    elif direx == 0b1011:
                        arr[ni][nj].value &= 0b1110
                    elif direx == 0b0111:
                        arr[ni][nj].value &= 0b1101
                    dfs(ni, nj)

        dfs(0, 0)
        self.arr = arr
        
        if not self.perfect:
            self.perfect_false()

        my_text: str = ""
        for i in arr:
            for j in i:
                my_text += str(format(j.value, 'X'))
            my_text += "\n"
        
        with open(self.outputfile, "w") as file:
            file.write(my_text)

        x, y = self.entry
        x_2, y_2 = self.exit
        text_1: str = f"{x},{y}"
        text_2: str = f"{x_2},{y_2}"
        with open(self.outputfile, "a") as same_f:
            same_f.write(f"\n{text_1}\n{text_2}")

    # ================== False case =====================
    def perfect_false(self) -> None:
        """Breaks random walls to create a Braid maze if PERFECT is set to False."""
        if self.arr is None: return
        top: int = ((self.height - 5) // 2) - 1
        right: int = ((self.width - 7) // 2) - 1
        down: int = top + 6
        left: int = right + 7
        for i, row in enumerate(self.arr):
            for x, cell in enumerate(row):
                if cell.value == 0b0101 and not cell.static and (0 < i < top or down < i < self.height - 1) and (0 < x <= right or left <= x < self.width - 2):
                    cell.value = 0b0000
                    self.arr[i + 1][x].value &= 0b1110
                    self.arr[i - 1][x].value &= 0b1011
                if cell.value == 0b1010 and not cell.static and (0 < i < top or down < i < self.height - 1) and (0 < x <= right or left <= x < self.width - 2):
                    cell.value = 0b0000
                    self.arr[i][x-1].value &= 0b1101
                    self.arr[i][x+1].value &= 0b0111

    # ================= BFS =================
    def resolve_bfs(self) -> None:
        """Finds the shortest path from entry to exit using Breadth-First Search."""
        if self.arr is None: return
        queue: deque = deque([self.entry])
        visited: Set[Tuple[int, int]] = {self.entry}
        parent: Dict[Tuple[int, int], Tuple[int, int]] = {}

        arr = self.arr
        found: bool = False
        while queue:
            x, y = queue.popleft()
            if (x, y) == self.exit:
                found = True
                break
            cell = arr[x][y]
            directions: List[Tuple[int, int, int]] = [
                (-1, 0, 0b0001),  # Up
                (0, 1, 0b0010),   # Right
                (1, 0, 0b0100),   # Down
                (0, -1, 0b1000)   # Left
            ]
            for dx, dy, wall_bit in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.height and
                    0 <= ny < self.width and
                    not arr[nx][ny].static and
                    (nx, ny) not in visited and
                    not (cell.value & wall_bit)):
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

        node: Tuple[int, int] = self.exit
        if not found or node not in parent:
            print("No path found")
            return

        path: str = ""
        while node != self.entry:
            x, y = node
            px, py = parent[node]
            if x == px - 1:
                arr[x][y].arrow = "\033[31m▲\033[0m"; path += "N"
            elif x == px + 1:
                arr[x][y].arrow = "\033[31m▼\033[0m"; path += "S"
            elif y == py - 1:
                arr[x][y].arrow = "\033[31m◀\033[0m"; path += "W"
            elif y == py + 1:
                arr[x][y].arrow = "\033[31m▶\033[0m"; path += "E"
            arr[x][y].path = True
            node = (px, py)

        with open(self.outputfile, "a") as path_t:
            path_t.write(f"\n{path[::-1]}")

    def display(self, wall_color: str = "\033[32m", show_path: bool = True) -> None:
        """Renders the maze to the terminal with ANSI colors."""
        if self.arr is None: return
        arr = self.arr
        ex, ey = self.entry
        xx, xy = self.exit
        reset_color: str = "\033[0m"
        
        print(wall_color + "█" + reset_color + (wall_color + "████" + reset_color) * self.width)
        for i in range(self.height):
            line1: str = wall_color + "█" + reset_color
            line2: str = wall_color + "█" + reset_color
            for j in range(self.width):
                cell = arr[i][j]
                if cell.static: line1 += "\033[34m###\033[0m"
                elif (i == ex and j == ey): line1 += "⭐ "
                elif (i == xx and j == xy): line1 += "🏆 "
                elif show_path and cell.path and cell.arrow: line1 += f" {cell.arrow} "
                else: line1 += "   "
                
                line1 += wall_color + "█" + reset_color if cell.value & 0b0010 else " "
                line2 += wall_color + "████" + reset_color if cell.value & 0b0100 else wall_color + "   █" + reset_color
            print(line1)
            print(line2)

def interactive_menu(maze_instance: MazeGenerator) -> None:
    """Provides an interactive terminal interface to manage the maze."""
    current_color: str = "\033[32m"
    show_path: bool = True

    while True:
        print("\n" * 2) 
        maze_instance.display(wall_color=current_color, show_path=show_path)
        print("\n--- Interaction Menu ---")
        print("[R] Re-generate | [T] Toggle Path | [C] Change Color | [Q] Quit")
        try:
            choice: str = input("\nEnter choice: ").strip().upper()
        except EOFError: break

        if choice == 'Q': break
        elif choice == 'R':
            maze_instance.my_maze()
            maze_instance.resolve_bfs()
        elif choice == 'T':
            show_path = not show_path
        elif choice == 'C':
            colors: Dict[str, str] = {'1': "\033[31m", '2': "\033[32m", '3': "\033[33m", '4': "\033[34m", '5': "\033[35m", '6': "\033[36m"}
            print("1:Red, 2:Green, 3:Yellow, 4:Blue, 5:Purple, 6:Cyan")
            c_idx = input("Color #: ").strip()
            if c_idx in colors: current_color = colors[c_idx]

def main() -> None:
    """Main entry point for parsing config and running the generator."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt"); sys.exit(1)
    
    file_path: str = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found."); sys.exit(1)

    settings: Dict[str, str] = {}
    try:
        with open(file_path, "r") as param:
            for line in param:
                line = line.strip()
                if not line or line.startswith('#'): continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    settings[key.upper().strip()] = value.strip()
    except Exception as e:
        print(e); sys.exit(1)

    required: List[str] = ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT']
    for key in required:
        if key not in settings:
            print(f"Error: Missing mandatory key '{key}' in config."); sys.exit(1)

    try:
        width: int = int(settings['WIDTH'])
        height: int = int(settings['HEIGHT'])
        entry_x, entry_y = map(int, settings['ENTRY'].split(','))
        exit_x, exit_y = map(int, settings['EXIT'].split(','))
        output_file: str = settings['OUTPUT_FILE']
        perfect: bool = settings['PERFECT'].lower() == 'true'
        seed: Optional[int] = int(settings['SEED']) if 'SEED' in settings else None
        
        if width <= 0 or height <= 0 or not (0 <= entry_x < height and 0 <= entry_y < width) or not (0 <= exit_x < height and 0 <= exit_y < width):
            print("Error: Invalid dimensions or bounds."); sys.exit(1)
            
        p = MazeGenerator(height, width, entry_x, entry_y, exit_x, exit_y, output_file, perfect, seed)
        p.my_maze()
        p.resolve_bfs()
        interactive_menu(p)
    except Exception as e:
        print(f"Error parsing: {e}"); sys.exit(1)

if __name__ == "__main__":
    main()