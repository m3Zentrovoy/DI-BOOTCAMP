#OOP OERIENTED PROGRAMING

#WHAT IS AN OBJECT>
#WHAT IS AN A CLASS

#HOW TO CREATE A CLASS?

class Dog:
    def __init__(self, name, color, breed, age):
       print('creating object')
       self.name = name
       self.color = color
       self.breed = breed
       self.age = age
       


       pass

#how to created metod of the class:
    def bark(self):
        print(f'{self.name} is barking ')


    def walk(self,meters):
        print(f'{self.name} is walking {meters} meters')


    def birthday(self):
        self.age += 1
        return self
    
    def rename(self, name):
        self.name = name
        return name
    

# #instance (or object) of class Dog in craered:
# sheloter_dog = Dog()

# #creating attribute to the instance
# sheloter_dog.color = 'Black'
# print(sheloter_dog.color)

# pitbull = Dog()
# print(pitbull.color)



#cresating the inistance of dog after creating the __unit__() method:
# sheloter_dog = Dog('Rex', 'black','shelter', 5)
# print(sheloter_dog.__dict__)




#create two object (instancees) of the class Dog:


shpitz_dog = Dog('Kuki', 'Brown', 'Shpitz', 3)
print(shpitz_dog.__dict__)
shpitz_dog.birthday()  #----- change birthday 3 --> 4
print(shpitz_dog.__dict__)

maltipu_dog = Dog('Mia','White','Maltipu',2)
maltipu_dog.rename('Toy')    # ---- rename
print(maltipu_dog.__dict__)   # print all


#IF YOU WANT TO PRINT ALL OBJECT !!!!!!!!!!!!!!!!!!!!!!!!!!
# my_dog_objects = [obj for obj in globals().values() if isinstance(obj, Dog)]
# IF YOU WANT TO PRINT ALL OBJECT !!!!!!!!!!!!!!!!!!!!!!!!!!

# shpitz_dog.bark()
# maltipu_dog.bark()


# my_dog = [maltipu_dog, shpitz_dog]

# for dog in my_dog:
#     dog.bark()


# for dog in my_dog:
#     dog.walk(500)





    #EXERCISE: create is method called walk()

