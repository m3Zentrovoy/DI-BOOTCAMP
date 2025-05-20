
import random, string


#ex1

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     #Your code starts HERE


#     def __str__(self):
#       currency_name = self.currency + "s" if self.amount != 1 else self.currency
#       return f'{self.amount} {currency_name}'
    
#     def __int__(self):
#       return int(self.amount)

#     def __repr__(self):
#       return f"{self.amount}, {self.currency}"

    # def __add__(self, other):
    #     if isinstance(other, (int, float)):
    #         return self.amount + other
    #     if not isinstance(other, Currency):
    #         raise TypeError(f"Cannot add Currency with {type(other)}")
    #     if self.currency != other.currency:
    #         raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
    #     return self.amount + other.amount  
    


    # def __iadd__(self, other):
    #     if isinstance(other, (int, float)):
    #         self.amount += other
    #         return self
    #     if not isinstance(other, Currency):
    #         raise TypeError(f"Cannot add Currency with {type(other)}")
    #     if self.currency != other.currency:
    #         raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
    #     self.amount += other.amount
    #     return self


# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)


# print(str(c1))  
# print(int(c1))  
# print(repr(c1))  
# print(c1 + 5)  
# print(c1 + c2)  
# print(c1)  
# c1 += 5
# print(c1)  
# c1 += c2
# print(c1)  
# try:
#     print(c1 + c3) 
# except TypeError as e:
#     print(e)
    


#ex3

# letters = list(string.ascii_lowercase)
# random_letters = random.sample(letters, 5)
# print(', '.join(random_letters))


# #ex4
# from datetime import datetime


# class Person:
#     def __init__(self, name, birth_date):
#         self.name = name
#         self.birth_date = birth_date


#     def current_date(self):
#         current = datetime.now()
#         return current 

# #ex5

#     def difference_date(self):
#         future_date = datetime(2026, 1, 1)
#         current_date = datetime.now()
#         return future_date - current_date

# #ex6

#     @staticmethod
#     def parse_birthdate(birth_date):
#         current =  datetime.now().date()
#         my_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
#         return current - my_date
    


# p1 = Person("Max", "1995-03-09")

# print(p1.current_date())
# print(p1.difference_date())

# print(Person.parse_birthdate("1995-03-09"))



#ex7  

from faker import Faker
fake = Faker()

users_box= []
user = {
    "name":  fake.name(),
    "address": fake.address(),
    "language_code": fake.language_code()
}

def generate_user(num_users):
    for _ in range(num_users):
        users_box.append(user)
 
generate_user(3) 
print(users_box)