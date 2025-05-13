# shoping_list = ['milk', 'eggs', 'bread']
# shoping_list.append("butter")
# shoping_list.remove("eggs")
# shoping_list[0]

# student = {
#     "name" : "John",
#     "age" : 20,
#     "major" : "Computer Sciense"
# }

# print(student["major"])


# a_dictonary = {'color','blue','fruit', 'apple', 'pet', 'dog'}

# for key, value in _dict.items():
#     print(key, '->' value) 





#EXERCISE 
# Access the value of key history


# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# # print(sample_dict["class"]["student"]["marks"]["history"])
# x = sample_dict.get("history")
# print(x)




# Built-in methods

# keys() method returns a dict_keys of all the keys in my_dict
# values() method returns a dict_values of all the values in my_dict
# items() returns a dict_items of tuples containing the key-value pairs in a dictionary.

# my_dict = {
#     "KEY1" : "VALUE1",
#     "KEY2" : "VALUE2",
#     "KEY3": "VALUE3"
# }
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())




#EXERCISE

# Delete set of keys from Python Dictionary

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# del sample_dict["name"]
# del sample_dict["salary"]
# # keys_to_remove = ["name", "salary"]
# print(sample_dict)






# I. For Loops


# A. For Loops and dictionaries
# We can iterate over both the keys and the values of a dictionary.

# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }

# for x, y in my_books.items():
#     print("the" + x + "is" + y)

# numbers = [1,2,3,4,5,6,7]
# search = 9

# for num in numbers:
#     if num == search:
#        print(f"Where is it{search}")
#        break
# else:
#     print("Dont found ")







# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict_up = {
#   "year2": 1964
# }

# thisdict.update(thisdict_up)

# print(thisdict)

















user_a = {
    'first_name': 'Bob',
    'last_name': 'Ross', #STOP HERE, EXPLAIN
    'age': 53, #EXPLAIN DATA TYPES AS VALUES
    'address': 'Tel Aviv', #STOP HERE EXPLAIN ACESSING DATA
    'hobbies': ['painting', 'guitar'], #STOP HERE EXPLAIN DATA TYPES: DICTS AND LISTS
    'pets': [('Rufus', 9), ('Garfield', 8)], #EXPLAIN LIST OF OTHER DATA TYPES (EX.:TUPPLES)
    'family': {'partner':{
        'first_name': 'Lior', 
        'last_name': 'Alon', 
        'age': 50
        },
        'children':{
        'first_name': 'Anna', 
        'last_name': 'Ross', 
        'age': 15,
        'sports': ['volleyball', 'soccer']
        },
    }
}

user_a['first_name_2'] = user_a.pop('first_name')

print(user_a)

print(user_a['first_name'])
print(user_a['hobbies'][1])
print(user_a['pets'][2][0])


for pet in user_a['pets']:
    print(pet[0])

print(user_a['family']['partner']['last_name'])
print(user_a['family']['children']['sports'][0])
print(user_a['family'])



print('first_name' in user_a)
print('Rufus' in user_a.values())
print(53 == user_a['age'])

print('keys: ', user_a.keys())
print('values: ', user_a.values())

print(user_a.items())

print(user_a['family']['partner']['first_name'])
print(user_a['family']['children']['sports'][0])


shirts = [                  #A list of dicts
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]

# 4 Modufy An Entry In A Dict
# setting new value for a key
user_a['first_name'] = 'John'
print('changed first name: ', user_a)

# 5. Adding An Entry To An Existing Dictionary
user_a['email'] = 'bob@gmail.com'
print('email added: ', user_a)

# 6. Delete An Entry In A Dictionary

# Deleting (without removal) values by key - 'del' keyword
del user_a['last_name']
print('deleted last name: ', user_a)

# Popping values by key
name_removed = user_a.pop('first_name')

print(user_a)
print("Name removed:",name_removed)

# The IN keyword
print('Tel Aviv' in user_a.values())
print('Tel Aviv' == user_a['address'])
print('first_name' in user_a)

shirts = [                  #A list of dicts
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]

for shirt in shirts:
  print(shirt['size'])

# Build-in Methods
print(user_a.items())
for key, value in user_a.items():
   print(f'k: {key} -> v: {value} ')

# dictionary keys
print('keys: ', user_a.keys())
Collapse












