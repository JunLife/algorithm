def solution(s):
    s = s[1:-1].split('},{')
    dic = dict()
    
    for str in s:
        if str[0] == '{':
            str = str[1:]
        if str[-1] == '}':
            str = str[0:-1]
        
        nums = list(str.split(','))
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
    
    dic = dict(sorted(dic.items(), key = lambda x : x[1], reverse = True))
    
    return list(map(int, dic.keys()))