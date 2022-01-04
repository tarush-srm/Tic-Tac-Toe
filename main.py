board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
winner = None

current_player = "X"

def play_game():
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner +"won.")
    elif winner == None:
        print("Tie.")

def display_board():
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

def handle_turn(player):

    print(player + "'s turn.")

    position = int(input("choose a position from 1 to 9: ")) - 1
    while position not in range(0, 10):
        position = int(input("choose a position from 1 to 9: ")) - 1

    if board[position] != "-":
        print("You can't go there choose again")
        position = int(input("choose a position from 1 to 9: ")) - 1

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
      winner = row_winner
    elif column_winner:
      winner = column_winner
    elif diagonal_winner:
      winner = diagonal_winner
    else:
      winner = None


def check_rows():
    global game_still_going
    if (board[0] == board[1] == board[2] != "-" or board[3] == board[4] == board[5] != "-" or board[6] == board[7] ==\
            board[8] != "-"):
        game_still_going = False
        return board[0] or board[3] or board[6]
    else:
            return None

def check_columns():
    global game_still_going
    if (board[0] == board[3] == board[6] != "-" or board[1] == board[4] == board[7] != "-" or board[2] == board[4] ==\
            board[8] != "-"):
        game_still_going = False
        return board[0] or board[1] or board[2]
    else:
         return None


def check_diagonals():
    global game_still_going
    if (board[2] == board[4] == board[6] != "-" or board[0] == board[4] == board[8] != "-"):
        game_still_going = False
        return board[0] or board[2]
    else:
        return None


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "X":
       current_player = "O"

    elif current_player == "O":
       current_player = "X"
    return

play_game()
