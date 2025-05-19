#LISTS: ordered sequence

#A list is a sequence of elements

#Syntax
some_list = list('item 1') #to convert other sequence in a list
other_list = ['item 1'] # the best way to create an empty list

print(some_list)
print(other_list)

print(len(some_list))

#accessing by index
print(some_list[1])

my_list = []

#methods for lists
my_list.append('A')
print(my_list)

my_list.extend(['B', 'C', 'D'])
print(my_list)

#create an empty list called names and add (using a method) 4 names of your favorite character 
# of some show

names = []
names.extend(['Harry', 'Hermione', 'Ron', 'Giny'])

print(names)

nums_list = list(range(1,8))
print(nums_list)

print(nums_list[2:6])
print(nums_list[:5])
copied_list = nums_list[:]
print(copied_list)
copied_list = nums_list.copy()
print(copied_list)
print(id(nums_list))
print(id(copied_list))

# copied_list = nums_list
# name = 'Juliana'
# new_name = name
# print(id(name))
# print(id(new_name))

#other methods
# insert(where, what)
#remove(what) removes the first occurence of the element
#deleting some element:
# del nums_list[3]
# print(nums_list)

# nums_list.pop()
# print(nums_list)

# poped_el = nums_list.pop()
# print(poped_el)
# print(nums_list)

print(nums_list)

fruits = ['banana', 'orange', 'lime','apple']
#sorted()
# sorted(fruits)
# print(fruits)

#sort()
fruits.sort()
print(fruits)

#index(element) and it return you the index of this element

# EXERCISE
# Given this list:
list1 = [20, 5, 10, 15, 20, 25, 50, 20]
# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
# Hint : Look at the index method

if 20 in list1:
    index_found = list1.index(20)
    list1.insert(index_found, 200)
    list1.remove(20)
    print(list1)
else:
    print('element not found')


