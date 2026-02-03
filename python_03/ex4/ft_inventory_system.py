def inventory():
    data_alice = dict(sword={
        'tags': ['weapon', 'rare'],
        'qty': 1,
        'price': 500,
        },
        potion={
            'tags': ['consumable', 'common'],
            'qty': 5,
            'price': 50,
                },
        shield={
            'tags': ['armor', 'uncommon'],
            'qty': 1,
            'price': 200,
                })
    print("=== Player Inventory System ===")
    total_price = 0
    total_qt = 0
    cat = []
    print("\n=== Alice's Inventory ===")
    for key, value, in data_alice.items():
        for ky, val, in value.items():
            value_str = ", ".join(val)
            if "qty" in value:
                qt = data_alice[key]["qty"]
            if 'price' in value:
                prx = data_alice[key]['price']
            total_price += (qt * prx)
            total_qt += qt
            print(f"{key} ({value_str}) {qt}x @ {prx} gold each = {qt * prx}"
                  " gold")
            cat.append(val[0])
            break
    print(f"\nInventory value: {total_price} gold")
    print(f"Item count: {total_qt} items")
    print(f"Categories: {cat[0]}({data_alice['sword'].get('qty')}), "
          f"{cat[1]}({data_alice['potion'].get('qty')}), "
          f"{cat[2]}({data_alice['shield'].get('qty')})")
    {data_alice['potion'].update({'qty': 3})}
    print(f"\n=== Transaction: Alice gives Bob "
          f"{data_alice['potion'].get('qty')} potions ===")
    print("Transaction successful!")
    data_bob = dict(potion={
            'tags': ['consumable', 'common'],
            'qty': 2,
            'price': 50,
                })
    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {data_alice['potion'].get('qty')}")
    print(f"Bob potions: {data_bob['potion'].get('qty')}")
    print('\n=== Inventory Analytics ===')


inventory()
