# 🌟 Exercise 1: Converting Lists into Dictionaries

# You are given two lists. 

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# # Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
# for item in zip(keys,values):
#     print(item)


# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# 🌟 Exercise 2: Cinemax #2


# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15




# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# price = []
# for name, age in family.items():
    
#     if age < 3:
#         price.append(0)
#         print(f'Ticket for {name}, cost free')  
#     elif 3 < age < 12:
#         price.append(10)
#         print(f'Ticket for {name}, cost 10$')
#     elif age > 12:
#         price.append(15)
#         print(f'Ticket for {name}, cost 15$')
# else:
#     print(f'total cost is {sum(price)}$')

# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.




# # 🌟 Exercise 3: Zara

# # Create and manipulate a dictionary that contains information about the Zara brand.


# # Create a dictionary called brand with the provided data.
# brand = {
# 'name': 'Zara',
# 'creation_date' : 1975,
# 'creator_name' : "Amancio Ortega Gaona",
# 'type_of_clothes' : ['men', 'women', 'children', 'home'],
# 'international_competitors': ['Gap', 'H&M', 'Benetton'],
# 'number_stores': 7000,
# 'major_color':{

#     'France': 'blue', 
#     'Spain': 'red', 
#     'US': ['pink', 'green']

# }}



# # Change the value of number_stores to 2.
# brand['number_stores'] = 2

# # Print a sentence describing Zara’s clients using the type_of_clothes key.
# clients = ', '.join(brand['type_of_clothes'])
# print(f"Cliens Zara is {clients}")

# # Add a new key country_creation with the value Spain.
# brand['country_creation'] = 'Spain'

# # Check if international_competitors exists and, if so, add “Desigual” to the list.
# if 'international_competitors' in brand:
#     brand['international_competitors'] = 'Desigual'
# else:
#     pass

# # Delete the creation_date key.
# del brand['creation_date']

# # Print the last item in international_competitors.
# print(brand['international_competitors'])

# # Print the major colors in the US.
# print(brand['major_color']['US'])

# # Print the number of keys in the dictionary.
# print(len(brand.keys()))

# # Print all keys of the dictionary.
# keys = ', '.join(brand.keys())
# print(f"All keys of the dictionary is '{keys}'")


# # Bonus:

# more_on_zara = {

#     'сreation_date' : 1974,
#     'number_stores' : 2007
# }

# brand.update(more_on_zara)
# print(brand)





# 🌟 Exercise 4: Disney Characters

# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:


# 1.
# dictonary = {}
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# for char in users:
#     dictonary[char] = users.index(char)
# print(dictonary)

# 2.
# dictonary = {}
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# for index, name in enumerate(users):
#     dictonary[index] = name

# print(dictonary)

# 3.
# dictonary = {}
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# for name, index in enumerate(sorted(users)):
#     dictonary[index] = name

# print(dictonary)

