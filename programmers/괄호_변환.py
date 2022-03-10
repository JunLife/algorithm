def solution(p):
    answer = dq(p)
    return answer

def dq(s):
    if len(s) == 0:
        return ''
    
    # 균형잡힌 괄호 문자열 인덱스
    index = find_equal_index(s)
    
    u = s[0:index]
    v = s[index:]
    
    # 올바른 괄호 문자열
    if is_correct(u):
        if is_correct(v):
            return s
        return u + dq(v)
    
    # 올바르지 않은 괄호 문자열
    return '(' + dq(v) + ')' + reverse(u[1:-1])
    
def find_equal_index(s):
    open_c = 0
    close_c = 0
    for i, c in enumerate(s):
        if open_c != 0 and close_c != 0 and open_c == close_c:
            return i
        if c == '(':
            open_c += 1
            continue
            
        close_c += 1
        
    return len(s)
    
def is_correct(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)
        elif st:
            st.pop()
        else:
            return False
    return len(st) == 0

def reverse(u):
    result = ''
    for c in u:
        if c == '(':
            result += ')'
        else:
            result += '('
            
    return result

print(solution(")("))