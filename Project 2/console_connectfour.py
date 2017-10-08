from connectfour import *

def print_new_board(a):
    for row in range(0, 6):
        for col in range(0, 7):
            print(a.board[row][col], end = '  ')
        print('\n')
    print("Input slot for Player", a.turn, " :")
        

gs = new_game()
print_new_board(gs)

user_input = int(input('Enter a column: '))

while True:
    g_state = drop(gs, user_input)
    print_new_board(g_state)
    break
