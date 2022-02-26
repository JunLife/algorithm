import sys

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if path[i][k] + path[k][j] == 2:
                path[i][j] = 1
                
for e in path:
    print(' '.join(map(str, e)))