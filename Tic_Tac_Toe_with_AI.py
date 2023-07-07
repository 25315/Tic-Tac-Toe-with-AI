 count = 0       # variable to count the nubmer of chances the computer has done used to calculate the number of leaf nodes
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):    # function to chk whether there is space or not at a given position
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

def checkForWin():           # function to check for win
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):      # function to check which mark 'O' or 'X' can win
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return


def compMove():   
    bestScore = -100
    bestMove = 0
    global count 
    count = count + 1
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False,-100,100)       
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

# there is nothing such that the bestScore should be taken as -100 only it can be any number, code is working properly with it
def minimax(board, depth, isMaximizing,alpha,beta):
    d.append(depth)
    global leaf
    if (checkWhichMarkWon(bot)):
        if count == 1:       # count = 1 because, leaf nodes are calculating in the first chance of computer when it form the tree
            leaf = leaf + 1
        return 1
    elif (checkWhichMarkWon(player)):
        if count == 1:    # count = 1 because, leaf nodes are calculating in the first chance of computer when it form the tree
            leaf = leaf + 1
        return -1
    elif (checkDraw()):
        if count == 1:   # count = 1 because, leaf nodes are calculating in the first chance of computer when it form the tree
            leaf = leaf + 1
        return 0
    
    if (isMaximizing):
        bestScore = -100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False,alpha,beta)      # recursive call of the minimax function
                board[key] = ' '
                bestScore = max(bestScore,score)
                alpha = max(alpha,bestScore)
                if alpha >= beta :                           # alpha-beta pruning condition
                    break
        return bestScore

    else:
        bestScore = 100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True,alpha,beta)        # recursive call of the minimax function
                board[key] = ' '
                bestScore = min(bestScore,score)
                beta = min(beta,bestScore)
                if alpha >= beta:                       # alpha-beta pruning condition
                    break
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)                              # printing the empty board
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = False

while not checkForWin() and not checkDraw():   # loop to call the chance of the AI and ours
    playerMove()
    if(checkForWin() == 0 and checkDraw() == 0):
        compMove()
