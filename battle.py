import random
from player import Player
from enemy import Enemy

def battle(player: Player, enemy: Enemy) -> bool:
    """
    Conducts a battle between player and enemy.
    Returns True if battle ended (either win or death or run),
    False if player ran away (so maybe no XP).
    """
    print(f"\n⚔️ A wild **{enemy.name}** appears!")
    while player.is_alive() and enemy.is_alive():
        print(f"\nYour HP: {player.hp}/{player.max_hp} | {enemy.name} HP: {enemy.hp}")
        print("[1] Attack   [2] Use Potion   [3] Run")
        choice = input("> ").strip()

        if choice == "1":
            dmg = random.randint(max(1, player.attack - 2), player.attack + 2)
            enemy.hp -= dmg
            print(f"You hit {enemy.name} for {dmg} damage.")
        elif choice == "2":
            player.use_potion()
        elif choice == "3":
            # Running attempt
            print("You attempt to run away...")
            # 50% chance to successfully escape
            if random.random() < 0.5:
                print("You escape successfully!")
                return False
            else:
                print("Failed to escape!")
        else:
            print("Invalid choice; you lose your turn.")

        # Enemy's turn (if alive)
        if enemy.is_alive():
            edmg = random.randint(max(1, enemy.attack - 1), enemy.attack + 1)
            player.hp -= edmg
            print(f"{enemy.name} hits you for {edmg} damage.")

    # After loop: check results
    if not player.is_alive():
        print("\n💀 You died. Game Over.")
        return True
    else:
        print(f"\n✅ You defeated the {enemy.name}!")
        player.gain_xp(enemy.xp_reward)
        # Loot: maybe drop a potion
        from random import random
        if random() < 0.3:
            player.inventory["potion"] = player.inventory.get("potion", 0) + 1
            print("The enemy dropped a potion! You add it to your inventory.")
        return True
