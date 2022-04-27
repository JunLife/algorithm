import sys, copy
from collections import deque

def dfs(level, now):
    global n, m, result
    
    if level >= 3:
        result = max(result, bfs(copy.deepcopy(now)))
        return
    
    for i in range(n):
        for j in range(m):
            if now[i][j] == 0:
                now[i][j] = 1
                dfs(level + 1, now)
                now[i][j] = 0
                
def bfs(now):
    global dy, dx
    
    for i in range(n):
        for j in range(m):
            if now[i][j] == 2:
                now[i][j] = None
                q = deque()
                q.append((i, j))
                
                while q:
                    now_coor = q.popleft()
                    for k in range(4):
                        next_y = dy[k] + now_coor[0]
                        next_x = dx[k] + now_coor[1]
                        
                        if 0 <= next_y < n and 0 <= next_x < m and now[next_y][next_x] == 0:
                            q.append((next_y, next_x))
                            now[next_y][next_x] = None
    
    return count(now)
    
def count(now):
    count = 0
    
    for i in range(n):
        for j in range(m):
            if now[i][j] == 0:
                count += 1
    return count

if __name__ == '__main__':
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    n, m = map(int , sys.stdin.readline().strip().split())
    # 0: 빈칸, 1: 벽, 2: 바이러스
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    result = float('-inf')
    
    dfs(0, board)
    print(result)