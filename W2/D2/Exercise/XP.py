
# #🌟 Exercise 1: Pets

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    


# all_cats = [Siamese('Kot', 3), Bengal('Pers', 3), Chartreux('Sfinx', 4)]

# sara_pets = Pets(all_cats)

# sara_pets.walk()


# Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
       self.name = name
       self.age = age
       self.weight = weight
       
    
    def bark(self):
        return (f'{self.name} is barking ')


    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight  # Считаем силу первой собаки
        other_power = other_dog.run_speed() * other_dog.weight  # Считаем силу второй собаки
        if self_power >= other_power:
            return f"{self.name} won the fight!"
        else:
            return f"{other_dog.name} won the fight!"

         



dog1 = Dog('Kuki', 3, 15)
dog2 = Dog('Mia', 2, 20)
dog3 = Dog('Pushok', 1, 45)


print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

