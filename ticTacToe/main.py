# function to display check board
def checkboard(check_board):
    for x in range(3):
        print("\n+----+----+----+")
        print("|", end="")
        for y in range(3):
            print(check_board[x][y], "  |", end="")
    print("\n+----+----+----+")


# declare winner
def win_decision(check_board):
    # check row and column
    for i in range(3):
        if check_board[i][0] == check_board[i][1] == check_board[i][2] and check_board[i][0] != " ":
            return check_board[i][0]
        elif check_board[0][i] == check_board[1][i] == check_board[2][i] and check_board[0][i] != " ":
            return check_board[0][i]
    # check main diagonal
    if check_board[0][0] == check_board[1][1] == check_board[2][2] and check_board[0][0] != " ":
        return check_board[0][0]
    # check other diagonal
    if check_board[2][0] == check_board[1][1] == check_board[0][2] and check_board[2][0] != " ":
        return check_board[2][0]
    # check for Tie
    if " " not in check_board[0] and " " not in check_board[1] and " " not in check_board[2]:
        return "Tie"

    return None


# update check board
def updatecheckboard(check_board, move, player):
    for i in range(3):
        for j in range(3):
            if (3*i+j+1) == move:
                if check_board[i][j] == " ":
                    check_board[i][j] = player
                    return True
    return False

# update available move


def update_possible_moves(possible_moves, move):
    possible_moves.remove(move)


def main():
    available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    check_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # It will call check board and display in our console
    print("+--------------------------------------+")
    print("          WELCOME TO TIC-TAC-TOE       ")
    print("+--------------------------------------+")

    # available players
    players = ['X', 'O']
    current_player = 0  # It indicate player X

    while True:
        checkboard(check_board)
        print("Possible Moves:", available_moves)

        player = players[current_player]
        print(f"player{player} Turn:")

        # Selection of vailid move
        while True:
            try:
                move = int(input("Place your move [1-9]->"))
                if move in available_moves:
                    updatecheckboard(check_board, move, player)
                    update_possible_moves(available_moves, move)
                    break
                else:
                    print("Select from availabel moves")
            except ValueError:
                print("select from available move")

        winner = win_decision(check_board)

        if winner:
            checkboard(check_board)
            if winner == "Tie":
                print("It's a Tie")
            else:
                print(f"Player {winner} wins")
            break
        else:
            current_player = (current_player+1) % 2


if __name__ == "__main__":
    main()
