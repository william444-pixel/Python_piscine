class GardenError(Exception):
    """gardenerror from Exception error
    """
    pass


class PlantError(GardenError):
    """PlantError from GardenError error
    """
    pass


class WaterError(GardenError):
    """WaterError from GardenError error
    """
    pass


def check_plant():
    """Plant error raising
    """
    raise PlantError("The tomato plant is wilting!")


def check_water():
    """Water error raising
    """
    raise WaterError("Not enough water in the tank!")


def main():
    """test cases
    """
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print("Caught PlantError:", e)
    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print("Caught WaterError:", e)
    print("\nTesting catching all garden errors")
    try:
        check_plant()
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        check_water()
    except GardenError as e:
        print("Caught a garden error:", e)
    print("\nAll custom error types work correctly!")


main()
