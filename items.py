"""
Equipment system for the RPG game.
Defines weapons and armor that players can find and equip.
"""

class Weapon:
    def __init__(self, name: str, attack_bonus: int, rarity: str = "common"):
        self.name = name
        self.attack_bonus = attack_bonus
        self.rarity = rarity

class Armor:
    def __init__(self, name: str, defense_bonus: int, rarity: str = "common"):
        self.name = name
        self.defense_bonus = defense_bonus
        self.rarity = rarity

# Predefined equipment
WEAPONS = {
    "rusty_sword": Weapon("Rusty Sword", 3, "common"),
    "iron_sword": Weapon("Iron Sword", 5, "uncommon"),
    "steel_sword": Weapon("Steel Sword", 8, "rare"),
    "magic_sword": Weapon("Magic Sword", 12, "epic"),
    "dagger": Weapon("Sharp Dagger", 2, "common"),
    "battle_axe": Weapon("Battle Axe", 7, "uncommon"),
    "enchanted_blade": Weapon("Enchanted Blade", 10, "rare"),
}

ARMOR = {
    "leather_armor": Armor("Leather Armor", 2, "common"),
    "chain_mail": Armor("Chain Mail", 4, "uncommon"),
    "plate_armor": Armor("Plate Armor", 7, "rare"),
    "enchanted_robes": Armor("Enchanted Robes", 6, "rare"),
    "cloth_tunic": Armor("Cloth Tunic", 1, "common"),
    "studded_leather": Armor("Studded Leather", 3, "common"),
}

def get_random_weapon() -> Weapon:
    """Return a random weapon from the available weapons."""
    import random
    return random.choice(list(WEAPONS.values()))

def get_random_armor() -> Armor:
    """Return a random armor from the available armor."""
    import random
    return random.choice(list(ARMOR.values()))
