import sys
from collections import deque

def dfs(st):
    print(st + 1, end = ' ')
    global check_dfs
    check_dfs[st] = True
    
    for i in range(n):
        if path[st][i] and check_dfs[i] == False:
            dfs(i)
            
# 정점의 수, 간선의 수, 시작 정점
n, m, v = map(int, sys.stdin.readline().split())
path = [[False] * n for _ in range(n)]
check_dfs = [False] * n
check_bfs = [False] * n
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    path[x - 1][y - 1] = True
    path[y - 1][x - 1] = True


dfs(v - 1)
result = list()

q = deque()
q.append(v)
while q:
    now = q.popleft()
    if check_bfs[now - 1]:
        continue
    check_bfs[now - 1] = True
    result.append(now)
    for i in range(n):
        if path[now - 1][i]:
            q.append(i + 1)
    
print('\n' + ' '.join(map(str, result)))