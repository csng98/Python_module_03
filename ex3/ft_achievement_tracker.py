import random


def generate_players(achievements):
    return {"Alice": set(random.sample(achievements, 6)),
            "Bob": set(random.sample(achievements, 7)),
            "Charlie": set(random.sample(achievements, 9)),
            "Dylan": set(random.sample(achievements, 5))}


def print_players(players):
    for player, player_achievements in players.items():
        print(f"Player {player}: {player_achievements}")


def print_unique_achievements(players):
    for player in players:
        others = set().union(*(players[p] for p in players if p != player))
        print(f"Only {player} has:", players[player] - others)


def print_missing_achievements(players, all_achievements):
    for player in players:
        print(f"{player} is missing:", all_achievements - players[player])


def gen_player_achievements():
    random.seed(42)

    achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                    "Collector Supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Unstoppable", "Speed Runner",
                    "Treasure Hunter", "First Steps", "Sharp Mind"]

    all_achievements = set(achievements)
    players = generate_players(achievements)

    print("=== Achievement Tracker System ===\n")

    print_players(players)

    print("\nAll distinct achievements:", set().union(*players.values()))

    print("\nCommon achievements:", set.intersection(*players.values()))

    print_unique_achievements(players)

    print_missing_achievements(players, all_achievements)


if __name__ == "__main__":
    print(gen_player_achievements())
