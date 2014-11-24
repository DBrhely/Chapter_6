#Challenge 4
#11/21/14
#Danielle Brhely
#
#Design
#
#use the function to create the computer strategy
#create the program so the computer is to be unbeatable
#######################################

#Function
def computer_move(board, computer, human):
    Moves = (5, 8, 0, 4, 3, 7, 1, 2, 6)
    board = move[:]

    print("Your'll never beat me.")

    for move in legal_move(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_move(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in Moves:
        if move in legal_moves(board):
            print(move)
            return move










        
