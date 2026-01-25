def ft_water_reminder() -> None:
    number: int = int(input("Days since last watering: "))
    if number > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
