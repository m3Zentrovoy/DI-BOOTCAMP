# #ex1 

# # Создаём пустой список
# item_list = []

# # Функция для вставки элемента
# def insert_item():
#     item = input("Введите элемент: ")  # Запрашиваем элемент
#     index = int(input("Введите индекс: "))  # Запрашиваем индекс
#     item_list.insert(index, item)  # Вставляем элемент в список
#     print("Список:", item_list)  # Показываем результат

# # Вызываем функцию
# insert_item()


#ex2


# user_input = input("Введите что-нибудь: ")
# print(user_input.count(' '))


#ex3


# counter_sup = 0
# counter_low = 0
# user_input = input("Введите что-нибудь: ")

# for char in user_input:
#     if char.isupper():
#         counter_sup += 1
#     elif char.islower():
#         counter_low += 1

# print(f'number of upper - {counter_sup} and number of lower - {counter_low}')

#ex4

# numbers = ([1,5,4,2])

# def fund_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
    
    
# result = fund_sum(numbers)
# print('Sum' ,result)


#ex5

# numbers = ([0,1,3,50,100])
# box = [numbers[0]]
# def find_max(numbers):
#     for num in numbers:
#         if num > box[0]:
#             box[0] = num
#     return box[0]
        


# result = (find_max(numbers))
# print("Max:" , result)


#ex6

# n = int(input("Write your number "))

# def factorial(n):
#     if n < 0:
#       print('not defined for negative numbers, write num > 0')

#     elif n == 0 or n == 1:
#       return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
    
# factorial(7)
# print(factorial(n))


#ex7


# user_list = input('Write you list (separeted space) ').split()

# item = input('Write element for search ')

# def count_lst(lst,element):
#     count = 0
#     for element in lst:
#         if item == element:
#             count += 1

#     return count

# print(count_lst(user_list, item))


#ex8