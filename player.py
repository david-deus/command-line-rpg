class Player:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.xp = 0
        self.max_hp = 20
        self.hp = self.max_hp
        self.attack = 5
        self.inventory = {"potion": 2}

    def is_alive(self) -> bool:
        return self.hp > 0

    def gain_xp(self, amount: int):
        self.xp += amount
        self._check_level_up()

    def _check_level_up(self):
        needed = self.level * 100
        while self.xp >= needed:
            self.xp -= needed
            self.level += 1
            self.max_hp += 5
            self.attack += 2
            self.hp = self.max_hp
            print(f"\n🎉 {self.name} leveled up to level {self.level}!")
            needed = self.level * 100

    def use_potion(self):
        if self.inventory.get("potion", 0) > 0:
            heal_amount = 10
            self.hp = min(self.max_hp, self.hp + heal_amount)
            self.inventory["potion"] -= 1
            print(f"You used a potion and restored {heal_amount} HP.")
        else:
            print("You have no potions left.")

    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"  Level: {self.level}")
        print(f"  HP: {self.hp}/{self.max_hp}")
        print(f"  Attack: {self.attack}")
        print(f"  XP: {self.xp}/{self.level * 100}")
        print(f"  Inventory: {self.inventory}")
