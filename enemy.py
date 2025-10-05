import random

class Enemy:
    def __init__(self, name: str, hp: int, attack: int, xp_reward: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.xp_reward = xp_reward

    def is_alive(self) -> bool:
        return self.hp > 0

    @staticmethod
    def random_enemy(player_level: int):
        # base enemy types
        templates = [
            ("Goblin", 10, 3, 20),
            ("Skeleton", 12, 4, 25),
            ("Orc", 16, 5, 35),
        ]
        name, base_hp, base_atk, xp = random.choice(templates)
        # scale stats by player level a bit
        hp = base_hp + player_level * 2
        attack = base_atk + player_level // 2
        xp_reward = xp + player_level * 5
        return Enemy(name, hp, attack, xp_reward)
