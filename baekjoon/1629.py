import sys

def dfs(a, b, c):
    if b == 0:
        return a % c
    if b == 1:
        return a % c
    elif b == 2:
        return a * a % c
    
    if b % 2 == 1:
        return (dfs(a, b // 2, c) ** 2 * a) % c
    else:
        return (dfs(a, b // 2, c) ** 2) % c

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().strip().split())
    
    print(dfs(A, B, C))