import sys
from collections import deque

def bfs(is_tell):
    global picture
    result = 0
    check = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if check[i][j] == False:
                q = deque()
                q.append((i, j))
                check[i][j] = True
                result += 1
                while q:
                    now = q.popleft()
                    
                    for k in range(4):
                        next_x = now[0] + dx[k]
                        next_y = now[1] + dy[k]
                        
                        if 0 <= next_x < n and 0 <= next_y < n and check[next_x][next_y] == False:
                            if is_tell and picture[now[0]][now[1]] == picture[next_x][next_y]:
                                q.append((next_x, next_y))
                                check[next_x][next_y] = True
                                
                            elif is_tell == False:
                                if picture[now[0]][now[1]] == 'R' or picture[now[0]][now[1]] == 'G':
                                    if picture[next_x][next_y] != 'B':
                                        q.append((next_x, next_y))
                                        check[next_x][next_y] = True
                                elif 'B' == picture[next_x][next_y]:
                                    q.append((next_x, next_y))
                                    check[next_x][next_y] = True
    
    return result


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(sys.stdin.readline())
picture = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

print(bfs(True), bfs(False))