#!/usr/bin/env python3
"""
Quick test script to verify the RPG game works correctly.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from player import Player
    from enemy import Enemy
    from items import Weapon, Armor
    from config import GameConfig

    print("✅ All imports successful!")

    # Test player creation
    player = Player("TestHero")
    print(f"✅ Player created: {player.name}, Level: {player.level}")

    # Test enemy creation
    enemy = Enemy.random_enemy(1)
    print(f"✅ Enemy created: {enemy.name}, HP: {enemy.hp}, Attack: {enemy.attack}")

    # Test equipment
    weapon = Weapon("Test Sword", 5)
    armor = Armor("Test Armor", 3)
    player.equip_weapon(weapon)
    player.equip_armor(armor)
    print(f"✅ Equipment system works: {player.weapon.name}, {player.armor.name}")

    # Test stats
    player.show_stats()
    print("✅ Stats display works!")

    print("\n🎉 All tests passed! Game is ready to play.")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
