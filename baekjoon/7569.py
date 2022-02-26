import sys
from collections import deque

def find_index():
    global board
    result = deque()
    
    for k in range(h):
        for i in range(m):
            for j in range(n):   
                if board[k][i][j] == 1:
                    result.append((k, i, j))
                    
    return result

def get_max():
    global days
    max = float('-inf')
    
    for k in range(h):
        for i in range(m):
            for j in range(n):
                if days[k][i][j] != float('inf') and max < days[k][i][j]:
                    max = days[k][i][j]
                    
    return max

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 없음
dz = [-1, 0, 0, 0, 0, 1]
dx = [0, -1, 0, 1, 0, 0]
dy = [0, 0, 1, 0, -1, 0]

# 가로, 세로, 높이
n, m, h = map(int, sys.stdin.readline().rstrip().split())
board = list()
for i in range(h):
    tmp = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
    board.append(tmp)
    
days = [[[float('inf')] * n for _ in range(m)] for _ in range(h)]
for k in range(h):
    for i in range(m):
        for j in range(n):   
            if board[k][i][j] == 1:
                days[k][i][j] = 0

q = find_index()

while q:
    now = q.popleft()
    
    for i in range(6):
        next = (now[0] + dz[i], now[1] + dx[i], now[2] + dy[i])
        if 0 <= next[0] < h and 0 <= next[1] < m and 0 <= next[2] < n and board[next[0]][next[1]][next[2]] == 0:
            q.append(next)
            board[next[0]][next[1]][next[2]] = 1
            days[next[0]][next[1]][next[2]] = days[now[0]][now[1]][now[2]] + 1

flag = False
for k in range(h):
    for i in range(m):
        for j in range(n):
            if board[k][i][j] == 0:
                flag = True
                break

if flag:
    print(-1)
else:
    print(get_max())