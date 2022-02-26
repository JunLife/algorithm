import sys

# 집의 수, 공유기의 수
n, c = map(int, sys.stdin.readline().split())
house_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

house_list.sort()
st = 0
ed = house_list[-1] - house_list[0]
result = float('inf')

while st <= ed:
    mid = (st + ed) // 2
    
    count = 1
    pre = house_list[0]
    for i in range(1, n):
        if house_list[i] - pre >= mid:
            pre = house_list[i]
            count += 1

    if count >= c:
        st = mid + 1
        result = mid
    else:
        ed = mid - 1
        
print(result)