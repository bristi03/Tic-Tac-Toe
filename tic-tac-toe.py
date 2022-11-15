import random

def printBoard(board):
    print(board[0],"|",board[1],"|",board[2])
    print("----------")
    print(board[3],"|",board[4],"|",board[5])
    print("----------")
    print(board[6],"|",board[7],"|",board[8])
def playerInput(board):
    pos=int(input("Enter the position (1-9):"))
    if pos>=1 and pos <= 9 and board[pos-1]=="-":
        board[pos-1]=player
    else:
        print("Choose a different position!!")
        playerInput(board)
def win(board):
    wins=[[0,1,2],[3,4,5],[6,7,8],[1,4,7],[0,3,6],[2,5,8],[0,4,8],[2,4,6]]
    for i in wins:
        if board[i[0]]==board[i[1]] and board[i[1]]==board[i[2]] and board[i[0]]!="-":
            winner=board[i[0]]
            print(winner,"wins!!")
            return True
    if "-" not in board:
        print("Tie")
        return True

def computer(board):
    global player
    while player == "O":
        pos= random.randint(1,9)
        if board[pos-1]=="-":
            board[pos-1]=player
            swap()
            #player="X"

def swap():
    global player
    if player=="X":
        player="O"
    else:
        player="X"

board=['-','-','-','-','-','-','-','-','-']
winner= None
player="X"
run= True
printBoard(board)
while run:
    print(player,"'s turn")
    playerInput(board)
    printBoard(board)
    print("-------------------------")
    if win(board)==True:
        break
    swap()
    #if player=="X":
    #    player="O"
    print(player,"'s turn")
    computer(board)
    printBoard(board)
    print("-------------------------")