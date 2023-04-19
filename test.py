<<<<<<< HEAD

outfile = open('example.txt', 'w')


def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("___|___|___")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("___|___|___")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

=======
wordOccurrences = [('rabbbit',1),('Alice',1),('rabbbit',4),('Alice',7),('Alice',10)]
>>>>>>> 6f71d35894b6e8826f5b971ea584cc5f6c9e0c28

def makeIndex(wordPageList):
    wordIndex = {}

<<<<<<< HEAD
outfile.write('his is the first line.')

outfile.write(' Still the first line...\n')

outfile.write('Now we are in the second line.\n')

outfile.write('Non string value like ' + str(5) +
              ' must be converted first.\n')

outfile.write('Non string value like {} must be converted first.\n'.format(5))

outfile.close()


def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    while True:
        print_board(board)
        move = input("It's " + player + "'s turn. Enter a position (1-9): ")
        if board[int(move)-1] != " ":
            print("That position is already taken. Please try again.")
            continue
        board[int(move)-1] = player
        if check_win(board, player):
            print_board(board)
            print("Congratulations, " + player + " wins!")
            break
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break
        if player == "X":
            player = "O"
=======
    for item in wordPageList:
        word = item[0]
        page = item[1]
        if word not in wordIndex:
            wordIndex[word] = [page]
>>>>>>> 6f71d35894b6e8826f5b971ea584cc5f6c9e0c28
        else:
            wordIndex[word].append(page)
    return wordIndex

aliceIndex = makeIndex(wordOccurrences)

print(aliceIndex)

<<<<<<< HEAD
play_game()
=======
>>>>>>> 6f71d35894b6e8826f5b971ea584cc5f6c9e0c28
