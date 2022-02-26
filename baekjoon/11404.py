import sys

# 도시의 수
n = int(sys.stdin.readline())
# 버스의 수
m = int(sys.stdin.readline())

path = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            path[i][j] = 0
            
for _ in range(m):
    st, ed, value = map(int, sys.stdin.readline().split())
    path[st - 1][ed - 1] = min(path[st - 1][ed - 1], value)

for k in range(n):
    for i in range(n):
        for j in range(n):
            path[i][j] = min(path[i][k] + path[k][j], path[i][j])
            
for i in range(n):
    for j in range(n):
        if path[i][j] == float('inf'):
            path[i][j] = 0
            
for e in path:
    print(' '.join(map(str, e)))