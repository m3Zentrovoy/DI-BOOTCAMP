import json

class MenuManager:
    def __init__(self):
        with open("restaurant_menu.json", "r") as json_file:
            self.menu = json.load(json_file)

    def add_item(self, name, price):
        new_item = {"name": name, "price": price}
        self.menu["items"].append(new_item)

    def remove_item(self, name):
        for item in self.menu["items"]:
            if item["name"] == name:
                self.menu["items"].remove(item)
                return True
        return False

    def save_to_file(self):
        with open("restaurant_menu.json", "w") as json_file:
            json.dump(self.menu, json_file, indent=4)