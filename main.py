from player import Player
from explore import explore
from config import GameConfig

def get_player_name() -> str:
    """Get and validate player name input."""
    while True:
        try:
            name = input("Enter your hero's name: ").strip()
            if not name:
                print(f"Name cannot be empty. Please enter a name (1-{GameConfig.MAX_NAME_LENGTH} characters).")
                continue

            player = Player(name)  # This will raise ValueError if invalid
            return name
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

def get_menu_choice() -> str:
    """Get and validate menu choice input."""
    while True:
        choice = input("> ").strip()
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Invalid choice, please select 1-4.")

def main():
    print("=== Welcome to Shards of Pyland ===")

    name = get_player_name()
    player = Player(name)

    print(f"\nWelcome, {name}! Your adventure begins now.\n")

    while True:
        if not player.is_alive():
            print("You cannot continue your journey. The end.")
            break

        print("\nWhat would you like to do?")
        print("[1] Explore")
        print("[2] View Stats")
        print("[3] Use Potion")
        print("[4] Quit Game")

        choice = get_menu_choice()

        if choice == "1":
            explore(player)
        elif choice == "2":
            player.show_stats()
        elif choice == "3":
            player.use_potion()
        elif choice == "4":
            print("\nFarewell, brave adventurer!")
            break

if __name__ == "__main__":
    main()
