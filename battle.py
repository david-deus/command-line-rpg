import random
from player import Player
from enemy import Enemy
from config import GameConfig

def battle(player: Player, enemy: Enemy) -> bool:
    """
    Conducts a battle between player and enemy.
    Returns True if battle ended (either win or death or run),
    False if player ran away (so maybe no XP).
    """
    print(f"\n⚔️ A wild **{enemy.name}** appears!")
    print(f"Enemy HP: {enemy.hp} | Enemy Attack: {enemy.attack}")

    while player.is_alive() and enemy.is_alive():
        print(f"\nYour HP: {player.hp}/{player.max_hp} | {enemy.name} HP: {enemy.hp}")
        print("[1] Attack   [2] Use Potion   [3] Run")

        choice = input("> ").strip()

        if choice == "1":
            # Player attack with variance
            base_damage = player.attack
            if player.weapon:
                base_damage += player.weapon.attack_bonus

            damage = random.randint(
                max(1, base_damage - GameConfig.PLAYER_ATTACK_VARIANCE),
                base_damage + GameConfig.PLAYER_ATTACK_VARIANCE
            )
            enemy.hp -= damage
            print(f"💥 You hit {enemy.name} for {damage} damage!")

            # Special attack messages for high damage
            if damage > base_damage + GameConfig.PLAYER_ATTACK_VARIANCE // 2:
                print("🎯 Critical hit!")

        elif choice == "2":
            if not player.use_potion():
                continue  # Skip enemy turn if potion use failed
        elif choice == "3":
            # Running attempt with configurable success rate
            print("🏃 You attempt to run away...")
            if random.random() < GameConfig.RUN_SUCCESS_CHANCE:
                print("✅ You escape successfully!")
                return False
            else:
                print("❌ Failed to escape!")
        else:
            print("❌ Invalid choice; you lose your turn.")

        # Enemy's turn (if still alive)
        if enemy.is_alive():
            # Enemy attack with variance
            enemy_damage = random.randint(
                max(1, enemy.attack - GameConfig.ENEMY_ATTACK_VARIANCE),
                enemy.attack + GameConfig.ENEMY_ATTACK_VARIANCE
            )

            # Reduce damage if player has armor
            if player.armor:
                enemy_damage -= player.armor.defense_bonus
                enemy_damage = max(1, enemy_damage)  # Minimum 1 damage

            player.hp -= enemy_damage
            print(f"⚔️ {enemy.name} hits you for {enemy_damage} damage!")

    # After loop: check results
    if not player.is_alive():
        print("\n💀 You died. Game Over.")
        return True
    else:
        print(f"\n✅ You defeated the {enemy.name}!")

        # Gain XP and check for level up
        player.gain_xp(enemy.xp_reward)

        # Loot drop with configurable chance
        if random.random() < GameConfig.POTION_DROP_CHANCE:
            loot_amount = random.randint(1, 2)
            player.inventory["potion"] = player.inventory.get("potion", 0) + loot_amount
            print(f"🎁 The enemy dropped {loot_amount} potion{'s' if loot_amount > 1 else ''}!")

        return True
