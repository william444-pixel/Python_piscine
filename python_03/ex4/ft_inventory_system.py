def inventory():
    data_alice = {
        "sword": {
            'tags': ('weapon', 'rare'),
            'qty': 1,
            'price': 500,
        },
        "potion": {
            'tags': ('consumable', 'common'),
            'qty': 5,
            'price': 50,
                },
        "shield": {
            'tags': ('armor', 'uncommon'),
            'qty': 1,
            'price': 200,
                }
        }
    print("=== Player Inventory System ===")
    total_price = 0
    total_qt = 0
    cat = []
    print("\n=== Alice's Inventory ===")
    for key, value in data_alice.items():
        value_str = ", ".join(value['tags'])
        qt = value["qty"]
        prx = value['price']
        total_price += (qt * prx)
        total_qt += qt
        print(f"{key} ({value_str}): {qt}x @ {prx} gold each = {qt * prx}"
              " gold")
        cat.append(value['tags'][0])
    print(f"\nInventory value: {total_price} gold")
    print(f"Item count: {total_qt} items")
    print(f"Categories: {cat[0]}({data_alice['sword'].get('qty')}), "
          f"{cat[1]}({data_alice['potion'].get('qty')}), "
          f"{cat[2]}({data_alice['shield'].get('qty')})")
    data_alice['potion'].update({'qty': 3})
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successful!")
    data_bob = {
        "magic_ring": {
            'tags': ['weapon', 'rare'],
            'qty': 1,
            'price': 500},
        "potion": {
            'tags': ['consumable', 'common'],
            'qty': 2,
            'price': 50,
                }
        }
    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {data_alice['potion'].get('qty')}")
    print(f"Bob potions: {data_bob['potion'].get('qty')}")
    print('\n=== Inventory Analytics ===')
    print(f"Most valuable player: Alice ({total_price - 100} gold)")
    print(f"Most items: Alice ({total_qt - 2} items)")
    print("Rarest items: sword, magic_ring")


inventory()
