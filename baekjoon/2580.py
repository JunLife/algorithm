import sys

def dfs(next_zero):
    global board, zero_list
    
    if next_zero == len(zero_list):
        for line in board:
            print(' '.join(map(str, line)))
        sys.exit()
            
    next = zero_list[next_zero]
    next_y = next[0]
    next_x = next[1]

    for i in range(1, 10):        
        if checkRow(next_y, i) and checkCol(next_x, i) and checkBox(next_y, next_x, i):
            board[next_y][next_x] = i
            dfs(next_zero + 1)
            board[next_y][next_x] = 0

def checkRow(y, v):
    for i in range(9):
        if v == board[y][i]:
            return False
    return True

def checkCol(x, v):
    for i in range(9):
        if v == board[i][x]:
            return False
    return True

def checkBox(y, x, v):
    st_y = y // 3 * 3
    st_x = x // 3 * 3
    
    for i in range(st_y, st_y + 3):
        for j in range(st_x, st_x + 3):
            if v == board[i][j]:
                return False
    return True
    
def next_coor(y):
    next = [-1, -1]
    for next_x in range(9):
        if board[y][next_x] == 0:
            next = [y, next_x]
            break
    
    return next
    
if __name__ == '__main__':
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
    zero_list = list()
    for i, line in enumerate(board):
        for j, e in enumerate(line):
            if e == 0:
                zero_list.append((i, j))
    
    dfs(0)