# #ex1
# list1 = [1,2,3]
# list2 = [4,5,6]
# for i in list2:
#     list1.append(i)

# print(list1)

#ex2


# for num in range(1500,2501):
#     if num % 5 == 0 and num % 7 == 0:
#         print(num)
        
#ex3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Write your name: ")

found = False

for i, name in enumerate(names):
    if user_name == name:      
        print(f"Nice to meet you {user_name}({[i]}) ")
        found = True

if not found:
    print("Try to write again")


#Ex4

