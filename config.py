# Game Constants and Configuration
class GameConfig:
    # Player starting stats
    PLAYER_START_LEVEL = 1
    PLAYER_START_HP = 20
    PLAYER_START_ATTACK = 5
    PLAYER_START_XP = 0

    # Level up requirements (XP needed per level)
    BASE_XP_PER_LEVEL = 100
    XP_SCALING_FACTOR = 100

    # Combat constants
    PLAYER_ATTACK_VARIANCE = 2
    ENEMY_ATTACK_VARIANCE = 1
    RUN_SUCCESS_CHANCE = 0.5
    POTION_DROP_CHANCE = 0.3
    POTION_HEAL_AMOUNT = 10

    # Enemy scaling (per player level)
    ENEMY_HP_SCALING = 2
    ENEMY_ATTACK_SCALING = 0.5  # per 2 levels
    ENEMY_XP_SCALING = 5

    # Exploration events
    EXPLORATION_EVENTS = ["enemy", "loot", "treasure", "merchant", "nothing"]
    EVENT_WEIGHTS = [0.4, 0.3, 0.1, 0.05, 0.15]  # Probabilities for each event

    # UI Constants
    MAX_NAME_LENGTH = 20
    MIN_NAME_LENGTH = 1

    # Game limits
    MAX_INVENTORY_SIZE = 99
    MAX_PLAYER_LEVEL = 50

    # File paths
    SAVE_FILE_PATH = "savegame.json"
