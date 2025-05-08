#exercise 1

numbers = [1,2,3,4]
list = [x for x in numbers]
print(list)

#exercise 2

numbers = [1,2,3,4]
b = [num * 20 for num in numbers]
print(b)

#exercise 3

names = ["Elie", "Tim", "Matt"]
first_letters = [n[0] for n in names]
print(first_letters)

#exercise 4

list = [1,2,3,4,5,6]
list_2  = [num for num in list if num % 2 == 0]
print(list_2)


#exercise 5

l1 = [1,2,3,4]
l2 = [3,4,5,6]
l3 = [num for num in l1 if num in l2]
print(l3)

#exercise 6

list = ["Elie", "Tim", "Matt"]
rev_list = [word[::-1].lower() for word in list]
print(rev_list)

#exercise 7

q = "first"
w = "third"
e = [str for str in q if str in w]
print(e)

#exercise 8

list = range(1,101)
list2 = [num for num in list if num % 12 == 0]
print(list2)

#exercise 9

s = "amazing"
l = [str for str in s if str not in "aeiou"]
print(l)

# exercise 10

q = [0,1,2]
w = [q for num in range(3)]
print(w)

# exercise 11

qq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ww = [qq for num in range(10)]
print(ww)