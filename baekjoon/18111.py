import sys

n, m, b = map(int, sys.stdin.readline().split()) # 행, 열, 인벤토리 블럭 수
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_list = list()
max_list = list()
for e in land:
    min_list.append(min(e))
    max_list.append(max(e))

time = float('inf')
high = -1

inven = [b] * (max(max_list) + 1)
for h in range(min(min_list), max(max_list) + 1):
    lack_flag = False
    time_sum = 0
    
    for i in range(n):
        for j in range(m):
            now_high = land[i][j]
            if now_high > h:
                inven[h - 1] += now_high - h
                
    for i in range(n):
        for j in range(m):
            now_high = land[i][j]
            if now_high == h:
                continue
            
            if now_high > h:
                dif = now_high - h
                time_sum += (dif * 2)
            else:
                dif = h - now_high
                if inven[h - 1] < dif:
                    lack_flag = True
                    time_sum = float('inf')
                    break
                time_sum += dif
                inven[h - 1] -= dif
        if lack_flag:
            break
    if lack_flag:
        break
    
    if time_sum <= time:
        time = time_sum
        high = h

print(time, high)