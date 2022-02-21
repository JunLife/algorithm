import sys

def dfs(now):
    global count
    
    if now == n:
        count += 1
        return
    
    for i in range(1, 4):
        if now + i <= n:
            dfs(now + i)

t = int(sys.stdin.readline())

result = list()
for _ in range(t):
    count = 0
    n = int(sys.stdin.readline())
    dfs(0)
    result.append(count)

print('\n'.join(map(str, result)))