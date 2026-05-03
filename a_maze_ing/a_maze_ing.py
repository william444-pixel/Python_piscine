import os
import sys
from mazegen import MazeGenerator, interactive_menu


def main() -> None:
    """Main entry point for parsing config and running the generator."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    file_path: str = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found.")
        sys.exit(1)

    settings: dict[str, str] = {}
    try:
        with open(file_path, "r") as param:
            for line in param:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    settings[key.upper().strip()] = value.strip()
    except Exception as e:
        print(e)
        sys.exit(1)

    required: list[str] = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT",
    ]
    for key in required:
        if key not in settings:
            print(f"Error: Missing mandatory key '{key}' in config.")
            sys.exit(1)

    try:
        width: int = int(settings["WIDTH"])
        height: int = int(settings["HEIGHT"])
        entry_x, entry_y = map(int, settings["ENTRY"].split(","))
        exit_x, exit_y = map(int, settings["EXIT"].split(","))
        output_file: str = settings["OUTPUT_FILE"]
        perfect: bool = settings["PERFECT"].lower() == "true"
        seed: int | None = int(
            settings["SEED"]) if "SEED" in settings else None

        if (
            width <= 0
            or height <= 0
            or not (0 <= entry_x < height and 0 <= entry_y < width)
            or not (0 <= exit_x < height and 0 <= exit_y < width)
        ):
            print("Error: Invalid dimensions or bounds.")
            sys.exit(1)

        p = MazeGenerator(
            height,
            width,
            entry_x,
            entry_y,
            exit_x,
            exit_y,
            output_file,
            perfect,
            seed,
        )
        p.my_maze()
        p.resolve_bfs()
        interactive_menu(p)
    except Exception as e:
        print(f"Error parsing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
