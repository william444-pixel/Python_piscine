def ft_plant_age() -> None:
    # Get the age of the plant from user input and convert it to an integer
    Age: int = int(input("Enter plant age in days: "))
    # Check if the plant has been growing for more than 60 days
    if Age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
