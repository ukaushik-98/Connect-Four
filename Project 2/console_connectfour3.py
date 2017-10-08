from connectfour import *

def game():
    gs = new_game()
    board = gs.board
    
    for i in range(6):
        for j in range(7):
            print(board[j][i], end = '\t')
        print('\n')
        break
        
game()
 
