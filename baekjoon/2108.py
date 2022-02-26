import sys

def find():
    map = dict()
    for i in range(n):
        if nums[i] in map.keys():
            map[nums[i]] += 1
        else:
            map[nums[i]] = 1
        
    result = list(map.items())
    result.sort(key = lambda x: -x[1])
    if len(result) == 1 or result[0][1] != result[1][1]:
        return result[0][0]

    return result[1][0]

n = int(sys.stdin.readline())
nums = list()

for i in range(n):
    nums.append(sys.stdin.readline())

print(round(sum(nums)/n))
nums.sort()
print(nums[n // 2])
print(find())
print(nums[-1] - nums[0])