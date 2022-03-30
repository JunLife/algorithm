from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    
    while True:
        if get_max(q) > q[0]:
            q.append(q.popleft())
            
            if 0 == location:
                location = len(q)
                 
        else:
            answer += 1
            q.popleft()
            
            if 0 == location:
                break
                
        location -= 1
    return answer

def get_max(q):
    _max = -1
    for i in range(1, len(q)):
        _max = max(q[i], _max)
        
    return _max