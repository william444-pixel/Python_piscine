def ft_harvest_total() -> None:
    """
    Asks for harvest amounts for 3 days and displays the total.
    """
    D1: int = int(input("Day 1 harvest: "))
    D2: int = int(input("Day 2 harvest: "))
    D3: int = int(input("Day 3 harvest: "))
    print(f"Total harvest: {D1 + D2 + D3}")
