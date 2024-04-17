# Project 8 = 'Tic Tac Toe game'

print('Welcome to the Tic Tac Toe game......')
# import random
Current_player ="X"
Game_Running = True
Winner = None

board = ["_","_","_",
        "_","_","_",
        "_","_","_"]

# printing the board
def printed_board(board):
    print(board[ 0 ] + " | " + board[1] + " | " + board[2])
    print('----------')
    print(board[ 3] + " | " + board[4] + " | " + board[5])
    print('----------')
    print(board[ 6 ] + " | " + board[7] + " | " + board[8])
    

# Taking player input

def player_input(board):
    
    user = int(input('Enter the number from 1 to 9:'))
    if user>=1 and user<=9 and board[user-1]=="_":
         board[user-1] = Current_player
    else:
         print('Player is already in that spot..')

# Checking the winning side
def check_horizontal(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0]!="_":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!="_":
        Winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!="_":
        Winner = board[6]
        return True
    

def check_vertical(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0]!="_":
        Winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!="_":
        Winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!="_":
        Winner = board[2]
        return True

def check_diagonal(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0]!="_":
        Winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!="_":
        Winner = board[2]
        return True

def game_tie(board):
    if"_" not in board:
        printed_board(board)
        print('Game is a Tie!')
        return False
    
# Switch the player
def switch_player(board):
    global Current_player
    if Current_player ==  "X":
        Current_player = 'O'
    else:
        Current_player ="X"

def Check_Win(board):
    if check_horizontal(board) or check_diagonal(board) or check_vertical(board):
        print(f'The winner is {Winner}')

# def Computer(board):
#     if Current_player == 'O':
#         position = random.randint(0,8)
#         if board[position]=="_":
#             board[position ]='O'
#             switch_player()





while Game_Running:
    printed_board(board)
    player_input(board)
    Check_Win(board)
    game_tie(board)
    switch_player(board)
    # Computer(board)
    # Check_Win(board)
    # game_tie(board)
    

    