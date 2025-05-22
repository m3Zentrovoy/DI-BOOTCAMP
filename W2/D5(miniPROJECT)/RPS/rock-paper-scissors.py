from game import Game

def get_user_menu_choice():
    valid_choices = {"1": "Play a new game", "2": "Show scores", "3": "Quit"}
    while True:
        print("\nMenu:")
        for key, value in valid_choices.items():
            print(f"{key}. {value}")
        choice = input("Enter your choice (1-3): ").strip()
        if choice in valid_choices:
            return valid_choices[choice]
        print("Invalid choice. Please select 1, 2, or 3.")

def print_results(results):
    print(f"Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "Play a new game":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "Show scores":
            print_results(results)
        elif choice == "Quit":
            print_results(results)
            break

if __name__ == "__main__":
    main()