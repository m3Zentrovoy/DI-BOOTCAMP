#ex1

# def display_message():
#     print("I am learning about functions in Python.")

# display_message()

#ex2


# def favorite_book(title):
#     print(f'One of my favorite books is {title}')

# favorite_book('Harry Potter')


#ex3

# def describe_city(city, country = 'Unknown'):
#     print(f'{city} is in {country}')

# describe_city('Spb', 'Russia')
# describe_city('Tel-Aviv')


 #ex4

# import random

# def f(number):
#     number =input('Write you number, and we are compare ')
#     random_number = random.randint(1, 100)
#     if number == random_number:
#         print('Success! (if the numbers match)')
#     else:
#         print(f'Fail! Your number:{number}, Random number: {random_number} (if they dont match)')

# f(1)


#ex5

# def make_shirt(size ='large',text = 'I love Python'):
#     print(f'The size of the shirt is {size} and the text is {text}.')

# make_shirt()
# make_shirt('medium')
# make_shirt('small','i have alrady done this code')


#ex6

# magician_names =['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians(magician_names):
#     for name in magician_names:
#         print(name)

# def make_great(magician_names):
#     for i in range(len(magician_names)):
#       magician_names[i] = magician_names[i] + ' the Great'

# make_great(magician_names)
# show_magicians(magician_names)


# #ex7
# import random

# def get_random_temp():
#     temp = random.randint(-10, 40)
#     return temp

# def main():
#     temp = get_random_temp()  
#     print(f'The temperature right now is {temp} degrees Celsius.')
#     if temp < 0:
#         print('Brrr, thats freezing! Wear some extra layers today.')
#     elif 0 <= temp < 16: 
#         print('Quite chilly! Dont forget your coat.')
#     elif 16 <= temp < 23:
#         print('Nice weather.')
#     elif 24 <= temp < 32:
#         print('A bit warm, stay hydrated.')
#     else:
#         print('Its really hot! Stay cool')

# main()  