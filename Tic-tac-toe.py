# Welcome function
def welcome():
    print("Welcome to tic-tac-toe")

# Function to print the board
def print_board():
    print("These are the available options where numbers are present:")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} ")

# Function to check for a winner
def check_winner(board, symbol):
    # Check rows, columns, and diagonals for a winner
    return ((board[6] == board[7] == board[8] == symbol) or
            (board[3] == board[4] == board[5] == symbol) or
            (board[0] == board[1] == board[2] == symbol) or
            (board[6] == board[3] == board[0] == symbol) or
            (board[7] == board[4] == board[1] == symbol) or
            (board[8] == board[5] == board[2] == symbol) or
            (board[6] == board[4] == board[2] == symbol) or
            (board[8] == board[4] == board[0] == symbol))

# Function for the player to make a selection
def player_selection(board, player):
    symbol = 'X' if player == 1 else 'O'
    selection = input(f"PLAYER {player}: Enter a number from 1 to 9: ")

    # Validate player's selection
    while not selection.isdigit() or int(selection) not in range(1, 10) or board[int(selection) - 1] in ['X', 'O']:
        print(f'Your selection "{selection}" is incorrect or the cell is already occupied')
        selection = input(f"PLAYER {player}: Select a valid number: ")

    # Update the board with the player's selection
    index = int(selection) - 1
    board[index] = symbol

# Example of usage
while True:
    # Initialize the board
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board()

    # Loop for each turn of the game
    for turn in range(1, 10):
        # Make the current player's selection
        player_selection(board, turn % 2 + 1)
        print_board()

        # Check if there is a winner
        if check_winner(board, 'X'):
            print("Player 1 (X) has won!")
            break
        elif check_winner(board, 'O'):
            print("Player 2 (O) has won!")
            break
        elif turn == 9:
            print("It's a tie!")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    while play_again not in ['yes', 'no']:
        print("Invalid response. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == 'no':
        break