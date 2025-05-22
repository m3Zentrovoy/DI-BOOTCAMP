import random

class Game:
    def __init__(self):
        self.valid_items = ["rock", "paper", "scissors"]

    def get_user_item(self):
        while True:
            user_item = input("Choose your weapon (rock/paper/scissors): ").strip().lower()
            if user_item in self.valid_items:
                return user_item
            print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        return random.choice(self.valid_items)
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == "rock":
            if computer_item == "paper":
                return "loss"
            else:
                return "win"
        elif user_item == "paper":
            if computer_item == "scissors":
                return "loss"
            else:
                return "win"
        elif user_item == "scissors":
            if computer_item == "rock":
                return "loss"
            else:
                return "win"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: {result}")
        return result