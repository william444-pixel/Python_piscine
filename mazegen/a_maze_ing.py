import os
import random
import sys
from collections import deque

class cell_content:
    def __init__(self, value, visited, static):
        self.value = value
        self.visited = visited
        self.static = static
        self.path = False
        self.arrow = None


class MazeGenerator:
    def __init__(self, height, width, entry_x, entry_y, exit_x, exit_y, output_file, perfect, seed):
        self.height = height
        self.width = width
        self.entry = (entry_x, entry_y)
        self.exit = (exit_x, exit_y)
        self.arr = None
        self.outputfile = output_file
        self.perfect = perfect
        self.seed = seed
    # ================= DFS =================

    def my_maze(self):

        top = (self.height - 5) // 2
        right = (self.width - 7) // 2

        arr = [[cell_content(0b1111, False, False)
                for _ in range(self.width)]
               for _ in range(self.height)]

        if self.height < 5 or self.width < 7:
            print("\033[33mWarning: Maze size too small to display '42' pattern.\033[0m")
            sys.exit(1)
        # ===== STATIC BLOCK =====
        static_coords = [
                (top, right), (top, right+4), (top, right+5), (top, right+6),
                (top+1, right), (top+1, right+6),
                (top+2, right), (top+2, right+1), (top+2, right+2), (top+2, right+4), (top+2, right+5), (top+2, right+6),
                (top+3, right+2), (top+3, right+4),
                (top+4, right+2), (top+4, right+4), (top+4, right+5), (top+4, right+6)
            ]
        for r, c in static_coords:
                # Safety: Only mark static if it's NOT the entry or exit
            if (r, c) != self.entry and (r, c) != self.exit:
                arr[r][c].static = True
            else:
                print("Error: ENTRY or exit is inside 42 bounds")
                sys.exit(1)
        if self.seed is not None:
            random.seed(self.seed)
        def dfs(i, j):
            
            if arr[i][j].static or arr[i][j].visited:
                return

            arr[i][j].visited = True

            directions = [0b1110, 0b1101, 0b1011, 0b0111]
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
        # file W
        if not self.perfect:
            self.perfect_false()
        my_text = ""
        for i in arr:
            for j in i:
                if (j.static == True):
                    my_text += "".join(str(format(j.value, 'X')))
                else:
                    my_text += "".join(str(format(j.value, 'X')))
            my_text += "\n"
        file = open(self.outputfile, "w")
        file.write(my_text)
        file.close()

        same_f = open(self.outputfile, "a")
        x, y = self.entry
        x_2, y_2 = self.exit
        text_1 = f"{x},{y}"
        text_2 = f"{x_2},{y_2}"
        same_f.write(f"\n{text_1}\n{text_2}")
        same_f.close()
    # ================== False case =====================
    def perfect_false(self):
        top = ((self.height - 5) // 2) - 1
        right = ((self.width - 7) // 2) - 1
        down = top + 6
        left = right + 7
        for i, row in enumerate(self.arr):
                x = -1
                for cell in row:
                    x += 1
                    if cell.value == 0b0101 and not cell.static and (0 < i < top or down < i < self.height - 1) and (0 < x <= right or left <= x < self.width - 2):
                        cell.value = 0b0000
                        self.arr[i + 1][x].value &= 0b1110
                        self.arr[i - 1][x].value &= 0b1011
                    if cell.value == 0b1010 and not cell.static and (0 < i < top or down < i < self.height - 1) and (0 < x <= right or left <= x < self.width - 2):
                        cell.value = 0b0000
                        self.arr[i][x-1].value &= 0b1101
                        self.arr[i][x+1].value &= 0b0111
    # ================= BFS =================
    def resolve_bfs(self):

        queue = deque([self.entry])
        visited = set([self.entry])
        parent = {}

        arr = self.arr

        while queue:
            x, y = queue.popleft()

            if (x, y) == self.exit:
                break

            cell = arr[x][y]

            directions = [
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

        # ===== Reconstruct the Path =====
        node = self.exit

        if node not in parent:
            print("No path found")
            return
        path = ""
        while node != self.entry:
            x, y = node
            px, py = parent[node]

            if x == px - 1:
                arr[x][y].arrow = "\033[31m▲\033[0m"
                path += "N"
            elif x == px + 1:
                arr[x][y].arrow = "\033[31m▼\033[0m"
                path += "S"
            elif y == py - 1:
                arr[x][y].arrow = "\033[31m◀\033[0m"
                path += "W"
            elif y == py + 1:
                arr[x][y].arrow = "\033[31m▶\033[0m"
                path += "E"

            arr[x][y].path = True
            node = (px, py)

        path_t = open(self.outputfile, "a")
        path_l = path[::-1]
        path_t.write(f"\n{path_l}")
        path_t.close()

# ===== TERMINAL DRAW FUNCTION =====
    def display(self, wall_color: str = "\033[32m", show_path: bool = True) -> None:
        arr = self.arr
        x, y = self.entry
        x_1, y_1 = self.exit
        
        reset_color = "\033[0m"
        
        # Top border
        print(wall_color + "█" + reset_color + (wall_color + "████" + reset_color) * self.width)

        for i in range(self.height):
            # Vertical walls
            line1 = wall_color + "█" + reset_color
            # Bottom walls
            line2 = wall_color + "█" + reset_color

            for j in range(self.width):
                cell = arr[i][j]

                # Cell body
                if cell.static:
                    line1 += "\033[34m###\033[0m"
                elif (i == x and j == y):
                    line1 += "⭐ "
                elif (i == x_1 and j == y_1):
                    line1 += "🏆 "
                elif show_path and cell.path and cell.arrow: # زدنا show_path هنا
                    line1 += f" {cell.arrow} "
                else:
                    line1 += "   "

                # Right wall
                if cell.value & 0b0010:
                    line1 += wall_color + "█" + reset_color
                else:
                    line1 += " "

                # Bottom wall
                if cell.value & 0b0100:
                    line2 += wall_color + "████" + reset_color
                else:
                    line2 += wall_color + "   █" + reset_color

            print(line1)
            print(line2)
        
def interactive_menu(maze_instance) -> None:
    """
    Provides an interactive terminal interface to manage the maze.
    
    Allows the user to re-generate the maze, toggle the solution path, 
    change wall colors, or exit the program.
    
    Args:
        maze_instance (maze): The instance of the Maze class to interact with.
    """
    # ANSI escape codes for colors
    current_color: str = "\033[32m"  # Default: Green
    show_path: bool = True           # State of the shortest path visibility

    while True:
        # 1. Display the maze with current settings
        # Printing newlines to clear the previous view slightly
        print("\n" * 2) 
        maze_instance.display(wall_color=current_color, show_path=show_path)

        # 2. Display available commands to the user
        print("\n--- Interaction Menu ---")
        print("[R] Re-generate : Create a new random maze")
        print("[T] Toggle Path : Show/Hide the shortest path")
        print("[C] Change Color: Update the wall colors")
        print("[Q] Quit        : Exit the program")

        # 3. Handle user input
        try:
            choice: str = input("\nEnter your choice (R/T/C/Q): ").strip().upper()
        except EOFError:
            # Handle Ctrl+D gracefully
            break

        if choice == 'Q':
            print("Exiting program... Goodbye!")
            break
            
        elif choice == 'R':
            print("Generating a new maze...")
            # Re-run generation and solver logic
            maze_instance.my_maze()      
            maze_instance.resolve_bfs()  
            
        elif choice == 'T':
            # Flip the boolean state of show_path
            show_path = not show_path
            status = "Visible" if show_path else "Hidden"
            print(f"Path visibility set to: {status}")
            
        elif choice == 'C':
            print("\nAvailable Colors:")
            print("[1] Red    [2] Green  [3] Yellow")
            print("[4] Blue   [5] Purple [6] Cyan")
            
            color_choice: str = input("Select a color number: ").strip()
            
            # Map numbers to ANSI color codes
            colors = {
                '1': "\033[31m", # Red
                '2': "\033[32m", # Green
                '3': "\033[33m", # Yellow
                '4': "\033[34m", # Blue
                '5': "\033[35m", # Magenta
                '6': "\033[36m"  # Cyan
            }
            # Fallback to current color if input is invalid
            if color_choice in colors:
                current_color = colors[color_choice]
            else:
                print("Invalid selection. Keeping current color.")
            
        else:
            print("Error: Invalid command. Please use R, T, C, or Q.")
            input("Press Enter to continue...")

# ===== RUN =====
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)
    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"Error: '{file}' not found.")
        sys.exit(1)

    settings = {}
    try:
        with open(file, "r") as param:
            for line in param:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    settings[key.upper().strip()] = value.strip()
    except Exception as e:
        print(e)
    try:
        width = int(settings['WIDTH'])
        height = int(settings['HEIGHT'])
        entry_x, entry_y = map(int, settings['ENTRY'].split(','))
        exit_x, exit_y = map(int, settings['EXIT'].split(','))
        output_file = settings['OUTPUT_FILE']
        perfect = settings['PERFECT'].lower() == 'true'
        seed = int(settings['SEED']) if 'SEED' in settings else None
        if width <= 0 or height <= 0:
            print("Error: WIDTH and HEIGHT must be positive integers.")
            sys.exit(1)
        if not (0 <= entry_x < height and 0 <= entry_y < width):
            print(f"Error: ENTRY {entry_x, entry_y} is outside maze bounds.")
            sys.exit(1)
        if not (0 <= exit_x < height and 0 <= exit_y < width):
            print(f"Error: EXIT {exit_x, exit_y} is outside maze bounds.")
            sys.exit(1)
    except Exception as e:
        print(f"Error parsing {e}")
        sys.exit(1)

    required = ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT']
    for key in required:
        if key not in settings:
            print(f"Error: Missing mandatory key '{key}' in config.")
            sys.exit(1)
    p = MazeGenerator(height, width, entry_x, entry_y, exit_x, exit_y, output_file, seed, perfect)
    p.my_maze()
    p.resolve_bfs()
    interactive_menu(p)
if __name__ == "__main__":
   main()