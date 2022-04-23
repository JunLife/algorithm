import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    
    st = 0
    ed = k
    result = 0
    while st <= ed:
        # mid: k번째에 어떤 값이 있을까
        mid = (st + ed) // 2
        
        # k보다 작은 수
        count = 0
        for i in range(1, n + 1):
            count += min(n, mid // i)
            
        if count >= k:
            result = mid
            ed = mid - 1
        else:
            st = mid + 1
            
    print(result)