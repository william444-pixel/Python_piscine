import math


def coordinate_system():
    my_coordinate = (10, 20, 5)
    base_cordinate = (0, 0, 0)
    x, y, z = my_coordinate
    pos = (math.sqrt(x**2 + y**2 + z**2))
    print("=== Game Coordinate System ===")
    print(f"\nPosition created: {my_coordinate}")
    print(f"Distance between {base_cordinate} and {my_coordinate}: {pos:.2f}")
    arg = "3,4,0"
    row_input = arg.split(",")
    num_list = [int(x) for x in row_input]
    print("\nParsing coordinates: \"3,4,0\"")
    print(f"Parsed position: {tuple(num_list)}")
    x, y, z = num_list
    user_pos = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance between {base_cordinate} and {tuple(num_list)}: "
          f"{user_pos}")
    try:
        arg = "abc,def,ghi"
        row_input = arg.split(",")
        num_list = [int(x) for x in row_input]
        print(f"\nParsing coordinates: {arg}")
        print(f"Parsed position: {tuple(num_list)}")
        x, y, z = num_list
        user_pos = math.sqrt(x**2 + y**2 + z**2)
        print(f"Distance between {base_cordinate} and {num_list}: "
              f"{user_pos:.2f}")
    except Exception as e:
        print(f'\nParsing invalid coordinates: "{arg}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


coordinate_system()
