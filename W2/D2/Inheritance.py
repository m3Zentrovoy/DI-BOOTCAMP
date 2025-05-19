# class Parent:



#     def speack(self):
#             print(f'Parent is speacking')

# class Child(Parent):
#           pass


# class Grandchaild(Child):
#        pass

# obj1 = Child()
# obj1.speack()

# obj2 = Grandchaild()
# obj2.speack()


class Animal:
    def __init__(self, name, family, legs):
            self.name = name
            self.family = family
            self.legs = legs
            self.full_name = f'{name} {family}'

class Dog(Animal):

    def __init__(self, name, family, legs, trained, age):
            ### в супер аргументы из parents class
            super().__init__(name, family, legs)
            self.trained = trained
            self.age = age


    def bark(self):
        print(f' A {self.name} is barking')

    def sleep(self):
        return f'{self.name} is sleeping '

class Cat(Animal):
    def __init__(self, name, family, legs, friendly, nick_name):
       ### в супер аргументы из parents class
       super().__init__(name, family, legs,)
       self.friendly = friendly
       self.nick_name = nick_name


    def get_crazy(self):
          print(f'{self.name} is running with {self.legs} legs in full puwer ')




class Alien:
    def __init__(self, personal_name, planet):
            self.personal_name = personal_name
            self.planet = planet
    
    def fly(self):
        return f'{self.name} is flying around'

    def sleep(self):
        return f'{self.name} is sleeping from the Alien class'

    def make_sound(self):
        return f'{self.name} is make_sound '

class Alien_Dog(Dog,Alien):
    def __init__(self, name, family, legs, personal_name, planet):
        Dog.__init__(self, name, family, legs)
        Alien.__init__(self, personal_name, planet)
lion = Animal('Lion','Felidae', 4)
print(lion.__dict__)

dog_1 = Dog('Dog', 'Canidae', 4, 'True', 2)
dog_1.bark()

cat1 = Cat('Cat', 'Lion', 4, 'just friendly','murk')
cat1.get_crazy()


aliendog1 = Alien_Dog('Dog', 'Canodae', 4, 'Rexi','Saturn')
print(aliendog1.name, aliendog1.family, aliendog1.planet, aliendog1.name)
print(aliendog1.sleep())

#if you want call the ,ethod in some specific parent class 
# ( nit by order of inhertance) we can do:
print(Dog.sleep(aliendog1))



#add two other atributes specific;y to the dog class: trained (boolean), age (int)
#use the super().__init__() to do so
#create an instance of Dog afetr that and analyse what change






    