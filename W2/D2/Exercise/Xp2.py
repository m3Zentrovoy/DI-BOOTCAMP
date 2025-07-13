#Exercise 3: Dogs Domesticated
import random
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

         



# dog1 = Dog('Kuki', 3, 15)
# dog2 = Dog('Mia', 2, 20)
# dog3 = Dog('Pushok', 1, 45)


# print(dog1.bark())
# print(dog2.run_speed())
# print(dog1.fight(dog2))


# class PetDog(Dog):

#     def __init__(self, name, age, weight, trained=False):
#         super().__init__(name, age, weight)
#         self.trained = trained
     
#     def train(self):
#          print(self.bark())
#          self.trained = True

#     def play(self, *args):
#         names = [self.name] + [dog.name for dog in args] 
#         print(", ".join(names) + " all play together")

    
#     def do_a_trick(self):
#         if self.trained == True:
#             tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
          
#             print(f"{self.name} {random.choice(tricks)}")



# my_dog = PetDog("Fido", 2, 10)
# dog2 = PetDog("Buddy", 3, 15)  
# dog3 = PetDog("Max", 4, 25)   

# my_dog.train()  
# my_dog.play(dog2, dog3) 
# my_dog.do_a_trick() 


#🌟 Exercise 4: Family and Person Classes



class Person():
    def __init__(self, first_name, age, ):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

class Family():
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = [] 

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

        
    def check_majority(self, first_name):
        found = False
        for person in self.members:
            if person.first_name == first_name:
                found = True
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:   
                    print("Sorry, you are not allowed to go out with your friends.")
                break
        
    def family_presentation(self):
        print(f"Family {self.last_name}")
        
        for person in self.members:  # Перебираем членов семьи
            print(f"{person.first_name} {person.age}")  # Печатаем имя и возраст



family = Family("Prokop")
family.born("Daria", 9)
family.born("Kseniia", 28)
family.check_majority("Daria")
family.check_majority("Kseniia")
family.family_presentation()