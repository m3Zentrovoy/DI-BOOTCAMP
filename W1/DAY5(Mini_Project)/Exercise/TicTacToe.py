
# # Шаг 1: Представление игрового поля
# field = [['▢' for _ in range(3)] for _ in range(3)]

# # Шаг 2: Отображение игрового поля
# def display_board(field):
#     for row_idx, row in enumerate(field):
#         for col_idx, cell in enumerate(row):
#             number = row_idx * 3 + col_idx + 1
#             if cell == '▢':
#                 print(number, end=" ")
#             else:
#                 print(cell, end=" ")
#         print()

# # Шаг 3: Получение ввода игрока
# def player_input(player, field):
#     while True:
#         try:
#             number = int(input(f"Player {player}, enter cell number (1-9): "))
#             if number < 1 or number > 9:
#                 print('Please enter a number between 1 and 9.')
#                 continue
#             row = (number - 1) // 3
#             col = (number - 1) % 3
#             if field[row][col] != '▢':
#                 print('Cell is already taken!')
#                 continue
#             return (row, col)
#         except ValueError:
#             print('Please enter a valid number!')

# # Шаг 4: Проверка победы
# def check_win(board, player):
#     # Проверка строк
#     for i in range(3):
#         if all(board[i][j] == player for j in range(3)):
#             return True
    
#     # Проверка столбцов
#     for i in range(3):
#         if all(board[j][i] == player for j in range(3)):
#             return True
    
#     # Проверка главной диагонали
#     if all(board[i][i] == player for i in range(3)):
#         return True
    
#     # Проверка побочной диагонали
#     if all(board[i][2-i] == player for i in range(3)):
#         return True
    
#     return False

# # Шаг 5: Проверка ничьей
# def check_tie(board):
#     return not any('▢' in row for row in board)

# # Шаг 6: Основной игровой цикл
# def play():
#     board = [['▢' for _ in range(3)] for _ in range(3)]
#     current_player = 'X'
    
#     while True:
#         display_board(board)
#         row, col = player_input(current_player, board)
#         board[row][col] = current_player
        
#         if check_win(board, current_player):
#             display_board(board)
#             print(f"Player {current_player} wins!")
#             break
        
#         if check_tie(board):
#             display_board(board)
#             print("It's a tie!")
#             break
        
#         current_player = 'O' if current_player == 'X' else 'X'

# # Запускаем игру
# play()



board_size = 3
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    '''view draw board'''
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' '* 3 + '|')* 3)
        print('', board[i*3], '|' , board[1 + i*3], '|', board[2 + i*3], '|')
        # print('_' * 4 * board_size)
        print(('_'* 3 + '|')* 3)
    
    pass
def game_step(index,char):
    if (index > 9 or index < 1):
  
    pass
def check_win():
    pass

def start_game():
    current_player = 'X'
    step = 1
    draw_board()

    while (step < 10) and check_win() == False:
        index = input('Step plyer')

                      
print("Welcome to TTT")
start_game()