class MenuManager():

    def __init__(self):
            
        self.menu = [
            {"name": "Soup", "price": 10, "spice": 'B', "gluten": False},
           {"name": "Hamburger", "price": 15, "spice": 'A', "gluten": True},
           {"name": "Salad", "price": 18, "spice": 'A', "gluten": False},
           {"name": "French Fries", "price": 5, "spice": 'C', "gluten": False},
           {"name": "Beef bourguignon", "price": 25, "spice": 'B', "gluten": True}
           ]
           

    def add_item(self, name, price, spice, gluten):

        for item in self.menu:
            if item['name'] == name:
                print(f'The dish {name} is already in menu.')
                return
        
        new_item = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_item)
        print(f'dish {name} succsesfuly added in menu')


    def update_item(self, name, new_price, new_spice, new_gluten):
        for item in self.menu:
            if item['name'] == name:
                item['price'] = new_price
                item['spice'] = new_spice
                item['gluten'] = new_gluten

                item_found = True
                break

        if item_found:
            print(f"Блюдо '{name}' успешно обновлено.")
        else:
            print(f"Ошибка: Блюдо с названием '{name}' не найдено в меню.")

        print(f"Error: dish {name} is not found.")
        return False


    def remove_item(self,name):
        item_to_remove = None
        
        for item in self.menu:
            if item['name'] == name:
                item_to_remove = item
                break

        if item_to_remove:
            self.menu.remove(item_to_remove)
            print(f"Dish '{name}' successfully removed.")
            return True
        else:
            print(f"Error: dish '{name}' not found")
            return False           

manager = MenuManager()
# Удаляем гамбургер
print("--- Попытка удалить 'Hamburger' ---")
manager.remove_item('Hamburger')
# print(manager.menu) # Раскомментируйте, чтобы увидеть меню после удаления

# Пытаемся удалить несуществующее блюдо
print("\n--- Попытка удалить 'Pizza' ---")
manager.remove_item('Pizza')

# Добавляем новое блюдо
print("\n--- Добавление 'Pizza' ---")
manager.add_item(name="Pizza", price=20, spice='A', gluten=True)

# Обновляем существующее блюдо
print("\n--- Обновление 'Soup' ---")
manager.update_item(name="Soup", new_price=12, new_spice='A', new_gluten=False)

# Выводим финальное меню
print("\n--- Финальное состояние меню ---")
# Используем цикл для красивого вывода
for dish in manager.menu:
    print(dish)
