def ft_count_harvest_recursive() -> None:
    number_days: int = int(input("Days until harvest: "))

    def count_days(day: int) -> None:
        if day > number_days:
            return
        print(f"Day {day}")
        count_days(day + 1)
    count_days(1)
    print("Harvest time!")
