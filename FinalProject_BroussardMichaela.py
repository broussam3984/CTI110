# Michaela Broussard
# May 5, 2026
# Final Project
# This program is a soimple adventure game using loops, functions, dictionaries, random and time

import random
import time


def pause():
    time.sleep(1)


def show_status(player):
    print("\n===== PLAYER STATUS =====")
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}")
    print(f"Energy: {player['energy']}")
    print(f"Coins: {player['coins']}")
    print(f"Inventory: {player['inventory']}")
    print("=========================\n")


def intro():
    print("🌤️ Welcome to Campus Quest!")
    pause()
    print("Your goal is to make it across campus and collect enough coins to buy lunch.")
    pause()
    print("Be careful though. You may lose energy or health along the way!")
    pause()


def choose_path(player):
    print("\nWhere would you like to go?")
    print("1. Library")
    print("2. Cafeteria")
    print("3. Computer Lab")
    print("4. Show Status")
    print("5. Quit Game")

    choice = input("Enter your choice: ")

    if choice == "1":
        library_event(player)
    elif choice == "2":
        cafeteria_event(player)
    elif choice == "3":
        lab_event(player)
    elif choice == "4":
        show_status(player)
    elif choice == "5":
        player["playing"] = False
        print("Thanks for playing Campus Quest!")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")


def library_event(player):
    print("\n📚 You entered the library.")
    pause()

    event = random.choice(["study", "quiz", "lost_coin"])

    if event == "study":
        print("You studied quietly and gained energy.")
        player["energy"] += 10
    elif event == "quiz":
        print("A surprise quiz popped up!")
        answer = input("What keyword is used to define a function in Python? ").lower()

        if answer == "def":
            print("Correct! You earned 5 coins.")
            player["coins"] += 5
        else:
            print("Wrong answer. You lost 5 energy.")
            player["energy"] -= 5
    else:
        print("You found 3 coins under a chair!")
        player["coins"] += 3


def cafeteria_event(player):
    print("\n🍔 You went to the cafeteria.")
    pause()

    if player["coins"] >= 5:
        print("You bought a snack for 5 coins and gained health.")
        player["coins"] -= 5
        player["health"] += 10
        player["inventory"]["snacks"] += 1
    else:
        print("You do not have enough coins to buy food.")
        print("You lost 5 energy from being hungry.")
        player["energy"] -= 5


def lab_event(player):
    print("\n💻 You entered the computer lab.")
    pause()

    event = random.choice(["fix_computer", "virus", "bonus"])

    if event == "fix_computer":
        print("You helped fix a computer and earned 10 coins!")
        player["coins"] += 10
        player["inventory"]["tech_badges"] += 1
    elif event == "virus":
        print("Oh no! A computer virus slowed you down.")
        player["health"] -= 10
        player["energy"] -= 5
    else:
        print("You completed a quick coding challenge and gained energy!")
        player["energy"] += 5
        player["coins"] += 5


def check_game_over(player):
    if player["health"] <= 0:
        print("\nYou ran out of health. Game over!")
        player["playing"] = False

    elif player["energy"] <= 0:
        print("\nYou ran out of energy. Game over!")
        player["playing"] = False

    elif player["coins"] >= 25:
        print("\n🎉 Congratulations! You collected enough coins to buy lunch and win the game!")
        player["playing"] = False


def main():
    player = {
        "name": "",
        "health": 50,
        "energy": 50,
        "coins": 0,
        "inventory": {
            "snacks": 0,
            "tech_badges": 0
        },
        "playing": True
    }

    intro()
    player["name"] = input("\nEnter your character's name: ")

    while player["playing"]:
        choose_path(player)
        check_game_over(player)

    print("\nFinal Status:")
    show_status(player)


if __name__ == "__main__":
    main()