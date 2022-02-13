n = int(input())
result = list()
for i in range(n):
    num = int(input())
    if num == 0:
        result.pop()
        continue
    result.append(num)
    
print(sum(result))