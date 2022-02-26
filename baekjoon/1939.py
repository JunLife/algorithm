import sys
from collections import deque

def bfs(node, weight):
    check = [False] * n
    check[st_node] = True

    q = deque()
    q.append(node)
    check[node] = True
    
    while q:
        now = q.popleft()
        if now == ed_node:
            return True
        
        for x in path[now]:
            if not check[x[0]] and x[1] >= weight:	
                check[x[0]] = True
                q.append(x[0])
                
    return False
    
# n: 섬의 수, m: 다리의 수
n, m = map(int, sys.stdin.readline().split())

# 경로와 무게를 인접행렬 방식으로 표현하면 메모리 초과임
path = [list() for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    path[a - 1].append((b - 1, c))
    path[b - 1].append((a - 1, c))

st_node, ed_node = map(lambda node : int(node) - 1, sys.stdin.readline().split())


st = 1
ed = 1000000000
result = -1
while st <= ed:
    mid = (st + ed) // 2
    status = bfs(st_node, mid)
    
    if status:
        st = mid + 1
        result = mid
    else:
        ed = mid - 1
        
print(result)