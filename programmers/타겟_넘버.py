answer = 0
def solution(numbers, target):
    global answer
    
    dfs(0, 0, numbers, target)
    return answer

def dfs(level, value, numbers, target):
    global answer
    
    if level >= len(numbers):
        if value == target:
            answer += 1
        return answer
    
    a = dfs(level + 1, value + numbers[level], numbers, target)
    b = dfs(level + 1, value - numbers[level], numbers, target)
    return a + b