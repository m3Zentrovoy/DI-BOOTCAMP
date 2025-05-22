import json
from W2.D4.Exercise.ninja_menu.menu_manager import MenuManager

def load_manager():
    return MenuManager()

def show_user_menu():
    with open("user_menu.json", "r", encoding="utf-8") as json_file:
        user_menu = json.load(json_file)
    
    print("Restaurant Menu Manager")
    for command, description in user_menu["menu"].items():
        print(f"({command}) : {description}")
    
    return input("Enter your choice: ")

def add_item_to_menu(manager):
    name = input("Enter the name of the item: ")
    try:
        price = float(input("Enter the price of the item: "))
        manager.add_item(name, price)
        print("Item was added successfully")
    except ValueError:
        print("Error: Price must be a number")

def remove_item_from_menu(manager):
    name = input("Enter the name of the item to remove: ")
    if manager.remove_item(name):
        print("Item was removed successfully")
    else:
        print("Error: Item not found")

def show_restaurant_menu(manager):
    print("Restaurant Menu:")
    for item in manager.menu["items"]:
        print(f"{item['name']}: {item['price']}")

def main():
    manager = load_manager()
    
    while True:
        choice = show_user_menu()
        
        if choice == "v":
            show_restaurant_menu(manager)
        elif choice == "a":
            add_item_to_menu(manager)
        elif choice == "d":
            remove_item_from_menu(manager)
        elif choice == "x":
            manager.save_to_file()
            print("Menu was saved. Exiting program.")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()