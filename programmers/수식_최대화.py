import re, copy

permutations = list()
def solution(expression):
    answer = 0
    dfs(0, [False, False, False], [])
    expression = re.split('([\+\-\*])', expression)

    for operation in permutations:
        exp = copy.deepcopy(expression)
        for op in operation:
            while op in exp:
                i = exp.index(op)
                value = eval(exp[i - 1] + op + exp[i + 1])
                exp[i - 1] = str(value)
                del exp[i:i + 2]

        answer = max(answer, abs(int(exp[0])))
            
    return answer

def dfs(level, check, now): # +, -, *
    global permutations
    
    if level >= 3:
        permutations.append(copy.deepcopy(now))
        return
    
    for i in range(3):
        if check[i]:
            continue
            
        if i == 0:
            now.append('+')
        elif i == 1:
            now.append('-')
        elif i == 2:
            now.append('*')
        check[i] = True
        dfs(level + 1, check, now)
        check[i] = False
        now.pop()