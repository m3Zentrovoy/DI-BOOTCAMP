#sequnces colectios in python
#organaizing, storing, retriving(извлечение) data

#lists
# Use cases: to store and organize data can be changed, ordered by index.
# The most "flexible" collections

#creating list  = [] squared brackets
#method
#append()
#extend()
#remove()
#pop()
#sort()
# methods rhat created a new list
#sorted()
#split()

# task = input('enter a task separated by coma: ')
# task_list = task.split(', ')
# print(task_list)


# list_1 =[1,2,3,3,4,5]
# list_2 = [6,7,8,9,]
# list_3 = [*list_1,*list_2]

# print(list_3)




#TUPLES

#use cases
#useful if you want to store information that shouldn't ve be changed:
#password list,.adresses,id_numbers.

x, y = (4,6) #unpucking a tuple
cordinate  = (4,6)
print(cordinate[1])

adresses =('Holon' , 'Bat-Yam','Holon')
print(adresses.count('Holon'))

#SETS
#Use cases: useful for data that you don't want to duplicated. Ids, 

#finding common elements between different colections
fruits = {'apple', 'banana','pineapple'}
vegetebles = {'brocoli','carrot', 'potato', 'tomato'}

