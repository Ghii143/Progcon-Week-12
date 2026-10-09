import random
random.seed()   #Prepare random number generator

board = [""] * (10)

for i in range(1, 9 + 1, 1):
    board[i] = " "
gameOver = False
winner = "None"
r = int(random.random() * 2)
if r == 0:
    currentPlayer = "O"
else:
    currentPlayer = "X"
while gameOver == False:
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(board[7] + " | " + board[8] + " | " + board[9])
    if currentPlayer == "O":
        while "validMove == False":
            print("Enter your move (1-9): ")
            move = int(input())
            if move >= 1 and move <= 9:
                if board[move] == " ":
                    validMove = True
                else:
                    print("Cell occupied! Try again.")
                    validMove = False
            else:
                print("Invalid position! Please enter a number from 1 to 9.")
                validMove = False
    else:
        validMove = False
        print("Computer ('X') is making a move...")
        while validMove == False:
            move = int(random.random() * 9) + 1
            if board[move] == " ":
                validMove = True
            else:
                validMove = False
    board[move] = currentPlayer
    if board[1] != " " and board[1] == board[2] and board[2] == board[3] or board[4] != " " and board[4] == board[5] and board[5] == board[6] or board[7] != " " and board[7] == board[8] and board[8] == board[9] or board[1] != " " and board[1] == board[4] and board[4] == board[7] or board[2] != " " and board[2] == board[5] and board[5] == board[8] or board[3] != " " and board[3] == board[6] and board[6] == board[9] or board[1] != " " and board[1] == board[5] and board[5] == board[9] or board[3] != " " and board[3] == board[5] and board[5] == board[7]:
        winner = currentPlayer
        gameOver = True
    else:
        if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
            winner = "Draw"
            gameOver = True
        else:
            if currentPlayer == "O":
                currentPlayer = "X"
            else:
                currentPlayer = "O"
print(board[1] + " | " + board[2] + " | " + board[3])
print("---+---+---")
print(board[4] + " | " + board[5] + " | " + board[6])
print("---+---+---")
print(board[7] + " | " + board[8] + " | " + board[9])
if winner == "O":
    print("Congratulations! You (O) win!")
else:
    if winner == "X":
        print("Game Over! Computer (X) wins!")
    else:
        print("It's a draw!")
