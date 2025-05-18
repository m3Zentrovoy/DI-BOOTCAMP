
# #ex1

# class Cat:

#     # Creating attributes for all instances
#     def __init__(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age
      
# cat1 = Cat('Persik', 'Brown', 3)
# cat2 = Cat('Bananas','White',2)
# cat3 = Cat('Apple','black',5)


# def find_oldest_cat(cat1, cat2, cat3):
#     if not (cat1 and cat2 and cat3):
#         return None
    
#     oldest_cat = cat1
    
#     for cat in (cat1, cat2, cat3):

#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
    
#     return oldest_cat

# # my_cat = [cat1, cat2, cat3]

# oldest = find_oldest_cat(cat1, cat2, cat3)
# print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")




# #ex 2

# class Dog:
#     def __init__(self, name, haight):
#        print('creating object')
#        self.name = name
#        self.haight = haight
      

#     def bark(self):
#         print(f'{self.name} goes woof! ')


#     def jump(self):
#         print(f"{self.name} jumps {self.haight * 2} cm high!")



# davids_dog = Dog('Davids', 60)
# print(davids_dog.__dict__)
# davids_dog.bark()
# davids_dog.jump()


# sarahs_dog = Dog('Sarahs', 40)
# print(sarahs_dog.__dict__)
# sarahs_dog.bark()
# sarahs_dog.jump()



#ex3

        
# stairway = ["There's a lady who's sure", 
#                  "all that glitters is gold", 
#                  "and she's buying a stairway to heaven"]


# class Song:
#         def __init__(self, lyrics):
#             self.lyrics = lyrics

#         def sing_me_a_song(self):
#             for stair in self.lyrics:
#                 print(stair)

# song = Song(stairway)
# song.sing_me_a_song()

#ex4
class Animal:
    def __init__(self):
        self.animals = []
     
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} already in zoo!")

    def get_animals(self):
        print("Animals in zoo:", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} sold from zoo!")
        else:
            print(f"{animal_sold} not found in zoo!")

    def sort_animals(self):
        self.animals.sort(key=str.lower)  
        
        res = {}
        
        for animal in self.animals:
            first_letter = animal[0].lower() 
            if first_letter not in res:
                res[first_letter] = []
            res[first_letter].append(animal)
        
        return res


    def get_groups(self):
        
        groups = self.sort_animals()
        
        if not groups:
            print("No animals in zoo!")
            return
        
        for letter, animal_list in groups.items():
            print(f"{letter.upper()}: {animal_list}")



zoo = Animal()


zoo.add_animal("Baboon")
zoo.add_animal("Bear")
zoo.add_animal("Cat")
zoo.add_animal("Cougar")
zoo.add_animal("Giraffe")
zoo.add_animal("Lion")
zoo.add_animal("Zebra")

# Class Zoo to manage a list of animals
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name  # Store the name of the zoo
        self.animals = []  # Initialize an empty list for animals

    def add_animal(self, new_animal):
        # Check if the animal is already in the list
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to {self.zoo_name}!")
        else:
            print(f"{new_animal} is already in the zoo!")

    def get_animals(self):
        # Display the list of animals
        print(f"Animals in {self.zoo_name}:", self.animals)

    def sell_animal(self, animal_sold):
        # Check if the animal is in the list and remove it
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} sold from {self.zoo_name}!")
        else:
            print(f"{animal_sold} not found in the zoo!")

    def sort_animals(self):
        # Sort the list of animals alphabetically
        self.animals.sort(key=str.lower)  # Ignore case while sorting
        
        # Create a dictionary for grouping
        res = {}
        
        # Iterate through animals
        for animal in self.animals:
            # Get the first letter (lowercase)
            first_letter = animal[0].lower()
            # If the letter is not in the dictionary, create an empty list
            if first_letter not in res:
                res[first_letter] = []
            # Add the animal to the list for that letter
            res[first_letter].append(animal)
        
        # Return the dictionary
        return res

    def get_groups(self):
        # Get the grouped animals
        groups = self.sort_animals()
        
        # Check if there are any animals
        if not groups:
            print("No animals in the zoo!")
            return
        
        # Iterate and print the groups
        print(f"Animal groups in {self.zoo_name}:")
        for letter, animal_list in groups.items():
            print(f"{letter.upper()}: {animal_list}")

# Step 2: Create a Zoo instance
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Step 3: Use the Zoo methods
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()