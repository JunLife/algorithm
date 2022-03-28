from collections import Counter

com = set()

def dfs(level, now, menus, course):
    if level > len(menus):
        return
    
    if any(map(lambda x : x == len(now), course)):
        now.sort()
        com.add(''.join(now))

    for i in range(level, len(menus)):
        now.append(menus[i])
        dfs(i + 1, now, menus, course)
        now.pop()

def solution(orders, course):
    answer = list()

    # 존재하는 경우의 수만 계산
    # menu set으로 모두 모아서 계산하면 존재하지 않는 경우의 수도 포함됨
    for order in orders:
        dfs(0, list(), sorted(order), course)
            
    len_list = [0] * (11)
    com_dict = dict()
    for c in com:
        c_len = len(c)
        st = 0
        count = 0
        for order in orders:
            if len(order) < c_len:
                continue
            else:
                exist = True
            
            for menu in c:
                if not menu in order:
                    exist = False
                    break
                    
            if exist:
                count += 1
                
        if count < 2:
            continue
        elif len_list[c_len] <= count:
            com_dict[c] = count
            len_list[c_len] = count
        
    answer = [c for c, v in com_dict.items() if len_list[len(c)] == v]

    return sorted(answer)