"""
49: Sudoku Solver
Backtracking algorithm to solve puzzles.
"""
def solve_sudoku(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if solve_sudoku(board): return True
                        board[r][c] = 0
                return False
    return True

def is_valid(b, r, c, n):
    for i in range(9):
        if b[r][i] == n or b[i][c] == n: return False
    start_r, start_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(3):
        for j in range(3):
            if b[start_r+i][start_c+j] == n: return False
    return True

if __name__ == "__main__":
    print("Sudoku backtracking solver initialized.")
