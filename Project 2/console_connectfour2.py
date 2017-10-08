from connectfour import *

def print_new_board(a):
    print(a.board)
    for row in range(0, BOARD_ROWS):
        for col in range(0, BOARD_COLUMNS):
            print(a.board[col][row], end= "   ")
        print("end\n")
    print("Input slot for Player", a.turn)

gs = new_game()
print_new_board(gs)

while True:
    try:
        user_input = int(input('Enter a column: '))
        gs = drop(gs, user_input-1)
        print_new_board(gs)
        winner(gs)
    except ValueError:
            print("Not valid integer! Please try again ...")


