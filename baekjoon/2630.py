import sys

def get_color(st_index, width):
    pre = board[st_index[0]][st_index[1]]
    
    for i in range(st_index[0], st_index[0] + width):
        for j in range(st_index[1], st_index[1] + width):
            if board[i][j] != pre:
                return -1
            
    return pre

def section(st_index, width):
    global blue_result, white_result
    
    color = get_color(st_index, width)

    if color == 1:
        blue_result += 1
    elif color == 0:
        white_result += 1
    elif color == -1:
        half = width // 2
        section(st_index, half)
        section((st_index[0] + half, st_index[1]), half)
        section((st_index[0] + half, st_index[1] + half), half)
        section((st_index[0], st_index[1] + half), half)
        
n = int(sys.stdin.readline())

# 0: white, 1: blue
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

white_result = 0
blue_result = 0

section((0, 0), n)
print(white_result)
print(blue_result)