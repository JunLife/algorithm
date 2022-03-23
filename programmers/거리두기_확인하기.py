from collections import deque

def solution(places):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # P: 사람, O: 빈 테이블, X: 파티션
    for place in places:
        status = 1
        start = list()
        
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    start.append((i, j))
                    
        for s in start:
            distance = [[float('inf')] * len(place[0]) for t in range(len(place)) ]
            check = [[False] * len(place[0]) for t in range(len(place)) ]
            
            q = deque()
            q.append(s)
            
            distance[s[0]][s[1]] = 0
            check[s[0]][s[1]] = True
            while q:
                now = q.popleft()
                
                for i in range(4):
                    next = (now[0] + dx[i], now[1] + dy[i])
                    if 0 <= next[0] < len(place[0]) and 0 <= next[1] < len(place) and not check[next[0]][next[1]]:
                        distance[next[0]][next[1]] = distance[now[0]][now[1]] + 1
                        
                        if place[next[0]][next[1]] == 'P' and distance[next[0]][next[1]] <= 2:
                            status = 0
                            break
                        if place[next[0]][next[1]] == 'O':
                            check[s[0]][s[1]] = True
                            q.append(next)
                            continue
                            
                        if distance[next[0]][next[1]] > 2:
                            q = deque()
                            break
                if status == 0:
                    break

        answer.append(status)
        
    return answer