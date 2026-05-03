def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    check plant health && raising errors
    """
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if 1 > water_level:
        raise ValueError(f"Error: Water level {water_level}"
                         "is too low (min 1)")
    if 10 < water_level:
        raise ValueError(f"Error: Water level {water_level}"
                         "is too high (max 10)")
    if 2 > sunlight_hours:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    if 12 < sunlight_hours:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         "is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """tester"""
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 4, 6))
    except ValueError as e:
        print(f"{e}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 4, 6)
    except ValueError as e:
        print(f"{e}")
    print("\nTesting bad water levele...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(f"{e}")
    print("\ntesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 4, 0)
    except ValueError as e:
        print(f"{e}")
    print("\nAll error raising tests completed!")


test_plant_checks()
