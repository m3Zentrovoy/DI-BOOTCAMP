
# #try to except block

# hello = "Hello World

# if hello == "Hello World":
#     print('Thats right')

# board = [['▢' for _ in range(3)] for _ in range(3)]


# def player_input(current_player):
#     valid = False
#     while not valid:
#         position = input('Enter the position 1-9:')
#         try:
#             position = int(position) - 1
#             if 0 <= position < 9 and board[position-1] == '_':
#                 board[position] = current_player
#                 print(board)
#                 valid = True
#             else:
#                 print('position not in range 1-9')

#         except:
#             print('Please enter a number')
#             continue
# player_input('X')





# my_list = [1,3,5,6.9,7,8,9,'number']
# try:
    # print('from try block'sum(my_list))

# except:
#     clean_list = []
#     for element in my_list:
#         if isinstance(element,int):
#             clean_list.append(element)
#             output = sum(clean_list)
#             print(f'from except block: {output}')

#     # raise TypeError("There are strings on the list")