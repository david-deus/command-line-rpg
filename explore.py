import random
from enemy import Enemy
from battle import battle
from player import Player
from config import GameConfig

def explore(player: Player):
    print("\n🌳 You venture into the wild...")
    # Use weighted random selection for more varied encounters
    event = random.choices(
        GameConfig.EXPLORATION_EVENTS,
        weights=GameConfig.EVENT_WEIGHTS,
        k=1
    )[0]

    if event == "enemy":
        enemy = Enemy.random_enemy(player.level)
        battle(player, enemy)
    elif event == "loot":
        # Random loot - potions or gold
        loot_type = random.choice(["potion", "gold"])
        if loot_type == "potion":
            loot_amount = random.randint(1, 3)
            player.inventory["potion"] = player.inventory.get("potion", 0) + loot_amount
            print(f"✨ You found {loot_amount} potion{'s' if loot_amount > 1 else ''}!")
        else:
            gold_amount = random.randint(5, 20) * player.level
            player.inventory["gold"] = player.inventory.get("gold", 0) + gold_amount
            print(f"💰 You found {gold_amount} gold coins!")
    elif event == "treasure":
        # Rare treasure chest with better loot
        print("💎 You discovered a treasure chest!")
        treasure_loot = random.choice(["rare_weapon", "armor", "potions", "gold"])
        if treasure_loot == "rare_weapon":
            print("🗡️ Inside you find a rare weapon!")
            # We'll implement weapon system next
        elif treasure_loot == "armor":
            print("🛡️ Inside you find sturdy armor!")
        elif treasure_loot == "potions":
            potions_found = random.randint(3, 5)
            player.inventory["potion"] = player.inventory.get("potion", 0) + potions_found
            print(f"🧪 You found {potions_found} potions!")
        else:
            gold_found = random.randint(50, 100) * player.level
            player.inventory["gold"] = player.inventory.get("gold", 0) + gold_found
            print(f"💰 You found {gold_found} gold coins!")
    elif event == "merchant":
        print("🤝 You encounter a traveling merchant!")
        print("They offer to sell you potions for 15 gold each.")
        print(f"You have {player.inventory.get('gold', 0)} gold.")
        choice = input("Buy a potion? (y/n): ").strip().lower()
        if choice == 'y' and player.inventory.get("gold", 0) >= 15:
            player.inventory["gold"] = player.inventory.get("gold", 0) - 15
            player.inventory["potion"] = player.inventory.get("potion", 0) + 1
            print("✅ You bought a potion!")
        else:
            print("❌ You decide not to buy anything.")
    elif event == "nothing":
        # Add some flavor text for variety
        flavor_texts = [
            "You walk for a while. Nothing eventful happens.",
            "The wind whispers through the trees. All is quiet.",
            "You find a peaceful clearing. A good place to rest.",
            "You hear birds singing in the distance. Peaceful journey.",
        ]
        print(random.choice(flavor_texts))
