import random
from enemy import Enemy
from battle import battle
from player import Player

def explore(player: Player):
    print("\n🌳 You venture into the wild...")
    # possible events
    events = ["enemy", "loot", "nothing"]
    event = random.choice(events)
    if event == "enemy":
        enemy = Enemy.random_enemy(player.level)
        battle(player, enemy)
    elif event == "loot":
        # always drop something (for now a potion)
        print("You found a potion on the ground!")
        player.inventory["potion"] = player.inventory.get("potion", 0) + 1
    elif event == "nothing":
        print("You walk for a while. Nothing eventful happens.")
