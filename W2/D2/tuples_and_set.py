# Tuples: immutable, there is no notion of an empty tuple

# my_tuple = ('TLV',)
# print(type(my_tuple))

#convert some other sequence into a tuple
# my_tuple = tuple(range(11))
# print(my_tuple)

# passwords = ('abc', 'cde', '123', 'abc')
# print(passwords.count('abc'))

# #accessing by index
# print(passwords[1])

# #workaround on how to change tuples:
# temp_list = list(my_tuple)
# temp_list.insert(8, 'A')
# my_tuple = tuple(temp_list)
# print(my_tuple)

# my_tuple += ('A', 'B', 'C')
# print(my_tuple)

#SETS: 
# not ordered: not possible to access by index
# don't allow duplicated elements

set = set()

countries = {'Israel', 'USA', 'Brazil'}
names = {'Shimon', 'Hanna', 'Israel'}

# print(countries[1]) # TypeError: 'set' object is not subscriptable

person_country = countries.intersection(names)
print(person_country)