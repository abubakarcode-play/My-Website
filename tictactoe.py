# Define the board
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
board_keys = list(theBoard.keys())

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(9):  # Maximum 9 moves in Tic-Tac-Toe
        printBoard(theBoard)
        print(f"It's your turn, {turn}. Move to which place?")
        move = input()

        if theBoard.get(move) == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        # Check for winner after 5 moves
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ' or \
               theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ' or \
               theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ' or \
               theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ' or \
               theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ' or \
               theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ' or \
               theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ' or \
               theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(f"**** {turn} won! ****")
                break

        # If all spots filled and no winner
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!")
            break

        # Switch turn
        turn = 'O' if turn == 'X' else 'X'

    restart = input("Do you want to play again? (y/n): ")
    if restart.lower() == 'y':
        for key in board_keys:
            theBoard[key] = ' '
        game()

if __name__ == "__main__":
    game()
