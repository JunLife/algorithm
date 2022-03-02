# N: 전체 스테이지의 수, stages: 사용자 현재 스테이지 번호 배열
def solution(N, stages):
    _list = [0] * N
    
    for i in range(N):
        fail = 0
        _try = 0
        for stage in stages:
            if i + 1 <= stage:
                _try += 1
                if i + 1 == stage:
                    fail += 1
        if _try == 0:
            _list[i] = (i + 1, 0)
            continue
        _list[i] = (i + 1, fail / _try)
    _list.sort(key = lambda x : -x[1])
    
    answer = list(map(lambda x : x[0], _list))

    return answer