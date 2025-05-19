#LOOPS: FOR AND WHILE LOOPS

# FOR LOOP:

# fruits = ['apple', 'banana', 'kiwi', 'pear']

# for each_fruit in fruits:
#     print(f'I love {each_fruit}')

# for i in range(1,11):
#     print(i)

# for i in range(len(fruits)+1):
#     print(i)

odd_nums = list(range(1, 11, 2))
print(min(odd_nums))
print(max(odd_nums))
print(sum(odd_nums))

# While loop: condition

num = 0
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

secret_num = 77
user_num = input('try a number')

while int(user_num) != secret_num:
    user_num = input('try a number')
    if user_num == 'q':
        print('exiting the game...')
        break
    print('Not the number, Try again or type`q` to quit')       
else:
    print('Congrats you won!')


    
