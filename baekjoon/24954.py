import sys

def dfs(level, now):
    global combi, check, n

    if level >= n:
        combi.append(now[:])
        return
    
    for i in range(n):
        if check[i]:
            continue
        
        check[i] = True
        now.append(i)
        dfs(level + 1, now)
        now.pop()
        check[i] = False
    

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    price_list = list(map(int, sys.stdin.readline().strip().split()))
    
    discount_info_list = [list()] * n
    # i 번째 물약을 사면 할인
    for i in range(n):
        discount_n = int(sys.stdin.readline())
        
        tmp = list()
        for j in range(discount_n):
            potion, discount = map(int, sys.stdin.readline().strip().split())
            tmp.append([potion - 1, discount])
        discount_info_list[i] = tmp

    check = [False] * n    
    combi = list()
    dfs(0, list())
    
    result = float('inf')
    for c in combi:
        tmp = price_list[:]
        _sum = 0
        for i in range(n):
            potion = c[i]
            _sum += tmp[potion]
            
            if discount_info_list[potion]:
                discount_info = discount_info_list[potion]
                for discount in discount_info:
                    tmp[discount[0]] = max(1, tmp[discount[0]] - discount[1])
        result = min(result, _sum)
        
    print(result)