def solution(s):
    answer = 1001
    
    for i in range(1, len(s) // 2 + 2):
        result = ''
        pre = ''
        count = 1
        
        for j in range(0, len(s), i):
            now = s[j:j + i]
            if pre != now:
                if count == 1:
                    result += pre                    
                else:
                    result += str(count) + pre
                pre = now
                count = 1
                continue
            count += 1

        if count == 1:
            result += pre                    
        else:
            result += str(count) + pre
        answer = min(answer, len(result))
    
    return answer