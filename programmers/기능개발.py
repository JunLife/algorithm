from collections import deque

def solution(progresses, speeds):
    answer = []
    job_queue = deque(progresses)
    job_speeds = deque(speeds)
    
    while job_queue:
        done = 0
        
        for i in range(len(job_queue)):
            job_queue[i] += job_speeds[i]
        
        if job_queue[0] >= 100:
            job_speeds.popleft()
            job_queue.popleft()
            done += 1
            
            while job_queue:
                if job_queue[0] >= 100:
                    job_speeds.popleft()
                    job_queue.popleft()
                    done += 1
                else:
                    break
                    
        if done > 0:
            answer.append(done)
            
    return answer