import random
from config import GameConfig

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
        # Expanded enemy types with more variety
        templates = [
            # (name, base_hp, base_attack, xp_reward)
            ("Goblin", 10, 3, 20),
            ("Skeleton", 12, 4, 25),
            ("Orc", 16, 5, 35),
            ("Troll", 25, 7, 50),
            ("Dark Elf", 14, 6, 40),
            ("Giant Spider", 8, 4, 30),
            ("Zombie", 15, 3, 28),
            ("Bandit", 12, 5, 32),
            ("Cave Bear", 20, 8, 45),
            ("Fire Elemental", 18, 9, 55),
        ]

        name, base_hp, base_atk, xp = random.choice(templates)

        # Scale stats based on player level using config constants
        hp = base_hp + player_level * GameConfig.ENEMY_HP_SCALING
        attack = base_atk + (player_level // 2) * int(GameConfig.ENEMY_ATTACK_SCALING * 2)
        xp_reward = xp + player_level * GameConfig.ENEMY_XP_SCALING

        # Add some randomness to make encounters more interesting
        hp = int(hp * random.uniform(0.8, 1.3))
        attack = int(attack * random.uniform(0.9, 1.2))

        return Enemy(name, hp, attack, xp_reward)
