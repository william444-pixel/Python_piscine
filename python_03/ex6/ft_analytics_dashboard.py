data_base = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements": "first_kill",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements": "first_kill",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements": "boss_slayer",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements": "first_kill",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements": "boss_slayer",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements": "level_10",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 4300,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 4300,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 4100,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 4100,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 3600,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 3600,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 4600,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 4600,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


def analytics():
    print("=== Game Analytics Dashboard ===")
    ##########################################
    print("\n=== List Comprehension Examples ===")
    list_high_score = [s["player"] for s in data_base["sessions"] if s["score"] > 2000]
    list_high_score_final = list(set(list_high_score))
    print(f"High scorers (>2000): {list_high_score_final}")
    all_scores = [s["score"] for s in data_base["sessions"]]
    duplicates = list(set([x for x in all_scores if all_scores.count(x) > 1]))
    print(f"Scores doubled: {duplicates}")
    ##################################################
    print("\n=== Dict Comprehension Examples ===")
    dict_info = {s["player"]: s["score"] for s in data_base["sessions"]}
    print(f"Player scores: {dict_info}")
    dict_categories = {
        "high": sum(
            1
            for name in data_base["players"]
            if data_base["players"][name]["level"] >= 20
        ),
        "medium": sum(
            1
            for name in data_base["players"]
            if 10 < data_base["players"][name]["level"] < 20
        ),
        "low": sum(
            1
            for name in data_base["players"]
            if data_base["players"][name]["level"] <= 10
        ),
    }
    print(f"Score categories: {dict_categories}")
    dict_achivement = {
        s: data_base["players"][s]["achievements_count"] for s in data_base["players"]
    }
    print(f"Achievement counts: {dict_achivement}")
    print("\n=== Set Comprehension Examples ===")
    set_unique = set(s["player"] for s in data_base["sessions"])
    print(f"Unique players: {set_unique}")
    set_achievement = set(
        data_base["players"][s]["achievements"] for s in data_base["players"]
    )
    print(f"Unique achievements: {set_achievement}")
    set_time = set(s["mode"] for s in data_base["sessions"])
    print(f"Unique mode: {set_time}")
    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(data_base['players'])}")
    print(f"Total unique achievements: {len(set(data_base["players"][s]
          ["achievements"]for s in data_base["players"]))}")
    scores = sum([s["score"] for s in data_base["sessions"]])
    lenght = len([s["score"] for s in data_base["sessions"]])
    avg = scores/lenght
    top_per = max({s["player"]: s["score"] for s in data_base["sessions"]})
    top_p = max({s["score"] for s in data_base["sessions"]})
    top = max({s["score"] for s in data_base["sessions"]})

    print(f"Average score: {avg:.1f}")
    print(f"Top performer: {top_per} ({top_p}, {top})")


analytics()
