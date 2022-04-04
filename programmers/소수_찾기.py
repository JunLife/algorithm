check = [False] * 7

def dfs(level, numbers, now, permu):
    if now:
        permu.add(int(''.join(now)))
    
    if level >= len(numbers):
        return permu
    
    for i in range(len(numbers)):
        if check[i]:
            continue
            
        check[i] = True
        now.append(numbers[i])
        permu = dfs(level + 1, numbers, now, permu)
        now.pop()
        check[i] = False
    return permu

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numbers.sort(reverse = True)
    _max = int(''.join(numbers))
    
    primes = [True] * (_max + 1)
    primes[0] = primes[1] = False
    for i in range(2, len(primes)):
        if primes[i] == True:
            for j in range(i + i, len(primes), i):
                primes[j] = False
    
    permu = dfs(0, numbers, list(), set())
    for number in permu:
        if primes[number]:
            answer += 1
    
    return answer