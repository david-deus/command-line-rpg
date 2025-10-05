from player import Player
from explore import explore

def main():
    print("=== Welcome to Shards of Pyland ===")
    name = input("Enter your hero’s name: ").strip()
    if not name:
        name = "Hero"
    player = Player(name)

    while True:
        if not player.is_alive():
            print("You cannot continue your journey. The end.")
            break

        print("\nWhat would you like to do?")
        print("[1] Explore")
        print("[2] View Stats")
        print("[3] Use Potion")
        print("[4] Quit Game")

        choice = input("> ").strip()
        if choice == "1":
            explore(player)
        elif choice == "2":
            player.show_stats()
        elif choice == "3":
            player.use_potion()
        elif choice == "4":
            print("\n👋 Farewell, brave adventurer!")
            break
        else:
            print("Invalid choice, please select 1–4.")

if __name__ == "__main__":
    main()
