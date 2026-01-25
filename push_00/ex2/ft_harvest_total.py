def ft_harvest_total() -> None:
    """
    Asks for harvest amounts for 3 days and displays the total.
    """
    d1: int = int(input("Day 1 harvest: "))
    d2: int = int(input("Day 2 harvest: "))
    d3: int = int(input("Day 3 harvest: "))
    print(f"Total harvest: {d1 + d2 + d3}")
