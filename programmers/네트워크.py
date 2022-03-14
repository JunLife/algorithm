from collections import deque

def solution(n, computers):
    answer = 0
    check = [False] * n
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not check[j]:
                answer += 1
                
                q.append(j)
                check[j] == True
                computers[i][j] = 0
                
                while q:
                    now = q.popleft()
                    
                    for k in range(n):
                        if computers[now][k] == 1 and not check[k] and now != k:
                            check[k] = True
                            q.append(k)
        
    return answer