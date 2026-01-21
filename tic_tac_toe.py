def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board
    """
    print("\nCurrent Board:")
    print("  0   1   2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print(" ---+---+---")
    print()


def is_valid_move(board, row, col):
    """
    Checks whether the move is valid:
    - Inside board limits
    - Cell is empty
    """
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    return board[row][col] == " "


def check_winner(board, player):
    """
    Checks if the given player has won
    """
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def play_game():
    """
    Main game loop
    """
    # Initialize empty board
    board = [[" " for _ in range(3)] for _ in range(3)]

    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            try:
                row, col = map(int, input("Enter row and column: ").split())
                if is_valid_move(board, row, col):
                    break
                else:
                    print("❌ Invalid move! Try again.")
            except:
                print("❌ Please enter two numbers separated by space.")

        # Place move
        board[row][col] = current_player
        moves += 1

        # Check win
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        # Check draw
        if moves == 9:
            print_board(board)
            print("🤝 It's a draw!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"


def main():
    print("=================================")
    print("     Welcome to Tic Tac Toe")
    print("=================================")
    print("Instructions:")
    print("1. Two players: X and O")
    print("2. Enter move as: row column")
    print("3. Row and column must be between 0 and 2\n")

    while True:
        play_game()
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != "y":
            print("Thanks for playing! 🎉")
            break


if __name__ == "__main__":
    main()
