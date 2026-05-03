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


class GardenManager():
    """gardenerror from Exception error
    """
    plants_list: list[str] = []

    def add_plant(self, plant):
        if plant == "":
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        else:
            self.plants_list.append(plant)
            print(f"Added {plant} successfully")

    def water_plants(self):
        """print && except Errors
        """
        print("Opening watering system")
        try:
            for plant in self.plants_list:
                print("Watering " + plant)
        except TypeError:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self, plant_name, water_level, sunlight_hours):
        """
            check plant health && raising errors
        """
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
        if 1 > water_level:
            raise ValueError(f"Error checking {plant_name}: Water level"
                             f" {water_level} is too low (min 1)")
        if 10 < water_level:
            raise ValueError(f"Error checking {plant_name}: Water level"
                             f" {water_level} is too high (max 10)")
        if 2 > sunlight_hours:
            raise ValueError(f"Error checking {plant_name}: Sunlight hours "
                             f"{sunlight_hours} is too low (min 2)")
        if 12 < sunlight_hours:
            raise ValueError(f"Error checking {plant_name}: Sunlight hours"
                             f" {sunlight_hours} is too high (max 12)")
        else:
            print(f"{plant_name}: healthy (water: {water_level},"
                  f" sun: {sunlight_hours})")

    def check_water(self, level):
        """
            check water is enough
        """
        if level < 5:
            raise WaterError("Not enough water in tank")
        print(f"Water level is okay: {level}")


def main():
    """
        main
    """
    garde_manager = GardenManager()
    print("=== Garden Management System ===")
    try:
        print("\nAdding plants to garden...")
        garde_manager.add_plant("tomato")
        garde_manager.add_plant("lettuce")
        garde_manager.add_plant("")
    except PlantError as e:
        print(f"{e}")
    print("\nWatering plants...")
    garde_manager.water_plants()
    print("\nChecking plant health...")
    try:
        garde_manager.check_plants_health("tomato", 5, 8)
        garde_manager.check_plants_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"{e}")
    print("\nTesting error recovery...")
    try:
        garde_manager.check_water(4)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


main()
