"""
06: Tic-Tac-Toe
2-player game using a 2D array and basic game logic.
"""
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(b, player):
    for i in range(3):
        if all(b[i][j] == player for j in range(3)) or all(b[j][i] == player for j in range(3)):
            return True
    if b[0][0] == b[1][1] == b[2][2] == player or b[0][2] == b[1][1] == b[2][0] == player:
        return True
    return False

if __name__ == "__main__":
    board = [[" "]*3 for _ in range(3)]
    print("Tic-Tac-Toe initialized.")
    print_board(board)
