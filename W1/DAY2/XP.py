
#ex 1

# my_fav_numbers = [42,67,95]
# my_fav_numbers.extend([35,36])
# my_fav_numbers.pop()

# friend_fav_numbers = [1,2,3,4,5]
# our_fav_numbers = [my_fav_numbers + friend_fav_numbers]


#ex2


# my_tuple = tuple(range(7))
# temp_list = list(my_tuple)
# temp_list.extend([8,9,10])
# my_tuple = tuple(temp_list)
# print(my_tuple)

#ex3


# # You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# # Remove "Banana" from the list.
# basket.remove('Banana')

# # Remove "Blueberries" from the list.
# basket.remove('Blueberries')

# # Add "Kiwi" to the end of the list.
# basket.append('Kiwi')

# # Add "Apples" to the beginning of the list.
# basket.insert(0,'Apples')

# # Count how many times "Apples" appear in the list.
# basket.count('Apples')

# # Empty the list.
# basket.clear()

# # Print the final state of the list.
# print(basket)


#ex4

# numbers = 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5

# Recap: What is a float? What’s the difference between a float and an integer?
# An integer is a whole number (10, -5, 0),
# Floats usually have a decimal point and represent numbers with fractional parts (3.14, -0.5, 2.0).

# numbers = []
# current = 1.5 #start num
# while current <= 5.0: #finish
#     numbers.append(current)
#     current += 0.5 #step
# print(numbers)



# ex5

# for i in range(1,21):
#     print(i)

# for i in range(1,21,2):
#     print(i)

    
#ex6

# active = True
# while active:

#     user_name = input('Write your name>> ') 
# # if user input my name 
#     if user_name == 'max':
#         active = False
#         print("okay,hello max! ")
# # if user input my name  this big M
#     elif user_name == 'Max':
#         active = False
#         print("okay,hello Max! ")
#     else:
#         print('Nice to meet you! ')


#ex7

# fruits = input("Write you favotite fruits>> ")

# user_fruits = fruits.split()

# fruit = input ('And whats you favorite fruit? ')

# if fruit in user_fruits:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy it!')



#ex8

# topping_list = []
# price = 10

# active = True
# while active:
    
#     toppings = input('Write you toppings for pizza>> ')
#     if toppings != 'quit':
#         topping_list.append(toppings)
#         price += 2.5
#         print(f"Adding {toppings} to your pizza.")
#     else:
#         active = False
#         print("Toppings:", topping_list)
#         print("Total price:", price)


#ex9 

# Представьте себе группу подростков, желающих посмотреть фильм с ограниченным доступом (только для лиц в возрасте от 16 до 21 года).
# Напишите программу для:
# Спросите возраст каждого человека.
# Удалите всех, кому не разрешено смотреть.
# Распечатайте окончательный список участников.

# active = True

# price =[]
# while active:
#     age = input("Write age for everyone frome you family. (enter 'quit'  when you are finished) >> ")

#     if age == 'quit':
#         active = False
#     if age != 'quit':
#          age = int(age)

#          if age < 3:
#              print('The ticket is free')
#              price.append(0)
#          elif 3 < age < 12:
#              price.append(10)
#              print('The ticket is 10$' )
#          elif age > 12:
#              price.append(15)
#              print('The ticket is 15$')
          
# print("Total cost:", sum(price), "$")



#ex10

# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

# finished_sandwiches = []

# while "Pastrami" in sandwich_orders:
#     x = sandwich_orders.index("Pastrami")
#     del sandwich_orders[x]

# for name in sandwich_orders:
#     finished_sandwiches.append(name)
#     print(f"I made your {name} sandwich.")

# print("Final list of sandwiches:\n" + '\n'.join(finished_sandwiches))