board=["-","-","-",
       "-","-","-",
       "-","-","-"]
current_player="x"
gameisgoing=True
winner=None
def display_board():
    print(board[0] + "|" + board[1] + "|"+  board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
def handle_turn():
    position=int(input("Choose a random position from to 8:"))
    if position<8:
        board[position]=current_player
    if position>8:
        position=int(input("Please choose a random position from 0 to 8:"))
    board[position]=current_player
def swap_player():
    global current_player
    if current_player=="x":
        current_player="0"
    elif current_player=="0":
        Current_player="x"
def check_who_is_the_winner():
    global winner
    row_winner=check_row()
    col_winner=check_column()
    dia_winner=check_diagonal()
    check_tie()

    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    else:
        winner=dia_winner
def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] !="-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gameisgoing=False
    if row1:
        return board[0]
    elif row2:
        return board[5]
    elif row2:
        return board[6]



def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
         gameisgoing=False
    if col1:
         return board[3]
    elif col2:
         return board[1]
    elif col3:
         return board[5]
def check_diagonal():
    global gameisgoing
    dia1 = board[0] == board[4] == board[8] !="-"
    dia2 = board[2] == board[4] == board[6] != "-"

    if dia1 or dia2:
        gameisgoing=False
    if dia1:
        return board[0]
    elif dia2:
        return board[6]
def check_tie():
    global gameisgoing

    if "-" not in board:
        gameisgoing=False
        print("Match is Tie")

def play_game():
    while gameisgoing:
        display_board()
        handle_turn()
        swap_player()
        check_who_is_the_winner()
    if winner=="x":
        print(("x is the winner"))
    elif winner=="0":
        print("0 is the winner")
play_game()