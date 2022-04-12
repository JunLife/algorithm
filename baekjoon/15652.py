import sys

def dfs(level, now, result):
    global m, n
    
    if level >= m:
        result.append(now[:])
        return result
    
    for i in range(1, n + 1):
        if now and now[-1] > i:
            continue
        now.append(i)
        result = dfs(level + 1, now, result)
        now.pop()
    
    return result
    
if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    result = dfs(0, list(), list())
    
    for e in result:
        for inner in e:
            print(inner, end = ' ')
        print()