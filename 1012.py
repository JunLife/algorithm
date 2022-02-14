from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

case = int(sys.stdin.readline()) # 테스트 케이스의 수
result = list()
for i in range(case):
    m, n, k = map(int, sys.stdin.readline().split()) # 가로길이, 세로길이, 배추 위치의 수
    land = [[0] * m for _ in range(n)]
    
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        land[y][x] = 1
    
    count = 0
    for j in range(n):
        for s in range(m):
            if land[j][s] == 1:
                q = deque()
                q.append((j, s))
                land[j][s] = 2
                count += 1
                
                while q:
                    now = q.popleft()
                    
                    for t in range(4):
                        next_y = now[0] + dx[t]
                        next_x = now[1] + dy[t]
                    
                        if 0 <= next_y < n and 0 <= next_x < m and land[next_y][next_x] == 1:
                            q.append((next_y, next_x))
                            land[next_y][next_x] = 2
    
    result.append(count)
    
for e in result:
    print(e)