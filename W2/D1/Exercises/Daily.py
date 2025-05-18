
class Farm:

       
    def __init__(self,farm_name):
       self.name = farm_name
       self.animals = {}
      
    def add_animal(self, animal_type, count = 1):
        
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
        
            
    def get_info(self):
        # Начинаем с названия фермы
        info = f"{self.name}'s farm\n\n"
        
        # Добавляем животных и их количество
        for animal, count in self.animals.items():
            info += f"{animal:<10} : {count}\n"
        
        # Добавляем фразу в конце
        info += "\n    E-I-E-I-0!"
        
        # Возвращаем строку
        return info
    
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    
    def get_short_info(self):
        new_name = []
        for name in self.get_animal_types():
            if self.animals[name] > 1:
                new_name.append(name + 's')
            else:
                new_name.append(name)

        final_str = (f'{self.name} farm has {', '.join(new_name)}.')
        return final_str
   


# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 1)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# print(macdonald.get_animal_types())
print(macdonald.get_short_info())