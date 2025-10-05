from config import GameConfig
from items import Weapon, Armor

class Player:
    def __init__(self, name: str):
        if not name or len(name.strip()) < GameConfig.MIN_NAME_LENGTH:
            raise ValueError(f"Player name must be at least {GameConfig.MIN_NAME_LENGTH} character long")
        if len(name) > GameConfig.MAX_NAME_LENGTH:
            raise ValueError(f"Player name cannot exceed {GameConfig.MAX_NAME_LENGTH} characters")

        self.name = name.strip()
        self.level = GameConfig.PLAYER_START_LEVEL
        self.xp = GameConfig.PLAYER_START_XP
        self.max_hp = GameConfig.PLAYER_START_HP
        self.hp = self.max_hp
        self.attack = GameConfig.PLAYER_START_ATTACK
        self.inventory = {"potion": 2}
        self.weapon = None
        self.armor = None

    def is_alive(self) -> bool:
        return self.hp > 0

    def gain_xp(self, amount: int):
        if amount < 0:
            raise ValueError("XP gain cannot be negative")
        self.xp += amount
        self._check_level_up()

    def _check_level_up(self):
        needed = GameConfig.BASE_XP_PER_LEVEL
        current_level = self.level

        while self.xp >= needed and self.level < GameConfig.MAX_PLAYER_LEVEL:
            self.xp -= needed
            self.level += 1
            self.max_hp += 5
            self.attack += 2
            self.hp = self.max_hp
            print(f"\n🎉 {self.name} leveled up to level {self.level}!")
            needed = self.level * GameConfig.XP_SCALING_FACTOR

    def use_potion(self):
        if self.inventory.get("potion", 0) <= 0:
            print("You have no potions left.")
            return False

        heal_amount = GameConfig.POTION_HEAL_AMOUNT
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + heal_amount)
        actual_heal = self.hp - old_hp
        self.inventory["potion"] -= 1
        print(f"You used a potion and restored {actual_heal} HP.")
        return True

    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"  Level: {self.level}")
        print(f"  Attack: {self.attack}")
        weapon_bonus = f" + {self.weapon.attack_bonus}" if self.weapon else ""
        print(f"  Attack Power: {self.attack}{weapon_bonus}")
        print(f"  XP: {self.xp}/{self.level * GameConfig.XP_SCALING_FACTOR}")
        print(f"  Inventory: {self.inventory}")
        if self.weapon:
            print(f"  Weapon: {self.weapon.name}")
        if self.armor:
            print(f"  Armor: {self.armor.name}")

    def equip_weapon(self, weapon: Weapon):
        """Equip a weapon, replacing the current one if any."""
        if self.weapon:
            print(f"You unequip your {self.weapon.name}.")
        self.weapon = weapon
        print(f"You equip the {weapon.name}! (+{weapon.attack_bonus} attack)")

    def equip_armor(self, armor: Armor):
        """Equip armor, replacing the current armor if any."""
        if self.armor:
            print(f"You unequip your {self.armor.name}.")
        self.armor = armor
        print(f"You equip the {armor.name}! (+{armor.defense_bonus} defense)")

    def get_total_attack(self) -> int:
        """Get total attack including weapon bonus."""
        base_attack = self.attack
        if self.weapon:
            base_attack += self.weapon.attack_bonus
        return base_attack

    def get_defense(self) -> int:
        """Get total defense from armor."""
        return self.armor.defense_bonus if self.armor else 0
