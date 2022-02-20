import sys

# 세로, 가로 크기
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

t1_move = [
    [[0, 0, 0], [1, 1, 1]],
    [[1, 1, 1], [0, 0, 0]]
]
t2_move = [
    [[0, 1, 0], [1, 0, -1]]
]
t3_move = [
    [[1, 1, -2], [0, 0, 1]], 
    [[0, 1, 1], [1, 0, 0]], 
    [[1, 1, 0], [0, 0, 1]], 
    [[1, 1, 0], [0, 0, -1]],
    [[0, 0, 1], [1, 1, 0]],
    [[1, -1, 0], [0, 1, 1]],
    [[1, 0, 0], [0, 1, 1]],
    [[0, 0, -1], [1, 1, 0]]
]
t4_move = [
    [[1, 0, 1], [0, 1, 0]],
    [[1, 0, 1], [0, -1, 0]],
    [[0, -1, 0], [1, 0 ,1]],
    [[0, 1, 0], [1, 0, 1]]
]
t5_move = [
    [[0, 0, 1], [1, 1, -1]],
    [[0, 0, -1], [1, 1, -1]],
    [[0, 1, -2], [1, 0, 0]],
    [[1, 1, -1], [0, 0, 1]]
]

t_list = [t1_move, t2_move, t3_move, t4_move, t5_move]

# O(5 * n * m * move * 3) = O(m * n)
_max = float('-inf')
for t in t_list: # 현재 블럭 모양
    for i in range(n): # now_x
        for j in range(m): # now_y
            for move in t: # 블럭 움직임
                
                flag = False
                next_x = i
                next_y = j
                sum = board[next_x][next_y]
                for k in range(3):
                    next_x += move[0][k]
                    next_y += move[1][k]
                    if 0 <= next_x < n and 0 <= next_y < m:
                        sum += board[next_x][next_y]
                    else:
                        flag = True
                        break
                if flag:
                    continue
                _max = max(_max, sum)

print(_max)
                