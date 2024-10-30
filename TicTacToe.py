def display_tictactoe(tictactoe):                                                                # Display the board.
    for line in tictactoe:
        print(" | ".join(line))
        print("-" * 9)

def display_victory(tictactoe, player):                                                          # Check if the player has won.
    for line in tictactoe:
        if all(s == player for s in line):
            return True
    for col in range(3):
        if all(tictactoe[row][col] == player for row in range(3)):
            return True
    if all(tictactoe[i][i] == player for i in range(3)) or all(tictactoe[i][2 - i] == player
                                                                for i in range(3)):
        return True
    return False

def game_tic_tac_toe():                                                                           # Create an empty board.
    tictactoe = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]                                                                          # The player 'X' and the player 'O'.
    turn = 0

    while turn < 9:                                                                               # maximum 9 turns
        player = players[turn % 2]                                                                # Alternate between players.
        display_tictactoe(tictactoe)                                                              # Display board.
       
        while True:
            try:
                line = int(input(f"player {player}, enter the line (0, 1, 2) : "))                # Prompt the user to choose
                col = int(input(f"player {player}, enter the column (0, 1, 2) : "))               # a row and a column.
                if tictactoe[line][col] == " ":                                                   # Check if the box is empty.
                    tictactoe[line][col] = player
                    break
                else:
                    print("This box is already taken. Please try again.")                         # Display box already occupied.
            except (ValueError, IndexError):
                print("Invalid entry. Please enter values between 0 and 2.")                      # Display invalid input.

        if display_victory(tictactoe, player):                                                    # Check if the player has won after their move.
            display_tictactoe(tictactoe)
            print(f"Congratulations! the player {player} won 🏆 !")                               # Display victory message.
            return

        turn += 1
    display_tictactoe(tictactoe)
    print("It's a draw!","🔄")                                                                    # Display draw message.
   
if __name__ == "__main__":
    game_tic_tac_toe()