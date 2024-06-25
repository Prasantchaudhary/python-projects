# CASHINO GAME LET'S MAKE THIS
import random  # TO generate ramdom symbol from the provided list
import time


def deposite():
    Amount = float(input("Enter your Deposite Amount:->"))
    return Amount


def display_board(boaard):
    for i in range(3):
        print("\n+----+----+----+")
        print("|", end="")
        for j in range(3):
            print(boaard[i][j], " |", end="")
    print("\n+----+----+----+")


def spin(board, symbols):
    for i in range(3):
        for j in range(3):
            board[i][j] = random.choice(symbols)
    return board


def payout(board, bet):
    count = 0
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == '💰':
                count += 1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "💰":
                count += 1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "💰":
            count += 1
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == "💰":
            count += 1

    return count*bet*10


def main():
    symbols = ["💵", "💴", "💶", "💷", "💰"]
    board = [["💵", "💰", "💵"], ["💴", "💰", "💶"], ["💷", "💰", "💷"]]
    print("+-----------------------------------+")
    print("         WELCOME TO CASHINO          ")
    print("+-----------------------------------+")
    display_board(board)
    Amount = 0
    playing = True
    while playing:  # Game started
        ask = input("Do you want to play?(Y/N)->").capitalize()
        if ask.isdigit():
            print("Enter 'Y' to play and Any other key to exit")
            continue
        elif not ask == 'Y':
            break
        else:
            while Amount > 0:
                print(f"Available Balance:${Amount}")
                bet = 0
                try:  # Checking for valid bet
                    bet = float(input("Place your bet:"))
                except ValueError:
                    print("Place valid bet")
                    continue
                if bet > Amount:
                    print("Insufficient balance")
                    continue
                Amount -= bet
                # spin the board
                spin(board, symbols)

                print("spinning..")
                time.sleep(2)
                # display the board after each spin
                display_board(board)
                # Track the wining amount
                win = payout(board, bet)
                if win > 0:
                    print(f"You won:{win}")
                    Amount += win
                    ask = input("Do you want to play?(Y/N)->").capitalize()
                    if ask == 'Y':
                        continue
                    else:
                        break
                else:
                    print("Try your luck next time")
                    ask = input("Do you want to play?(Y/N)->").capitalize()
                    if ask == 'Y':
                        continue
                    else:
                        break
            else:
                print("Insufficient Balance")
                depo = input("Do you want to Deposite?(Y/N)").capitalize()
                if depo != 'Y':
                    break
                else:
                    Amount = deposite()
                    print(f"${Amount} successfully deposited")
                    continue
            break

    print("Thank you! Try your luck next time")
    print(f"Your Balance:{Amount}")


if __name__ == "__main__":
    main()
