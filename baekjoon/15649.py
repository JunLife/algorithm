import sys
n, m = map(int, sys.stdin.readline().strip().split()) # 1 ~ n 까지 자연수, 중복없이 M개를 고른 수열

def dfs(level, now):
    global n, check

    if level == m:
        print(' '.join(map(str, now)))
        return
    
    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        now.append(i)
        dfs(level + 1, now)
        now.pop()
        check[i] = False
        
    
check = [False] * (n + 1)
dfs(0, list())