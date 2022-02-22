import sys
from collections import deque

# 정점의 수, 간선의 수
n, m = map(int, sys.stdin.readline().split())
check = [False] * n
path = [[False] * n for _ in range(n)]

for _ in range(m):
    ne1, ne2 = map(int, sys.stdin.readline().split())
    path[ne1 - 1][ne2 - 1] = True
    path[ne2 - 1][ne1 - 1] = True
    


count = 0
for j in range(n):
    if check[j]:
        continue
    
    q = deque()
    q.append(j)
    check[j] = True

    count += 1
    while q:
        now = q.popleft()
        
        next_path = path[now]
        for i in range(1, n):
            if next_path[i] and not check[i]:
                q.append(i)
                check[i] = True
                
print(count)