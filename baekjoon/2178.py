import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
time = [[0] * (m) for _ in range(n)]

q = deque()
q.append((0, 0))
time[0][0] = 1

while q:
    now = q.popleft()
    if now[0] == n - 1 and now[1] == m - 1:
        break
    
    for i in range(4):
        next = (now[0] + dx[i], now[1] + dy[i])
        if 0 <= next[0] < n and 0 <= next[1] < m and time[next[0]][next[1]] == 0 and board[next[0]][next[1]] == 1:
            q.append(next)
            time[next[0]][next[1]] = time[now[0]][now[1]] + 1

print(time[n - 1][m - 1])