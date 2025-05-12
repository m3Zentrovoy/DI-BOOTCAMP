# # LISTS ordered sequence

# #LIST is a qequence of element

# some_list = list('item 1') # to conbert other sequnce in a list
# other_list = ['item 1'] # the best way to create emty list

# print(some_list)
# print(other_list)

# print(len(some_list))

# print(some_list[1])

# my_list = []

#method for list
# my_list.append('A')
# print(my_list)

# my_list.extend(['B', 'C', 'D'])
# print(my_list)


# create an empty list called names and add (using a method) names of your favorite character of some show


# names_of_manga = []
# names_of_manga.extend(['Naruto', 'Aang','Shaman'])
# print(names_of_manga)


# my_list = (list(range(1,8)))
# print(my_list)


# print(my_list[2:6])
# copied_list = my_list[:]
# print(copied_list)

# copied_list = my_list.copy()
# print(copied_list)

#other = methods
# insert (where, what)
#remove (what) removes the first occurience of the element
#deliting some elements:
# del my_list[3]
# print(my_list)


#pop() by defoult delites the last element
# my_list.pop()   ????????????????????????????????????????????????????????????????????????????????
# print(my_list)   ?????????????????????????????????????????????????????????????????????????????



# fruits = ['banana','apple', 'lime']
#sorted()
# sorted_fruits= sorted(fruits)
# print(fruits)

#sort()

# fruits.sort()
# print(fruits)

#index(elemenmt) and it return you of this element




list1 = [5, 10, 15, 20, 25, 50, 20]

# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
# Hint : Look at the index method

if 20 in list1:
    index_found = list1.index(20)
    list1.insert(index_found,200)
    list1.remove(20)
    print(list1)
else:
    print('element not found')