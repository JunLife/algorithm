import sys

def dfs(now):
    global count

    for i in range(len(path[now])):
        if path[now][i] and not check[i]:
            check[i] = True
            count += 1
            dfs(i)
            
# 컴퓨터의 수
n = int(sys.stdin.readline())
# 연결 링크 수
m = int(sys.stdin.readline())

path = [[False] * n for _ in range(n)]
for _ in range(m):
    ne1, ne2 = map(int, sys.stdin.readline().rstrip().split())
    path[ne1 - 1][ne2 - 1] = True
    path[ne2 - 1][ne1 - 1] = True
    
count = 0
check = [False] * n
check[0] = True
dfs(0)
print(count)