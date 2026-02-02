def achievement_analytics(player1, player2, player3):
    unique_achievements = player1.union(player2, player3)
    p1_unique = player1.difference(player2)
    p2_unique = player2.difference(player1)
    common = player1.intersection(player2, player3)
    common1_2 = player1.intersection(player2)
    rare1 = player1.difference(player2).difference(player3)
    rare2 = player2.difference(player1).difference(player3)
    rare3 = player3.difference(player1).difference(player2)
    rare = rare1.union(rare2, rare3)
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")
    print(f"\nAlice vs Bob common: {common1_2}")
    print(f"Alice unique: {p1_unique}")
    print(f"Alice unique: {p2_unique}")


def achievement_tracker():
    alice = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
    bob = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    charlie = ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist']
    s_alice = set(alice)
    s_bob = set(bob)
    s_charlie = set(charlie)
    print("=== Achievement Tracker System ===")
    print(f"\nPlayer alice achievements: {s_alice}")
    print(f"Player bob achievements: {s_bob}")
    print(f"Player charlie achievements: {s_charlie}")
    achievement_analytics(s_alice, s_bob, s_charlie)


achievement_tracker()
