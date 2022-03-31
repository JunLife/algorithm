import sys

def dfs(level, board):
    global count, n, allow_col

    if level == n:
        count += 1
        return

    for col in range(n):
        if allow_col[col] and put(board, level, col):
            board[level] = col
            allow_col[col] = False
            dfs(level + 1, board)
            allow_col[col] = True
            
            
def put(board, level, col):
    global allow_col
    for row in range(level):
        if board[row] == col or abs(board[row] - col) == abs(row - level): # 같은 열이거나 대각선이면
            return False

    return True

n = int(sys.stdin.readline().strip())

allow_col = [True] * n
board = [None] * n
count = 0

dfs(0, board)
print(count)