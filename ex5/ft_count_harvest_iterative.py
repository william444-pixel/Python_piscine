def ft_count_harvest_iterative() -> None:
    number_days: int = int(input("Days until harvest: "))
    for count in range(1, number_days + 1):
        print(f"Day {count}")
    print("Harvest time!")
