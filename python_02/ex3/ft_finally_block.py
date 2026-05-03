def water_plants(plant_list):
    """print && except Errors
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """test cases
    """
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    plant = ["tomato", "lettuce", "carrots"]
    water_plants(plant)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    plant = ["tomato", None]
    water_plants(plant)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
