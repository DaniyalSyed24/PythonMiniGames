#  Tic Tac Toe
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

COLS = 3
ROWS = 4


# [[EMPTY] * COLS] * ROWS (een gedeelde rij voor elke rij)
board = [None] * ROWS
row = 0
while row < ROWS:
    board[row] = [EMPTY] * COLS
    row = row + 1


border_line = "+"
row = 0
while row < COLS:
    border_line = border_line + "---+"
    row = row + 1

row = 0
print(border_line)
while row < ROWS:
    line = "|"
    col = 0
    while col < COLS:
        line = line + " " + board[row][col] + " |"
        col = col + 1
    print(line)  # line niet meer nodig mag hergebruikt worden
    print(border_line)
    row = row + 1

current_player = PLAYER_X
winner = False
while not winner:
    correct_input = False
    while not correct_input:
        print("Where do you want to place the next " + current_player + "?")
        row = int(input("Which row?")) - 1
        col = int(input("Which col?")) - 1

        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            print("Error: Row and/or Col is invalid.")
        elif board[row][col] != EMPTY:
            print("Error: Cell already occupied.")
        else:
            correct_input = True
            board[row][col] = current_player

    row = 0
    print(border_line)
    while row < ROWS:
        line = "|"
        col = 0
        while col < COLS:
            line = line + " " + board[row][col] + " |"
            col = col + 1
        print(line)  # line niet meer nodig mag hergebruikt worden
        print(border_line)
        row = row + 1

    if current_player == PLAYER_X:  # or with odd or even turn
        current_player = PLAYER_O
    else:
        current_player = PLAYER_X

    # decide winner
    winner = False  # TODO find actual computation
