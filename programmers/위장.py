def solution(clothes):
    answer = 1
    
    _hash = dict()
    for cloth in clothes:
        if cloth[1] in _hash:
            _hash[cloth[1]].append(cloth[0])
        else:
            _hash[cloth[1]] = [cloth[0]]
    
    for kinds in _hash.values():
        answer *= len(kinds) + 1
    answer -= 1
    
    return answer