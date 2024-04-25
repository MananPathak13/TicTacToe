def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Print a separator between rows

def check_win(board, player):
    # Check horizontal, vertical, and diagonal conditions
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tictactoe_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"It's {current_player}'s turn. Enter your move (row col): ")
        row, col = map(int, input().split())
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tictactoe_game()
