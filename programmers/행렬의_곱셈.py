def solution(arr1, arr2):
    
    result = list()
    for i in range(len(arr1)): # result의 행 길이
        _list = list()
        for j in range(len(arr2[0])): # result의 열 길이
            _sum = 0
            for s in range(len(arr1[0])): # 돌아야 하는 길이 == len(arr2)
                _sum += arr1[i][s] * arr2[s][j]
            _list.append(_sum)
        result.append(_list)

    return result

# arr1    arr2    result
# 2 3 2   5 4 3   22 22 11
# 4 2 4   2 4 1   36 28 18
# 3 1 4   3 1 1   29 20 14

# 1 4     3 3     15 15
# 3 2     3 3     15 15
# 4 1             15 15